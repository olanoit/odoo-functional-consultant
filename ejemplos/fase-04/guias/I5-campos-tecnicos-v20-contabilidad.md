# I5 — Chuleta de campos técnicos: Contabilidad (Odoo 20)

> Verificado contra `addons/account` (y `stock_account`, `analytic`, `account_accountant`) de v20.0. Complementa las chuletas de las Fases
> [1](../../fase-01/guias/E4-campos-tecnicos-v20.md), [2](../../fase-02/guias/G5-campos-tecnicos-v20-ventas.md)
> y [3](../../fase-03/guias/H5-campos-tecnicos-v20-inventario.md).

---

## 1. Cambios recientes que rompen material antiguo

Las filas marcadas **v20** son nuevas en esta versión; las demás llegaron en v19 y siguen vigentes.

| Concepto | Antes | **En v20** | Impacto |
|---|---|---|---|
| Mapeo de impuestos en posición fiscal | Modelo `account.fiscal.position.tax` (origen → destino) | **Eliminado.** El impuesto destino declara `original_tax_ids` y `fiscal_position_ids`; la posición tiene `tax_ids` (M2M) | Todo CSV o tutorial anterior de posiciones fiscales falla |
| Modelos de conciliación | `rule_type` (`writeoff_button`, `writeoff_suggestion`, `invoice_matching`) | **`trigger`** (`manual` / `auto_reconcile`) + `can_be_proposed`, `match_amount`, `match_label` (v19) y, **v20**, un `rule_type` nuevo: `reco_model` / `matching_rule` con `payment_tolerance`, `payment_tolerance_type`, `matching_order` | Cambia por completo la importación de modelos; en v20 aparecen las *reglas de coincidencia* |
| Cuenta ↔ compañía | `company_id` (Many2one) | **`company_ids`** (Many2many) | Una cuenta puede compartirse entre compañías |
| Cuenta obsoleta | `deprecated` | **eliminado** — se archiva con `active = False` | Un CSV con `deprecated` falla |
| Plan analítico ↔ compañía | `company_id` | **eliminado** de `account.analytic.plan` | Los planes ya no se limitan por compañía |
| Valoración de inventario (categoría) | `manual_periodic` | **`periodic`** (*at closing*) / `real_time` (*at invoicing*) | Ver chuleta de la Fase 3 |
| **v20** — Módulo dueño de la valoración | `stock_account` | **`account`**: `property_valuation`, `property_cost_method` (`standard`, `average`), `property_stock_valuation_account_id`, `property_stock_journal`, `property_price_difference_account_id` en la categoría; `inventory_valuation`, `cost_method`, `account_stock_valuation_id`, `account_stock_journal_id`, `inventory_period` en la compañía; `account_stock_variation_id` / `account_stock_expense_id` en la cuenta. **FIFO** lo sigue añadiendo `stock_account` | La valoración periódica funciona incluso sin Inventario (aproximación cantidad × costo) |
| **v20** — Informe de valoración | `stock_account.stock.valuation.report` | **`account.stock.valuation.report`**, con sección **devengos** (*Accruals*) y botón *Generate Entries* que publica devengos + *Stock Closing* | El cuadre de cierre se hace en una sola pantalla |
| **v20** — Cuentas de devengo (categoría) | — | `property_account_bills_to_receive_id`, `property_account_billed_not_received_id` (`purchase`); `property_account_invoices_to_issue_id`, `property_account_invoiced_not_delivered_id` (`sale`) | Sin ellas el botón no contabiliza los devengos |
| **v20** — Cierre de PdV | Asiento misceláneo en el diario del PdV | **Factura resumen** (`out_invoice`) al cliente *Odoo POS* en `closing_journal_id` (diario `POSC`) + un cobro por método de pago | Cambia el laboratorio I1, operación 12 |
| **v20** — Activos (Enterprise) | Un único cuadro por activo | `account.asset.variant`: variantes del activo por libro contable (p. ej. financiero y fiscal) | Útil para diferencias PCGE / tributarias |
| **v20** — Cuentas de cierre de IGV | En el grupo de impuestos (`account.tax.group`) | En el tipo de declaración (`account.return.type`, Enterprise) | Revisar al configurar la declaración |
| **Momento del asiento de existencias** | Cada movimiento validado generaba su asiento | **Ninguno lo genera**: perpetua contabiliza al **facturar**, periódica al **cierre** | Recepciones, entregas y ajustes ya no producen asiento al validarlos |
| Costo de ventas | Asiento separado, en la entrega | **En el mismo asiento de la factura de venta**, junto al ingreso | Ingreso y costo caen siempre en el mismo período |
| Cuenta de entrada de existencias | `property_stock_account_input_categ_id` (transitoria) | **eliminada**; la factura de compra carga directamente la cuenta de valoración | El cuadre de cierre pasa de un saldo contable a dos listados de documentos pendientes |

