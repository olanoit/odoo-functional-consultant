# Fase 3 — Compras e Inventario (cadena de suministro)

**Horas estimadas:** 45–50 h · **Prerrequisitos:** Fases 1 y 2 · **Base:** `LAB`

> **Objetivo:** entender el motor de existencias de Odoo —el más potente y el más
> malentendido— y saber diseñar una operación logística: almacenes, ubicaciones, rutas,
> reabastecimiento, trazabilidad por lote y valoración de inventario.

---

## 1. Resultados de aprendizaje

1. Ejecutar el ciclo Procure-to-Pay: solicitud → orden de compra → recepción → factura de proveedor.
2. Diseñar un almacén multi-etapa (recepción en 2/3 pasos, entrega en 2/3 pasos) y justificarlo.
3. Explicar **rutas, reglas de abastecimiento (pull) y reglas de stock (push)** con un ejemplo real.
4. Configurar reabastecimiento: reglas de reordenamiento, fabricar/comprar bajo pedido (MTO), plazos de entrega.
5. Implementar trazabilidad por **lote/número de serie** con fechas de vencimiento y estrategia FEFO.
6. Explicar la **valoración de inventario** (manual vs. automática, estándar/PEPS/promedio) y su asiento contable.
7. Leer los reportes de existencias y previsión, y diagnosticar por qué un producto "no está disponible".

## 2. Mapa de contenidos y fuentes

### Compras
| # | Tema | Documentación |
|---|---|---|
| 3.1 | Compras (visión general: RFQ, acuerdos, control de facturas) | [inventory_and_mrp/purchase.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/purchase.html) |

### Inventario
| # | Tema | Documentación |
|---|---|---|
| 3.2 | Inventario (índice) | [inventory.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory.html) |
| 3.3 | Gestión de productos (tipos, UdM, paquetes, embalaje) | [inventory/product_management.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/product_management.html) |
| 3.4 | Seguimiento: lotes, series, caducidad | [product_management/product_tracking.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/product_management/product_tracking.html) |
| 3.5 | Almacenes y ubicaciones, ajustes y conteos cíclicos | [warehouses_storage/inventory_management.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management.html) |
| 3.6 | Reabastecimiento (reglas de reordenamiento, MTO, plazos, interalmacén) | [warehouses_storage/replenishment.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment.html) |
| 3.7 | Reportes de inventario (previsión, niveles, tableros) | [warehouses_storage/reporting.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/warehouses_storage/reporting.html) |
| 3.8 | Operaciones diarias: rutas, push/pull, multi-paso, ubicación de destino, dropshipping, consignación | [shipping_receiving/daily_operations.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations.html) |
| 3.9 | Métodos de reserva (al confirmar, manual, programada) | [shipping_receiving/reservation_methods.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/shipping_receiving/reservation_methods.html) |
| 3.10 | Métodos de preparación (lote, clúster, oleada) | [shipping_receiving/picking_methods.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/shipping_receiving/picking_methods.html) |
| 3.11 | Estrategias de remoción (PEPS, UEPS, FEFO, cercanía) | [shipping_receiving/removal_strategies.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies.html) |
| 3.12 | Valoración de inventario (incl. costos en destino, chatarra) | [inventory/inventory_valuation.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/inventory/inventory_valuation.html) |
| 3.13 | Código de barras | [inventory_and_mrp/barcode.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/barcode.html) |

## 3. Ruta de estudio paso a paso

### Bloque 3.1 — Compras de punta a punta (7 h)
1. Configurar proveedores: precios de proveedor (lista de precios de compra), plazo de entrega,
   UdM de compra, moneda, condiciones de pago.
2. Ciclo: solicitud de cotización → enviar por correo → recibir → confirmar orden → recibir mercancía
   → **control de facturas** (por cantidades pedidas o recibidas) → factura de proveedor.
3. **Acuerdos de compra**: licitaciones (comparar ofertas de 3 proveedores) y contratos marco de reposición.
4. Recepción parcial y su efecto en la orden y en la factura pendiente.
5. Devolución a proveedor y nota de crédito.
6. Analizar el reporte de compras: precio promedio, plazos reales vs. prometidos, gasto por proveedor.

> **Romper:** confirmar la factura del proveedor antes de recibir la mercancía con control por
> "cantidades recibidas". Observar el aviso y entender el concepto de **factura en espera**.

