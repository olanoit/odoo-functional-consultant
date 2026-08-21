# Soluciones — I1: laboratorio de asientos

> Cuentas según `datos/01-cuentas.csv`. IGV 18 %. Valoración perpetua con PEPS.
> Los nombres exactos de las cuentas transitorias varían según la configuración; lo que debe
> coincidir es **la lógica**, no el número de cuenta.

---

**1. Factura de venta: 120 conservas a S/ 9.75 + IGV**

| Cuenta | Debe | Haber |
|---|---|---|
| 1212 Facturas por cobrar | 1 380.60 | |
| 7012 Ventas - productos terminados | | 1 170.00 |
| 4011 IGV por pagar | | 210.60 |

**2. Entrega de las 120 conservas (costo 6.80 c/u = 816.00)**

| Cuenta | Debe | Haber |
|---|---|---|
| 6911 Costo de ventas | 816.00 | |
| 2011 Existencias (valoración) | | 816.00 |

> **Asiento independiente del anterior.** El ingreso se reconoce al facturar y el costo al entregar.
> Si se factura en un mes y se entrega en otro, el margen queda partido entre dos períodos: por eso
> importa la política de facturación (Fase 2) y por eso el cierre revisa entregas sin facturar.

**3. Cobro por transferencia**

| Cuenta | Debe | Haber |
|---|---|---|
| Pagos pendientes de cobro (transitoria) | 1 380.60 | |
| 1212 Facturas por cobrar | | 1 380.60 |

Y al **conciliar** el extracto:

| Cuenta | Debe | Haber |
|---|---|---|
| 1041 Banco BCP MN | 1 380.60 | |
| Pagos pendientes de cobro | | 1 380.60 |

> Son **dos** pasos: registrar el pago y conciliarlo con el banco. La cuenta transitoria de pagos
> pendientes es lo que permite saber qué está cobrado pero aún no confirmado por el banco.

**4. Factura de compra: 1 000 frascos a S/ 1.35 + IGV**

| Cuenta | Debe | Haber |
|---|---|---|
| Entrada de existencias (transitoria) | 1 350.00 | |
| 4017 IGV crédito fiscal | 243.00 | |
| 4212 Facturas por pagar | | 1 593.00 |

**5. Recepción de los 1 000 frascos**

| Cuenta | Debe | Haber |
|---|---|---|
| 2511 Envases y embalajes (valoración) | 1 350.00 | |
| Entrada de existencias (transitoria) | | 1 350.00 |

> La cuenta **entrada de existencias** conecta ambos hechos. Si al cierre tiene saldo, significa que
> hay recepciones sin factura (o facturas sin recepción). Es normal que tenga saldo **durante** el
> mes; lo que no es normal es que nadie lo explique al cierre.

**6. Pago al proveedor**

| Cuenta | Debe | Haber |
|---|---|---|
| 4212 Facturas por pagar | 1 593.00 | |
| Pagos pendientes de pago (transitoria) | | 1 593.00 |

Y al conciliar, la transitoria se salda contra 1041 Banco.

**7. Ajuste de inventario: faltan 12 conservas (costo 6.80 = 81.60)**

| Cuenta | Debe | Haber |
|---|---|---|
| 6595 Faltantes y mermas de inventario | 81.60 | |
| 2011 Existencias | | 81.60 |

**8. Depreciación mensual (36 000 / 5 años / 12 meses = 600.00)**

| Cuenta | Debe | Haber |
|---|---|---|
| 6811 Depreciación del ejercicio | 600.00 | |
| 3911 Depreciación acumulada | | 600.00 |

**9. Comisión bancaria conciliada con modelo automático**

| Cuenta | Debe | Haber |
|---|---|---|
| 6532 Gastos bancarios | 25.00 | |
| 1041 Banco BCP MN | | 25.00 |

**10. Factura de venta en USD por $ 1 000 (TC 3.75)**

| Cuenta | Debe | Haber |
|---|---|---|
| 1212 Facturas por cobrar | 3 750.00 (= $ 1 000) | |
| 7012 Ventas | | 3 750.00 |

El apunte guarda **ambos** importes: moneda de la compañía (3 750.00 PEN) y moneda del documento ($ 1 000).

**11. Cobro de esa factura con TC 3.82**

| Cuenta | Debe | Haber |
|---|---|---|
| 1042 Banco USD | 3 820.00 | |
| 1212 Facturas por cobrar | | 3 750.00 |
| 7761 Diferencia de cambio - ganancia | | 70.00 |

Diferencia de cambio **realizada**: la operación se cerró y la ganancia es efectiva.

**12. Cierre de sesión de PdV (S/ 1 180 efectivo + S/ 620 tarjeta, IGV incluido)**

| Cuenta | Debe | Haber |
|---|---|---|
| 1011 Caja (efectivo) | 1 180.00 | |
| Cuenta transitoria de tarjetas | 620.00 | |
| 7012 Ventas | | 1 525.42 |
| 4011 IGV por pagar | | 274.58 |

*(1 800.00 / 1.18 = 1 525.42 de base; 274.58 de IGV, porque el PdV trabaja con impuesto incluido.)*
Si hubiera diferencia de caja al arqueo, aparece una línea adicional contra la cuenta de diferencias.

---

## Respuestas a las preguntas

**A. Por qué 1 y 2 son asientos distintos.** Responden a hechos económicos distintos: el ingreso se
devenga con la factura, el costo con la salida física de la mercancía. Si se facturara en agosto y
se entregara en septiembre, agosto tendría ingreso sin costo (margen inflado) y septiembre costo sin
ingreso. Por eso el checklist de cierre revisa **entregas sin facturar** y **facturas sin entregar**.

**B. Contra qué se acredita el inventario sin factura.** Contra la cuenta de **entrada de existencias**
(*stock interim - received*), una cuenta transitoria. Se salda cuando llega la factura del proveedor.

**C. Saldo en la cuenta de entrada de existencias al cierre.** No es un error en sí: significa que hay
mercancía recibida y aún no facturada (o al revés). Debe poder detallarse recepción por recepción.
Un saldo creciente e inexplicable sí es un problema: normalmente indica facturas de proveedor
registradas sin vincular a su recepción.

**D. Ajuste vs. desecho.** Contablemente ambos reducen el inventario, pero contra cuentas distintas y
con significado distinto: el ajuste va a **faltantes/sobrantes de inventario** (diferencia de conteo);
el desecho va a una cuenta de **pérdida por mermas/desechos** (decisión consciente de descartar
mercancía). Mezclarlos impide medir cuánto se pierde por descontrol y cuánto por calidad.

**E. Diferencia de cambio realizada vs. no realizada.** En la operación 11 es **realizada**: la factura
se cobró. Si al cierre siguiera pendiente, habría que registrar una diferencia **no realizada**
(revalorización al tipo de cambio de cierre), que normalmente se revierte al inicio del período
siguiente. Odoo tiene un asistente para ello.

**F. Un solo asiento por sesión de PdV.** Se gana simplicidad y velocidad: 300 tickets diarios
generarían 300 asientos y una contabilidad ilegible. Se pierde el detalle contable ticket a ticket
—que sigue existiendo en el módulo de PdV, con su trazabilidad—. La contabilidad registra el
**resumen del turno**, que es como funciona cualquier caja del mundo real.

---

| Aciertos | Lectura |
|---|---|
| 11–12 | Puedes sentarte con un contador de igual a igual |
| 8–10 | Aprobado; repasa los asientos fallados hasta poder escribirlos de memoria |
| 5–7 | Repite el bloque 4.0 de nivelación contable y vuelve |
| < 5 | No configures contabilidad en un cliente todavía |
