# Soluciones — Cuestionario de la Fase 3

> Se aprueba con **10 de 12**.

---

**1. ¿Qué es una ubicación virtual y por qué existe?**
Una ubicación que no corresponde a un espacio físico propio: proveedores, clientes, pérdidas de
inventario, producción, tránsito, chatarra. Existe porque en Odoo **todo movimiento tiene origen y
destino**: es la partida doble del inventario. Una compra no "aparece", viene *desde* la ubicación
del proveedor; un ajuste positivo viene *desde* la ubicación de pérdidas. Gracias a eso todo
movimiento es auditable y el inventario cuadra por construcción.

**2. Regla push vs. pull.**
La regla **pull** (jalar) se dispara por una **necesidad**: hay un pedido en la ubicación destino y
el sistema busca de dónde traerlo. La regla **push** (empujar) se dispara por una **llegada**: algo
entró en una ubicación y debe seguir hacia otra.
En ANDINA GOURMET: *pull* → una venta en Arequipa jala mercancía desde Lima. *Push* → lo recibido en
la zona de entrada se empuja al control de calidad y de ahí a existencias.

**3. Documentos al confirmar una venta MTO sin stock.**
La entrega (en espera) **y** el documento de abastecimiento vinculado: solicitud de compra si la
ruta es *comprar*, u orden de fabricación si es *fabricar*. Ambos quedan enlazados al pedido de
venta, de modo que se puede rastrear el origen de la necesidad.

**4. 100 unidades a mano pero la entrega "En espera" — 4 causas.**
(1) Están reservadas por otra entrega; (2) están en otra ubicación o almacén; (3) el lote que exige
la estrategia (FEFO) no tiene stock; (4) el método de reserva no es automático, o es un paso
posterior de una cadena cuyo paso previo no se validó.
Se verifica con el reporte de previsión, el detalle de operaciones y la pestaña de transferencias
vinculadas.

**5. Asientos de una recepción con valoración automática y PEPS.**
**Ninguno.** En Odoo 19 la valoración perpetua se llama, literalmente, *Perpetual (at invoicing)*:
validar la recepción sube el stock y crea la capa de costo PEPS, pero **no genera asiento**.

El asiento aparece al **validar la factura de compra**, y carga **directamente** la cuenta de
valoración de existencias contra la de proveedores (más el IGV). La antigua cuenta transitoria de
**entrada de existencias** (`property_stock_account_input_categ_id`) **fue eliminada**: ya no hay
dos momentos que conectar. Si el precio facturado difiere del recibido, la diferencia va a la cuenta
de **diferencia de precio** de la categoría.

> Es el error más probable de quien viene de v16–v18: buscar en la recepción un asiento que ya no
> se genera y concluir que la valoración está mal configurada.

**6. *Packaging* vs. paquete.**
El **empaque** (en v19, `uom_ids`) es una presentación comercial estándar: "caja de 24 latas" —
sirve para comprar y vender en múltiplos. El **paquete** es un bulto físico concreto e identificable
que agrupa productos en el almacén. Para "caja de 24 latas" se usa **empaque**.

**7. Garantizar que salga primero el lote que vence antes.**
Estrategia de remoción **FEFO** configurada en la ubicación o en la categoría de producto, con los
productos con `tracking = lot` y `use_expiration_date` activado y **fecha de caducidad cargada en
cada lote**. Sin la fecha en el lote, FEFO no tiene con qué ordenar y se comporta como FIFO.

**8. ¿Recepción en 2 o en 3 pasos?**
2 pasos cuando hay una zona de recepción distinta del almacén pero **no** hay inspección que pueda
rechazar. 3 pasos cuando existe un control de calidad real, con criterio de aceptación y alguien
responsable de ejecutarlo. Si el "control" es mirar la mercancía mientras se guarda, son 2 pasos —
o incluso 1.

**9. Costo en destino y bases de distribución.**
Es un costo adicional (flete, aduana, seguro, manipuleo) que se incorpora al **costo del producto**
recibido. Se puede distribuir por **cantidad**, **peso**, **volumen**, **valor** o a partes iguales.
Se elige la base que refleje cómo se genera el costo: flete por peso/volumen, seguro y aranceles por
valor.

**10. Que el almacenero no pueda hacer ajustes de inventario.**
Con los grupos de Inventario: *Usuario* puede operar transferencias, pero los ajustes requieren
permisos de administrador de inventario. Se configura con grupos, se verifica entrando con su
usuario. La discusión de fondo con el cliente es de **control interno**: quien mueve la mercancía no
debería ser quien ajusta las diferencias.

**11. Control de factura por cantidades pedidas vs. recibidas (compras).**
Campo `purchase_method` del producto. *Pedidas*: se puede facturar todo lo que se ordenó. *Recibidas*:
solo lo que efectivamente llegó. Para mercancía física se recomienda **recibidas**: es la mitad de la
coincidencia a tres bandas (orden ↔ recepción ↔ factura) y evita pagar lo que no llegó.

**12. Cambiar el método de costo de un producto con movimientos.**
Odoo revalúa y genera asientos de ajuste; el valor del inventario cambia de golpe y esa diferencia
impacta el resultado del período. Se decide **antes** de operar. Si hay que cambiarlo, se hace en un
corte de período, coordinado con el contador y documentado.

---

| Aciertos | Lectura |
|---|---|
| 11–12 | Listo para la Fase 4 |
| 10 | Aprobado; repasa lo fallado |
| 8–9 | Repite los laboratorios H2 y H3 |
| < 8 | No configures inventario en un cliente todavía |
