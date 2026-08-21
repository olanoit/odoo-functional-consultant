# Soluciones — Cuestionario de la Fase 4

> Se aprueba con **12 de 14**.

---

**1. ¿Por qué el tipo de cuenta importa más que el número?**
El `account_type` determina el comportamiento: si la cuenta va al balance o al resultado, si arrastra
saldo al ejercicio siguiente, si admite conciliación, y cómo se comporta en el cierre anual. El código
es una convención de presentación (y en Perú, del PCGE). Una cuenta con el número correcto y el tipo
equivocado produce estados financieros incorrectos.

**2. Los tres bloqueos de fecha.**
*Para todos*: nadie puede registrar antes de esa fecha (ni el administrador). *Para no asesores*: los
usuarios normales no pueden, los contables sí. *Bloqueo fiscal*: impide modificar lo ya declarado a
la autoridad tributaria. Es la herramienta antifraude y anti-error más importante, y se usa **cada mes**.

**3. Cliente exonerado que compra un producto gravado.**
Con una **posición fiscal** asignada al cliente. En v19 el impuesto *Exonerado* declara
`original_tax_ids = IGV 18 %` y `fiscal_position_ids = Cliente exonerado`. No se toca el producto:
el producto siempre lleva su impuesto normal y la posición lo sustituye al facturar.

**4. Modelo de conciliación.**
Una regla que reconoce automáticamente líneas de extracto repetitivas (comisiones, ITF, intereses) y
propone o crea la contrapartida. Resuelve el problema de las decenas de movimientos pequeños que, a
mano, convierten la conciliación en una tarea de horas.

**5. Pago en exceso.**
El excedente queda en la cuenta del cliente como saldo a favor (crédito pendiente de aplicar).
Se aplica a la siguiente factura desde la conciliación de la cuenta por cobrar del cliente, o se
devuelve. Lo que no debe hacerse es registrarlo como ingreso.

**6. Nota de crédito por reversión vs. "modificar factura".**
*Reversión*: emite una nota de crédito que anula la factura y deja todo saldado. *Modificar factura*:
además de la nota de crédito, crea un **nuevo borrador** copiando la factura original para corregirla
y volver a emitirla. La primera se usa para anular; la segunda, para corregir un error de emisión.

**7. Asiento de la depreciación mensual y quién lo dispara.**
Debe *Depreciación del ejercicio* (gasto), haber *Depreciación acumulada* (activo negativo). Lo genera
el modelo de activo según su cuadro de depreciación, publicado por una acción planificada o
confirmado manualmente en el cierre.

**8. Distribución analítica y su automatización.**
Permite repartir un apunte entre una o varias cuentas analíticas por porcentaje, en una o varias
dimensiones (línea de negocio, canal, proyecto). Se automatiza con **modelos de distribución
analítica**, que la aplican según producto, cliente, cuenta o diario, sin intervención del usuario.

**9. Inventario 120 000 vs. cuenta contable 118 500 — 5 causas.**
(1) Categorías con valoración periódica mezcladas con perpetua; (2) asientos manuales a la cuenta de
existencias; (3) recepciones sin factura o facturas sin recepción (cuenta transitoria de entrada);
(4) costos en destino sin aplicar; (5) ajustes o desechos del último día sin contabilizar, o cambio de
método de costo durante el período.

**10. Coincidencia a tres bandas.**
El control cruzado entre **orden de compra**, **recepción** y **factura del proveedor**: se paga solo
lo que se pidió y llegó, al precio acordado. Odoo lo facilita con el control de facturas por
cantidades recibidas y avisa de las diferencias de precio y cantidad.

**11. Factura en USD con compañía en PEN.**
El apunte guarda el importe en moneda del documento y su equivalente en moneda de la compañía al tipo
de cambio de la fecha. Al cobrar con otro tipo de cambio surge una **diferencia de cambio realizada**
(cuenta de ganancia o pérdida por diferencia de cambio). Si al cierre sigue pendiente, se registra
una diferencia **no realizada** por revalorización.

**12. Publicar una factura en un período bloqueado.**
Odoo lo impide y avisa. Las opciones son: registrarla con fecha del período abierto (lo correcto si
el cierre ya se declaró) o —solo con autorización del contador y trazabilidad— levantar el bloqueo,
registrar y volver a bloquear. La decisión es del contador, no del consultor.

**13. Impuesto incluido en el precio.**
Se usa cuando el precio de cara al público ya contiene el impuesto: punto de venta, tienda en línea,
listas de precios al consumidor final. Efecto en el margen: la base imponible es menor que el precio
mostrado (precio / 1.18), así que el ingreso reconocido es menor de lo que el vendedor "ve".
Confundirlo es una causa habitual de márgenes mal calculados.

**14. Cierre de ejercicio en 6 pasos.**
(1) Completar y conciliar todas las operaciones del año; (2) registrar ajustes: depreciaciones,
diferidos, provisiones, diferencias de cambio, inventario final; (3) revisar el balance de
comprobación y las cuentas transitorias; (4) emitir y validar los estados financieros;
(5) generar el asiento de cierre que traslada el resultado a resultados acumulados;
(6) bloquear las fechas del ejercicio y respaldar.

---

| Aciertos | Lectura |
|---|---|
| 13–14 | Listo para la Fase 5 |
| 12 | Aprobado; repasa lo fallado |
| 9–11 | Repite los Ejemplos 3 (asientos) y 7 (cierre) |
| < 9 | Vuelve al bloque 4.0 y rehaz el cuaderno completo |
