# Soluciones — H3: laboratorio de valoración

> Cálculo paso a paso de las 5 operaciones con los tres métodos.
> Precio estándar de referencia: **S/ 1.35**.

---

## Resultado final

| Método | Costo salida op. 3 (1 200 u) | Costo salida op. 5 (800 u) | Stock final | **Valor final** | Costo unitario final |
|---|---|---|---|---|---|
| **Estándar** | 1 620.00 | 1 080.00 | 500 | **675.00** | 1.3500 |
| **PEPS (FIFO)** | 1 650.00 | 1 200.00 | 500 | **900.00** | 1.8000 |
| **Promedio (AVCO)** | 1 710.00 | 1 255.38 | 500 | **784.62** | 1.5692 |

**Las mismas 500 unidades valen 675, 784.62 o 900 soles según el método.** Esa frase, dicha en una
reunión con el gerente y el contador, es lo que justifica que el consultor participe en la decisión.

## Detalle del cálculo

### PEPS (FIFO)
```
compra 1 000 @ 1.35  → capas: [1000@1.35]                 valor 1 350.00
compra 1 000 @ 1.50  → capas: [1000@1.35, 1000@1.50]      valor 2 850.00
venta  1 200         → consume 1000@1.35 + 200@1.50 = 1 650.00
                        capas: [800@1.50]                 valor 1 200.00
compra   500 @ 1.80  → capas: [800@1.50, 500@1.80]        valor 2 100.00
venta    800         → consume 800@1.50 = 1 200.00
                        capas: [500@1.80]                 valor   900.00
```
El costo unitario final (1.80) refleja **la última compra**, porque lo viejo ya salió.

### Promedio ponderado (AVCO)
```
compra 1 000 @ 1.35  → valor 1 350.00 / 1 000 u  → AVCO 1.3500
compra 1 000 @ 1.50  → valor 2 850.00 / 2 000 u  → AVCO 1.4250
venta  1 200 @ 1.4250 → costo 1 710.00           → valor 1 140.00 (800 u)
compra   500 @ 1.80  → valor 2 040.00 / 1 300 u  → AVCO 1.5692
venta    800 @ 1.5692 → costo 1 255.38           → valor   784.62 (500 u)
```
Cada compra **recalcula** el costo unitario de todo el stock.

### Precio estándar
```
Todas las entradas y salidas se valoran a 1.35.
Entradas: 2 500 u × 1.35 = 3 375.00   Salidas: 2 000 u × 1.35 = 2 700.00
Valor final: 500 × 1.35 = 675.00
```
Las diferencias contra el precio real pagado (0.15 × 1 000 + 0.45 × 500 = **375.00**) van a la
**cuenta de diferencia de precio**, no al inventario.

## Respuestas a las preguntas

**A. ¿Cuál es el correcto?**
Los tres. No es una cuestión de exactitud sino de **política contable**: la empresa elige un método,
lo declara y lo mantiene. Al gerente se le responde: *"su inventario vale S/ 784.62 con el método
que su contador definió (promedio); si usáramos PEPS valdría 900. Lo importante es que el criterio
sea uno solo y no cambie, porque de ahí sale su costo de ventas y su utilidad."*

**B. La diferencia con precio estándar** va a la cuenta de **diferencia de precio de compra**.
Si nadie la revisa en seis meses, se acumula un saldo que nadie sabe explicar y que distorsiona el
estado de resultados: el inventario parece barato y el gasto aparece en otra línea. Por eso el
precio estándar **exige** revisión periódica y actualización del estándar.

**C. Recomendación por tipo de producto**

| Producto | Método | Razón |
|---|---|---|
| Materia prima perecible (aguaymanto, quinua) | **Promedio (AVCO)** | Precios muy volátiles; el promedio suaviza y evita costos erráticos por lote |
| Envases y embalajes | **Estándar** | Precio estable y negociado por volumen; simplifica y las diferencias son pequeñas |
| Producto terminado de alta rotación | **PEPS (FIFO)** | Coherente con la rotación física real (FEFO/FIFO) y con la trazabilidad por lote |

**D. Cambiar el método con movimientos existentes:** Odoo recalcula la valoración y genera asientos
de ajuste. El valor cambia de golpe y esa diferencia hay que explicarla al contador.
**Se decide antes de operar**; cambiarlo después es una decisión contable, no una configuración.

**E. `lot_valuated` (v19):** permite que **cada lote tenga su propio costo**. Resuelve el caso de
compras del mismo insumo a precios muy distintos donde importa el costo real de cada lote
(importaciones, campañas agrícolas). El costo operativo: obliga a manejar lotes en todo el flujo y
complica los ajustes.
Para ANDINA GOURMET **no lo recomendaría al inicio**: agrega complejidad antes de que el cliente
domine lo básico. Se deja como mejora de segunda fase, si el margen por lote resulta relevante.

## Costos en destino (parte 6)

Con 12 000 frascos a 1.35 (S/ 16 200) más S/ 6 000 de flete y aduana:

| Distribución | Cálculo | Resultado |
|---|---|---|
| Por cantidad | 6 000 / 12 000 | +S/ 0.50 por unidad → costo 1.85 |
| Por valor | Proporcional al importe de cada línea | Igual si hay una sola línea; distinto con varias |
| Por peso | Proporcional al peso de cada línea | El más justo para flete marítimo |

**Criterio:** el **flete** se distribuye por **peso o volumen** (es lo que cobra el transportista);
el **seguro** y los **derechos arancelarios**, por **valor** (se calculan sobre el importe).
Distribuir todo por cantidad es cómodo pero castiga a los productos livianos y baratos.

**Verificación obligatoria:** el valor del inventario debe subir **exactamente S/ 6 000**.
Si sube menos, alguna línea de la recepción quedó fuera del costo en destino.
