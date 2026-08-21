# H5 — Chuleta de campos técnicos: Inventario y Compras (Odoo 19)

> Verificado contra el código de v19 (`addons/stock`, `addons/stock_account`, `addons/purchase`,
> `addons/product_expiry`). Complementa las chuletas de la
> [Fase 1](../../fase-01/guias/E4-campos-tecnicos-v19.md) y la
> [Fase 2](../../fase-02/guias/G5-campos-tecnicos-v19-ventas.md).

---

## 1. Cambios de v19 que rompen material antiguo

| Concepto | Antes | **En v19** | Impacto |
|---|---|---|---|
| Valoración de inventario | `manual_periodic` / `real_time` | **`periodic`** / `real_time` | Un CSV o script con `manual_periodic` falla |
| Lotes | Modelo `stock.production.lot` | **`stock.lot`** | Cambió el nombre del modelo (desde v17) |
| Múltiplo de compra en reordenamiento | `qty_multiple` | **eliminado**; ahora `qty_to_order` (computado) y `qty_to_order_manual` | Las reglas antiguas no se importan igual |
| Valoración por lote | No existía | **`lot_valuated`** en producto y categoría | Permite costo distinto por lote |
| Método de costo en el producto | Solo en la categoría | `cost_method` y `valuation` **calculados** en `product.template` (solo lectura) | Se siguen configurando en la categoría |
| Empaques | `product.packaging` | `uom_ids` en el producto | Cambia el modelado de "caja de 12" |

## 2. `stock.warehouse` — Almacén

| Campo | Valores |
|---|---|
| `name`, `code` | Nombre y código corto (aparece en las referencias) |
| `reception_steps` | `one_step`, `two_steps`, `three_steps` |
| `delivery_steps` | `ship_only`, `pick_ship`, `pick_pack_ship` |
| `wh_input_stock_loc_id`, `wh_qc_stock_loc_id`, `wh_output_stock_loc_id`, `wh_pack_stock_loc_id` | Ubicaciones que Odoo crea al activar los pasos |

## 3. `stock.location` — Ubicación

| Campo | Notas |
|---|---|
| `name`, `complete_name` | El completo se calcula (`WH/Stock/Estante A`) |
| `location_id` | Ubicación padre |
| `usage` | `internal`, `view`, `supplier`, `customer`, `inventory`, `production`, `transit` |
| `removal_strategy_id` | Estrategia de remoción (FIFO, LIFO, FEFO, cercanía…) |
| `barcode` | Para escaneo |
| `storage_category_id` | Categoría de almacenamiento (capacidad, restricciones) |

> **Las ubicaciones virtuales no son un adorno**: `inventory` (ajustes), `production` (fabricación),
> `supplier`/`customer` (fuera de la empresa). Todo movimiento sale de una y entra a otra:
> es la partida doble del inventario.

## 4. `stock.quant` — Existencias por ubicación

| Campo | Notas |
|---|---|
| `product_id`, `location_id`, `lot_id`, `package_id`, `owner_id` | Dimensiones del stock |
| `quantity` | **Solo lectura**: es el resultado de los movimientos |
| `reserved_quantity`, `available_quantity` | Reservado y libre |
| `inventory_quantity` | Cantidad **contada** (ajuste pendiente de aplicar) |
| `inventory_diff_quantity` | Diferencia calculada |
| `inventory_quantity_auto_apply` | **Truco de importación**: escribe la cantidad y **aplica el ajuste de una vez** |
| `inventory_date` | Próximo conteo programado (conteos cíclicos) |

> Para cargar stock inicial por CSV se usa **`inventory_quantity_auto_apply`**. Con
> `inventory_quantity` tendrías que aplicar el ajuste después, registro por registro.

## 5. `stock.lot` — Lote / número de serie

| Campo | Notas |
|---|---|
| `name` | Número de lote o serie (único por producto) |
| `product_id` | Producto |
| `ref` | Referencia interna del proveedor o fabricante |
| `expiration_date` | **Datetime**: caducidad (módulo *Caducidad de producto*) |
| `use_date`, `removal_date`, `alert_date` | Consumo preferente, retiro y alerta |

**En el producto** (`product.template` con *product_expiry*): `use_expiration_date` (Boolean),
`expiration_time`, `use_time`, `removal_time`, `alert_time` (días desde la recepción).

**Seguimiento:** `tracking` = `none` / `lot` / `serial`.

## 6. `stock.warehouse.orderpoint` — Regla de reordenamiento

| Campo | Notas |
|---|---|
| `product_id`, `location_id`, `warehouse_id` | Qué y dónde |
| `product_min_qty`, `product_max_qty` | Mínimo que dispara, máximo al que repone |
| `trigger` | `auto` (planificador) o `manual` |
| `route_id` | Ruta a usar (comprar, fabricar, transferir) |
| `qty_to_order` | **Calculado** en v19 (reemplaza a `qty_multiple`) |

## 7. `product.category` — Valoración

| Campo | Valores |
|---|---|
| `property_cost_method` | `standard`, `fifo`, `average` |
| `property_valuation` | **`periodic`**, `real_time` |
| `property_stock_journal` | Diario de existencias |
| `property_stock_valuation_account_id` | Cuenta de valoración |
| `property_stock_account_input_categ_id` / `_output_categ_id` | Entrada y salida de existencias |
| `property_price_difference_account_id` | Diferencia de precio (con costo estándar) |
| `lot_valuated` | Valoración específica por lote (**novedad v19**) |

Son campos **dependientes de compañía**: en multiempresa cada una tiene su valor.

## 8. `purchase.order` y línea

**Orden:** `partner_id`, `date_order` (Datetime), `date_planned`, `currency_id`, `payment_term_id`,
`picking_type_id`, `state` (`draft`, `sent`, `purchase`, `done`, `cancel`).

**Línea:** `product_id`, `product_qty`, `product_uom_id`, `price_unit`, `date_planned`, `taxes_id`.

**En el producto:** `purchase_method` (`purchase` = cantidades pedidas, `receive` = recibidas)
controla el control de facturas de compra — el equivalente a `invoice_policy` en ventas.

## 9. Notación útil al importar en inventario

| Necesito | Columnas |
|---|---|
| Stock inicial sin lote | `product_id/id`, `location_id/id`, `inventory_quantity_auto_apply` |
| Stock inicial con lote | lo anterior + `lot_id/id` |
| Lote con caducidad | `name`, `product_id/id`, `expiration_date` (`AAAA-MM-DD HH:MM:SS`) |
| Regla de reordenamiento | `product_id/id`, `location_id/id`, `product_min_qty`, `product_max_qty`, `trigger` |
| Orden de compra con líneas | `partner_id/id`, `date_order`, `order_line/product_id/id`, `order_line/product_qty` |

**Ubicaciones estándar por ID externo:** `stock.stock_location_stock` (WH/Existencias),
`stock.stock_location_customers`, `stock.stock_location_suppliers`,
`stock.stock_location_inter_company` (tránsito), `stock.location_production`,
`stock.stock_location_scrapped`.
