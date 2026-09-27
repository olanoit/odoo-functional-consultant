# J1 — Laboratorio de costeo: del insumo al producto terminado

> **Calcula el costo a mano antes de que Odoo te lo diga.** Es la única forma de detectar cuando
> el sistema se equivoca — que casi siempre significa que la configuración está mal.
>
> Soluciones en [`../soluciones/respuestas-laboratorio-costeo.md`](../soluciones/respuestas-laboratorio-costeo.md).

---

## 1. La estructura de producto de ANDINA GOURMET

```
Conserva de Aguaymanto 400 g  (LdM: 1 000 unidades)
├── Pulpa de aguaymanto pasteurizada   240 kg   ← se fabrica (LdM: 100 kg)
│   ├── Aguaymanto fresco              120 kg
│   ├── Ácido cítrico                  0.4 kg
│   ├── Op. Lavado y selección         45 min · Recepción
│   └── Op. Pulpeado y pasteurizado    90 min · Línea de pulpeado
├── Almíbar base 40 Brix               180 L    ← se fabrica (LdM: 200 L)
│   ├── Azúcar rubia                    80 kg
│   ├── Ácido cítrico                  0.6 kg
│   ├── Sorbato de potasio             0.2 kg
│   └── Op. Cocción de almíbar        120 min · Cocina
├── Frasco de vidrio 400 g           1 000 u
├── Tapa metálica 63 mm              1 000 u
├── Etiqueta frontal / posterior     1 000 u c/u
├── Caja de cartón 12 u                 84 u
├── Op. Envasado y sellado            240 min · Línea de envasado
└── Op. Etiquetado y encajado         180 min · Etiquetado
```

**Costos de los insumos** (de la Fase 1): aguaymanto 8.50/kg · ácido cítrico 18.50/kg ·
azúcar 4.20/kg · sorbato 34.00/kg · frasco 1.35 · tapa 0.28 · etiquetas 0.12 y 0.10 · caja 1.85.

**Costos por hora de los centros de trabajo** (archivo `02-centros-trabajo.csv`), con sus tiempos
de preparación y limpieza y su **eficiencia de tiempo**:

| Centro | S//hora | Preparación | Limpieza | Eficiencia |
|---|---|---|---|---|
| Recepción y lavado | 18.00 | 10 min | 15 min | 95 % |
| Pulpeado y pasteurizado | 42.50 | 20 min | 30 min | 90 % |
| Cocina de almíbar | 35.00 | 15 min | 20 min | 92 % |
| Envasado y sellado | 56.00 | 25 min | 25 min | 88 % |
| Etiquetado y empaque | 22.00 | 10 min | 10 min | 95 % |

**Cómo calcula Odoo la duración de una operación** (`mrp.routing.workcenter`, campo `time_total`):

```
duración = preparación + limpieza + ciclos × tiempo del ciclo × 100 / eficiencia
costo    = duración / 60 × costo por hora          (redondeado a céntimos por operación)
```

Los **ciclos** son la cantidad a fabricar dividida entre la capacidad del centro, redondeada hacia
arriba; sin capacidad configurada, la capacidad es la cantidad de la propia LdM, así que una orden
del tamaño de la LdM es **1 ciclo**. La eficiencia **alarga** el tiempo de ciclo: con 88 %, 240
minutos teóricos se convierten en 272.73.

## 2. Calcula (antes de abrir Odoo)

| # | Pregunta | Tu respuesta |
|---|---|---|
| 1 | Costo de materiales de **100 kg de pulpa** | |
| 2 | Costo de mano de obra de esa orden (incluye preparación, limpieza y eficiencia) | |
| 3 | **Costo por kg de pulpa** | |
| 4 | Costo por litro de **almíbar** | |
| 5 | Costo de materiales de **1 000 conservas** | |
| 6 | Costo de mano de obra de esa orden | |
| 7 | **Costo unitario de la conserva** | |
| 8 | Margen sobre el precio de venta de S/ 12.50 | |
| 9 | Diferencia con el costo estándar de S/ 6.80 cargado en la Fase 1 | |
| 10 | Si el aguaymanto sube a S/ 12.00/kg, ¿cuál es el nuevo costo unitario? | |

