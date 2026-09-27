# E4 — Chuleta de nombres técnicos (Odoo 20)

> Verificado leyendo el código fuente de Odoo 20.0 (`odoo/addons/base`, `addons/product`,
> `addons/uom`, `addons/stock`, `addons/account`) y comparándolo con saas-19.4. **Varios campos
> cambiaron respecto de v16–v18, y algunos otra vez en v20**: los CSV y tutoriales de versiones
> anteriores fallan precisamente por esto.
>
> Cómo verificarlo tú mismo: activa el modo desarrollador y pasa el cursor sobre la etiqueta
> del campo, o abre *Ajustes → Técnico → Estructura de la base de datos → Campos*.

---

## 1. Cambios de v19 que rompen archivos antiguos (siguen vigentes en v20)

| Concepto | Antes (v16–v18) | **Desde v19 (igual en v20)** | Impacto |
|---|---|---|---|
| Producto almacenable | `type = 'product'` | `type = 'consu'` **+** `is_storable = True` | Un CSV con `type=product` **falla** |
| Unidad de compra | `uom_po_id` | **eliminado** — solo existe `uom_id` | La columna `uom_po_id` ya no se puede importar |
| Empaques del producto | modelo `product.packaging` | `uom_ids` (Many2many a `uom.uom`) | Cambia el modelado de "caja de 12" |
| Unidades de medida | `category_id` + `uom_type` + `factor` (editable) | `relative_factor` + `relative_uom_id` (jerarquía); `factor` sigue existiendo pero es **calculado** | Ya no hay "categoría de UdM"; no se puede importar `factor` |
| Celular del contacto | `mobile` | **eliminado** — solo `phone` | Una columna `mobile` provoca error de campo desconocido |
| Empresa / persona | `company_type` (`company`/`person`) | **eliminado**. `is_company` existe pero es **calculado y no importable**: sale de `vat` | Ni `company_type` ni `is_company` sirven como columna de CSV |
| Grupos del usuario | `groups_id` | `group_ids` | Rompe importaciones de usuarios |
| Categoría raíz de producto | `product.product_category_all` ("All") | `product.product_category_goods` ("Goods"), `..._services`, `..._expenses` | El ID externo antiguo **no existe** |

> *Producto almacenable* (`type='consu'` + `is_storable`) llegó en v18; el resto de la tabla, en v19.
> Desde saas-19.4 `is_storable` vive en el módulo `product` (en v18 y 19.0 lo añadía `stock`).

## 1 bis. Lo que vuelve a cambiar en v20 (respecto de v19)

| Concepto | En v19 (saas-19.4) | **En v20** | Impacto |
|---|---|---|---|
| Validación del RUC/NIF | Módulo aparte `base_vat`, que llegaba con la localización (`l10n_pe`) | Integrada en `base`: `res.partner.vat` se valida **siempre** según el país del contacto | Un RUC con dígito verificador incorrecto **rechaza la fila** al importar |
| Tipo de identificación (LATAM) | `l10n_latam_base`: campo `l10n_latam_identification_type_id` (RUC, DNI, CE…) | Módulo **eliminado**. El RUC va en `vat`; DNI, CE, pasaporte, etc. van en `additional_identifiers` (JSON). En Perú, `l10n_pe_sunat_id_code` se **calcula** (6 = RUC, 1 = DNI…) | Las columnas `l10n_latam_identification_type_id` de plantillas antiguas **ya no existen** (Fase 10) |
| Seguimiento del producto | `tracking` = `none` / `lot` / `serial` | `tracking` = `lot` / `serial` o **vacío** (el valor `none` desapareció). Nuevo campo `store_by` (*Rastreo*): `untracked` / `quantity` / `lot` / `serial`, calculado y editable | Un CSV con `tracking=none` **falla**; deja la celda vacía |
| Código de barras de la plantilla | Calculado desde la variante, sin almacenar | **Almacenado** en `product.template` (se puede buscar y agrupar), y la unicidad se comprueba también entre plantillas | Se sigue importando igual; la unicidad sigue siendo **por compañía**, como en v19 |
| Rol del usuario | `role` = `group_user` / `group_system` | `role` = `light_user` (*ligero*) / `regular_user` / `group_system`. El ligero solo admite grupos "ligeros" (ausencias, asistencia…) | Un usuario ligero no ve Contactos ni Ventas |

