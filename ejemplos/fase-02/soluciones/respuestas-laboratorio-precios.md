# Soluciones — G2: laboratorio de listas de precios

> Calculado con el algoritmo real de Odoo 20 (idéntico al de v19 para estos casos): se filtran las reglas aplicables (producto, cantidad,
> fecha) y se ordenan por `applied_on, min_quantity desc, categ_id desc, id desc`; **gana la primera**.

---

## Los 18 casos

| # | Producto | Cant. | Lista | Fecha | Lista S/ | **Precio neto unitario** | Subtotal de la línea | Regla que gana |
|---|---|---|---|---|---|---|---|---|
| 1 | `CON-AGU-400g` | 1 | Mayorista | 2026-09-01 | 12.50 | **10.625** | 10.63 | `may_global` (−15 %) |
| 2 | `CON-AGU-400g` | 100 | Mayorista | 2026-09-01 | 12.50 | **9.75** | 975.00 | `may_cons100` (−22 %) |
| 3 | `CON-AGU-400g` | 500 | Mayorista | 2026-09-01 | 12.50 | **9.00** | 4 500.00 | `may_cons500` (−28 %) |
| 4 | `CON-AGU-400g` | 1 000 | Mayorista | 2026-09-01 | 12.50 | **8.50** | 8 500.00 | `may_agu400` (fijo) |
| 5 | `CON-AGU-400g` | 1 200 | Mayorista | 2026-09-01 | 12.50 | **8.50** | 10 200.00 | `may_agu400` (fijo) |
| 6 | `CON-SAU-400g` | 500 | Mayorista | 2026-09-01 | 13.12 | **9.4464** | 4 723.20 | `may_cons500` (−28 %) |
| 7 | `SNK-QUI-50g` | 100 | Mayorista | 2026-09-01 | 4.50 | **3.825** | 382.50 | `may_global` (−15 %) |
| 8 | `SNK-QUI-50g` | 200 | Mayorista | 2026-09-01 | 4.50 | **3.375** | 675.00 | `may_snack200` (−25 %) |
| 9 | `HAR-QUI-500g` | 50 | Mayorista | 2026-09-01 | 11.50 | **9.775** | 488.75 | `may_global` (−15 %) |
| 10 | `BEB-AGU-300ml` | 24 | Mayorista | 2026-09-01 | 3.90 | **3.315** | 79.56 | `may_global` (−15 %) |
| 11 | `CON-AGU-400g` | 1 | Tienda | 2026-09-01 | 12.50 | **12.50** | 12.50 | sin regla → precio de lista |
| 12 | `SNK-QUI-50g` | 500 | Tienda | 2026-09-01 | 4.50 | **4.50** | 2 250.00 | sin regla → precio de lista |
| 13 | `SNK-QUI-50g` | 1 | Promoción | 2026-11-30 | 4.50 | **4.50** | 4.50 | fuera de vigencia → precio de lista |
| 14 | `SNK-QUI-50g` | 1 | Promoción | 2026-12-15 | 4.50 | **3.60** | 3.60 | `promo_snacks` (−20 %) |
| 15 | `BEB-AGU-300ml` | 1 | Promoción | 2026-12-15 | 3.90 | **3.315** | 3.32 | `promo_bebidas` (−15 %) |
| 16 | `CON-AGU-400g` | 1 | Promoción | 2026-12-15 | 12.50 | **12.50** | 12.50 | la promo no cubre conservas |
| 17 | `CON-AGU-400g` | 1 | Exportación USD | 2026-09-01 | 12.50 | **11.875 PEN → $ 3.166667** | $ 3.17 | `exp_global` (−5 %) |
| 18 | `SNK-QUI-100g` | 240 | Exportación USD | 2026-09-01 | 7.88 | **7.486 PEN → $ 1.996267** | $ 479.10 | `exp_global` (−5 %) |

> **Sobre los decimales (comprobado en Odoo 20).** La regla calcula `precio − precio × % / 100` y en
> v20 **ese valor no se redondea a 2 decimales** en el precio unitario: el campo usa
> `min_display_digits` (mínimo 2 decimales, hasta 6), así que la línea muestra el valor exacto.
> El redondeo al céntimo (hacia arriba en el medio céntimo) ocurre recién en el **subtotal**:
>
> | Caso | Cálculo | Sin el ajuste *Descuentos* (la línea muestra) | Con *Descuentos* activo (la línea muestra) | Subtotal |
> |---|---|---|---|---|
> | 1 | 12.50 − 12.50 × 15 % | precio **10.625** | precio 12.50, desc. 15 % | **10.63** (1 u) |
> | 7 | 4.50 − 4.50 × 15 % | precio **3.825** | precio 4.50, desc. 15 % | **382.50** (100 u) |
> | 10 | 3.90 − 3.90 × 15 % | precio **3.315** | precio 3.90, desc. 15 % | **79.56** (24 u) |
> | 15 | 3.90 − 3.90 × 15 % | precio **3.315** | precio 3.90, desc. 15 % | **3.32** (1 u) |
>
> Lo mismo pasa con 9.4464, 3.375 y 9.775 (casos 6, 8 y 9). Si ves 10.62 / 3.83 / 3.31 en material
> antiguo, viene de versiones que redondeaban el precio unitario a 2 decimales; en v20 no es así. **Conclusión práctica:**
> valida la **regla que gana** y el **subtotal**, que es lo que se factura; no discutas con el cliente
> el tercer decimal del precio unitario.

