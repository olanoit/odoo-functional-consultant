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

> **Las cinco líneas van en el mismo asiento.** Es el cambio que llegó en v19 y que v20 mantiene: con
> valoración perpetua —que ahora se llama *Perpetual (at invoicing)*— el costo de ventas se registra
> **al facturar**, no al entregar. Verificado en Odoo 20: la factura de venta genera un único asiento
> con ingreso (1 170.00), IGV (210.60), cuenta por cobrar (1 380.60) y las dos líneas de costo
> (816.00 = 120 × 6.80), que son apuntes de tipo `cogs` de la propia factura (`_create_cogs_lines` de
> `account.move`, módulo `account`).
>
> **¿De dónde sale la cuenta de costo?** Odoo no tiene una cuenta de "costo de ventas" aparte: el debe
> va a la **cuenta de gastos** del producto o de su categoría (`property_account_expense_categ_id`).
> Con el plan PE tal como se instala, esa cuenta es la **6011 Compras de mercaderías**, y ahí cae el
> costo. Para que vaya a **6911 Costo de ventas** hay que poner 6911 como *Cuenta de gastos* en la
> categoría *Conservas* (en una categoría valorada en tiempo real la factura de compra no usa esa
> cuenta: carga la de valoración, ver operación 4). Es un punto de configuración que se decide con el
> contador antes de facturar.

**2. Entrega de las 120 conservas (costo 6.80 c/u = 816.00)**

> **No genera ningún asiento.** Verificado en v20: tras validar la entrega, el número de asientos
> nuevos es **cero** y las líneas de costo de la factura no cambian (816.00).
>
> La entrega mueve el inventario **físico** y actualiza la valoración del producto, pero la
> contabilidad espera a la factura. Si nunca se factura esa entrega, el costo nunca llega al
> resultado: ese es el control que reemplaza al viejo cuadre de la cuenta transitoria.
>
> Consecuencia que debes saber explicar: si entregas el 30 de agosto y facturas el 2 de septiembre,
> **ni el ingreso ni el costo** están en agosto. En v18 el costo sí caía en agosto y el ingreso en
> septiembre, y el margen quedaba partido. Desde v19 ese descuadre desaparece a cambio de que el
> inventario contable vaya por detrás del físico mientras haya entregas sin facturar.
>
> **Matiz de v20:** si la factura se publica **antes** de la entrega, su costo de ventas se calcula con
> el costo vigente del producto; al validar la entrega, Odoo **actualiza esas mismas líneas** de costo
> en la factura ya publicada con el valor real de la salida (PEPS). Sigue sin haber asiento nuevo.

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
>
> **Depende de la configuración del diario (igual que en v18 y v19).** El primer asiento solo existe
> si el método de pago del diario de banco tiene **cuenta de pagos pendientes** (*Recibos pendientes*
> / *Pagos pendientes*). En Enterprise, por defecto, no la tiene: registrar el pago **no genera
> asiento**, la factura queda *En proceso de pago* y el único asiento es el de la conciliación con el
> extracto (*1041 Banco / 1212 Facturas por cobrar*). En Community (solo *Facturación*), Odoo fuerza la
> cuenta de pagos pendientes y siempre salen los dos asientos.

**4. Factura de compra: 1 000 frascos a S/ 1.35 + IGV**

| Cuenta | Debe | Haber |
|---|---|---|
| 2511 Envases y embalajes (valoración) | 1 350.00 | |
| 4017 IGV crédito fiscal | 243.00 | |
| 4212 Facturas por pagar | | 1 593.00 |

> **Sin cuenta transitoria.** La factura carga **directamente** la cuenta de valoración de
> existencias de la categoría. Verificado en v20: el asiento de la factura de compra es exactamente
> *Existencias 1 350.00 + IGV 243.00 / Facturas por pagar 1 593.00*, aunque la factura se registre
> **antes** de la recepción; la redirección a la cuenta de valoración la hace `account.move.line` en
> el propio módulo `account`.
>
> Si los frascos se valoraran a **costo estándar** y la factura llegara a un precio distinto, la
> factura añadiría dos líneas más contra la **cuenta de diferencia de precio** de la categoría. Con
> 1.35 = costo registrado, no hay diferencia.

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

Y al conciliar, la transitoria se salda contra 1041 Banco. (Misma salvedad que en la operación 3:
sin cuenta de pagos pendientes en el método de pago, el único asiento es *4212 / 1041* al conciliar.)

**7. Ajuste de inventario: faltan 12 conservas (costo 6.80 = 81.60)**

| Cuenta | Debe | Haber |
|---|---|---|
| 6595 Faltantes y mermas de inventario | 81.60 | |
| 2011 Existencias | | 81.60 |

