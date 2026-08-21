# Soluciones — H2: laboratorio de rutas

> Con Lima en 3 pasos (recepción y entrega) y Arequipa en 1 paso.

---

**1. Compra de 400 kg de aguaymanto (Lima, recepción 3 pasos).**
Al confirmar la orden se crea **una** transferencia: la *Recepción* (Proveedor → WH/Entrada).
Al validarla, Odoo genera la siguiente: *Control de calidad* (WH/Entrada → WH/Control de calidad),
y al validar esa, *Almacenamiento* (WH/Control de calidad → WH/Existencias).
**Total: 3 transferencias encadenadas**, creadas una tras otra, no todas de golpe.
Recorrido: `Proveedor → Entrada → Control de calidad → Existencias`.

**2. Venta de 120 conservas (Lima, entrega 3 pasos).**
Tres transferencias, en este orden: *Recogida* (Existencias → Empaque), *Empaque* (Empaque → Salida),
*Envío* (Salida → Cliente). La primera se genera al confirmar el pedido; las demás, al validar la anterior.

**3. La misma venta con solo 80 unidades disponibles.**
La entrega queda **En espera** (disponibilidad parcial). El almacenero puede:
(a) entregar las 80 y dejar el resto en un albarán de retropedido (*backorder*),
(b) esperar a completar, (c) forzar la cantidad si el stock existe pero no está reservado,
(d) cancelar. La opción por defecto —crear retropedido— es la correcta en la mayoría de negocios.

**4. Venta desde Arequipa de producto que está en Lima (con ruta de reabastecimiento).**
Cadena: *Entrega Arequipa* (AREQ/Existencias → Cliente) **en espera** →
*Transferencia interalmacén* Lima → Tránsito → Arequipa (2 documentos: salida de Lima y entrada en
Arequipa) que la abastece. Es una cadena **pull**: la necesidad del cliente jala el movimiento
desde Lima. Si no hay stock en Lima tampoco, se encadena una compra (si el producto tiene esa ruta).

**5. Producto MTO sin stock.**
Además de la entrega en espera, se crea automáticamente una **solicitud de compra** (o una orden de
fabricación, según la ruta del producto), **vinculada** al pedido de venta. La diferencia con el
escenario 3 es esa: en MTS el sistema espera stock; en MTO **lo genera**.

**6. Dropshipping.**
La mercancía **nunca entra al almacén**. Se crea una orden de compra al proveedor y un movimiento
`Proveedor → Cliente`. No hay recepción ni entrega propias. El control de calidad y la trazabilidad
quedan fuera de tu alcance: es un argumento para no usar dropshipping en productos con lote.

**7. Control de calidad rechaza un lote.**
La mercancía está físicamente en *WH/Control de calidad*, que es una ubicación **interna**: cuenta
como stock. Para sacarla: transferencia interna a **Cuarentena** (y si se descarta definitivamente,
**desecho**, que la manda a la ubicación virtual de chatarra) o **devolución al proveedor**
(transferencia inversa de la recepción). Mientras esté en una ubicación interna sin restricción,
puede reservarse para ventas: ese es el riesgo.

**8. Devolución de cliente de 20 unidades.**
Se crea una transferencia de **devolución** desde la entrega original (`Cliente → WH/Existencias`,
o a la ubicación que definas). Odoo propone el **mismo lote** que salió, porque lo conoce por la
trazabilidad — y eso es exactamente lo que necesitas para decidir si esa mercancía se revende o se
descarta. La devolución **no** genera nota de crédito: son hechos distintos (ver Fase 2).

**9. Regla de reordenamiento con 1 500 en stock y 3 000 reservadas.**
Odoo trabaja con la **cantidad prevista** (a mano − reservada + entrante), no con la física.
Previsto = 1 500 − 3 000 = **−1 500**. Como está por debajo del mínimo (2 000), repone hasta el
máximo (10 000): propone comprar **11 500 unidades**.
Quien espera "8 500" (10 000 − 1 500) está mirando el stock físico y olvidando lo comprometido.
Este es el escenario que más confunde al cliente en las primeras semanas.

**10. Transferencia interna del estante A a la cámara refrigerada.**
En la **valoración, nada**: ambas son ubicaciones internas de la misma compañía, el valor total del
inventario no cambia y no se genera asiento contable.
En la **trazabilidad, sí**: queda registrado el movimiento del lote entre ubicaciones, con fecha y
responsable. Es la diferencia entre "dónde está" (trazabilidad) y "cuánto vale" (valoración).

---

## Preguntas de diagnóstico

**A. "En espera" con producto en el almacén — 5 causas:**

| Causa | Verificación (< 1 min) |
|---|---|
| El stock está **reservado** por otra entrega anterior | Ver *Previsión* del producto o la pestaña *Otras operaciones* |
| Está en otra **ubicación** (cuarentena, control de calidad, otro almacén) | Reporte de existencias agrupado por ubicación |
| El **lote** requerido no tiene stock (con FEFO, el que toca está agotado) | Detalle de operaciones de la entrega |
| La reserva es **manual** o **programada** y aún no se ejecutó | Tipo de operación → método de reserva |
| Es la **etapa siguiente** de una cadena multi-paso y la anterior no se validó | Documento origen / transferencias vinculadas |

**B. "Validé la recepción y el stock no subió."**
Casi siempre: con recepción multi-paso, se validó solo el **primer** paso; la mercancía está en
*Entrada* o *Control de calidad*, no en *Existencias*. Se verifica mirando la ubicación destino de la
transferencia validada. Segunda causa: se miró el stock de otro almacén.

**C. "El sistema quiere que compre algo que ya pedí."**
La orden de compra existente está **en borrador** (no confirmada), por lo que no cuenta como
cantidad entrante; o la fecha prevista de llegada es posterior al horizonte de la regla; o la regla
está en otra ubicación distinta de la que recibe la compra.

**D. Priorizar la reserva para un cliente importante.**
Odoo ofrece: **prioridad** (estrella) en la entrega, **método de reserva** por tipo de operación
(al confirmar / manual / programada antes de X días) y **desreservar** manualmente.
Recomendación: método de reserva **manual o programada** en entregas, para que el jefe de almacén
decida a quién asigna el stock escaso, en lugar de que gane el que confirmó primero.

**E. Cantidad negativa en una ubicación.**
Se llega ahí validando salidas sin haber registrado la entrada correspondiente (una venta antes de
recibir la compra, o una fabricación sin registrar componentes). Se corrige con un **ajuste de
inventario** contra la ubicación de pérdidas, **y** encontrando la causa: si no, vuelve a pasar el
mes siguiente. Los negativos son el síntoma número uno de un proceso de almacén no respetado.