### Bloque 3.2 — Anatomía del inventario (6 h)
1. **Ubicaciones**: internas, de proveedor, de cliente, de tránsito, virtuales (pérdida, producción, inventario).
   Entender la partida doble de existencias: *todo movimiento sale de una ubicación y entra a otra*.
2. Crear la jerarquía de ubicaciones del almacén de Lima (recepción, estanterías A/B/C, salida, control de calidad).
3. **Tipos de operación** (recepciones, entregas, transferencias internas): secuencias, ubicaciones por defecto,
   reserva, y cómo aparecen en el tablero.
4. Ajustes de inventario: conteo inicial, conteos cíclicos, diferencias y su contrapartida contable.
5. Registrar el stock inicial de los 75 productos por importación.

> **Concepto central a explicar al cliente:** en Odoo *no se "edita" el stock*; se registran
> movimientos. Un ajuste **también** es un movimiento contra una ubicación virtual. Es la base de la auditabilidad.

### Bloque 3.3 — Rutas y operaciones multi-etapa (8 h)
1. Activar ubicaciones de almacenamiento y rutas de varias etapas.
2. Configurar el almacén de Lima con **recepción en 3 pasos** (recibir → control de calidad → almacenar)
   y **entrega en 3 pasos** (recoger → empacar → enviar). Ejecutar el flujo completo y observar cada transferencia.
3. Diseccionar una **ruta**: reglas *pull* (jalar) y *push* (empujar), ubicación origen/destino, tipo de operación.
4. Configurar **segundo almacén (Arequipa)** y una **ruta de reabastecimiento interalmacén** con tránsito.
5. **Dropshipping** (envío directo del proveedor al cliente) y **consignación**. Ejecutar uno de cada uno.
6. **Reglas de ubicación de destino (putaway)** y almacenamiento por categoría de producto.

> **Prueba de dominio:** dibujar en papel la cadena completa de movimientos de un pedido de venta
> de Arequipa cuyo producto está en Lima y no hay stock — incluyendo qué documento crea qué.

### Bloque 3.4 — Reabastecimiento y planificación (6 h)
1. **Reglas de reordenamiento** (mín/máx, multiplicador de cantidad) y el reporte de reabastecimiento.
2. **MTO** (bajo pedido) vs. **MTS** (contra existencias): configurar ambos y comparar qué documento se dispara.
3. **Plazos de entrega**: del proveedor, de fabricación, de seguridad, de compra, de entrega al cliente.
   Calcular a mano la fecha planificada y verificar contra Odoo.
4. Reporte de **previsión** (forecast): leer entradas, salidas, disponible y "libre para usar".
5. Diagnosticar los tres motivos por los que una entrega queda en espera.

### Bloque 3.5 — Trazabilidad: lotes, series y vencimientos (6 h)
1. Activar lotes/series. Configurar productos de ANDINA GOURMET con **lote** y **fecha de caducidad**.
2. Recibir con lote, vender, y usar el **reporte de trazabilidad** hacia adelante y hacia atrás.
3. **FEFO**: configurar la estrategia de remoción y comprobar que Odoo reserva el lote que vence primero.
4. Simular una **recuperación de producto (recall)**: dado un lote defectuoso, encontrar todos los clientes afectados.
5. Números de serie: un producto con serie única, entrega y garantía.
6. Paquetes y embalaje: diferencia entre *packaging* (caja de 12) y *paquete* (bulto físico).

> Este bloque es el argumento de venta #1 en alimentos, farma y agroindustria. Domínalo a nivel demo.

### Bloque 3.6 — Valoración de inventario (7 h) ← *puente con la Fase 4*
1. Métodos de costo: **estándar**, **PEPS (FIFO)** y **promedio ponderado (AVCO)**. Crear tres productos,
   uno con cada método, y comprarlos a precios distintos. Comparar el costo resultante.
2. Valoración **manual (periódica)** vs. **automática (perpetua)**: qué asientos genera cada una y cuándo.
3. Configurar las cuentas de valoración en la categoría de producto (entrada de stock, salida, valoración,
   diferencia de precio) y rastrear el asiento de una recepción y de una entrega.
4. **Costos en destino (landed costs)**: distribuir flete e impuestos de importación sobre el costo de los productos.
5. **Chatarra (scrap)** y su impacto contable.
6. Revalorización manual de inventario.