## 2. `account.account` — Cuenta contable

| Campo | Notas |
|---|---|
| `code` | Código; **calculado con inverse** (depende de la compañía) |
| `name` | Nombre |
| `account_type` | **Lo más importante**: determina el comportamiento en reportes y cierre |
| `reconcile` | Permite conciliación (obligatorio en cuentas por cobrar/pagar) |
| `tax_ids` | Impuestos por defecto de la cuenta |
| `currency_id` | Fuerza una moneda concreta |
| `company_ids` | **Many2many** (desde v19) |
| `active` | `False` archiva la cuenta (**sustituye a `deprecated`**, que ya no existe desde v19) |
| `account_stock_variation_id` / `account_stock_expense_id` | Solo en cuentas de valoración: contrapartidas del asiento de cierre de existencias (**v20**: vienen de `account`, antes de `stock_account`) |

**Valores de `account_type`:** `asset_receivable`, `asset_cash`, `asset_current`, `asset_non_current`,
`asset_prepayments`, `asset_fixed`, `liability_payable`, `liability_credit_card`, `liability_current`,
`liability_non_current`, `equity`, `equity_unaffected`, `income`, `income_other`, `expense`,
`expense_other`, `expense_depreciation`, `expense_direct_cost`, `off_balance`.

> El **tipo** manda sobre el número: define si la cuenta arrastra saldo al año siguiente, si aparece
> en el balance o en el resultado, y si se puede conciliar.

## 3. `account.journal` — Diario

| Campo | Valores |
|---|---|
| `name`, `code` | Nombre y código corto (aparece en el número del asiento) |
| `type` | `sale`, `purchase`, `cash`, `bank`, `credit`, `general` |
| `default_account_id` | Cuenta por defecto de la contrapartida |
| `currency_id` | Moneda propia (diarios en USD) |
| `sequence` | Orden en el tablero |

## 4. `account.tax` — Impuesto

| Campo | Valores / notas |
|---|---|
| `name`, `amount` | Nombre e importe |
| `amount_type` | `percent`, `fixed`, `group`, `division` |
| `type_tax_use` | `sale`, `purchase`, `none` |
| `price_include_override` | `tax_included` / `tax_excluded` / vacío (hereda `account_price_include` de la compañía). **Es el que se importa** |
| `price_include` | Calculado, **no almacenado**: resultado de lo anterior. Un CSV con esta columna no surte efecto |
| `tax_group_id` | Agrupación para subtotales y reportes |
| `invoice_repartition_line_ids` / `refund_repartition_line_ids` | Reparto en factura y en nota de crédito: cuenta, porcentaje y etiquetas de reporte |
| **`original_tax_ids`** | Impuestos a los que **reemplaza** (mapeo de posición fiscal, desde v19) |
| **`fiscal_position_ids`** | Posiciones en las que aplica ese reemplazo (desde v19) |

## 5. `account.fiscal.position` — Posición fiscal

