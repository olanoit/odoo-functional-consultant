# I2 — Configuración fiscal: impuestos y posiciones en v19

> ⚠️ **Este tema cambió radicalmente en Odoo 19.** El modelo `account.fiscal.position.tax`
> (con impuesto origen → impuesto destino) **ya no existe**. Todo el material anterior a v19
> sobre posiciones fiscales está obsoleto.

---

## 1. Cómo funciona ahora el mapeo de impuestos

**Antes (v16–v18):** la posición fiscal contenía líneas *"si el producto lleva IGV 18 %, cámbialo por Exonerado"*.

**En v19:** la relación vive **en el impuesto destino**:

| Campo | Modelo | Significado |
|---|---|---|
| `original_tax_ids` | `account.tax` | A qué impuesto(s) **reemplaza** este impuesto |
| `fiscal_position_ids` | `account.tax` | En qué posiciones fiscales aplica ese reemplazo |
| `tax_ids` | `account.fiscal.position` | Many2many con los impuestos **destino** (la otra cara de la relación) |

Es decir: el impuesto *Exonerado (venta)* declara *"yo reemplazo al IGV 18 % cuando la posición
fiscal es Cliente exonerado"*.

En los CSV de este cuaderno:
- `03-impuestos.csv` trae la columna **`original_tax_ids/id`**: el exonerado y el inafecto apuntan al IGV 18 %.
- `04-posiciones-fiscales.csv` trae **`tax_ids/id`** con los impuestos destino de cada posición.

## 2. Anatomía de un impuesto

| Campo | Qué controla |
|---|---|
| `name` | Lo que ve el usuario en la factura |
| `amount` + `amount_type` | Cuánto y cómo: `percent`, `fixed`, `group`, `division` |
| `type_tax_use` | `sale`, `purchase`, `none` (los de grupo o los que solo se usan dentro de otro) |
| `price_include` | Si el precio ya lo incluye (Boolean) |
| `tax_group_id` | Agrupa para el subtotal de la factura y para los reportes |
| `invoice_repartition_line_ids` / `refund_repartition_line_ids` | **Lo importante**: a qué cuenta va el impuesto y con qué etiquetas de reporte, en factura y en nota de crédito |

> Las **líneas de repartición** son lo que casi nadie configura y lo que hace que el reporte de
> impuestos salga bien o mal. Un impuesto sin cuenta de repartición correcta produce un reporte de
> IGV que no cuadra con la contabilidad.

## 3. Los impuestos de ANDINA GOURMET

| Impuesto | Tipo | Uso | Reemplaza a |
|---|---|---|---|
| IGV 18 % (venta) | 18 % | venta | — |
| IGV 18 % (compra) | 18 % | compra | — |
| IGV 18 % incluido | 18 %, `price_include` | venta | — (para PdV y tienda en línea) |
| Exonerado (venta / compra) | 0 % | venta / compra | IGV 18 % |
| Inafecto (venta) | 0 % | venta | IGV 18 % |
| Gratuito | 0 % | venta | — (transferencias gratuitas: muestras) |

**Ejercicio obligatorio:** una vez importados, abre cada impuesto y **configura las líneas de
repartición** con las cuentas del archivo `01-cuentas.csv` (4011 IGV por pagar, 4017 IGV crédito
fiscal). Sin eso, el reporte de impuestos no sirve.

## 4. Posiciones fiscales

| Posición | Cuándo aplica | Efecto |
|---|---|---|
| Cliente exonerado (Amazonía) | Clientes en zona con beneficio tributario | IGV 18 % → Exonerado |
| Operación inafecta | Operaciones fuera del ámbito del impuesto | IGV 18 % → Inafecto |
| Exportación | Cliente en el extranjero (`auto_apply`) | IGV 18 % → Inafecto (exportación) |

**Prueba de fuego:** el **mismo producto** facturado a tres clientes con posiciones distintas debe
producir **tres facturas distintas** sin tocar el producto. Hazlo y guarda las tres capturas: es la
mejor demostración de por qué las posiciones fiscales existen.

## 5. Cómo se elige la posición fiscal de una factura

1. La que tenga asignada el **cliente** en su ficha (pestaña Ventas y compras).
2. Si no tiene, la que se detecte automáticamente (`auto_apply`) según país / grupo de países /
   estado / rango de código postal y si tiene RUC (`vat_required`).
3. Si nada aplica, se usan los impuestos por defecto del producto.

**Error clásico:** configurar la posición pero no asignarla al cliente ni marcar `auto_apply`,
y luego afirmar que "Odoo no aplica el impuesto correcto".

## 6. Rompe a propósito

1. Cambia la cuenta de repartición de un impuesto **después** de emitir 3 facturas.
   Mira el reporte de impuestos: las viejas siguen apuntando a la cuenta anterior.
   **Conclusión para tu bitácora:** la configuración fiscal se define *antes* de operar; corregirla
   después obliga a reprocesar o a asientos de ajuste.
2. Factura a un cliente con posición fiscal y luego quítasela: ¿cambia la factura ya emitida? ¿Por qué no?

## 7. Lista de verificación fiscal antes del go-live

- [ ] Todos los impuestos que usa el negocio existen y tienen líneas de repartición con cuenta.
- [ ] Los impuestos por defecto están puestos en las **categorías de producto**, no producto por producto.
- [ ] Cada posición fiscal tiene sus impuestos destino y su `original_tax_ids` correcto.
- [ ] Los clientes con régimen especial tienen su posición asignada.
- [ ] Se emitió una factura de prueba por cada combinación y se revisó el asiento y el reporte.
- [ ] El contador **firmó** que la configuración refleja su realidad tributaria.
