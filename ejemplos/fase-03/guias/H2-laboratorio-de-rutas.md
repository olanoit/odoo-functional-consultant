# H2 — Laboratorio de rutas: ¿qué documentos crea Odoo?

> **Instrucción:** para cada escenario, escribe **antes de tocar Odoo** qué documentos se crean,
> en qué orden y entre qué ubicaciones. Después ejecútalo y compara.
> Soluciones en [`../soluciones/respuestas-laboratorio-rutas.md`](../soluciones/respuestas-laboratorio-rutas.md).
>
> Objetivo: **≥ 8 de 10**. Si no predices los movimientos, no puedes diagnosticar por qué una
> entrega está en espera — que es el 80 % del soporte de almacén.

**Configuración previa:** Lima con recepción y entrega en 3 pasos; Arequipa en 1 paso;
ruta de reabastecimiento Lima → Arequipa con tránsito; los datos de los CSV 01 a 08 cargados.

---

## Escenarios

**1.** Compra de 400 kg de aguaymanto al proveedor Valle Sagrado, almacén Lima.
¿Qué documentos se crean al **confirmar la orden**? ¿Y qué ubicaciones recorre la mercancía?

**2.** Venta de 120 conservas de aguaymanto 400 g a Sol de Oro, desde Lima.
¿Cuántas transferencias hay que validar hasta que el producto sale? ¿En qué orden?

**3.** La misma venta, pero **no hay stock suficiente** (solo 80 unidades).
¿Qué estado tiene la entrega? ¿Qué opciones tiene el almacenero?

**4.** Venta desde **Arequipa** de un producto que solo existe en Lima, con la ruta de
reabastecimiento activa. ¿Qué cadena de documentos aparece?

**5.** Un producto configurado como **MTO** (bajo pedido) se vende sin stock.
¿Qué documento adicional se crea respecto al escenario 3?

**6.** **Dropshipping**: venta de un producto marcado con la ruta de envío directo.
¿Entra alguna vez al almacén? ¿Qué documentos existen?

**7.** El control de calidad **rechaza** un lote recibido (Lima, 3 pasos).
¿Dónde queda físicamente la mercancía y cómo la sacas del stock disponible?

**8.** Devolución de un cliente de 20 unidades ya entregadas.
¿Qué documento se crea y contra qué ubicación? ¿Vuelve al mismo lote?

**9.** La regla de reordenamiento del frasco de vidrio 400 g (mín. 2 000 / máx. 10 000) se dispara
con 1 500 unidades en stock y 3 000 ya reservadas para producción.
¿Qué cantidad propone Odoo comprar y por qué?

**10.** Transferencia interna del estante A a la cámara refrigerada de 50 unidades de un producto
con lote. ¿Qué cambia en la valoración? ¿Y en la trazabilidad?

---

## Preguntas de diagnóstico (las que hará el cliente)

**A.** "La entrega dice *En espera* pero tengo el producto en el almacén." Enumera 5 causas posibles
y cómo verificar cada una en menos de 1 minuto.

**B.** "Validé la recepción pero el stock no subió." ¿Qué revisas primero?

**C.** "El sistema quiere que compre algo que ya pedí." ¿Qué está mal configurado?

**D.** "Necesito reservar mercancía para un cliente importante antes que para los demás."
¿Qué herramientas da Odoo (prioridad, método de reserva, reserva manual) y cuál recomiendas?

**E.** Un producto aparece con cantidad negativa en una ubicación. ¿Cómo llegó ahí y cómo se corrige?
