# H4 — Trazabilidad y simulacro de retiro de producto (recall)

> El argumento de venta número uno en alimentos, farmacia y agroindustria.
> Se demuestra en 3 minutos o no se demuestra.

---

## 1. Preparación

Con los CSV `04-productos-trazabilidad.csv`, `05-lotes.csv` y `06-stock-inicial.csv` cargados tienes
10 productos con seguimiento por **lote** y **fecha de caducidad**, y 14 lotes con stock real.

Configura además:
- *Inventario → Configuración*: activar **Lotes y números de serie** y **Fechas de caducidad**.
- Estrategia de remoción **FEFO** (primero el que caduca antes) en la ubicación *Estante A*
  o en la categoría *Conservas*.

> **Campo clave:** `alert_time` (días antes de la caducidad para generar la alerta). En el CSV están
> 30 días para conservas y 3 para productos frescos. Ese número lo define el cliente, no tú:
> depende de cuánto tarda en colocar el producto en el mercado.

## 2. Ejercicio A — FEFO en acción (20 min)

El producto *Conserva de Aguaymanto 400 g* tiene 4 lotes con caducidades distintas
(feb, abr, jun y ago de 2028) y stock en cada uno.

1. Crea una venta de 300 unidades y **reserva**.
2. **Antes de mirar**, escribe qué lote(s) debería tomar Odoo y en qué orden.
3. Comprueba en el detalle de las operaciones de la entrega.
4. Cambia la estrategia a **PEPS (FIFO)** y repite con otra venta. ¿Cambió algo? ¿Por qué?
5. Fuerza manualmente un lote distinto al sugerido. ¿Odoo lo permite? ¿Queda registrado quién lo hizo?

**Concepto que debes poder explicar:** FEFO ordena por **fecha de caducidad**, FIFO por **fecha de
entrada**. En alimentos casi nunca coinciden, y confundirlos genera mermas por vencimiento.

## 3. Ejercicio B — El simulacro de recall (cronometrado)

> **Escenario:** la autoridad sanitaria informa que el lote `LT-AGU400-20260419` presenta un defecto.
> Tienes que responder **en menos de 3 minutos**:

| # | Pregunta | Dónde se responde | Tu respuesta |
|---|---|---|---|
| 1 | ¿Cuántas unidades se produjeron/recibieron de ese lote? | | |
| 2 | ¿Cuántas quedan en almacén y en qué ubicación? | | |
| 3 | ¿A qué clientes se les entregó y en qué fechas? | | |
| 4 | ¿Qué documentos (entregas, facturas) están involucrados? | | |
| 5 | ¿Qué materia prima entró en ese lote? *(se completa en la Fase 5)* | | |
| 6 | ¿Cuánto vale la mercancía afectada? | | |

**Herramientas:** botón **Trazabilidad** del lote, reporte de *Movimientos de existencias*
filtrado por lote, e historial del producto.

**Cronométrate.** Si tardas más de 3 minutos, el problema no es Odoo: es que no conoces los reportes.
Repite hasta bajar de 3.

## 4. Ejercicio C — Retirar el lote del stock disponible

Una vez identificado:
1. Mueve el stock afectado a la ubicación **Cuarentena** con una transferencia interna.
2. Verifica que ya no se puede reservar para ventas.
3. Registra la baja definitiva como **desecho (scrap)** y observa contra qué ubicación virtual va.
4. Anota el impacto en la valoración (lo cuadrarás en la Fase 4).

## 5. Ejercicio D — Alertas de caducidad

1. Crea un lote con caducidad dentro de 10 días.
2. Revisa dónde aparece la alerta y quién la ve.
3. Configura una acción: ¿qué hace la empresa con producto próximo a vencer? (liquidación, donación,
   baja). Esa decisión es **proceso de negocio**, y va documentada en el TO-BE.

## 6. Guion de demo (3 minutos, para la Fase 11)

> "Suponga que mañana Digesa le pide el rastro de un lote.
> *(abro el lote)* Aquí está: se produjo el 19 de abril, 240 unidades.
> *(clic en trazabilidad)* Se entregaron 180 a tres clientes: Sol de Oro el 5 de mayo,
> Los Andes el 12, Vega Norte el 20. Quedan 60 en el estante A.
> *(muevo a cuarentena)* Y con esto ya nadie puede venderlas.
> Eso que acaba de ver toma tres minutos. Hoy, ¿cuánto les tomaría?"

## 7. Errores frecuentes

| Error | Consecuencia |
|---|---|
| Activar lotes después de tener movimientos | El histórico queda sin trazabilidad y la cadena se corta |
| Poner lote solo al producto terminado | No puedes rastrear qué materia prima entró (Fase 5) |
| Dejar que el sistema genere lotes automáticos sin criterio | Números sin relación con la producción real; el operario no los reconoce |
| Confundir FEFO con FIFO | Mermas por vencimiento con stock "correcto" según el sistema |
| Prometer trazabilidad sin lote en los componentes | La demo se cae en la primera pregunta seria |