| Campo | Notas |
|---|---|
| `name` | Nombre |
| **`tax_ids`** | **Many2many a `account.tax`** (impuestos destino) — desde v19 |
| `sequence` | Orden de la detección automática: gana la primera que encaja |
| `is_domestic` | Calculado: `True` en la posición doméstica de la compañía (la primera con el país de la compañía) |
| `account_ids` | Mapeo de cuentas (`account.fiscal.position.account`, sigue existiendo) |
| `auto_apply` | Detección automática |
| `country_id`, `country_group_id`, `state_ids`, `zip_from`, `zip_to` | Criterios geográficos |
| `vat_required` | Solo si el cliente tiene RUC/NIF |
| `foreign_vat` | Registro fiscal en otra jurisdicción |

## 6. `account.payment.term` — Condición de pago

`name`, `note`, `line_ids`, `display_on_invoice`, `early_discount`, `discount_percentage`, `discount_days`.

**Línea:** `value` (`percent` / `fixed`), `value_amount`, `delay_type`
(`days_after`, `days_after_end_of_month`, `days_after_end_of_next_month`, `days_end_of_month_on_the`), `nb_days`.

## 7. Analítica

| Modelo | Campos |
|---|---|
| `account.analytic.plan` | `name`, `parent_id`, `default_applicability`, `applicability_ids` (**sin `company_id`** desde v19) |
| `account.analytic.account` | `name`, `code`, `plan_id`, `root_plan_id`, `partner_id`, `company_id` |
| Distribución | En los apuntes: `analytic_distribution` (JSON con porcentajes por cuenta analítica) |
| `account.analytic.distribution.model` | Reglas automáticas: por producto, socio, cuenta… |

> La distribución analítica **ya no es un campo Many2one**: es un diccionario que permite repartir un
> mismo apunte entre varias cuentas analíticas por porcentaje.

## 8. Banco y conciliación

**`account.bank.statement.line`:** `journal_id`, `date`, `payment_ref` (etiqueta), `partner_id`,
`partner_name`, `account_number`, `amount`, `statement_id`, `ref`, `narration`.

**`account.reconcile.model`:** `name`, `sequence`, **`rule_type`** (**v20**: `reco_model` por defecto /
`matching_rule`), **`trigger`** (`manual` / `auto_reconcile`; se propone según `rule_type`, una regla de
coincidencia siempre es automática), `match_label` (`contains`, `not_contains`, `match_regex`) +
`match_label_param`, `match_amount` (`lower`, `greater`, `between`) + `match_amount_min` /
`match_amount_max`, `match_journal_ids`, `match_partner_ids`, y solo para reglas de coincidencia
`payment_tolerance`, `payment_tolerance_type` (`amount` / `percentage`) y `matching_order`
(`old_first` / `new_first`); `line_ids` (contrapartidas: `account_id`, `label`, `amount_type`
(`fixed`, `percentage`, `percentage_st_line`, `regex`), `amount_string`).

## 9. Notación útil al importar en contabilidad

| Necesito | Columnas |
|---|---|
| Cuenta | `code`, `name`, `account_type`, `reconcile` |
| Diario | `name`, `code`, `type`, `default_account_id/id` |
| Impuesto con mapeo fiscal | `name`, `amount`, `amount_type`, `type_tax_use`, `price_include_override`, `original_tax_ids/id` |
| Posición fiscal | `name`, `sequence`, `auto_apply`, `country_id/id`, `tax_ids/id` |
| Cuenta analítica | `name`, `code`, `plan_id/id` |
| Línea de extracto | `journal_id/id`, `date`, `payment_ref`, `partner_id/id`, `amount` |
| Modelo de conciliación | `name`, `trigger`, `match_label`, `match_label_param`, `line_ids/account_id/id`, `line_ids/label` (`rule_type` vacío = `reco_model`) |

## 10. Lo que **no** conviene importar

| Modelo | Por qué |
|---|---|
| `account.payment.term` con líneas | Las líneas deben sumar 100 % y el modelo crea una por defecto: más frágil que crearlas a mano |
| `account.move` (asientos) | Se generan desde los documentos operativos; importarlos a mano rompe la trazabilidad |
| Líneas de repartición de impuestos | Se configuran en la interfaz, donde Odoo valida la coherencia |
| Saldos de apertura | Se cargan como **un** asiento de diario misceláneo, revisado y cuadrado a mano |
