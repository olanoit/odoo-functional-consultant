# Cuaderno de ejemplos — Fase 12: Capstone y certificación

Material de cierre para [`../../fases/fase-12-capstone-certificacion.md`](../../fases/fase-12-capstone-certificacion.md).

---

## Contenido

| Archivo | Qué es |
|---|---|
| `guias/Q1-guion-del-capstone.md` | Plan día a día de las 4 semanas del proyecto integrador |
| `simulacro/preguntas.md` | **Simulacro de 60 preguntas** en 45 minutos |
| `simulacro/respuestas.md` | Clave, explicaciones de las más falladas y mapa de repaso por fase |

---

## Cómo usar este cuaderno

### 1. Antes del capstone: diagnóstico

Haz el simulacro **en frío**, cronometrado, antes de empezar el proyecto integrador.
Corrígelo con la penalización real (−0.5 por error) y usa el **mapa de preguntas por fase** para
identificar qué cuadernos necesitas repasar. Repásalos **antes** de construir `CAPSTONE`, no después.

### 2. Durante el capstone

Sigue [`guias/Q1-guion-del-capstone.md`](guias/Q1-guion-del-capstone.md). Cuatro semanas, cuatro
gates. Si un gate no se cumple, no avances: el capstone no es una carrera, es la demostración de que
puedes implementar de punta a punta.

### 3. Antes del examen oficial

1. Repite el simulacro. Deberías superar 50/60.
2. Haz el **examen de muestra oficial** (gratuito):
   <https://www.odoo.com/slides/odoo-functional-certification-sample-test-50>
3. Repasa los cuestionarios B de las 12 fases en una sola sesión.
4. Refuerza los temas que la Fase 12 marca como los más fallados.
5. Agenda el examen: <https://www.odoo.com/slides/odoo-19-functional-certification-502>

---

## Los cambios de v19 que hay que llevar frescos al examen

Este plan los documentó fase por fase, verificándolos en el código fuente. Son los que más
probablemente aparezcan y los que más gente falla por venir de versiones anteriores:

| Área | Cambio |
|---|---|
| Producto | `type = product` **ya no existe** → `consu` + `is_storable` |
| Producto | `uom_po_id` (unidad de compra) **eliminado**; `product.packaging` → `uom_ids` |
| Contacto | `mobile` **eliminado**; solo `phone` |
| Usuario | `groups_id` → **`group_ids`** |
| Categoría | `product_category_all` → **`product_category_goods`** |
| CRM | `crm.stage.team_id` → **`team_ids`** (Many2many); nuevo `rotting_threshold_days` |
| Ventas | Opcionales de plantilla: modelo propio → línea con **`is_optional`** |
| Ventas | Variantes importables con **`import_attribute_values`** (`"Atributo:Valor"`) |
| Inventario | `stock.production.lot` → **`stock.lot`** |
| Inventario | Valoración `manual_periodic` → **`periodic`**; nuevo `lot_valuated` |
| Inventario | `qty_multiple` **eliminado** en reglas de reordenamiento |
| Contabilidad | `account.fiscal.position.tax` **eliminado** → `original_tax_ids` + `fiscal_position_ids` |
| Contacto | `company_type` **eliminado**; `is_company` es **calculado** (desde `vat` / tipo de identificación) y no se importa |
| Producto | ID externo de plantilla ≠ de variante: para `product_id` hace falta `product_variant_ids/id` |
| Compras | Línea: `product_uom_id` → **`uom_id`**; `taxes_id` → **`tax_ids`**; el estado `done` ya no existe |
| Contabilidad | `account.account.deprecated` **eliminado** → `active`; `account.analytic.plan` sin `company_id` |
| Inventario | Categoría: `property_stock_account_input_categ_id`/`_output_categ_id` → **`account_stock_variation_id`** |
| Inventario | **`stock.valuation.layer` eliminado**: el importe está en `stock.move.value`; el producto usa `total_value` / `avg_cost` (antes `value_svl` / `quantity_svl`) |
| Inventario | `stock.move` pierde `name` y `product_uom`: descripción en `description_picking`, unidad heredada del producto |
| Contabilidad | **Los movimientos de existencias ya no generan asiento al validarse**: perpetua (`real_time`) contabiliza al facturar, periódica (`periodic`) al cierre |
| Contabilidad | El **costo de ventas** va en el mismo asiento que la factura de venta; la cuenta transitoria de entrada de existencias desapareció |
| Contactos | El modelo **`res.bank` ya no existe**: las cuentas bancarias viven en `res.partner.bank` |
| Localización PE | La documentación oficial cita `l10n_pe_edi_stock_20` y `l10n_pe_website_sale`, que **no existen** en saas-19.4; el proveedor de firma `digiflow` se llama ahora **«Estela»** |
| RR. HH. | `hr.leave.type` **eliminado** → **`hr.work.entry.type`** (con `code` obligatorio); `time_type` → **`count_as`** |
| RR. HH. | `resource.calendar` **sin `tz`**: la zona horaria vive en el empleado |
| UdM | `uom.category_id` y `uom_type` **eliminados**; `factor` pasa a ser **calculado** |
| Contabilidad | Modelos de conciliación: `rule_type` → **`trigger`** |
| Contabilidad | `account.account.company_id` → **`company_ids`** (Many2many) |
| RR. HH. | `hr.contract` **eliminado** → **`hr.version`** |

---

## Después de la certificación

- Publica la credencial y actualiza tu perfil.
- Guarda tu bitácora y tus entregables: son tu **portafolio** y tu kit reutilizable.
- Elige una especialización: contabilidad + localización, manufactura, o retail/PdV.
- Si quieres dar el salto técnico, empieza por los
  [tutoriales de desarrollador](https://www.odoo.com/documentation/saas-19.4/es/developer/tutorials.html).

> A partir de aquí el aprendizaje sigue con clientes reales, y el método no cambia:
> **leer la documentación, configurar, romper a propósito, explicar. Y documentar todo.**



---

## Para ampliar

### Cybrosys — libro de Odoo 19 y artículos

Enlaces verificados uno a uno. Todos están **en inglés**.

**Capítulos del [libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)**: [Índice completo del libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)

| Artículo | Para qué en esta fase | Fecha |
|---|---|---|
| [The Ultimate Guide to Odoo 19 New Features and Enhancements](https://www.cybrosys.com/blog/the-ultimate-guide-to-odoo-19-new-features-and-enhancements) | Repaso de las novedades de v19 módulo por módulo — para el examen | *sep 2025* |

### Odoo en Español — YouTube

[**Buscar «Odoo 19 novedades» en el canal**](https://www.youtube.com/@OdooSpanish/search?query=Odoo+19+novedades) — vídeos en español sobre las novedades de Odoo 19.

> El canal no publica un índice enlazable por tema, así que el enlace abre la **búsqueda dentro del
> canal**: siempre devuelve lo que haya publicado sobre el tema, aunque renombre o reordene sus
> vídeos. El canal completo está en <https://www.youtube.com/@OdooSpanish>.

> **Úsalos para el concepto, no para la configuración.** Todo lo marcado con ⚠️ es de una versión
> anterior, y aun en los artículos de v19 conviene contrastar los nombres de campo: verifica contra
> la documentación 19.4, contra la tabla de cambios de v19 de este mismo cuaderno y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
