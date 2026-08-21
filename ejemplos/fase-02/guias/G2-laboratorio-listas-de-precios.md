# G2 — Laboratorio de listas de precios

> **Instrucción:** completa la columna *Tu predicción* **antes** de abrir Odoo. Después comprueba
> creando una cotización con ese cliente, producto y cantidad. Solo entonces mira las soluciones en
> [`../soluciones/respuestas-laboratorio-precios.md`](../soluciones/respuestas-laboratorio-precios.md).
>
> Objetivo: **≥ 14 de 18**. Menos que eso significa que no dominas la precedencia de reglas, que es
> la causa #1 de los reclamos *"Odoo me pone mal los precios"*.

---

## 1. Cómo resuelve Odoo el precio (el algoritmo real)

Odoo toma **todas** las reglas de la lista que apliquen al producto, a la cantidad y a la fecha,
las ordena y **usa la primera**. El orden es (verificado en el código de v19):

```
applied_on ascendente , min_quantity DESCENDENTE , categoría , id
```

Traducido a lenguaje de negocio, gana la regla **más específica**:

```
1º  Variante concreta      (0_product_variant)
2º  Producto concreto      (1_product)
3º  Categoría de producto  (2_product_category)
4º  Todos los productos    (3_global)
```

y dentro del mismo nivel, **la de mayor cantidad mínima que el pedido alcance**.

Si **ninguna** regla aplica, el precio es el **precio de venta del producto** (`list_price`).

> Consecuencia práctica que debes poder explicar: una regla de *producto* con 15 % de descuento
> **le gana** a una de *categoría* con 30 %, aunque el cliente compre mucho. La especificidad manda
> sobre el importe. Ahí nacen la mayoría de los "descuentos que no se aplican".

## 2. Las reglas cargadas

**Mayorista B2B** (PEN)

| Regla | Aplica a | Cant. mín. | Cálculo |
|---|---|---|---|
| `may_global` | Todos los productos | 0 | −15 % |
| `may_cons100` | Categoría *Conservas* | 100 | −22 % |
| `may_cons500` | Categoría *Conservas* | 500 | −28 % |
| `may_snack200` | Categoría *Snacks* | 200 | −25 % |
| `may_agu400` | Producto *Conserva de Aguaymanto 400 g* | 1 000 | Precio fijo S/ 8.50 |

**Exportación USD** — `exp_global`: todos los productos, −5 %, en USD (tasa 1 USD = 3.75 PEN).

**Promoción Fin de Año** (PEN) — vigencia **2026-12-01 → 2026-12-31**:
`promo_snacks` (categoría Snacks, −20 %) y `promo_bebidas` (categoría Bebidas, −15 %).

**Tienda / Público** — sin reglas.

## 3. Los 18 casos

Precio de lista de referencia: Conserva Aguaymanto 400 g = **12.50** · Conserva Sauco 400 g = **13.12** ·
Snack Quinua 50 g = **4.50** · Snack Quinua 100 g = **7.88** · Harina Quinua 500 g = **11.50** ·
Néctar Aguaymanto 300 ml = **3.90**

| # | Producto | Cant. | Lista | Fecha del pedido | Tu predicción | Regla que crees que gana |
|---|---|---|---|---|---|---|
| 1 | Conserva Aguaymanto 400 g | 1 | Mayorista | 2026-09-01 | | |
| 2 | Conserva Aguaymanto 400 g | 100 | Mayorista | 2026-09-01 | | |
| 3 | Conserva Aguaymanto 400 g | 500 | Mayorista | 2026-09-01 | | |
| 4 | Conserva Aguaymanto 400 g | 1 000 | Mayorista | 2026-09-01 | | |
| 5 | Conserva Aguaymanto 400 g | 1 200 | Mayorista | 2026-09-01 | | |
| 6 | Conserva Sauco 400 g | 500 | Mayorista | 2026-09-01 | | |
| 7 | Snack Quinua 50 g | 100 | Mayorista | 2026-09-01 | | |
| 8 | Snack Quinua 50 g | 200 | Mayorista | 2026-09-01 | | |
| 9 | Harina Quinua 500 g | 50 | Mayorista | 2026-09-01 | | |
| 10 | Néctar Aguaymanto 300 ml | 24 | Mayorista | 2026-09-01 | | |
| 11 | Conserva Aguaymanto 400 g | 1 | Tienda | 2026-09-01 | | |
| 12 | Snack Quinua 50 g | 500 | Tienda | 2026-09-01 | | |
| 13 | Snack Quinua 50 g | 1 | Promoción | 2026-11-30 | | |
| 14 | Snack Quinua 50 g | 1 | Promoción | 2026-12-15 | | |
| 15 | Néctar Aguaymanto 300 ml | 1 | Promoción | 2026-12-15 | | |
| 16 | Conserva Aguaymanto 400 g | 1 | Promoción | 2026-12-15 | | |
| 17 | Conserva Aguaymanto 400 g | 1 | Exportación USD | 2026-09-01 | | |
| 18 | Snack Quinua 100 g | 240 | Exportación USD | 2026-09-01 | | |

## 4. Preguntas de diseño (responder por escrito)

**A.** El cliente pide: *"a Sol de Oro dale 30 % en todo"*. ¿Creas una lista nueva, una regla nueva
o un descuento de línea? Argumenta con criterio de mantenimiento a 2 años.

**B.** ¿Qué pasa si el mismo producto tiene dos reglas de categoría con la misma cantidad mínima?
¿Cómo lo evitas al diseñar?

**C.** El gerente quiere que la promoción de diciembre **no** se acumule con el descuento mayorista.
Con estas listas, ¿se acumula o no? ¿Por qué?

**D.** ¿Cuándo usarías `compute_price = formula` (descuento + margen + redondeo) en lugar de un
porcentaje simple? Da un caso de ANDINA GOURMET.

**E.** El vendedor pone un descuento manual del 10 % en una línea que ya trae precio de lista.
¿Sobre qué importe se calcula? ¿Cómo lo controlas?

## 5. Trampas conocidas

| Síntoma que reporta el cliente | Causa real |
|---|---|
| "El descuento por volumen no se aplica" | Hay una regla de *producto* más específica que gana |
| "Al cambiar la cantidad no cambia el precio" | El precio se recalcula al modificar la línea; si se editó a mano, queda fijo |
| "La promoción sigue activa en enero" | Fechas cargadas sin hora, o zona horaria: revisa `date_end` |
| "En la tienda en línea sale otro precio" | El sitio web usa la lista pública, no la del cliente (Fase 8) |
| "El precio en dólares está raro" | Falta la tasa de cambio del día o está invertida |