## 2. Contactos — `res.partner`

| Campo técnico | Tipo | Notas para importar |
|---|---|---|
| `name` | Char | Obligatorio |
| `is_company` | Boolean **calculado** | `True` si el contacto es su propia entidad comercial y tiene `vat` (no vacío, ni `/`, `na` o `NA`: lo resume el campo calculado `has_vat`). **No se importa**: no tiene `inverse`. En v20 ya no existe `l10n_latam_identification_type_id`: un contacto con RUC en `vat` sale como empresa; uno con solo DNI (en identificadores adicionales) sale como persona. `company_type` ya no existe |
| `parent_id` | Many2one → `res.partner` | Empresa a la que pertenece el contacto hijo |
| `type` | Selección | `contact`, `invoice`, `delivery`, `other` |
| `vat` | Char | RUC/NIF. **En v20 se valida siempre** que el contacto tenga país (Perú: 11 dígitos con dígito verificador). Para "sin RUC" usa `/` |
| `ref` | Char | Referencia interna del contacto (código de cliente) |
| `street`, `zip`, `city` | Char | Texto libre |
| `state_id`, `country_id` | Many2one | Importar como `country_id/id` = `base.pe` |
| `phone`, `email`, `website` | Char | **No existe `mobile`** (eliminado en v19, sigue así en v20) |
| `function` | Char | Puesto de trabajo de la persona |
| `category_id` | Many2many → `res.partner.category` | Etiquetas; varios IDs separados por coma |
| `customer_rank` / `supplier_rank` | Integer | `1` marca como cliente / proveedor *(definidos por el módulo Contabilidad)* |
| `user_id` | Many2one → `res.users` | Vendedor asignado |
| `comment` | Html | Notas internas |
| `active` | Boolean | `False` = archivado |

## 3. Producto — `product.template`

| Campo técnico | Tipo | Notas |
|---|---|---|
| `name` | Char | Obligatorio |
| `type` | Selección | **Solo** `consu` (bienes), `service`, `combo` |
| `is_storable` | Boolean | *Rastrear inventario*. Definido en el módulo `product`, pero solo tiene efecto con **Inventario**. Es el "producto almacenable" de antes |
| `categ_id` | Many2one → `product.category` | **Opcional** (no es obligatorio desde v19), pero en este cuaderno siempre se llena |
| `uom_id` | Many2one → `uom.uom` | Unidad; obligatorio (por defecto, *Unidades*) |
| `uom_ids` | Many2many → `uom.uom` | *Embalajes* adicionales (reemplaza `product.packaging`) |
| `default_code` | Char | Referencia interna |
| `barcode` | Char | **Único** dentro de la compañía (en v20 se almacena en la plantilla) |
| `list_price` | Float | Precio de venta |
| `standard_price` | Float | Coste |
| `sale_ok`, `purchase_ok` | Boolean | Si aparece en ventas / compras |
| `product_tag_ids` | Many2many | Etiquetas de producto |
| `weight`, `volume` | Float | Logística |
| `description_sale` | Text | Descripción visible al cliente |
| `seller_ids` | One2many → `product.supplierinfo` | Proveedores |
| `tracking` | Selección | `lot`, `serial` o vacío (= por cantidad). **En v20 ya no existe `none`** *(Inventario; se usa en la Fase 3)* |
| `store_by` | Selección calculada | *Rastreo* en el formulario (v20): `untracked`, `quantity`, `lot`, `serial`. Resume `is_storable` + `tracking`; para importar, usa esos dos |

