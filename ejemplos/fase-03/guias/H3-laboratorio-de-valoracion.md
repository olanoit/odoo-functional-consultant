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
Pruébalo en un producto de prueba y describe qué hizo Odoo.

**E.** Novedad de v19: `lot_valuated` (valoración por lote). ¿Qué problema resuelve y qué costo
operativo añade? ¿Para ANDINA GOURMET lo recomendarías?

## 5. Segunda parte: valoración automática y su asiento

1. Configura una categoría con **valoración perpetua** (`property_valuation = real_time`) y sus
   cuentas: entrada de existencias, salida de existencias, valoración y diferencia de precio.
2. Ejecuta una recepción y busca el asiento generado. Escribe el asiento a mano **antes** de mirarlo.
3. Ejecuta una entrega y haz lo mismo.
4. Compara con una categoría en **valoración periódica**: ¿qué asientos hay? ¿Cuándo se registran?

> **Nota v19:** los valores del campo cambiaron. Antes eran `manual_periodic` / `real_time`;
> ahora son **`periodic`** / **`real_time`**. Un CSV o script de v16–v18 con `manual_periodic` falla.

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
| Valor del inventario | Inventario → Reportes → Valoración | = saldo de la cuenta contable de existencias |
| Diferencias | Comparar ambos | Explicables una por una |

Este procedimiento es un **entregable de la Fase 4**; escríbelo ya, mientras tienes el contexto fresco.