*(Casos 17 y 18: con tasa 1 USD = 3.75 PEN. Odoo convierte el precio base a la moneda de la lista y
luego aplica el descuento; el orden no altera el resultado. Si tu tasa es otra, el importe en dólares
cambia; el de soles no.)*

## Los cuatro casos que más se fallan

**Caso 4 y 5 — el precio fijo gana aunque el descuento por categoría sea mayor.**
Con 1 000 unidades hay dos reglas aplicables: `may_cons500` (−28 % → 9.00) y `may_agu400` (fijo 8.50).
Gana el **precio fijo** porque es una regla de **producto** (`1_product`), más específica que una de
categoría. Aquí da igual cuál es más barata: manda la especificidad.

> Si el precio fijo hubiera sido S/ 11.00, **también** habría ganado, y el cliente mayorista pagaría
> **más** comprando **más**. Eso es exactamente lo que pasa en las implementaciones reales cuando
> alguien agrega una regla de producto sin revisar las de categoría.

**Caso 7 — el escalón no aplica todavía.**
100 unidades de snacks: la regla de snacks exige **200**. Solo queda la global. Muchos predicen 3.375
por confundir el escalón de conservas (100) con el de snacks (200). Los escalones se leen por categoría.

**Caso 13 vs. 14 — la vigencia manda.**
El 30 de noviembre la promoción no existe todavía; el 15 de diciembre sí. Si en Odoo te sale 3.60 el
día 30 de noviembre, revisa `date_start`: es un campo **Datetime** y la hora/zona horaria importa.

**Caso 16 — una lista sin regla para ese producto no es un error.**
La lista *Promoción* solo tiene reglas para snacks y bebidas. Una conserva cae al precio de lista.
Si el negocio esperaba mantener el descuento mayorista durante la promoción, la lista está mal
diseñada: haría falta una regla global o basar la lista *en otra lista* (`base = pricelist`).

## Respuestas a las preguntas de diseño

**A. "A Sol de Oro dale 30 % en todo".**
Ni descuento de línea ni lista nueva por cliente. Un descuento de línea no es auditable ni sobrevive
al vendedor; una lista por cliente es inmantenible con 300 clientes.
La respuesta correcta es preguntar **por qué** ese 30 %: si es por volumen, va como escalón en la lista
mayorista; si es una condición comercial permanente, se crea una lista *"Mayorista preferente"*
que agrupe a los clientes de ese nivel. **Se modela el criterio, no el caso particular.**

**B. Dos reglas de categoría con la misma cantidad mínima.**
El desempate final es por `id desc` — en la práctica, gana la creada más recientemente. Es un
comportamiento que **no debes usar como diseño**: revisa las reglas y elimina la duplicidad. Si dos
reglas compiten, el precio deja de ser explicable, y un precio inexplicable destruye la confianza.

**C. ¿Se acumulan la promoción y el descuento mayorista?**
**No.** Un pedido usa **una sola lista de precios**. Si el cliente mayorista compra en diciembre con la
lista *Mayorista*, no ve la promoción; si le pones la lista *Promoción*, pierde su descuento mayorista.
Para acumular habría que basar la promoción en la lista mayorista (regla de *Descuento* con
`base_pricelist_id = Mayorista`, que deja `base = pricelist`) y aplicar el descuento adicional sobre
ese resultado.
**Esta es una decisión de negocio que se pregunta y se documenta antes de configurar.**

**D. ¿Cuándo un *Recargo* (`markup`)?**
Cuando el precio se calcula **sobre el coste** con margen y redondeo: por ejemplo, exportación con
`base = standard_price`, recargo del 45 %, redondeo a 0.10 y margen mínimo garantizado (es lo que en v19
era el tipo *Fórmula*; los márgenes solo se ven en modo desarrollador). Con precios de
insumos volátiles (aguaymanto, azúcar), fijar precios sobre coste protege el margen sin recalcular
manualmente el catálogo cada mes.

**E. Descuento manual del 10 % sobre una línea con precio de lista.**
Se calcula sobre el **precio unitario ya resuelto por la lista**, no sobre el precio de venta original.
Es decir, se acumula. Se controla con: permisos (quién puede ver el campo descuento), reglas de
aprobación sobre cierto porcentaje (Fase 9) y el reporte de márgenes por vendedor.

## Autoevaluación

| Aciertos | Lectura |
|---|---|
| 17–18 | Dominas la resolución de precios. Puedes explicarla a un cliente |
| 14–16 | Aprobado. Revisa los casos fallados y repite el ejercicio en una semana |
| 10–13 | Vuelve a la sección 1 de G2 y rehaz las 4 listas desde cero |
| < 10 | No configures listas de precios en un cliente todavía |