### Proveedor del producto — `product.supplierinfo`
Se importa desde el mismo CSV del producto con notación de ruta:

| Columna en el CSV | Significado |
|---|---|
| `seller_ids/partner_id/id` | Proveedor (por ID externo) |
| `seller_ids/price` | Precio de compra |
| `seller_ids/delay` | Plazo de entrega en días |
| `seller_ids/min_qty` | Cantidad mínima |
| `seller_ids/product_code` | Código del producto en el catálogo del proveedor |

## 4. Unidades de medida — `uom.uom` (IDs externos útiles)

| ID externo | Unidad |
|---|---|
| `uom.product_uom_unit` | Unidades |
| `uom.product_uom_dozen` | Docenas |
| `uom.product_uom_pack_6` | Paquete de 6 |
| `uom.product_uom_kgm` | kg |
| `uom.product_uom_gram` | g |
| `uom.product_uom_litre` | L |
| `uom.product_uom_lb` / `uom.product_uom_oz` | lb / oz |
| `uom.product_uom_hour` / `uom.product_uom_day` | Horas / Días |
| `uom.product_uom_meter` / `uom.product_uom_cm` / `uom.product_uom_km` | m / cm / km |

> Desde v19 (y en v20) las unidades forman una **jerarquía** (`relative_uom_id` + `relative_factor`) en lugar de
> agruparse por categoría. La conversión sigue siendo automática entre unidades emparentadas.

## 5. Categorías de producto por defecto — `product.category`

| ID externo | Nombre |
|---|---|
| `product.product_category_goods` | Goods / Bienes |
| `product.product_category_services` | Services / Servicios |
| `product.product_category_expenses` | Expenses / Gastos |

## 6. Notación de columnas al importar

| Forma | Ejemplo | Cuándo usarla |
|---|---|---|
| `campo` | `name` | Campos simples |
| `campo` (Many2one por nombre) | `categ_id` → `Conservas` | Rápido, pero **depende del idioma** y falla con nombres repetidos |
| **`campo/id`** | `categ_id/id` → `andina.categ_conservas` | **Siempre en migraciones**: inequívoco e idempotente |
| `o2m/subcampo` | `seller_ids/price` | Importar líneas hijas desde el mismo archivo |
| `o2m/m2o/id` | `seller_ids/partner_id/id` | Relación dentro de una línea hija |
| `id` | `andina.cli_001` | ID externo del propio registro → permite **actualizar** |
| `product_variant_ids/id` | `andina.var_001` | Al importar en `product.template`, **da ID externo también a la variante** |

> **Plantilla ≠ variante.** Un ID externo creado al importar en `product.template` **no se puede usar**
> en un campo `product_id` (que apunta a `product.product`): Odoo responde
> *«Invalid external ID …: expected model 'product.product', found 'product.template'»*.
> Solución en el propio CSV del catálogo: la columna **`product_variant_ids/id`**, que crea el ID externo
> de la variante en el mismo paso. Regla del cuaderno: `product_tmpl_id/id` → `andina.prod_XXX`;
> `product_id/id` → `andina.var_XXX`.

## 7. Valores que Odoo acepta en la importación

| Tipo | Acepta | No acepta |
|---|---|---|
| Boolean | `True` / `False`, `1` / `0`, `verdadero` / `falso` | `sí`, `X`, `yes/no` mezclados |
| Float | `12.50` (punto decimal, según el formato configurado) | `12,50` si el separador esperado es el punto |
| Fecha | `AAAA-MM-DD` | `DD/MM/AAAA` sin ajustar el formato en el diálogo |
| Selección | El **valor técnico** (`consu`) o la etiqueta exacta mostrada | Sinónimos o traducciones libres |
| Many2many | IDs externos separados por coma, entre comillas | Punto y coma como separador |
