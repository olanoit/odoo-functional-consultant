# I1 — Laboratorio de asientos: predice el asiento

> **La prueba definitiva de que entiendes Odoo contablemente.** Para cada operación, escribe el
> asiento (cuenta, debe, haber) **antes** de ejecutarla, y después búscalo en Odoo con modo
> desarrollador o desde el botón *Apuntes contables*.
>
> Soluciones en [`../soluciones/respuestas-laboratorio-asientos.md`](../soluciones/respuestas-laboratorio-asientos.md).
> Objetivo: **≥ 8 de 12**.

**Supuestos:** IGV 18 %, valoración **perpetua** (`real_time`) con PEPS en conservas,
moneda de la compañía PEN, tipo de cambio 1 USD = 3.75 PEN.

---

| # | Operación | Importe | Tu asiento |
|---|---|---|---|
| 1 | Factura de venta a Sol de Oro, 120 conservas a S/ 9.75 + IGV | 1 170.00 + IGV | |
| 2 | La **entrega** de esas 120 conservas (costo unitario 6.80) | — | |
| 3 | Cobro de la factura por transferencia | 1 380.60 | |
| 4 | Factura de compra de 1 000 frascos a S/ 1.35 + IGV | 1 350.00 + IGV | |
| 5 | La **recepción** de esos 1 000 frascos | — | |
| 6 | Pago al proveedor | 1 593.00 | |
| 7 | Ajuste de inventario: faltan 12 conservas (costo 6.80) | — | |
| 8 | Depreciación mensual de una máquina de S/ 36 000 a 5 años | — | |
| 9 | Comisión bancaria conciliada con modelo automático | 25.00 | |
| 10 | Factura de venta en USD por $ 1 000 (TC 3.75) | — | |
| 11 | Cobro de esa factura cuando el TC subió a 3.82 | — | |
| 12 | Cierre de sesión de PdV: 10 tickets, S/ 1 180 en efectivo y S/ 620 en tarjeta | — | |

---

## Preguntas que acompañan al laboratorio

**A.** ¿Por qué la operación 1 y la 2 son asientos **distintos**? ¿Qué pasaría si el cliente factura
hoy y entrega el mes siguiente, a caballo entre dos períodos?

**B.** En la operación 5, ¿contra qué cuenta se acredita el inventario si aún no llegó la factura?
¿Cómo se llama esa cuenta y cuándo se salda?

**C.** La cuenta de **entrada de existencias** tiene saldo al cierre del mes. ¿Es un error?
¿Qué significa exactamente?

**D.** ¿Qué diferencia hay entre el asiento de la operación 7 (ajuste) y el de un **desecho**?

**E.** En la operación 11, ¿la diferencia de cambio es realizada o no realizada? ¿Y si al cierre del
mes la factura siguiera pendiente de cobro?

**F.** ¿Por qué el cierre de PdV genera **un solo asiento** y no uno por ticket? ¿Qué se pierde y
qué se gana con eso?

## Cómo encontrar cualquier asiento en Odoo

1. Desde el documento: botón *Apuntes contables* / *Asiento contable* en la parte superior.
2. Desde el producto: *Inventario → Reportes → Valoración*, cada línea enlaza a su asiento.
3. Desde la contabilidad: *Contabilidad → Contabilidad → Asientos contables*, filtrando por diario y fecha.
4. Con modo desarrollador: en cualquier registro, menú de desarrollador → *Ver metadatos* / campos.

Aprender a llegar al asiento **desde el documento operativo** es lo que te permite responder
"¿por qué mi balance dice esto?" en una reunión, en vivo.
