# E4 — Chuleta de nombres técnicos (Odoo 19)

> Verificado leyendo el código fuente de Odoo 19 (`odoo/addons/base`, `addons/product`,
> `addons/uom`, `addons/stock`, `addons/account`). **Varios campos cambiaron respecto de v16–v18**:
> los CSV y tutoriales de versiones anteriores fallan en v19 precisamente por esto.
>
> Cómo verificarlo tú mismo: activa el modo desarrollador y pasa el cursor sobre la etiqueta
> del campo, o abre *Ajustes → Técnico → Estructura de la base de datos → Campos*.

---

## 1. Cambios de v19 que rompen archivos antiguos

| Concepto | Antes (v16–v18) | **En v19** | Impacto |
|---|---|---|---|
| Producto almacenable | `type = 'product'` | `type = 'consu'` **+** `is_storable = True` | Un CSV con `type=product` **falla** |
| Unidad de compra | `uom_po_id` | **eliminado** — solo existe `uom_id` | La columna `uom_po_id` ya no se puede importar |
| Empaques del producto | modelo `product.packaging` | `uom_ids` (Many2many a `uom.uom`) | Cambia el modelado de "caja de 12" |
| Unidades de medida | `category_id` + `uom_type` + `factor` (editable) | `relative_factor` + `relative_uom_id` (jerarquía); `factor` sigue existiendo pero es **calculado** | Ya no hay "categoría de UdM"; no se puede importar `factor` |
| Celular del contacto | `mobile` | **eliminado** — solo `phone` | Una columna `mobile` provoca error de campo desconocido |
| Empresa / persona | `company_type` (`company`/`person`) | **eliminado**. `is_company` existe pero es **calculado y no importable**: sale de `vat` (y del tipo de identificación con la localización LATAM instalada) | Ni `company_type` ni `is_company` sirven como columna de CSV |
| Grupos del usuario | `groups_id` | `group_ids` | Rompe importaciones de usuarios |
| Categoría raíz de producto | `product.product_category_all` ("All") | `product.product_category_goods` ("Goods"), `..._services`, `..._expenses` | El ID externo antiguo **no existe** |

## 2. Contactos — `res.partner`

| Campo técnico | Tipo | Notas para importar |
|---|---|---|
| `name` | Char | Obligatorio |
| `is_company` | Boolean **calculado** | `True` si el contacto es su propia entidad comercial y tiene `vat`. **No se importa**: no tiene `inverse`. Con la localización LATAM instalada depende de `l10n_latam_identification_type_id` (RUC → empresa, DNI → persona). `company_type` ya no existe |
| `parent_id` | Many2one → `res.partner` | Empresa a la que pertenece el contacto hijo |
| `type` | Selección | `contact`, `invoice`, `delivery`, `other` |
| `vat` | Char | RUC/NIF. Solo se valida con la localización instalada |
| `ref` | Char | Referencia interna del contacto (código de cliente) |
| `street`, `zip`, `city` | Char | Texto libre |
| `state_id`, `country_id` | Many2one | Importar como `country_id/id` = `base.pe` |
| `phone`, `email`, `website` | Char | **No existe `mobile` en v19** |
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
| `is_storable` | Boolean | Añadido por **Inventario**. Es el "producto almacenable" de antes |
| `categ_id` | Many2one → `product.category` | Obligatorio |
| `uom_id` | Many2one → `uom.uom` | Unidad; obligatorio |
| `uom_ids` | Many2many → `uom.uom` | Empaques adicionales (reemplaza `product.packaging`) |
| `default_code` | Char | Referencia interna |
| `barcode` | Char | **Único** en toda la base |
| `list_price` | Float | Precio de venta |
| `standard_price` | Float | Coste |
| `sale_ok`, `purchase_ok` | Boolean | Si aparece en ventas / compras |
| `product_tag_ids` | Many2many | Etiquetas de producto |
| `weight`, `volume` | Float | Logística |
| `description_sale` | Text | Descripción visible al cliente |
| `seller_ids` | One2many → `product.supplierinfo` | Proveedores |
| `tracking` | Selección | `none`, `lot`, `serial` *(Inventario; se usa en la Fase 3)* |

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

> En v19 las unidades forman una **jerarquía** (`relative_uom_id` + `relative_factor`) en lugar de
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
