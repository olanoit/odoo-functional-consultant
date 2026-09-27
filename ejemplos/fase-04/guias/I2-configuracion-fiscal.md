# I2 — Configuración fiscal: impuestos y posiciones en v20

> ⚠️ **Este tema cambió radicalmente en Odoo 19 y v20 mantiene el mismo modelo.** El modelo
> `account.fiscal.position.tax` (con impuesto origen → impuesto destino) **ya no existe**. Todo el
> material anterior a v19 sobre posiciones fiscales está obsoleto.

---

## 1. Cómo funciona ahora el mapeo de impuestos

**Antes (v16–v18):** la posición fiscal contenía líneas *"si el producto lleva IGV 18 %, cámbialo por Exonerado"*.

**Desde v19 (igual en v20):** la relación vive **en el impuesto destino**:

| Campo | Modelo | Significado |
|---|---|---|
| `original_tax_ids` | `account.tax` | A qué impuesto(s) **reemplaza** este impuesto |
| `fiscal_position_ids` | `account.tax` | En qué posiciones fiscales aplica ese reemplazo |
| `tax_ids` | `account.fiscal.position` | Many2many con los impuestos **destino** (la otra cara de la relación) |

Es decir: el impuesto *Exonerado (venta)* declara *"yo reemplazo al IGV 18 % cuando la posición
fiscal es Cliente exonerado"*.

En los CSV de este cuaderno:
- `03-impuestos.csv` trae la columna **`original_tax_ids/id`**: el exonerado y el inafecto apuntan al IGV 18 %.
- `04-posiciones-fiscales.csv` trae **`tax_ids/id`** con los impuestos destino de cada posición, y
  una posición **Local Perú** sin impuestos destino (ver §4).
- `03-impuestos.csv` usa **`price_include_override`** (`tax_included` / `tax_excluded`), no
  `price_include`: este último es un campo **calculado no almacenado** (depende del ajuste de la
  compañía *Impuestos incluidos/excluidos* y del valor propio del impuesto) y el importador lo ignora.

## 2. Anatomía de un impuesto

| Campo | Qué controla |
|---|---|
| `name` | Lo que ve el usuario en la factura |
| `amount` + `amount_type` | Cuánto y cómo: `percent`, `fixed`, `group`, `division` |
| `type_tax_use` | `sale`, `purchase`, `none` (los de grupo o los que solo se usan dentro de otro) |
| `price_include_override` | Si el precio ya lo incluye: `tax_included`, `tax_excluded` o vacío (hereda el ajuste de la compañía). `price_include` es el resultado calculado, de solo lectura |
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
| IGV 18 % incluido | 18 %, `price_include_override = tax_included` | venta | — (para PdV y tienda en línea) |
| Exonerado (venta / compra) | 0 % | venta / compra | IGV 18 % |
| Inafecto (venta) | 0 % | venta | IGV 18 % |
| Gratuito | 0 % | venta | — (transferencias gratuitas: muestras) |

**Ejercicio obligatorio:** una vez importados, abre cada impuesto y **configura las líneas de
repartición** con las cuentas del archivo `01-cuentas.csv` (4011 IGV por pagar, 4017 IGV crédito
fiscal). Sin eso, el reporte de impuestos no sirve.

## 4. Posiciones fiscales

| Posición | Cuándo aplica | Efecto |
|---|---|---|
| Local Perú | Cliente con país Perú (`auto_apply`, secuencia 10) | Ninguno: es la **posición doméstica** |
| Cliente exonerado (Amazonía) | Clientes en zona con beneficio tributario (se asigna en el cliente) | IGV 18 % → Exonerado |
| Operación inafecta | Operaciones fuera del ámbito del impuesto (se asigna en el cliente) | IGV 18 % → Inafecto |
| Exportación | Cliente con país distinto de Perú (`auto_apply` sin país, secuencia 40) | IGV 18 % → Inafecto (exportación) |

> **Por qué la posición local:** la detección automática recorre las posiciones con `auto_apply` por
> **secuencia** y se queda con la primera que encaja. Una *Exportación* sin país encaja con cualquier
> cliente, peruanos incluidos; si además se le pusiera país Perú, Odoo la tomaría como **posición
> doméstica** de la compañía (`domestic_fiscal_position_id`) y aplicaría la exportación a todo el
> mercado local. La posición *Local Perú*, con país y secuencia menor, gana para los peruanos y deja
> la exportación para el resto. Es el mismo patrón del plan contable peruano (`LOCAL PERU` /
> `EXTRANJERO - EXPORTACIÓN`).
>
> **Con el plan contable peruano ya instalado (la base `LAB` tiene país Perú)**, esas dos posiciones
> existen antes de importar: *LOCAL PERÚ* (secuencia 10, país Perú) y *EXTRANJERO - EXPORTACIÓN*
> (secuencia 20, sin país). Verificado en v20: para un cliente peruano la detección automática elige
> *LOCAL PERÚ* (empata en secuencia con *Local Perú* y gana la que ya existía) y para un cliente
> extranjero, *EXTRANJERO - EXPORTACIÓN*; la *Exportación* del CSV (secuencia 40) nunca se aplica sola.
> Para que actúen las posiciones del CSV, **archiva las dos del plan** (o dale a las del CSV una
> secuencia menor). Es exactamente el tipo de duplicado que hay que detectar antes de un go-live.

**Prueba de fuego:** el **mismo producto** facturado a tres clientes con posiciones distintas debe
producir **tres facturas distintas** sin tocar el producto. Hazlo y guarda las tres capturas: es la
mejor demostración de por qué las posiciones fiscales existen.

## 5. Cómo se elige la posición fiscal de una factura

1. La que tenga asignada el **cliente** en su ficha (pestaña Ventas y compras).
2. Si no tiene, la **primera por secuencia** de las que se detectan automáticamente (`auto_apply`)
   según país / grupo de países / estado / rango de código postal y si tiene RUC (`vat_required`).
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
