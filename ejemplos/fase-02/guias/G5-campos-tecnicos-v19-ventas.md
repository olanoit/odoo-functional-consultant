# G5 — Chuleta de campos técnicos: Ventas y CRM (Odoo 19)

> Verificado contra el código fuente de v19 (`addons/crm`, `addons/sale`, `addons/sale_management`,
> `addons/product`, `addons/account`). Complementa la chuleta general de la Fase 1:
> [`../../fase-01/guias/E4-campos-tecnicos-v19.md`](../../fase-01/guias/E4-campos-tecnicos-v19.md).

---

## 1. Cambios de v19 que rompen material antiguo

| Concepto | Antes | **En v19** | Impacto |
|---|---|---|---|
| Etapa de CRM ↔ equipo | `team_id` (Many2one) | **`team_ids`** (Many2many) | Las etapas se comparten entre equipos; un CSV con `team_id` falla |
| Productos opcionales en plantilla | Modelo `sale.order.template.option` | Línea normal con **`is_optional = True`** | Cambia por completo cómo se importa una plantilla |
| Alerta de oportunidad estancada | No existía | **`rotting_threshold_days`** en `crm.stage` | Nueva palanca de gestión del embudo |
| Importación de variantes | Manual, vía `attribute_line_ids` | **`import_attribute_values`** (`"Atributo:Valor,Atributo2:Valor2"`) | Permite crear plantilla + variantes + atributos desde un solo CSV |
| Secciones en líneas | `line_section`, `line_note` | Se añade **`line_subsection`** | Cotizaciones con dos niveles de agrupación |
| Precio con margen en lista | — | **`price_markup`** en `product.pricelist.item` | Nueva forma de calcular precio sobre coste |

## 2. `crm.team` — Equipo de ventas

| Campo | Tipo | Notas |
|---|---|---|
| `name` | Char | Obligatorio |
| `sequence` | Integer | Orden y equipo por defecto |
| `user_id` | Many2one → `res.users` | Líder del equipo |
| `member_ids` | Many2many → `res.users` | Vendedores |
| `use_leads` | Boolean | Activa la fase de leads **para ese equipo** |
| `use_opportunities` | Boolean | Activa el flujo (pipeline) |
| `alias_name` | Char | Alias de correo que crea leads |

## 3. `crm.stage` — Etapa del embudo

| Campo | Tipo | Notas |
|---|---|---|
| `name`, `sequence` | Char, Integer | Orden: menor primero |
| `is_won` | Boolean | Marca la etapa ganadora (probabilidad 100) |
| `fold` | Boolean | Etapa plegada en el kanban |
| `requirements` | Text | **Criterio de avance**; se ve como tooltip |
| `rotting_threshold_days` | Integer | Días sin actividad tras los que se marca como estancada |
| `team_ids` | Many2many → `crm.team` | **Vacío = disponible para todos los equipos** |

## 4. `crm.lead` — Lead / Oportunidad

| Campo | Tipo | Notas |
|---|---|---|
| `name` | Char | Título de la oportunidad |
| `type` | Selección | `lead` u `opportunity` |
| `partner_id` | Many2one → `res.partner` | Cliente |
| `contact_name`, `partner_name` | Char | Persona y empresa cuando **aún no** hay contacto creado |
| `email_from`, `phone` | Char | Datos de contacto del lead |
| `expected_revenue` | Monetary | Ingreso esperado |
| `prorated_revenue` | Monetary (calculado) | Ingreso × probabilidad |
| `probability` | Float | 0–100; se autocalcula salvo que la fijes |
| `date_deadline` | Date | Cierre esperado → base del pronóstico |
| `priority` | Selección | `0`–`3` (estrellas) |
| `stage_id`, `team_id`, `user_id` | Many2one | Etapa, equipo, vendedor |
| `tag_ids` | Many2many → `crm.tag` | Etiquetas |
| `lost_reason_id` | Many2one → `crm.lost.reason` | Motivo de pérdida |
| `active` | Boolean | `False` = perdida/archivada |

## 5. `product.pricelist` y `product.pricelist.item`

**Lista:** `name`, `currency_id`, `sequence`, `company_id`, `country_group_ids`, `item_ids`.

**Regla (`item`):**

