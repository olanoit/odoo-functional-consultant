# Cuaderno de ejemplos — Fase 3: Compras e Inventario

Casos prácticos para [`../../fases/fase-03-compras-inventario.md`](../../fases/fase-03-compras-inventario.md).
Continúa sobre la base `LAB` con los 79 productos de la Fase 1 y las **entregas pendientes** que
dejaron los 12 pedidos de la Fase 2.

> **Versión objetivo:** Odoo 19. Aquí hay cuatro cambios que rompen material antiguo:
> `stock.production.lot` → **`stock.lot`**, valoración `manual_periodic` → **`periodic`**,
> `qty_multiple` **eliminado** en reglas de reordenamiento, y `product.packaging` → `uom_ids`.
> Detalle en [`guias/H5-campos-tecnicos-v19-inventario.md`](guias/H5-campos-tecnicos-v19-inventario.md).

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-almacen-arequipa.csv` | Segundo almacén (1 paso), para contrastar con Lima |
| `datos/02-ubicaciones-lima.csv` | 6 ubicaciones internas incluida **cuarentena**, con código de barras |
| `datos/03-categorias-costo.csv` | Método de costo por categoría: FIFO, promedio y estándar conviviendo |
| `datos/04-productos-trazabilidad.csv` | 10 productos con lote, caducidad y días de alerta |
| `datos/05-lotes.csv` | 14 lotes con fechas de caducidad escalonadas (para FEFO) |
| `datos/06-stock-inicial.csv` | 29 líneas de stock inicial, con y sin lote |
| `datos/07-reglas-reordenamiento.csv` | 8 reglas mín./máx. sobre insumos y envases |
| `datos/08-ordenes-compra.csv` | 6 órdenes de compra con varias líneas |
| `guias/H1` | Diseño del almacén: cuántos pasos y por qué |
| `guias/H2` | **Laboratorio de rutas**: 10 escenarios + 5 diagnósticos |
| `guias/H3` | **Laboratorio de valoración**: 3 métodos, mismas operaciones |
| `guias/H4` | Trazabilidad y simulacro de retiro de producto |
| `guias/H5` | Chuleta de campos v19 de Inventario y Compras |
| `soluciones/` | Rutas, valoración y cuestionario |

## Antes de empezar

1. Apps: **Inventario**, **Compras**, **Ventas**, **Contabilidad** (para las cuentas de valoración).
2. En *Inventario → Configuración* activa: **Ubicaciones de almacenamiento**, **Rutas de varios pasos**,
   **Lotes y números de serie**, **Fechas de caducidad**, **Múltiples almacenes**,
   **Costos en destino**, **Estrategias de remoción**.
3. Configura el almacén de Lima a **3 pasos** de recepción y **3 pasos** de entrega
   (a mano: es el almacén por defecto y no tiene ID externo propio).

---

## Ejemplo 1 — Los dos almacenes
*(Bloque 3.2–3.3 · 60 min)*

1. Cambia Lima a 3+3 pasos. **Antes de guardar**, anota qué ubicaciones crees que va a crear Odoo.
2. Importa `01-almacen-arequipa.csv` (1 paso) y `02-ubicaciones-lima.csv`.
3. Compara en *Configuración → Ubicaciones* lo que existe ahora con lo que había antes.
4. Revisa *Configuración → Rutas*: lee las reglas que Odoo creó solo al activar los pasos.
   **Esa lectura es la mejor clase sobre rutas que vas a tener.**
5. Documenta la decisión con [`guias/H1-diseno-de-almacen.md`](guias/H1-diseno-de-almacen.md).

## Ejemplo 2 — Stock inicial y trazabilidad
*(Bloque 3.2 y 3.5 · 60 min)*

**Orden de carga:** `04-productos-trazabilidad.csv` → `05-lotes.csv` → `06-stock-inicial.csv`.

El archivo 06 usa **`inventory_quantity_auto_apply`**: escribe la cantidad contada **y aplica el
ajuste en el mismo paso**. Con el campo `inventory_quantity` normal tendrías que aplicar el ajuste
registro por registro después de importar. Es el truco que convierte una carga de stock de 4 000
líneas en un solo archivo.

**Verificaciones:**
1. Existencias totales: 14 líneas con lote y 15 sin lote, repartidas en 4 ubicaciones.
2. Abre *Conserva de Aguaymanto 400 g*: 4 lotes con caducidades de feb, abr, jun y ago de 2028.
3. El ajuste generó movimientos desde la ubicación **virtual de inventario**: búscalos y explícalos.
4. Comprueba que el valor del inventario ya no es cero (lo cuadrarás en la Fase 4).

## Ejemplo 3 — Laboratorio de rutas
*(Bloque 3.3 · 90 min)* ← **predice antes de ejecutar**

[`guias/H2-laboratorio-de-rutas.md`](guias/H2-laboratorio-de-rutas.md): 10 escenarios
(compra multi-paso, venta en 3 pasos, falta de stock, reabastecimiento entre almacenes, MTO,
dropshipping, rechazo de calidad, devolución, reordenamiento con reservas, transferencia interna)
y 5 preguntas de diagnóstico que **son literalmente los tickets de soporte** de las primeras semanas.

Aquí es donde por fin validas las entregas pendientes que dejaste en la Fase 2.

## Ejemplo 4 — Compras de punta a punta
*(Bloque 3.1 · 60 min)*

Importa `08-ordenes-compra.csv` (6 órdenes, sin precios: los toma del proveedor configurado en la
Fase 1). Luego:

1. Confirma 4 órdenes y recibe **una parcialmente** (crea retropedido).
2. Configura `purchase_method = receive` (control por cantidades recibidas) en los insumos y
   registra la factura de proveedor: comprueba que solo puedes facturar lo recibido.
3. Haz una **devolución al proveedor** de mercancía defectuosa.
4. Prueba un **acuerdo de compra** (licitación) pidiendo el mismo insumo a 3 proveedores y comparando.
5. Revisa el reporte de compras: precio promedio por proveedor y plazo real vs. prometido.

**Rompe a propósito:** intenta facturar antes de recibir con control por *recibidas*. Anota el aviso.

## Ejemplo 5 — Reabastecimiento
*(Bloque 3.4 · 60 min)*

1. Importa `07-reglas-reordenamiento.csv` (8 reglas mín./máx.).
2. Ejecuta el **reabastecimiento** y revisa qué propone comprar.
3. **El ejercicio clave:** toma el frasco de vidrio 400 g (mín. 2 000 / máx. 10 000), reserva 3 000
   unidades para una venta y vuelve a ejecutar. ¿Cuánto propone ahora? Calcúlalo antes.
   *(La respuesta, en el escenario 9 de H2. Pista: Odoo mira el stock **previsto**, no el físico.)*
4. Configura un producto como **MTO** y otro como **MTS** y compara qué documento dispara cada venta.
5. Calcula a mano la fecha planificada de una entrega usando los plazos del proveedor, de compra y de
   seguridad; luego compárala con la que muestra Odoo.

> **Nota v19:** el campo `qty_multiple` (múltiplo de compra) **ya no existe**. Ahora hay
> `qty_to_order` calculado y `qty_to_order_manual` para forzar una cantidad.

## Ejemplo 6 — Valoración de inventario
*(Bloque 3.6 · 90 min)* ← **el puente con la Fase 4**

[`guias/H3-laboratorio-de-valoracion.md`](guias/H3-laboratorio-de-valoracion.md): las mismas cinco
operaciones con precio estándar, PEPS y promedio. Spoiler del resultado, para que veas por qué importa:
las mismas 500 unidades finales valen **S/ 675.00**, **S/ 900.00** o **S/ 784.62** según el método.

Incluye además: asientos de la valoración automática, costos en destino con tres bases de
distribución, y el **procedimiento de cuadre inventario ↔ contabilidad** que será entregable en la Fase 4.

## Ejemplo 7 — Simulacro de retiro de producto
*(Bloque 3.5 · 45 min)*

[`guias/H4-trazabilidad-y-recall.md`](guias/H4-trazabilidad-y-recall.md): FEFO en acción, el recall
cronometrado (**menos de 3 minutos**), la retirada a cuarentena y el guion de demo de 3 minutos que
usarás en preventa con cualquier cliente de alimentos.

## Ejemplo 8 — Código de barras y operación en piso
*(Bloque 3.7 · 45 min)*

1. Instala **Código de barras**. Las ubicaciones del archivo 02 ya traen código (`LIMA-A`…).
2. Imprime (o genera en PDF) etiquetas de producto, de lote y de ubicación.
3. Ejecuta una recepción completa **solo con el escáner** (o simulando con el teclado).
4. Prueba una preparación por **lotes** (varias entregas a la vez) y compárala con la individual.
5. Anota el tiempo de cada método: ese dato es el argumento para justificar la inversión en lectores.

---

## Cierre: entregables de la Fase 3

- [ ] 2 almacenes configurados con pasos distintos y justificados (Ejemplo 1, guía H1).
- [ ] Stock inicial cargado por importación, con lotes y caducidades (Ejemplo 2).
- [ ] Laboratorio de rutas ≥ 8/10 (Ejemplo 3).
- [ ] Laboratorio de valoración resuelto y **cuadre inventario ↔ contabilidad documentado** (Ejemplo 6).
- [ ] Recall ejecutado en menos de 3 minutos, con evidencia (Ejemplo 7).
- [ ] **Entregable C:** *"Diseño logístico de ANDINA GOURMET"* — almacenes, ubicaciones, rutas y
      matriz de decisión (por qué 3 pasos, por qué FEFO, por qué cada método de costo).
- [ ] Respaldo `LAB_fase03_AAAAMMDD.zip`.

## Lo que la Fase 4 necesita de aquí

Compras recibidas y facturadas, ventas entregadas, ajustes de inventario y un valor de inventario
distinto de cero. Con eso podrás hacer un **cierre de mes real** en vez de un ejercicio teórico.
No borres nada: el desorden acumulado es el material de trabajo.

---

## Para ampliar

Dos fuentes de comunidad que conviene tener abiertas durante toda la fase:

| Recurso | Para qué en esta fase |
|---|---|
| **[Odoo en Español](https://www.youtube.com/@OdooSpanish)** | Ver explicado en video rutas de almacén, trazabilidad por lote y los métodos de valoración — **después** de haberlo hecho tú con estos datos |
| **[Cybrosys](https://www.cybrosys.com)** | Artículos por módulo; útiles para profundizar en las reglas de reordenamiento, los costos en destino y el cuadre de inventario |

> **Úsalas para el concepto, no para la configuración.** Buena parte de ese material está grabado o
> escrito para v15–v18, y en v19 cambiaron nombres de campo, valores de selección y modelos enteros.
> Contrasta siempre contra la documentación 19.4, contra [la tabla de cambios de v19](../fase-12/README.md#los-cambios-de-v19-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