> **Cuidado con el momento y con la cuenta.** Verificado en v20 (`_should_create_account_move` de
> `stock.move`): aplicar el ajuste **no genera el asiento en ese
> instante** —salen cero asientos nuevos— mientras la ubicación virtual *Ajuste de inventario* no
> tenga cuenta de valoración. La diferencia queda registrada como movimiento de existencias valorado
> y llega a la contabilidad con el **asiento de cierre de existencias** (*Stock Closing*, botón
> *Generate Entries* del informe de valoración), contra la cuenta de **variación de existencias**
> (`account_stock_variation_id` de la cuenta de valoración; si no hay, la cuenta de gastos por
> defecto de la compañía). Es decir, sin más configuración el haber va a 2011 y el debe a la cuenta
> de variación, no a 6595.
>
> El asiento de arriba, **con 6595**, es el que obtienes si pones 6595 como *Cuenta de valoración de
> stock* de la ubicación virtual *Ajuste de inventario*: entonces sí se genera **en el momento** de
> aplicar el ajuste. Lo que cambió desde v19 es **cuándo** aparece y **dónde** se configura la
> cuenta, no la lógica contable.

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

En v20 salen **dos** asientos. Al conciliar el extracto en dólares con la factura:

| Cuenta | Debe | Haber |
|---|---|---|
| 1042 Banco USD | 3 820.00 (= $ 1 000) | |
| 1212 Facturas por cobrar | | 3 820.00 (= $ 1 000) |

y Odoo genera automáticamente, en el diario **Diferencia de cambio** (`EXCH`; en una base creada en
español el código es `CAMBIO`), el asiento que salda
la cuenta por cobrar en soles:

| Cuenta | Debe | Haber |
|---|---|---|
| 1212 Facturas por cobrar | 70.00 | |
| 7761 Diferencia de cambio - ganancia | | 70.00 |

Efecto neto: Banco 3 820.00 al debe; Facturas por cobrar 3 750.00 y ganancia 70.00 al haber.
Diferencia de cambio **realizada**: la operación se cerró y la ganancia es efectiva.
*(Verificado en v20. Igual que en la operación 3: si el método de pago no tiene cuenta de pagos
pendientes, registrar el pago no crea asiento y todo ocurre al conciliar el extracto.)*

**12. Cierre de sesión de PdV (S/ 1 180 efectivo + S/ 620 tarjeta, IGV incluido)**

**Cambio de v20:** el cierre ya no es un asiento misceláneo. Genera una **factura de cliente
resumen** (`out_invoice`) en el **diario de cierre del PdV** (*Point of Sale Closing*, código `POSC`)
a nombre del cliente por defecto de la sesión (*Odoo POS*), y la paga con un cobro por cada método
de pago (`point_of_sale/models/pos_session.py`, `_create_session_account_move`).

Factura resumen:

| Cuenta | Debe | Haber |
|---|---|---|
| Cuenta por cobrar del PdV — efectivo | 1 180.00 | |
| Cuenta por cobrar del PdV — tarjeta | 620.00 | |
| 7012 Ventas | | 1 525.42 |
| 4011 IGV por pagar | | 274.58 |

Cobros que la saldan (se concilian solos con la factura):

| Documento | Debe | Haber |
|---|---|---|
| Línea de extracto del diario de caja | 1011 Caja 1 180.00 | Cuenta por cobrar del PdV 1 180.00 |
| Pago del método *tarjeta* | Pagos pendientes (outstanding) 620.00 | Cuenta por cobrar del PdV 620.00 |

**Efecto neto** (el que debes predecir): Caja 1 180.00 + transitoria de tarjetas 620.00 al debe;
Ventas 1 525.42 + IGV 274.58 al haber.
*(1 800.00 / 1.18 = 1 525.42 de base; 274.58 de IGV, porque el PdV trabaja con impuesto incluido.
Ojo: el IGV se calcula ticket por ticket, así que el total puede diferir en un céntimo. Verificado en
v20 con 10 tickets —cinco de 180 y uno de 280 en efectivo; tres de 180 y uno de 80 con tarjeta— la
factura resumen salió con base 1 525.41 e IGV 274.59.)*
Con valoración perpetua, la factura resumen trae además sus líneas de **costo de ventas** (una
pareja *cuenta de gastos / existencias* por movimiento de stock de la sesión), igual que la operación 1. Si hubiera diferencia de caja al arqueo, aparece un movimiento adicional contra la
cuenta de diferencias del diario de caja.

---

## Respuestas a las preguntas

