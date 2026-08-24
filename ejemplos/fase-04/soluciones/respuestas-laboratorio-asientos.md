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
| 6911 Costo de ventas | 816.00 | |
| 2011 Existencias (valoración) | | 816.00 |

> **Las cinco líneas van en el mismo asiento.** Es el cambio de v19: con valoración perpetua
> —que ahora se llama *Perpetual (at invoicing)*— el costo de ventas se registra **al facturar**,
> no al entregar. Verificado en saas~19.4: la factura de venta genera un único asiento con ingreso,
> IGV, costo y descargo de existencias.

**2. Entrega de las 120 conservas (costo 6.80 c/u = 816.00)**

> **No genera ningún asiento.** Verificado: tras validar la entrega, el número de asientos nuevos
> es **cero**.
>
> La entrega mueve el inventario **físico** y actualiza la valoración del producto, pero la
> contabilidad espera a la factura. Si nunca se factura esa entrega, el costo nunca llega al
> resultado: ese es el control que reemplaza al viejo cuadre de la cuenta transitoria.
>
> Consecuencia que debes saber explicar: si entregas el 30 de agosto y facturas el 2 de septiembre,
> **ni el ingreso ni el costo** están en agosto. En v18 el costo sí caía en agosto y el ingreso en
> septiembre, y el margen quedaba partido. v19 elimina ese descuadre a cambio de que el inventario
> contable vaya por detrás del físico mientras haya entregas sin facturar.

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
| 2511 Envases y embalajes (valoración) | 1 350.00 | |
| 4017 IGV crédito fiscal | 243.00 | |
| 4212 Facturas por pagar | | 1 593.00 |

> **Sin cuenta transitoria.** La factura carga **directamente** la cuenta de valoración de
> existencias de la categoría. Verificado en saas~19.4: el asiento de la factura de compra es
> exactamente *Existencias / Facturas por pagar* (más el IGV).

**5. Recepción de los 1 000 frascos**

> **No genera ningún asiento.** Verificado: cero asientos nuevos en el diario de existencias tras
> validar la recepción.
>
> La recepción sube el stock y alimenta las capas de costo (PEPS/promedio), pero el hecho contable
> es la factura. Por eso `property_stock_account_input_categ_id` desapareció: no queda ningún
> momento intermedio que cuadrar.

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

> **Cuidado con el momento.** Verificado en saas~19.4: aplicar el ajuste **no genera el asiento en
> ese instante** —salen cero asientos nuevos—. La diferencia queda registrada como movimiento de
> existencias valorado y llega a la contabilidad en el **asiento de cierre**, contra la cuenta de
> **variación de existencias** (`account_stock_variation_id` de la categoría). El asiento de arriba
> es el resultado final; lo que cambió en v19 es **cuándo** aparece, no **qué** dice.

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

**A. De dos asientos a uno.** En v18 el ingreso se devengaba con la factura y el costo con la
salida física, en asientos separados. Si se facturaba en agosto y se entregaba en septiembre, agosto
mostraba ingreso sin costo (margen inflado) y septiembre costo sin ingreso: el margen quedaba partido
entre dos períodos. **v19 resuelve ese descuadre** poniendo ingreso y costo en el mismo asiento, con
la fecha de la factura.

El problema nuevo va en la dirección contraria: si entregas el 30 de agosto y facturas el 2 de
septiembre, **agosto no registra nada** —ni el ingreso ni el costo—, aunque la mercancía ya salió del
almacén. El inventario contable queda por encima del físico hasta que se emita la factura. Por eso el
checklist de cierre sigue revisando **entregas sin facturar**, pero ahora por una razón distinta: ya
no busca cuadrar una cuenta transitoria, busca **ingresos y costos que faltan** en el período.

**B. Entre la recepción y la factura, ¿cuadran físico y contable?** **No, y es lo esperado.** La
recepción sube el stock físico y la valoración del producto; la contabilidad no se entera hasta la
factura. Al contador se le responde con la cifra concreta: *"el almacén tiene 1 000 frascos más que
la contabilidad porque hay una recepción de S/ 1 350 pendiente de factura del proveedor; aquí está
el listado de recepciones sin facturar"*.

La diferencia debe ser **explicable y transitoria**, no cero. Lo que en v17 se comprobaba mirando el
saldo de la cuenta de entrada de existencias, en v19 se comprueba con el **informe de recepciones
sin factura** (Compras → Facturación → *Facturas por crear*) contrastado contra el informe de
valoración.

**C. El cliente que migra de v17 y pide "su" cuenta de entrada de existencias.** Ya no existe, y no
hay que recrearla a mano: el control cambia de sitio, no desaparece. Lo que se pone en su lugar, como
paso del checklist de cierre mensual:

1. **Recepciones sin factura de proveedor** — Compras → *Facturas por crear*. Es el equivalente
   directo del antiguo saldo deudor de la cuenta transitoria.
2. **Entregas sin factura de cliente** — Ventas → pedidos *Por facturar*. Este control **gana
   importancia** en v19, porque ahora ahí es donde se esconden ingreso y costo no registrados.
3. **Informe de valoración contra el saldo de la cuenta de existencias** — la diferencia entre ambos
   debe explicarse íntegramente con los dos listados anteriores.

Dicho al cliente en una frase: *"la cuenta que usted cuadraba ya no existe porque Odoo 19 dejó de
necesitar un paso intermedio; el mismo control ahora se hace con dos listados de documentos
pendientes, y son más fáciles de auditar que un saldo contable, porque cada línea es un documento
con su responsable."*

**D. Ajuste vs. desecho, si ninguno genera asiento inmediato.** La diferencia sigue existiendo, solo
que se materializa más tarde. Ambos reducen el inventario y ambos llegan a la contabilidad por la vía
del **cierre**, pero por ubicaciones virtuales distintas —*Ajuste de inventario* y *Desechos*— y con
significado distinto: el ajuste es una **diferencia de conteo** (descontrol) y el desecho es una
**decisión consciente** de descartar mercancía (calidad, caducidad, rotura).

Que el asiento sea diferido hace **más** importante separarlos, no menos: si ambos caen en la misma
cuenta de variación de existencias sin distinguir ubicación de origen, al cierre queda un único
importe que nadie puede desglosar entre "se nos perdió" y "lo tiramos porque estaba vencido". La
separación se configura en las cuentas de las **ubicaciones virtuales**, no en el movimiento.

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
