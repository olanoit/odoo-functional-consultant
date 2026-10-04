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
   <https://www.odoo.com/slides/odoo-certification-sample-test-50>
3. Repasa los cuestionarios B de las 12 fases en una sola sesión.
4. Refuerza los temas que la Fase 12 marca como los más fallados.
5. Agenda el examen. La certificación de **Odoo 20 aún no está publicada** (comprobado el
   04-10-2026): revisa el [listado de certificaciones](https://www.odoo.com/slides?slide_category=certification).
   Mientras tanto, la vigente es la de Odoo 19:
   <https://www.odoo.com/slides/odoo-19-functional-certification-502> · en español:
   <https://www.odoo.com/slides/certificacion-funcional-de-odoo-19-espanol-517>

---

## Los cambios de v20 que hay que llevar frescos al examen

Este plan los documentó fase por fase, verificándolos en el código fuente de Odoo 20.0 (comparado
con saas-19.4). Son los que más probablemente aparezcan y los que más gente falla por venir de
versiones anteriores.

> **Ojo con la versión del examen.** Mientras no se publique la certificación de Odoo 20, el examen
> disponible es el de **Odoo 19**, que pregunta por el comportamiento de v19. La columna *Desde*
> te dice qué cambios ya aplican en v19 (y entran en ese examen) y cuáles son **nuevos de v20**.

### A. Novedades de v20 (respecto de saas-19.4)

| Área | Cambio | Desde |
|---|---|---|
| Aplicaciones | **Servicio de campo** ya no es `industry_fsm`: la app es `planning_field_service` (sobre Planificación). `industry_fsm` existía en 19.0 y desapareció en las versiones saas-19.x | v20 (ya en saas-19.x) |
| Aplicaciones | La app **IA** pasa de `ai_app` a **`ai_agentic`** (agentes y herramientas de IA) | v20 |
| Aplicaciones | **Traslados por lote, olas y en grupos** ya no son un módulo aparte (`stock_picking_batch` eliminado): se activan con una opción de Inventario (`group_stock_picking_batch`) | v20 |
| Aplicaciones | `base_vat` eliminado: la validación del NIF/RUC está en `base` y la consulta VIES en `account` (+ `l10n_eu_account_vies`) | v20 |
| Seguridad | Desde las saas-19.x los permisos por modelo y las reglas de registro (`ir.model.access` + `ir.rule`) son un único modelo, **`ir.access`** (*Técnico → Seguridad → Permisos de acceso*) | v20 (ya en saas-19.x) |
| Usuarios | El tipo de usuario interno se desdobla: `role` = *Light* (`light_user`) · *Usuario* (`regular_user`) · *Administrador*; nuevo grupo `base.group_user_regular` (el menú Contactos lo exige) | v20 |
| Contactos / Localización | **`l10n_latam_base` eliminado**: desaparece el *Tipo de identificación* (`l10n_latam_identification_type_id`). El RUC va en `vat` y DNI, CE, pasaporte… en **`additional_identifiers`** (JSON, p. ej. `{"PE_DNI": "12345678"}`); `l10n_pe` calcula `l10n_pe_sunat_id_code` / `l10n_pe_sunat_id_value` | v20 |
| Contactos | `is_company` = entidad comercial propia **y** con NIF (`has_vat`); el RUC se valida siempre al guardar o importar si el contacto tiene país | v20 |
| Aplicaciones | Eliminados también `portal_address_extended` y `hr_work_entry_attendance` | v20 |
| Ventas | `require_payment` **eliminado** en pedido y plantilla: el pago en línea se expresa solo con `prepayment_percent` (0 = no se exige pago); nuevo `prepayment_amount` | v20 |
| Ventas | Listas de precios: `compute_price` pasa de `percentage` / `formula` / `fixed` a **`discount`** (*Descuento*) / **`markup`** (*Surcharge*) / `fixed` (*Precio fijo*); `percent_price` eliminado (el descuento usa `price_discount`) | v20 |
| Ventas / Compras | Nuevas cuentas de **periodificación** en la categoría de producto: *Invoices to be Issued* / *Invoiced Not Delivered* (ventas) y *Bills to Receive* / *Billed Not Received* (compras) | v20 |
| Ventas | Cambiar la lista de precios del pedido **recalcula al instante** todas las líneas; desaparece el botón *Actualizar precios* | v20 |
| Ventas / Producto | Cada **variante guarda su propio precio de venta** (`lst_price`); ya no es precio de plantilla + extras de atributos (verificado importando variantes en v20) | v20 |
| CRM | `crm.team` pierde el objetivo de facturación (`invoiced_target`) | v20 |
| Producto / Inventario | Nuevo campo **`store_by`** (*Seguimiento*: Ninguno · Por cantidad · Por lotes · Por número de serie único) que combina `is_storable` + `tracking`; `tracking` ya no tiene el valor `none` | v20 |
| Inventario | Reglas de reordenamiento: mín./máx. sugeridos según la demanda (`min_max_based_on`: últimos 7/30 días, 3/12 meses, año anterior… o *Custom Demand* con `daily_demand`) | v20 |
| Inventario | Costos en destino: cada línea indica a qué productos se aplica (`apply_on_product_ids`) | v20 |
| Inventario / Contabilidad | Los campos de valoración de la categoría (`property_valuation`, `property_cost_method`, cuentas y diario de existencias) y sus valores por defecto en la compañía pasan de `stock_account` al módulo **`account`**; PEPS (FIFO) sigue llegando con `stock_account` | v20 |
| Inventario | Cambiar el método de costo **revalúa hacia atrás** desde el último cierre de inventario; las ubicaciones valoradas usan un solo campo `is_valued` | v20 |
| Inventario / Contabilidad | El informe de valoración pasa a `account.stock.valuation.report` (*Contabilidad → Revisión → Inventario*), con sección de periodificaciones y botón *Generate Entries* (periodificaciones con reversión + cierre de existencias) | v20 |
| Manufactura | La LdM ya no tiene consumo *Estricto / Flexible* (`consumption`): siempre avisa del consumo distinto al previsto | v20 (ya en saas-19.x) |
| Manufactura | La LdM tiene **costo adicional por unidad** (`extra_cost`: mano de obra, energía, embalaje) | v20 |
| Manufactura | PLM: la ECO pierde el campo *Aplicar en* (`type`) | v20 |
| Contabilidad | Modelos de conciliación: vuelve **`rule_type`** con otro significado — *Matching rule* (regla de coincidencia, con `payment_tolerance` y `matching_order`) o *Reconciliation model*; `trigger` se mantiene | v20 |
| Contabilidad | Activos con **varios libros** (multi-ledger): los datos de depreciación viven en `account.asset.variant` | v20 |
| Contabilidad | Las cuentas de liquidación de impuestos (a pagar / a cobrar / anticipos) pasan del grupo de impuestos (`account.tax.group`) al tipo de declaración (`account.return.type`) | v20 |
| Punto de venta | La contabilización ya no es un asiento por sesión: se genera una **factura resumen** al *cliente por defecto* del PdV en el *diario de cierre*, y una nota de crédito aparte para las devoluciones. Por defecto se contabiliza **a diario** a una hora fija (4:00), aunque la sesión siga abierta (`session_closing_mode`) | v20 |
| Punto de venta | La sesión pierde `cash_control` y `move_id`; el método de pago pierde `split_transactions` e `is_cash_count` | v20 |
| RR. HH. | Horas extra: las reglas de asistencia (`hr.attendance.overtime.ruleset`) se sustituyen por **reglas de tiempo** (`hr.time.rule`, en `hr_work_entry`); la asistencia tiene estado (*Borrador* · *Validated* · *Rechazado*) y tipo de entrada de trabajo | v20 |
| RR. HH. | Acumulación de ausencias: `postpone_max_days` → **`max_carriedover_duration`**; el horario de trabajo puede llevar un plan de acumulación (`leave_accrual_plan_id`) | v20 |
| RR. HH. | Nómina: desaparece `hr.payslip.input.type`; la entrada de nómina apunta directamente a la regla salarial | v20 |
| RR. HH. | Horarios de trabajo con **horario de referencia** (`reference_calendar_id`) del que sale la jornada completa | v20 |
| Marketing | Automatización de marketing renovada: nuevas actividades (*Split*, nota, suscribir a lista…) y disparadores (fecha, aniversario, webhook, bajo demanda); en correo masivo los favoritos pasan a **plantillas** (`is_template`) | v20 |
| Proyecto | Colaboradores del portal: `limited_access` → **`access_mode`** (*Vista* · *Editar* · *Advanced Edit*) | v20 |
| Servicio de asistencia | Las valoraciones se activan **por etapa** (`rating_active` en `helpdesk.stage`), ya no por equipo (`use_rating`) | v20 |
| Dispositivos | Balanzas conectables **directamente al navegador** (Web Serial, `iot_webserial`) en PdV y control de calidad, sin IoT Box | v20 |

### B. Cambios de v19 que siguen vigentes en v20

| Área | Cambio | Desde |
|---|---|---|
| Producto | `type = product` **ya no existe** → `consu` + `is_storable` | v18 |
| Producto | `uom_po_id` (unidad de compra) **eliminado**; `product.packaging` → `uom_ids` | v19 |
| Contacto | `mobile` **eliminado**; solo `phone` | v19 |
| Usuario | `groups_id` → **`group_ids`** | v19 |
| Categoría | `product_category_all` → **`product_category_goods`** | v19 |
| CRM | `crm.stage.team_id` → **`team_ids`** (Many2many); nuevo `rotting_threshold_days` | v19 |
| Ventas | Opcionales de plantilla: modelo propio → línea con **`is_optional`** (en v20, en la sección) | v19 |
| Ventas | Variantes importables con **`import_attribute_values`** (`"Atributo:Valor"`) | v19 |
| Inventario | `stock.production.lot` → **`stock.lot`** | v16 |
| Inventario | Valoración `manual_periodic` → **`periodic`**; nuevo `lot_valuated` | v19 |
| Inventario | `qty_multiple` **eliminado** en reglas de reordenamiento | v19 |
| Contabilidad | `account.fiscal.position.tax` **eliminado** → `original_tax_ids` + `fiscal_position_ids` | v19 |
| Contacto | `company_type` **eliminado**; `is_company` es **calculado** (desde `vat`; en v20 ya no hay tipo de identificación) y no se importa | v19 |
| Producto | ID externo de plantilla ≠ de variante: para `product_id` hace falta `product_variant_ids/id` | v19 |
| Compras | Línea: `product_uom_id` → **`uom_id`**; `taxes_id` → **`tax_ids`**; el estado `done` ya no existe | v19 |
| Contabilidad | `account.account.deprecated` **eliminado** → `active`; `account.analytic.plan` sin `company_id` | v19 |
| Inventario | Categoría: `property_stock_account_input_categ_id`/`_output_categ_id` → **`account_stock_variation_id`** | v19 |
| Inventario | **`stock.valuation.layer` eliminado**: el importe está en `stock.move.value`; el producto usa `total_value` / `avg_cost` (antes `value_svl` / `quantity_svl`) | v19 |
| Inventario | `stock.move` pierde `name` y `product_uom`: descripción en `description_picking`, unidad heredada del producto | v19 |
| Contabilidad | **Los movimientos de existencias ya no generan asiento al validarse**: perpetua (`real_time`) contabiliza al facturar, periódica (`periodic`) al cierre | v19 |
| Contabilidad | El **costo de ventas** va en el mismo asiento que la factura de venta; la cuenta transitoria de entrada de existencias desapareció | v19 |
| Contactos | El modelo **`res.bank` ya no existe**: las cuentas bancarias viven en `res.partner.bank` | v19 |
| Localización PE | La documentación oficial (también la de 20.0) cita `l10n_pe_edi_stock_20` y `l10n_pe_website_sale`, que **no existen** en el código; el proveedor de firma `digiflow` se llama ahora **«Estela»** | v19 |
| RR. HH. | `hr.leave.type` **eliminado** → **`hr.work.entry.type`** (con `code` obligatorio); `time_type` → **`count_as`** | v19 |
| RR. HH. | `resource.calendar` **sin `tz`**: la zona horaria vive en el empleado | v19 |
| UdM | `uom.category_id` y `uom_type` **eliminados**; `factor` pasa a ser **calculado** | v19 |
| Contabilidad | Modelos de conciliación: `rule_type` → **`trigger`** (en v20 `rule_type` reaparece con otro significado: ver tabla A) | v19 |
| Contabilidad | `account.account.company_id` → **`company_ids`** (Many2many) | v19 |
| RR. HH. | `hr.contract` **eliminado** → **`hr.version`** | v19 |

---

## Después de la certificación

- Publica la credencial y actualiza tu perfil.
- Guarda tu bitácora y tus entregables: son tu **portafolio** y tu kit reutilizable.
- Elige una especialización: contabilidad + localización, manufactura, o retail/PdV.
- Si quieres dar el salto técnico, empieza por los
  [tutoriales de desarrollador](https://www.odoo.com/documentation/20.0/developer/tutorials.html).

> A partir de aquí el aprendizaje sigue con clientes reales, y el método no cambia:
> **leer la documentación, configurar, romper a propósito, explicar. Y documentar todo.**



---

## Para ampliar

### Cybrosys — libro de Odoo 19 y artículos

Enlaces verificados uno a uno. Todos están **en inglés**.

**Capítulos del [libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)**: [Índice completo del libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)

| Artículo | Para qué en esta fase | Fecha |
|---|---|---|
| [The Ultimate Guide to Odoo 19 New Features and Enhancements](https://www.cybrosys.com/blog/the-ultimate-guide-to-odoo-19-new-features-and-enhancements) | Repaso de las novedades de v19 módulo por módulo — la base sobre la que se construye v20 y lo que pregunta el examen de v19 | *sep 2025* ⚠️ **v19** |

### Odoo en Español — YouTube

[**Conoce Odoo 20**](https://www.youtube.com/watch?v=9QW4XNqkLys) — presentación oficial de la versión 20 en Odoo Experience América Latina, en español. 
[**Odoo 20: novedades del sector servicios**](https://www.youtube.com/watch?v=QO8YRa_1kv0) — proyecto, servicio de campo y planeación en v20. 
[**Buscar «Odoo 20» en el canal**](https://www.youtube.com/@OdooSpanish/search?query=Odoo+20) — el resto de vídeos de la versión, a medida que se publiquen. 
[**Notas de lanzamiento de Odoo 20 (en español)**](https://www.odoo.com/es/odoo-20-release-notes) — el resumen oficial de novedades, app por app: léelo junto con la tabla de cambios de arriba.

> El canal no publica un índice enlazable por tema, así que el enlace abre la **búsqueda dentro del
> canal**: siempre devuelve lo que haya publicado sobre el tema, aunque renombre o reordene sus
> vídeos. El canal completo está en <https://www.youtube.com/@OdooSpanish>.

> **Úsalos para el concepto, no para la configuración.** Todo lo marcado con ⚠️ es de una versión
> anterior, y aun en los artículos de v19 conviene contrastar los nombres de campo: verifica contra
> la documentación 20.0, contra la tabla de cambios de v20 de este mismo cuaderno y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
