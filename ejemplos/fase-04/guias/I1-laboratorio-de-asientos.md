# I1 — Laboratorio de asientos: predice el asiento

> **La prueba definitiva de que entiendes Odoo contablemente.** Para cada operación, escribe el
> asiento (cuenta, debe, haber) **antes** de ejecutarla, y después búscalo en Odoo con modo
> desarrollador o desde el botón *Apuntes contables*.
>
> Soluciones en [`../soluciones/respuestas-laboratorio-asientos.md`](../soluciones/respuestas-laboratorio-asientos.md).
> Objetivo: **≥ 8 de 12**.

**Supuestos:** IGV 18 %, valoración **perpetua** (`real_time`) con PEPS en conservas,
moneda de la compañía PEN, tipo de cambio 1 USD = 3.75 PEN.

> ### ⚠ Antes de empezar: en Odoo 19 el inventario se contabiliza al facturar
>
> Este es **el cambio contable más importante de la versión** y el que más veces vas a tener que
> explicar. Hasta v18, con valoración perpetua cada movimiento de existencias generaba su propio
> asiento en el momento de validarlo, contra una cuenta transitoria de *entrada de existencias*.
>
> En v19 eso desapareció. Las dos opciones de valoración se llaman ahora, literalmente:
>
> | Valor del campo | Etiqueta en la interfaz | Cuándo se contabiliza |
> |---|---|---|
> | `real_time` | **Perpetual (at invoicing)** | Al **validar la factura** |
> | `periodic` | **Periodic (at closing)** | Al **cierre del período** |
>
> Consecuencias, verificadas ejecutando las operaciones en saas~19.4:
>
> - Validar una **recepción** no genera ningún asiento. Cero.
> - Validar una **entrega** no genera ningún asiento. Cero.
> - Un **ajuste de inventario** tampoco genera asiento en el momento.
> - La **factura de venta** trae el ingreso **y** el costo de ventas en el **mismo** asiento.
> - La **factura de compra** carga directamente la cuenta de valoración de existencias.
> - La cuenta transitoria de *entrada de existencias* (`property_stock_account_input_categ_id`)
>   **ya no existe**; en su lugar la categoría tiene `account_stock_variation_id`, que es la cuenta
>   de **variación de existencias** que usa el asiento de cierre periódico.
>
> Por eso los casos 2, 5 y 7 de la tabla siguiente tienen una respuesta que sorprende. Predícelos
> igual: saber que **no hay asiento** vale tanto como saber escribirlo.

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

**A.** En v18 las operaciones 1 y 2 eran **dos asientos**; en v19 son **uno solo**. ¿Qué problema
de descuadre entre períodos resuelve ese cambio, y qué problema nuevo crea cuando se entrega en
agosto y se factura en septiembre?

**B.** En la operación 5 la mercancía entra al almacén pero **no hay asiento**. Entonces, entre la
recepción y la factura, ¿el inventario físico y el contable coinciden? ¿Qué le respondes al contador
que ve la diferencia?

**C.** Un cliente que migra de v17 te pide "la cuenta de entrada de existencias, que siempre
cuadrábamos al cierre". Ya no existe. ¿Qué control pones en su lugar para detectar recepciones sin
facturar?

**D.** ¿Qué diferencia hay entre la operación 7 (ajuste) y un **desecho**, si ninguno de los dos
genera asiento en el momento? ¿Dónde acaba reflejándose cada uno?

**E.** En la operación 11, ¿la diferencia de cambio es realizada o no realizada? ¿Y si al cierre del
mes la factura siguiera pendiente de cobro?

**F.** ¿Por qué el cierre de PdV genera **un solo asiento** y no uno por ticket? ¿Qué se pierde y
qué se gana con eso?

## Cómo encontrar cualquier asiento en Odoo

1. Desde el documento: botón *Apuntes contables* / *Asiento contable* en la parte superior.
2. Desde el producto: *Inventario → Reportes → Valoración*. En v19 es un informe dedicado
   (`stock_account.stock.valuation.report`), no la antigua lista de capas de valoración.
3. Desde la contabilidad: *Contabilidad → Contabilidad → Asientos contables*, filtrando por diario y fecha.
4. Con modo desarrollador: en cualquier registro, menú de desarrollador → *Ver metadatos* / campos.

Aprender a llegar al asiento **desde el documento operativo** es lo que te permite responder
"¿por qué mi balance dice esto?" en una reunión, en vivo.