**A. De dos asientos a uno.** En v18 el ingreso se devengaba con la factura y el costo con la
salida física, en asientos separados. Si se facturaba en agosto y se entregaba en septiembre, agosto
mostraba ingreso sin costo (margen inflado) y septiembre costo sin ingreso: el margen quedaba partido
entre dos períodos. **Desde v19 ese descuadre se resuelve** poniendo ingreso y costo en el mismo
asiento, con la fecha de la factura.

El problema nuevo va en la dirección contraria: si entregas el 30 de agosto y facturas el 2 de
septiembre, **agosto no registra nada** —ni el ingreso ni el costo—, aunque la mercancía ya salió del
almacén. El inventario contable queda por encima del físico hasta que se emita la factura. Por eso el
checklist de cierre sigue revisando **entregas sin facturar**, pero ahora por una razón distinta: ya
no busca cuadrar una cuenta transitoria, busca **ingresos y costos que faltan** en el período. En v20
el propio informe de valoración los lista (*Accruals* → *Invoices to be Issued*) y puede
contabilizarlos como devengo con reversión automática al pulsar *Generate Entries*.

**B. Entre la recepción y la factura, ¿cuadran físico y contable?** **No, y es lo esperado.** La
recepción sube el stock físico y la valoración del producto; la contabilidad no se entera hasta la
factura. Al contador se le responde con la cifra concreta: *"el almacén tiene 1 000 frascos más que
la contabilidad porque hay una recepción de S/ 1 350 pendiente de factura del proveedor; aquí está
el listado de recepciones sin facturar"*.

La diferencia debe ser **explicable y transitoria**, no cero. Lo que en v17 se comprobaba mirando el
saldo de la cuenta de entrada de existencias, en v20 se comprueba en el **informe de valoración**:
su sección *Accruals* → *Bills to Receive* lista las recepciones sin factura con su importe (y en
Compras, el filtro *Facturas en espera* de los pedidos de compra).

**C. El cliente que migra de v17 y pide "su" cuenta de entrada de existencias.** Ya no existe, y no
hay que recrearla a mano: el control cambia de sitio, no desaparece. Lo que se pone en su lugar, como
paso del checklist de cierre mensual:

1. **Recepciones sin factura de proveedor** — informe de valoración, *Accruals* → *Bills to
   Receive*. Es el equivalente directo del antiguo saldo deudor de la cuenta transitoria.
2. **Entregas sin factura de cliente** — *Accruals* → *Invoices to be Issued*. Este control **gana
   importancia** desde v19, porque ahora ahí es donde se esconden ingreso y costo no registrados.
3. **Informe de valoración contra el saldo de la cuenta de existencias** — la diferencia entre ambos
   debe explicarse íntegramente con los dos listados anteriores. En v20, si el contador quiere verlo
   en el balance, *Generate Entries* los contabiliza como devengos con reversión automática, usando
   las cuentas de devengo de la categoría (*Bills to Receive* / *Invoices to be Issued*).

Dicho al cliente en una frase: *"la cuenta que usted cuadraba ya no existe porque desde Odoo 19 no
hace falta un paso intermedio; el mismo control ahora se hace con dos listados de documentos
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
separación se configura en las cuentas de las **ubicaciones virtuales**, no en el movimiento (y en
cuanto una ubicación virtual tiene cuenta, sus movimientos vuelven a generar asiento en el momento).
El informe de valoración de v20 los muestra aparte en la sección *Inventory Loss*.

**E. Diferencia de cambio realizada vs. no realizada.** En la operación 11 es **realizada**: la factura
se cobró. Si al cierre siguiera pendiente, habría que registrar una diferencia **no realizada**
(revalorización al tipo de cambio de cierre), que normalmente se revierte al inicio del período
siguiente. Odoo tiene un asistente para ello.

**F. Una sola factura resumen por sesión de PdV.** Se gana simplicidad y velocidad: 300 tickets
diarios generarían 300 asientos y una contabilidad ilegible. Se pierde el detalle contable ticket a
ticket —que sigue existiendo en el módulo de PdV, con su trazabilidad—. La contabilidad registra el
**resumen del turno**, que es como funciona cualquier caja del mundo real. En v20 ese resumen es una
factura al cliente genérico *Odoo POS* (más los cobros por método de pago); los tickets que el
cliente pidió facturar aparte no entran en ella porque ya tienen su propia factura.

---

| Aciertos | Lectura |
|---|---|
| 11–12 | Puedes sentarte con un contador de igual a igual |
| 8–10 | Aprobado; repasa los asientos fallados hasta poder escribirlos de memoria |
| 5–7 | Repite el bloque 4.0 de nivelación contable y vuelve |
| < 5 | No configures contabilidad en un cliente todavía |
