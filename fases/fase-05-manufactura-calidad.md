# Fase 5 — Manufactura, Calidad, Mantenimiento y PLM

**Horas estimadas:** 35–40 h · **Prerrequisitos:** Fase 3 (imprescindible) y Fase 4 (para costos) · **Base:** `LAB`

> **Objetivo:** implementar una planta productiva en Odoo: desde la lista de materiales hasta el
> costo real de fabricación, pasando por centros de trabajo, subcontratación, control de calidad y
> mantenimiento de equipos.

---

## 1. Resultados de aprendizaje

1. Modelar productos fabricados con LdM multinivel, variantes y **kits (LdM tipo conjunto)**.
2. Ejecutar una orden de fabricación con y sin órdenes de trabajo, y leer sus movimientos de stock.
3. Configurar centros de trabajo con capacidad, tiempos y costo/hora, y explicar el **costo real** resultante.
4. Configurar subcontratación (con y sin envío de componentes).
5. Planificar con MPS y reglas de reabastecimiento, incluyendo plazos de fabricación.
6. Configurar controles de calidad en recepción, producción y entrega, con no conformidades.
7. Gestionar mantenimiento preventivo y correctivo de equipos, y su efecto en la disponibilidad.
8. Explicar PLM: versiones de ingeniería (ECO) y control de cambios.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 5.1 | Manufactura (índice) | [inventory_and_mrp/manufacturing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/manufacturing.html) |
| 5.2 | Configuración básica (LdM, órdenes, órdenes de trabajo) | [manufacturing/basic_setup.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/manufacturing/basic_setup.html) |
| 5.3 | Configuración avanzada (centros de trabajo, kits, LdM multinivel) | [manufacturing/advanced_configuration.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/manufacturing/advanced_configuration.html) |
| 5.4 | Flujos de trabajo de producción (MPS, desechos, desmontaje, secuencias) | [manufacturing/workflows.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/manufacturing/workflows.html) |
| 5.5 | Subcontratación | [manufacturing/subcontracting.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/manufacturing/subcontracting.html) |
| 5.6 | Calidad | [inventory_and_mrp/quality.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/quality.html) |
| 5.7 | Mantenimiento | [inventory_and_mrp/maintenance.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/maintenance.html) |
| 5.8 | PLM (gestión del ciclo de vida del producto) | [inventory_and_mrp/plm.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/plm.html) |
| 5.9 | Reparaciones | [inventory_and_mrp/repairs.html](https://www.odoo.com/documentation/saas-19.4/es/applications/inventory_and_mrp/repairs.html) |

> **Nota de edición:** Calidad, PLM y algunas funciones avanzadas son **Enterprise**.

## 3. Ruta de estudio paso a paso

### Bloque 5.1 — Listas de materiales (6 h)
1. Crear la LdM de "Conserva de aguaymanto 400 g": insumos, envase, etiqueta, merma.
2. **LdM multinivel**: producto terminado → semielaborado (pulpa) → materia prima. Ver cómo Odoo
   crea órdenes de fabricación encadenadas.
3. **Kit** (tipo conjunto): diferencia radical con una LdM de fabricación — no genera orden ni stock propio.
   Explicar cuándo usar cada uno (regla: ¿existe físicamente el producto padre en el almacén?).
4. LdM por **variante** y con **líneas de operación**.
5. Cantidades con decimales, mermas y consumo flexible (permitir consumir más o menos de lo previsto).
6. Reporte **estructura y costo** de la LdM: leer el costo teórico desglosado.

### Bloque 5.2 — Órdenes de fabricación y órdenes de trabajo (7 h)
1. Fabricar sin órdenes de trabajo: confirmar, reservar componentes, marcar como hecho.
   Identificar los movimientos: componentes → ubicación de producción → producto terminado.
2. Activar órdenes de trabajo y **centros de trabajo**: capacidad, eficiencia, tiempo de preparación
   y limpieza, costo por hora, OEE.
3. Ejecutar una orden en la **vista de taller (tablet)**: iniciar, pausar, registrar producción, terminar.
4. Producción parcial, órdenes divididas, sobreproducción y desechos (*scrap*) durante la fabricación.
5. Consumo de lotes en componentes y asignación de lote al producto terminado → **trazabilidad completa**
   (de materia prima a cliente final).
6. Desmontaje (*unbuild*) y su efecto en stock y costos.

### Bloque 5.3 — Costos de producción (5 h) ← *el bloque que más se vende*
1. Configurar el costo de los componentes (Fase 3) y el costo/hora de los centros de trabajo.
2. Comparar **costo estándar** vs. **costo real** de la orden de fabricación.
3. Ver el asiento contable generado con valoración automática: consumo de componentes,
   absorción de mano de obra y entrada del producto terminado.
4. Analizar la varianza: por qué el costo real difiere del teórico (mermas, tiempos, precio de insumos).
5. Construir el reporte de costo de producción por producto y por período.

### Bloque 5.4 — Planificación (5 h)
1. **Plazos de fabricación** y planificación hacia atrás desde la fecha de entrega comprometida.
2. **MPS (programa maestro de producción)**: demanda prevista, stock objetivo, sugerencias de reposición.
3. Reglas de reordenamiento sobre productos fabricados (MTS) vs. **fabricar bajo pedido** (MTO).
4. Diagnosticar: pedido de venta con fecha imposible → dónde se ve el cuello de botella.
5. Vista de planificación de centros de trabajo (carga y capacidad).

### Bloque 5.5 — Subcontratación (4 h)
1. Configurar un producto subcontratado: proveedor subcontratista, LdM de subcontratación.
2. Flujo **sin envío de componentes** (el subcontratista pone todo).
3. Flujo **con envío de componentes** (recogida y entrega al subcontratista, control de stock en su ubicación).
4. Costo del servicio de subcontratación en el costo final del producto.

### Bloque 5.6 — Calidad (4 h)
1. **Puntos de control de calidad**: por operación (recepción, fabricación, entrega), por producto,
   por categoría, con frecuencia (todas, periódica, aleatoria).
2. Tipos de control: instrucción, aprobar/rechazar, medición (con tolerancias), hoja de trabajo.
3. **Alertas de calidad** y no conformidades: flujo, responsables, acciones correctivas.
4. Caso ANDINA GOURMET: control de °Brix en la pulpa y de sellado en la conserva.

### Bloque 5.7 — Mantenimiento y PLM (4 h)
1. **Equipos**: registro, categorías, responsable, ubicación, criticidad.
2. Mantenimiento **preventivo** (por frecuencia o por métrica) y **correctivo** (solicitud desde el taller).
3. Indicadores: MTBF, MTTR, próximo mantenimiento previsto. Efecto en la planificación del centro de trabajo.
4. **PLM**: crear una ECO (orden de cambio de ingeniería) sobre una LdM, revisarla, aprobarla y aplicarla.
   Ver el versionado y el historial del cambio.
5. **Reparaciones**: orden de reparación de un producto devuelto, con piezas y facturación.

## 4. Laboratorio integrador

**Encargo:** *"Producimos conservas en 3 etapas, tercerizamos el etiquetado y necesitamos saber
cuánto cuesta realmente cada lote y quién compró un lote defectuoso."*

En `LAB`:
1. LdM de 3 niveles con al menos 8 componentes y merma declarada.
2. 2 centros de trabajo con costo/hora y tiempos; 4 operaciones definidas.
3. Etiquetado configurado como **subcontratación con envío de componentes**.
4. 2 puntos de control de calidad (uno de medición con tolerancia, uno de aprobación).
5. 1 equipo con mantenimiento preventivo programado.
6. 3 órdenes de fabricación completadas con lotes, una con desecho y una con sobreproducción.
7. Reporte de costo real vs. teórico explicado por escrito.
8. Trazabilidad demostrada: lote de aguaymanto → lote de pulpa → lote de conserva → cliente.

## 5. Preguntas de comprensión (prueba B)

1. Diferencia entre LdM de fabricación y kit. Da un caso donde elegir mal cuesta caro.
2. ¿Qué movimientos de stock genera una orden de fabricación y contra qué ubicación?
3. ¿Cómo se calcula el costo real de una orden con órdenes de trabajo?
4. ¿Qué diferencia hay entre subcontratación con y sin envío de componentes en términos de propiedad del stock?
5. ¿Cómo se planifica hacia atrás desde una fecha de entrega y qué plazos intervienen?
6. ¿Cuándo usar MPS en lugar de reglas de reordenamiento?
7. ¿Qué es una ECO y qué problema real resuelve?
8. Un control de calidad falla en producción. ¿Qué pasa con la orden y qué opciones tiene el operario?
9. ¿Cómo se rastrea desde un lote de materia prima hasta el cliente final?
10. ¿Qué efecto tiene el desmontaje (*unbuild*) sobre el inventario y la valoración?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (120 min):** crear LdM de 2 niveles, 1 centro de trabajo con costo, fabricar con
      lotes y mostrar el costo real y la trazabilidad completa.
- [ ] **B.** ≥ 8/10 en preguntas.
- [ ] **C. Entregable:** *"Diseño del proceso productivo de ANDINA GOURMET"*: diagrama de LdM,
      rutas de operaciones, puntos de control y modelo de costeo.
- [ ] **D.** Demo de 15 min: "de la materia prima al cliente, con trazabilidad y costo".
- [ ] Respaldo `LAB_fase05`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Usar kits para todo | Sin órdenes de fabricación no hay costo de producción ni trazabilidad del padre. |
| Ignorar mermas y sobreconsumo | El costo real se desvía y el cliente pierde confianza en el sistema. |
| Configurar órdenes de trabajo sin necesidad | Cada operación es un registro manual del operario en planta. Se justifica o se elimina. |
| Prometer trazabilidad sin lotes en componentes | La cadena se corta en el primer eslabón sin seguimiento. |
| Olvidar el costo/hora del centro de trabajo | El costo real sale igual al teórico y la analítica no sirve. |