Después compara con el informe **Resumen de la LdM** (*BoM Overview*) de la lista de materiales en
Odoo. Ojo: para la conserva, ese informe despliega la pulpa y el almíbar **para la cantidad exacta que
se necesita** (240 kg = 3 ciclos de la LdM de 100 kg, con una sola preparación y limpieza), no a partir
del costo por kg de una orden de 100 kg; por eso su total difiere unos céntimos del tuyo (ver la
solución).

## 3. Lo que enseña el resultado

Cuando termines, tendrás una conversación real que ofrecer a un cliente:

- **Qué componente pesa más** en el costo (pista: no son los envases).
- **Cuánto pesa la mano de obra** frente a los materiales, y si vale la pena medir tiempos por operación.
- **Qué pasa con el margen** cuando sube la materia prima agrícola — el riesgo real del negocio.
- Si el costo estándar que la empresa venía usando **estaba bien o mal**, y cuánto le costó ese error.

## 4. Segunda parte: costo real vs. teórico

1. Ejecuta una orden de fabricación de 1 000 conservas **exactamente** como dice la LdM.
   El costo real debe coincidir con el teórico. Si no coincide, revisa la configuración. Recuerda que,
   por defecto, las operaciones se costean con el **tiempo real registrado** (campo *Coste basado
   en* de la operación = *Actual time*, traducido como «Hora actual»); para que coincida al céntimo,
   registra la duración esperada o cambia la operación a *Theoretical time*.
2. Ejecuta una segunda orden con desviaciones deliberadas:
   - consume 260 kg de pulpa en vez de 240 (merma),
   - la operación de envasado toma 300 minutos en vez de 240,
   - se desechan 15 unidades al final.
3. Compara ambas órdenes. **Escribe el análisis de varianza**: cuánto se desvió por material,
   cuánto por tiempo y cuánto por desecho.

> Ese análisis es exactamente el reporte que un gerente de planta paga por tener. Aprende a producirlo.

## 5. Tercera parte: el asiento contable de la producción

Con valoración perpetua (Fase 4), una orden de fabricación terminada **solo genera asientos si la
ubicación virtual *Producción* tiene cuenta de valoración** (una cuenta de producción en proceso,
*WIP*). Es la misma regla de la Fase 4: desde v19, y también en v20, un movimiento de existencias
contabiliza en el momento solo cuando toca una ubicación con cuenta propia
(`stock_account/models/stock_move.py`, `_should_create_account_move`; `mrp_account`, `_post_labour`).
Con esa cuenta configurada:

| Movimiento | Efecto contable |
|---|---|
| Consumo de componentes | Debe *WIP* / Haber existencias (componentes) |
| Absorción de mano de obra | Debe *WIP* / Haber la *Cuenta de gastos* del centro de trabajo (o la de gastos del producto) |
| Entrada del producto terminado | Debe existencias (producto terminado) / Haber *WIP*, por el costo real total |

Sin cuenta en la ubicación de producción, la orden **no genera ningún asiento**: el valor queda en
los movimientos de existencias y llega al mayor con el asiento de cierre de existencias del informe de
valoración (Fase 4, guía I4). Para órdenes que cruzan el cierre de mes, *Publicar asiento contable del
trabajo en curso* (acción sobre las órdenes de fabricación) contabiliza el WIP a la fecha.

**Escríbelo a mano** con las cuentas de la Fase 4 antes de mirarlo en Odoo, en las dos variantes.

## 6. Preguntas de diseño

**A.** ¿La pulpa debe ser un producto almacenable con su propia LdM, o una fase interna de la conserva?
Argumenta por trazabilidad, por costeo y por operación de planta.

**B.** El *Kit Navideño* es una LdM de tipo **kit** (`phantom`). ¿Cuánto cuesta el kit?
¿Y por qué **no** aparece una orden de fabricación al venderlo?

**C.** Si ANDINA GOURMET terceriza el etiquetado, ¿desaparece la operación de la LdM o cambia de forma?

**D.** ¿Qué método de costo (estándar, PEPS, promedio) recomiendas para los **semielaborados**?
¿Y para el producto terminado? Relaciónalo con lo aprendido en la Fase 3.