| Campo | Valores / notas |
|---|---|
| `applied_on` | `3_global`, `2_product_category`, `1_product`, `0_product_variant` |
| `categ_id` / `product_tmpl_id` / `product_id` | Según `applied_on` |
| `min_quantity` | Cantidad mínima para que aplique |
| `base` | `list_price` (precio de venta), `standard_price` (coste), `pricelist` (otra lista) |
| `compute_price` | `fixed` (precio fijo), `percentage` (descuento), `formula` |
| `fixed_price` | Con `compute_price = fixed` |
| `percent_price` | Con `compute_price = percentage` |
| `price_discount`, `price_surcharge`, `price_round`, `price_markup`, `price_min_margin`, `price_max_margin` | Con `compute_price = formula` |
| `date_start`, `date_end` | **Datetime** (no Date): incluye hora |
| `base_pricelist_id` | Lista base cuando `base = pricelist` |

**Orden de resolución (código v19):** `applied_on, min_quantity desc, categ_id desc, id desc`
→ gana la regla **más específica**, y dentro del mismo nivel, la de **mayor cantidad mínima alcanzada**.

**Asignación al cliente:** `property_product_pricelist` en `res.partner`
(campo con fallback por compañía; el valor específico se guarda en `specific_property_product_pricelist`).

## 6. `sale.order` y `sale.order.line`

**Pedido:** `partner_id`, `partner_invoice_id`, `partner_shipping_id`, `date_order` (Datetime),
`validity_date`, `pricelist_id`, `payment_term_id`, `user_id`, `team_id`, `client_order_ref`,
`commitment_date`, `note`, `state` (`draft`/`sent`/`sale`/`cancel`), `locked` (Boolean: pedido bloqueado).

**Línea:** `product_id`, `product_uom_qty`, `product_uom_id`, `price_unit`, `discount`, `tax_ids`,
`name`, `sequence`, `display_type`, `qty_delivered`, `qty_invoiced`.

> Al importar líneas **sin `price_unit`**, Odoo lo calcula desde la lista de precios del pedido.
> Es la forma correcta de importar: así verificas que tus reglas de precio funcionan.

## 7. `sale.order.template` — Plantilla de cotización

| Campo | Notas |
|---|---|
| `name` | Obligatorio |
| `number_of_days` | Validez de la oferta en días |
| `require_signature` | Exige firma en línea |
| `require_payment` | Exige pago en línea |
| `prepayment_percent` | Porcentaje de anticipo (0.30 = 30 %) |
| `note` | Términos y condiciones (Html) |
| `journal_id` | Diario de facturación específico |
| `sale_order_template_line_ids` | Líneas |

**Línea de plantilla:** `product_id`, `product_uom_qty`, `product_uom_id`, `name`, `sequence`,
`display_type` (`line_section` / `line_subsection` / `line_note`) y **`is_optional`**.

## 8. `product.template` — campos de venta

| Campo | Notas |
|---|---|
| `invoice_policy` | `order` (cantidades pedidas) / `delivery` (cantidades entregadas) |
| `sale_ok` | Se puede vender |
| `list_price` | Precio de venta |
| `import_attribute_values` | **Solo para importar**: `"Tamaño:Grande,Sabor:Quinua"` |

**Atributos:** `product.attribute` con `create_variant` (`always` / `dynamic` / `no_variant`) y
`display_type` (`radio`, `pills`, `select`, `color`, `multi`, `image`).
Al importar con `import_attribute_values`, los atributos que falten se crean como
`create_variant = 'dynamic'`, `display_type = 'radio'`.

## 9. `account.payment.term` — Condiciones de pago

| Campo | Notas |
|---|---|
| `name`, `note`, `sequence` | Datos generales |
| `line_ids` | Vencimientos |
| `display_on_invoice` | Muestra las fechas de cuota en la factura |
| `early_discount`, `discount_percentage`, `discount_days` | Descuento por pronto pago |

**Línea:** `value` (`percent` / `fixed`), `value_amount`, `delay_type`
(`days_after`, `days_after_end_of_month`, `days_after_end_of_next_month`, `days_end_of_month_on_the`),
`nb_days`.

> Las condiciones de pago de este cuaderno se crean **a mano** (son 3) porque la suma de las líneas
> debe dar 100 % y el modelo trae una línea por defecto: importarlas por CSV es más frágil que crearlas.
