# H3 — Laboratorio de valoración: los 3 métodos con las mismas operaciones

> El bloque que separa a un consultor funcional de un usuario avanzado.
> **Predice los tres resultados antes de ejecutar.** Soluciones en
> [`../soluciones/respuestas-laboratorio-valoracion.md`](../soluciones/respuestas-laboratorio-valoracion.md).

---

## 1. El experimento

Crea **tres productos idénticos** (cópialos del *Frasco de vidrio 400 g*, coste inicial S/ 1.35),
cada uno en una categoría con método de costo distinto:

| Producto de prueba | Categoría | `property_cost_method` |
|---|---|---|
| FRASCO-STD | Envases y Embalajes | `standard` (precio estándar) |
| FRASCO-FIFO | Conservas *(o una categoría de prueba)* | `fifo` (PEPS) |
| FRASCO-AVCO | Snacks *(o una categoría de prueba)* | `average` (promedio ponderado) |

> El archivo `03-categorias-costo.csv` ya asigna un método distinto a cada categoría de ANDINA
> GOURMET, precisamente para que puedas comparar sin crear categorías nuevas.

## 2. Las operaciones (idénticas para los tres)

| # | Operación | Cantidad | Precio unitario |
|---|---|---|---|
| 1 | Compra | 1 000 | S/ 1.35 |
| 2 | Compra | 1 000 | S/ 1.50 |
| 3 | **Venta / salida** | 1 200 | — |
| 4 | Compra | 500 | S/ 1.80 |
| 5 | **Venta / salida** | 800 | — |

## 3. Predice antes de ejecutar

| Método | Costo de salida de la operación 3 | Costo de salida de la operación 5 | Stock final (u) | **Valor final** | Costo unitario final |
|---|---|---|---|---|---|
| Estándar | | | 500 | | |
| PEPS (FIFO) | | | 500 | | |
| Promedio (AVCO) | | | 500 | | |

## 4. Preguntas que van con el ejercicio

**A.** Los tres terminan con **500 unidades** pero con **valores distintos**. ¿Cuál es "el correcto"?
¿Qué le respondes a un gerente que pregunta cuánto vale su inventario?

**B.** Con precio **estándar**, ¿dónde va la diferencia entre S/ 1.35 y el precio real pagado?
¿Qué pasa si nadie revisa esa cuenta durante seis meses?

**C.** ¿Qué método recomiendas para: materia prima perecible, envases, producto terminado de alta
rotación? Justifica cada uno.

**D.** ¿Qué ocurre si cambias el método de costo de un producto que **ya tiene movimientos**?
Pruébalo en un producto de prueba (el método se cambia en la categoría) y describe qué hizo Odoo.

**E.** Desde v19 existe `lot_valuated` (valoración por lote). ¿Qué problema resuelve y qué costo
operativo añade? ¿Para ANDINA GOURMET lo recomendarías?

## 5. Segunda parte: valoración automática y su asiento

1. Configura una categoría con **valoración perpetua** (`property_valuation = real_time`) y sus
   cuentas, en la pestaña *Contabilidad* de la categoría (en v20 estos campos los aporta el módulo
   `account`; los nombres técnicos no cambian). Ojo con los nombres desde v19: **cuenta de existencias**,
   **variación de existencias** (`account_stock_variation_id`) y **diferencia de precio** (esta solo
   aparece con costo estándar y valoración perpetua). Las antiguas cuentas de *entrada* y *salida de
   existencias* **ya no existen**.
2. Ejecuta una recepción y busca el asiento generado. Escribe el asiento a mano **antes** de mirarlo.
3. Ejecuta una entrega y haz lo mismo.
4. Compara con una categoría en **valoración periódica**: ¿qué asientos hay? ¿Cuándo se registran?

> **Spoiler que necesitas para no perder una hora:** en los pasos 2 y 3 el asiento que vas a buscar
> **no existe**. Desde v19 `real_time` se llama *Perpetual (at invoicing)* (etiqueta aún sin traducir en v20): la recepción y la entrega no
> generan asiento; el asiento llega con la **factura**, y en la venta trae el costo de ventas dentro
> del mismo apunte que el ingreso. `periodic` es *Periodic (at closing)* y contabiliza al cierre,
> contra la cuenta de **variación de existencias**. El ejercicio real es explicar **por qué** el
> asiento no está donde lo buscabas y qué controles reemplazan al viejo cuadre de la cuenta
> transitoria. Lo desarrolla el laboratorio **I1** de la Fase 4.

> **Desde v19** los valores del campo son **`periodic`** / **`real_time`** (antes `manual_periodic` /
> `real_time`). Un CSV o script de v16–v18 con `manual_periodic` falla. En v20 el cierre periódico puede
> incluir además los **devengos** (facturas por emitir, facturas de proveedor por recibir), con cuentas
> nuevas en la categoría y en la compañía — lo verás en la Fase 4.

## 6. Tercera parte: costos en destino (landed costs)

Importas 12 000 frascos a S/ 1.35 y pagas S/ 4 800 de flete internacional y S/ 1 200 de
gastos de aduana.

1. Crea el costo en destino y distribúyelo **por cantidad**; anota el nuevo costo unitario.
2. Repite distribuyendo **por valor** y por **peso**; compara los tres resultados.
3. ¿Cuál usarías para el flete marítimo? ¿Y para un seguro de mercancía? Justifica.

**Verificación:** el valor total del inventario debe subir exactamente en S/ 6 000.
Si no, el costo en destino no se aplicó a todas las líneas.

## 7. El cuadre que exige el contador

Al terminar, ejecuta y documenta:

| Control | Dónde | Debe cumplirse |
|---|---|---|
| Valor del inventario | Informe *Valoración del inventario* (en v20 es `account.stock.valuation.report`, del módulo `account`) | = saldo de la cuenta contable de existencias |
| Diferencias | Comparar ambos | Explicables una por una |

Este procedimiento es un **entregable de la Fase 4**; escríbelo ya, mientras tienes el contexto fresco.
