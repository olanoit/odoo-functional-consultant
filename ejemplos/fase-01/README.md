# Cuaderno de ejemplos — Fase 1: Fundamentos

Casos prácticos ejecutables para [`../../fases/fase-01-fundamentos.md`](../../fases/fase-01-fundamentos.md).
Todo gira alrededor de **ANDINA GOURMET S.A.C.** y usa datos listos para importar.

> **Versión objetivo:** Odoo 19 / saas-19.4. Los nombres técnicos de campos usados en los CSV fueron
> verificados contra el código fuente de esta versión (ver [`guias/E4-campos-tecnicos-v19.md`](guias/E4-campos-tecnicos-v19.md)):
> varios cambiaron respecto de v16–v18 y los archivos de tutoriales antiguos **ya no funcionan**.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-etiquetas-contacto.csv` | 10 etiquetas de segmentación de contactos |
| `datos/02-clientes.csv` | 25 clientes con RUC válido, ciudad, teléfono, etiquetas |
| `datos/03-proveedores.csv` | 15 proveedores clasificados por tipo de suministro |
| `datos/04-contactos-hijos.csv` | 10 contactos hijos: personas, direcciones de entrega y de facturación |
| `datos/05-categorias-producto.csv` | 11 categorías de producto en jerarquía de 3 niveles |
| `datos/06-productos.csv` | **79 productos**: terminados, insumos y servicios, con proveedor, costo y plazo. Crea plantilla (`andina.prod_XXX`) **y** variante (`andina.var_XXX`) |
| `datos/07-productos-con-errores.csv` | 9 filas con 8 errores de importación frecuentes, a propósito; **solo 5 los reporta Odoo** |
| `datos/08-clientes-actualizacion.csv` | 5 clientes para demostrar actualización sin duplicar |
| `guias/E1-matriz-de-permisos.md` | Los 4 usuarios de la fase, sus grupos y las pruebas de acceso |
| `guias/E2-ejercicios-busqueda-reportes.md` | 15 ejercicios de filtros, agrupaciones y pivote |
| `guias/E3-errores-de-importacion.md` | Síntoma → causa → solución de cada error provocado |
| `guias/E4-campos-tecnicos-v19.md` | Chuleta de nombres técnicos verificados en v19 |
| `soluciones/` | Respuestas de los ejercicios y del cuestionario de la fase |

## Antes de empezar

1. Base de datos **`LAB`**, creada **sin datos demo**, idioma español, país Perú.
2. Apps instaladas: **Contactos, Ventas, Inventario, Compras**.
3. **Modo desarrollador activado** (Ajustes → Herramientas para desarrolladores).
4. Descarga esta carpeta `datos/` a tu equipo: los archivos se suben desde el diálogo de importación.

> **Codificación:** los CSV están en **UTF-8 sin BOM**. Si los abres y guardas con Excel en Windows,
> revisa que los acentos no se rompan; en el diálogo de importación de Odoo, el campo *Codificación*
> debe decir `utf-8`. Es el error más tonto y más frecuente de una migración.

---

## Ejemplo 1 — Reconocimiento: instalar y desinstalar un módulo
*(Bloque 1.1 · 30 min · base `SANDBOX`)*

1. Ve a **Aplicaciones**, quita el filtro *Aplicaciones* del buscador y observa la diferencia entre
   **apps** (paquetes visibles) y **módulos** (piezas técnicas). Cuenta cuántos hay de cada uno.
2. Abre el formulario de un producto cualquiera y **captura la pantalla** (o anota las pestañas que ves).
3. Instala **Encuestas**. Observa: aparece un menú nuevo, pero el producto no cambió.
4. Instala **Compras**. Vuelve al producto: ahora hay pestaña **Compra**, con el campo *Proveedores*
   y el control de facturas. **Un módulo añadió campos a un modelo que ya existía.**
   *(Nota v19: el antiguo campo "Unidad de medida de compra" ya no existe; ver `guias/E4-campos-tecnicos-v19.md`.)*
5. Desinstala **Encuestas** y responde en tu bitácora: ¿qué pasó con las encuestas que había?

**Qué debes poder explicar al terminar:** por qué instalar Contabilidad cambia el formulario de Producto,
y por qué desinstalar no es lo mismo que "deshacer".

> ⚠️ Nunca desinstales un módulo en producción para "probar". Se lleva sus datos por delante.

---

## Ejemplo 2 — Configuración de la compañía ANDINA GOURMET
*(Bloque 1.4 · 45 min · base `LAB`)*

Configura en **Ajustes → Usuarios y compañías → Compañías**:

| Campo | Valor |
|---|---|
| Nombre | ANDINA GOURMET S.A.C. |
| RUC (NIF/Tax ID) | `20510211015` *(ficticio, con dígito verificador válido)* |
| Dirección | Av. Los Frutales 1250, Ate — Lima — Perú |
| Teléfono | +51 1 7015000 |
| Correo | contacto@andinagourmet.com.pe |
| Moneda | PEN (S/) |
| Idioma | Español |
| Zona horaria | America/Lima |

Luego, en **Ajustes → Configuración general**:
- Activa **Múltiples monedas** (la usarás en la Fase 4 para las compras en USD).
- Activa **Unidades de medida** y **Variantes de producto** (Inventario / Ventas).
- Revisa el formato de números y fechas del idioma español.

**Verificación:** crea un presupuesto vacío y comprueba que el importe sale como `S/ 0.00`.
Si sale `$`, la moneda de la compañía está mal y **todo** lo que hagas después estará mal.

---

## Ejemplo 3 — Los 4 usuarios y sus permisos
*(Bloque 1.4 · 60 min · base `LAB`)*

Sigue [`guias/E1-matriz-de-permisos.md`](guias/E1-matriz-de-permisos.md): crea los 4 usuarios
(vendedor, comprador, almacenero, gerente), asigna los grupos indicados y **ejecuta las 12 pruebas de acceso**
entrando con cada uno en una ventana privada.

El objetivo real del ejercicio no es crear usuarios: es **ver con tus ojos la diferencia entre
un grupo (qué menús ve) y una regla de registro (qué filas ve)** con el caso
*"Ver solo lo propio"* vs. *"Ver todo"* del vendedor.

---

## Ejemplo 4 — Importar contactos con relaciones
*(Bloque 1.6 · 60 min · base `LAB`)*

**Orden de carga obligatorio** (cada archivo depende del anterior):

```
01-etiquetas-contacto.csv  →  02-clientes.csv  →  03-proveedores.csv  →  04-contactos-hijos.csv
```

Para cada archivo:
1. Abre la lista del modelo correspondiente (Contactos, o Ajustes → Técnico → Etiquetas de contacto).
2. **Favoritos → Importar registros → Subir archivo**.
3. Verifica que la codificación sea `utf-8` y el separador `,`.
4. **Probar importación** antes de importar. Lee los mensajes. Solo entonces, **Importar**.

### Qué mirar en cada archivo

**`01-etiquetas-contacto.csv`** — modelo `res.partner.category`. Se importa **primero** porque los
clientes la referencian. Fíjate en la columna `id`: son **identificadores externos** con prefijo `andina.`.

**`02-clientes.csv`** — modelo `res.partner`. Columnas que debes entender:

| Columna | Por qué está así |
|---|---|
| `id` | ID externo propio (`andina.cli_001`) → permite reimportar y **actualizar** |
| *(sin columna empresa/persona)* | En v19 `company_type` no existe e `is_company` es **calculado**: Odoo marca como empresa a todo contacto sin padre que tenga `vat`. Por eso los 25 clientes salen como empresas **sin declararlo** |
| `vat` | RUC. Sin la localización peruana instalada **no se valida** (eso llega en la Fase 10) |
| `country_id/id` | `base.pe` → referencia por **ID externo**, inmune al idioma de la base |
| `category_id/id` | Many2many: varios IDs externos separados por coma, entre comillas |
| `customer_rank` | `1` marca el contacto como cliente. Es lo que lo hace aparecer en Ventas |

> **La lección del `/id`**: `country_id` esperaría el texto *"Perú"* (y fallaría si la base está en inglés);
> `country_id/id` espera el ID externo `base.pe` y **funciona siempre**. Usa siempre `/id` en migraciones.

**`04-contactos-hijos.csv`** — el mismo modelo `res.partner`, pero con `parent_id/id` apuntando al
cliente y `type` definiendo su rol: `contact` (persona), `delivery` (dirección de entrega),
`invoice` (dirección de facturación).

**Verificación:** abre `Distribuidora Sol de Oro S.A.C.` → pestaña **Contactos y direcciones**:
debe tener 3 hijos (una persona, una dirección de entrega, una de facturación).
Ese cliente tendrá dos direcciones distintas en la Fase 2 al cotizar y entregar.

---

## Ejemplo 5 — Importar el catálogo de productos
*(Bloque 1.6 · 45 min · base `LAB`)*

Orden: `05-categorias-producto.csv` → `06-productos.csv`.

### Lo que hay dentro de los 79 productos

| Grupo | Cantidad | Características |
|---|---|---|
| Conservas, snacks, harinas, bebidas | 48 | `sale_ok=True`, con código de barras EAN-13 válido y peso |
| Materia prima y aditivos | 13 | En **kg** y **litros**, con proveedor, precio y plazo de entrega |
| Envases y embalajes | 12 | Compra por unidad, con cantidad mínima de pedido |
| Servicios | 6 | `type=service`, `is_storable` vacío — no hay stock de un servicio |

### Columnas que enseñan algo

| Columna | Lección |
|---|---|
| `type` | En **v19** solo acepta `consu`, `service` o `combo`. El valor `product` de versiones anteriores **ya no existe** |
| `is_storable` | Es lo que reemplaza al antiguo "producto almacenable". Requiere Inventario instalado |
| `uom_id/id` | `uom.product_uom_unit`, `uom.product_uom_kgm`, `uom.product_uom_litre` — por ID externo |
| `categ_id/id` | Apunta a las categorías del archivo 05, no a las de Odoo |
| `seller_ids/partner_id/id` | Importa una **línea One2many** (el proveedor) desde el mismo CSV |
| `seller_ids/price`, `/delay`, `/min_qty` | Precio de proveedor, plazo en días y cantidad mínima → los usarás en la Fase 3 para reglas de reordenamiento |
| `product_variant_ids/id` | **Crea también el ID externo de la variante** (`andina.var_001`). Sin esta columna, `andina.prod_001` sería solo la *plantilla* y todos los CSV que piden `product_id` (stock, lotes, líneas de pedido, componentes de LdM) fallarían con *«expected model product.product, found product.template»* |

> **Plantilla vs. variante — el detalle que rompe medio cuaderno.** El catálogo se importa en
> `product.template` (el menú *Productos*), pero `stock.quant`, `stock.lot`, `sale.order.line`,
> `purchase.order.line`, `mrp.bom.line` y `delivery.carrier` apuntan a **`product.product`** (la variante).
> Un ID externo de plantilla **no sirve** ahí. Por eso el CSV trae `product_variant_ids/id`: en el mismo
> paso crea la plantilla `andina.prod_XXX` **y** su variante `andina.var_XXX`. A partir de la Fase 2,
> todo lo que sea `product_id/id` usa `andina.var_XXX`; lo que sea `product_tmpl_id/id`, `andina.prod_XXX`.

**Verificaciones después de importar:**
1. Filtra por categoría *Materia Prima*: 9 productos, todos en kg o litros, todos con proveedor.
2. Abre *Aguaymanto fresco* → pestaña **Compra**: proveedor Agroexportadora Valle Sagrado, S/ 8.50, 5 días.
3. Agrupa la lista de productos por **Categoría de producto** y comprueba la jerarquía de 3 niveles.
4. Busca `CON-AGU-400g` por referencia interna: debe encontrarlo al teclear el código.

---

## Ejemplo 6 — Romper la importación a propósito
*(Bloque 1.6 · 45 min · base `LAB`)* ← **el ejercicio más valioso de la fase**

Importa `07-productos-con-errores.csv` con **Probar importación**.

**Antes de leer la solución**, escribe en tu bitácora tu diagnóstico de cada fila.
Las 9 filas contienen 8 errores distintos (uno se repite en dos filas):

| Fila | Producto | Pista |
|---|---|---|
| 1 | Conserva de Mango | Mira la columna `type` |
| 2 | Mermelada de Mango | Mira `categ_id/id` contra el archivo 05 |
| 3 | Snack de Maca | Mira el precio |
| 4 y 5 | Harina de Maca | Mira la columna `id` de ambas |
| 6 | *(sin nombre)* | Falta algo obligatorio |
| 7 | Néctar de Maracuyá | Mira la unidad de medida |
| 8 | Conserva de Higo | Compara su código de barras con el del producto `andina.prod_001` |
| 9 | Barra de Maca | Mira `is_storable` |

> **La trampa del ejercicio.** Odoo **no rechaza el archivo entero**: verificado en v19, solo avisa
> de **5 de los 8 errores**. Los otros 3 se importan mal en silencio —un precio cien veces mayor, un
> producto que desaparece y un booleano inventado— y ninguno se ve en la pantalla de resultados.
>
> Así que el ejercicio no termina cuando Odoo deja de quejarse. Termina cuando **cuentas los
> registros creados** y **compruebas los valores** contra el archivo. Anota antes de importar cuáles
> de las 9 filas crees que Odoo va a reportar; acertar eso vale más que diagnosticar los 8 errores.

Luego contrasta con [`guias/E3-errores-de-importacion.md`](guias/E3-errores-de-importacion.md),
que trae el mensaje esperado, la causa y la corrección de cada uno, y marca cuáles son silenciosos.

**Cierre del ejercicio:** corrige el archivo y consigue importarlo **sin errores**.
Ese archivo corregido —y tu diagnóstico— son el borrador de tu *checklist personal de importación*,
uno de los entregables de la Fase 11.

---

## Ejemplo 7 — Actualizar sin duplicar (el súperpoder)
*(Bloque 1.6 · 30 min · base `LAB`)*

1. Cuenta cuántos contactos tienes (debe ser 50: 25 clientes + 15 proveedores + 10 hijos).
2. Importa `08-clientes-actualizacion.csv`.
3. Vuelve a contar: **siguen siendo 50**. Cambiaron teléfono y correo de 5 clientes.
4. Ahora repite el experimento **borrando la columna `id`** del archivo (guarda una copia antes):
   importa de nuevo → ahora tienes **55 contactos**, con 5 duplicados.
5. Deshaz el desastre archivando los duplicados.

**La lección, escrita en tu bitácora en una frase:**
> Sin ID externo, cada corrección crea duplicados; con ID externo, cada importación es idempotente.

Complemento: exporta 10 clientes con la casilla **"Quiero actualizar datos (importación compatible)"**
activada y compara el archivo resultante con el que importaste. Fíjate en cómo Odoo exporta las
relaciones (`/id`) y por qué ese formato se puede reimportar tal cual.

---

## Ejemplo 8 — Preguntas de negocio con la interfaz
*(Bloque 1.2 · 45 min · base `LAB`)*

Resuelve los 15 ejercicios de [`guias/E2-ejercicios-busqueda-reportes.md`](guias/E2-ejercicios-busqueda-reportes.md)
usando solo filtros, agrupaciones, vista pivote y vista gráfico. **Sin exportar a Excel.**

Guarda como **favorito compartido** los 3 filtros que pide el laboratorio de la fase y
un reporte pivote que responda una pregunta de gerencia.

---

## Cierre: el entregable de la fase

Con los ejemplos 2 a 7 ya tienes el laboratorio integrador de la Fase 1 casi completo. Falta:

- [ ] Los 3 filtros favoritos compartidos y el reporte pivote guardado (Ejemplo 8).
- [ ] El documento *"Guía de navegación y datos maestros de ANDINA GOURMET"* (2–4 páginas):
      cómo dar de alta un cliente y un producto, con las convenciones que acabas de usar
      (referencia interna, categorías, etiquetas, unidad de medida).
- [ ] Respaldo `LAB_fase01_AAAAMMDD.zip`.
- [ ] Cuestionario de la fase respondido; contrasta con
      [`soluciones/respuestas-cuestionario-fase-01.md`](soluciones/respuestas-cuestionario-fase-01.md)
      **solo después** de haberlo respondido.

## Reutilización en fases siguientes

Estos datos **no se tiran**: la base `LAB` sigue creciendo sobre ellos.

| Fase | Qué reutiliza |
|---|---|
| 2 — Ventas | Los 25 clientes y sus etiquetas para segmentar listas de precios |
| 3 — Inventario | Los 79 productos, sus proveedores, plazos y cantidades mínimas |
| 4 — Contabilidad | Las ventas y compras generadas sobre estos maestros |
| 5 — Manufactura | Insumos y envases como componentes de la lista de materiales |
| 10 — Localización PE | Los RUC (que **entonces sí** se validarán) |



---

## Para ampliar

### Cybrosys — libro de Odoo 19 y artículos

Enlaces verificados uno a uno. Todos están **en inglés**.

**Capítulos del [libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)**: [Contacts](https://www.cybrosys.com/odoo/odoo-books/v19/contacts/)

| Artículo | Para qué en esta fase | Fecha |
|---|---|---|
| [How Data File Loading Works in Odoo 19](https://www.cybrosys.com/blog/how-data-file-loading-works-in-odoo-19) | Orden de carga de los archivos de datos y por qué el orden importa | *ene 2026* |
| [Overview of Access Control Lists (ACLs) in Odoo 19](https://www.cybrosys.com/blog/overview-of-access-control-lists-acls-in-odoo-19) | Grupos de seguridad y permisos, el tema del Ejemplo 5 | *dic 2025* |

### Odoo en Español — YouTube

[**Buscar «importar datos» en el canal**](https://www.youtube.com/@OdooSpanish/search?query=importar+datos) — vídeos en español sobre importación de datos, contactos y permisos.

> El canal no publica un índice enlazable por tema, así que el enlace abre la **búsqueda dentro del
> canal**: siempre devuelve lo que haya publicado sobre el tema, aunque renombre o reordene sus
> vídeos. El canal completo está en <https://www.youtube.com/@OdooSpanish>.

> **Úsalos para el concepto, no para la configuración.** Todo lo marcado con ⚠️ es de una versión
> anterior, y aun en los artículos de v19 conviene contrastar los nombres de campo: verifica contra
> la documentación 19.4, contra [la tabla de cambios de v19](../fase-12/README.md#los-cambios-de-v19-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
