# Soluciones — Cuestionario de la Fase 2

> Respóndelo primero tú. Se aprueba con **8 de 10**.

---

**1. Un cliente entrega parcialmente y quiere facturar solo lo entregado. ¿Qué configuras y dónde?**

La **política de facturación** del producto en *Ventas → Productos → pestaña Ventas* (campo
`invoice_policy`), con valor **Cantidades entregadas**. Es **por producto**, no global: se decide
producto por producto o por categoría al cargar el catálogo.
Consecuencia operativa que hay que advertir: si el almacén no registra la entrega a tiempo, no se
puede facturar. La política correcta obliga a un proceso de almacén disciplinado.

**2. Orden de precedencia entre lista de precios, descuento de línea y promoción.**

1. La **lista de precios** del pedido resuelve el precio unitario (una sola lista por pedido).
2. Dentro de la lista, gana la regla **más específica**: variante → producto → categoría → global;
   a igual especificidad, la de **mayor cantidad mínima** alcanzada.
3. El **descuento de línea** se aplica **sobre** ese precio ya resuelto (se acumula).
4. Las **promociones y cupones** (módulo de promociones) actúan a nivel de pedido, después,
   como líneas de descuento o productos gratis.

Las listas **no se acumulan entre sí**: para encadenar, una lista debe basarse en otra
(`base = pricelist`).

**3. Diferencia entre lead y oportunidad. ¿Cuándo activar leads?**

El **lead** es información en bruto sin calificar (un formulario web, una tarjeta de feria).
La **oportunidad** es un negocio identificado, con cliente, valor esperado y fecha de cierre,
que vive en el embudo.
Se activan leads cuando entra volumen de baja calidad y calificar tiene costo; si los contactos
llegan filtrados, los leads solo agregan un paso burocrático. Se decide **por equipo** (`use_leads`).

**4. ¿Qué pasa contablemente al cerrar una sesión de PdV?**

El cierre genera un **asiento contable** que resume la sesión: ingresos por ventas, impuestos,
y los cobros por método de pago (efectivo a la cuenta de caja, tarjeta a su cuenta transitoria).
La **diferencia de caja** declarada frente a la teórica se registra en una cuenta de diferencias.
Por eso el arqueo no es un trámite: es lo que hace que la contabilidad cuadre con el dinero real.

**5. Un pedido confirmado necesita una línea adicional después de entregado.**

Opciones: (a) agregar la línea al mismo pedido, lo que genera una nueva entrega y una factura
adicional; (b) crear un pedido nuevo; (c) si el pedido está **bloqueado** (`locked`), desbloquearlo
primero — y esa es una decisión con implicancias de control interno.
Criterio: si es la misma negociación y el mismo despacho, se agrega al pedido; si es una venta nueva,
pedido nuevo. Lo que **no** se hace es modificar líneas ya facturadas: para eso está la nota de crédito.

**6. ¿Cómo cotizas un producto con variantes cuando cada variante tiene precio distinto?**

Se cotiza la **variante**, no la plantilla: el precio (`list_price`) puede definirse por variante,
o mediante un **precio adicional por valor de atributo** sobre el precio base. En listas de precios
se puede afinar con reglas de tipo `0_product_variant`.
Si las variantes tienen precios muy dispares y procesos distintos, la señal es que deberían ser
productos separados.

**7. Explica MRR y por qué se pide desde el día 1.**

MRR = *Monthly Recurring Revenue*, el ingreso recurrente mensual normalizado de las suscripciones
activas. Es el indicador que dice cuánto factura la empresa **sin vender nada nuevo**.
Un negocio de suscripción se valora y se gestiona por MRR y por su tasa de cancelación: sin ese dato
no puede saber si crece o si está reemplazando clientes que se van.

**8. Nota de crédito vs. devolución de mercancía. ¿Pueden ir por separado?**

La **devolución** es un hecho logístico (la mercancía vuelve al almacén); la **nota de crédito** es
un hecho contable (se anula o reduce un importe facturado).
Sí, van por separado: puede haber devolución sin nota de crédito (cambio por producto idéntico) y
nota de crédito sin devolución (descuento comercial posterior, error de precio).
Odoo no las encadena automáticamente, y eso es correcto.

**9. ¿Cómo garantizas que un vendedor no vea las oportunidades de otro equipo?**

Con el grupo de Ventas *Usuario: solo documentos propios* (regla de registro por vendedor) y/o
restringiendo la pertenencia a equipos. Para "solo lo de mi equipo", el usuario debe ser miembro
del equipo y la visibilidad se controla por la configuración del equipo.
Es **configuración**, no desarrollo — y se prueba entrando con el usuario, no leyendo la casilla.

**10. "Aprobación del jefe si el descuento supera el 20 %": ¿estándar, Studio o desarrollo?**

**Studio**, con una **regla de aprobación** sobre el pedido de venta condicionada al descuento
(lo verás en la Fase 9). No requiere desarrollo.
La respuesta completa de consultor incluye la pregunta previa: *¿por qué se dan descuentos mayores
al 20 %?* Si es habitual, quizá el problema es la lista de precios y la aprobación solo documenta
un proceso mal diseñado. Primero se arregla el proceso; después se automatiza el control.

---

## Calificación

| Aciertos | Lectura |
|---|---|
| 9–10 | Listo para la Fase 3 |
| 8 | Aprobado; repasa lo fallado |
| 6–7 | Repite los Ejemplos 3 (precios) y 6 (facturación) |
| < 6 | Rehaz el cuaderno completo antes de avanzar |