> **Regla:** un consultor que no sabe explicar el asiento de una recepción con valoración automática
> **no puede** implementar contabilidad. Este bloque se repasa en la Fase 4.

### Bloque 3.7 — Código de barras y operación en piso (4 h)
1. Configurar la app de Código de barras: nomenclatura, códigos de ubicación y de producto.
2. Ejecutar recepción, transferencia interna y entrega con el escáner (o con el simulador de teclado).
3. Métodos de preparación: lote, clúster y oleada — cuándo recomendar cada uno.
4. Impresión de etiquetas de producto, lote y ubicación.

## 4. Laboratorio integrador

**Encargo:** *"Tenemos dos almacenes, productos con vencimiento y estamos perdiendo plata porque
no sabemos cuánto nos cuesta realmente el producto. Necesitamos control."*

Construir en `LAB`:
1. Almacén Lima con recepción y entrega en 3 pasos; almacén Arequipa en 1 paso.
2. Ruta de reabastecimiento Lima → Arequipa con ubicación de tránsito.
3. 10 productos con lote y caducidad, estrategia FEFO, y stock inicial cargado por importación.
4. Reglas de reordenamiento en 5 insumos con plazos de proveedor reales.
5. Valoración automática con PEPS en una categoría y promedio en otra, con cuentas configuradas.
6. Un caso de **costos en destino** con flete distribuido por peso.
7. Un ejercicio de *recall* documentado: lote → clientes afectados en < 3 minutos.
8. Reporte de previsión explicando por qué un pedido concreto está en espera.

## 5. Preguntas de comprensión (prueba B)

1. Explica en 5 líneas qué es una ubicación virtual y por qué existe.
2. Diferencia entre regla *push* y regla *pull*. Un ejemplo de cada una en ANDINA GOURMET.
3. ¿Qué documentos se crean al confirmar una venta de un producto MTO sin stock?
4. Un producto tiene 100 unidades a mano pero la entrega dice "En espera". Enumera 4 causas posibles y cómo verificar cada una.
5. ¿Qué asientos genera una recepción de mercancía con valoración automática y PEPS?
6. Diferencia entre *packaging* y *paquete*. ¿Cuál usarías para "caja de 24 latas"?
7. ¿Cómo garantizas que siempre salga primero el lote que vence antes?
8. ¿Cuándo recomiendas recepción en 2 pasos y cuándo en 3?
9. ¿Qué es un costo en destino y sobre qué base se puede distribuir?
10. Un cliente quiere que el almacenero no pueda hacer ajustes de inventario. ¿Cómo lo resuelves?
11. Diferencia entre control de factura por "cantidades pedidas" y "recibidas" en compras.
12. ¿Qué pasa con la valoración si cambias el método de costo de un producto que ya tiene movimientos?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (120 min):** en base nueva — crear 2 almacenes, entrega en 2 pasos, un producto
      con lote y FEFO, una regla de reordenamiento, valoración automática con cuentas, y ejecutar
      compra → recepción → venta → entrega mostrando el asiento de valoración.
- [ ] **B.** ≥ 10/12 en preguntas.
- [ ] **C. Entregable:** *"Diseño logístico de ANDINA GOURMET"*: diagrama de almacenes, ubicaciones,
      rutas y matriz de decisión (por qué 3 pasos, por qué FEFO, por qué PEPS).
- [ ] **D.** Ejercicio de trazabilidad *recall* ejecutado en < 3 min delante de un testigo (o grabado).
- [ ] Respaldo `LAB_fase03`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Activar multi-etapa "porque se ve profesional" | Cada paso extra es trabajo humano diario. Se justifica por control real, no por estética. |
| Ignorar la valoración hasta la fase contable | El contador descubre en el go-live que el inventario no cuadra. Es el defecto más caro. |
| Cambiar método de costo con movimientos existentes | Genera diferencias imposibles de explicar. Se decide **antes** de operar. |
| Cargar stock inicial a mano | En un cliente real son miles de líneas y lotes. Siempre por importación. |
| Confundir "a mano" con "disponible" | La reserva es la clave; el 80 % de los tickets de soporte de almacén son esto. |
| Prometer código de barras sin probar el hardware | La nomenclatura y el lector dan sorpresas; se prueba en preventa. |
