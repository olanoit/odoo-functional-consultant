# I3 — Conciliación bancaria: 40 líneas en menos de 10 minutos

> La tarea **diaria** del contador. Si tu configuración no permite conciliar rápido, el cliente
> vuelve a Excel — sin importar lo bien configurado que esté todo lo demás.

---

## 1. El extracto

`07-extracto-bancario.csv` trae **40 líneas** de agosto de 2026 en el diario *Banco BCP soles*:

| Tipo | Líneas | Qué representan |
|---|---|---|
| Cobros de clientes | 12 | Transferencias y depósitos identificados con su cliente |
| Pagos a proveedores | 8 | Con proveedor identificado |
| Comisiones, ITF y portes | 8 | Gastos bancarios pequeños y repetitivos |
| Planilla, AFP, SUNAT, detracciones | 4 | Pagos institucionales |
| Liquidaciones POS y depósitos de tienda | 4 | Enlace con el Punto de Venta (Fase 2) |
| Movimientos no identificados | 4 | **A propósito**: la realidad siempre los tiene |

Saldo neto del extracto: **S/ 8 401.85**.

## 2. Los tres tipos de línea y cómo se tratan

| Situación | Cómo se concilia | Tiempo por línea |
|---|---|---|
| Coincide con una factura pendiente | Odoo la propone; un clic | 2 segundos |
| Es un gasto recurrente (comisión, ITF) | **Modelo de conciliación** automático | 0 segundos |
| No se identifica | Se investiga o se manda a una cuenta transitoria | minutos |

**La productividad está en el segundo tipo.** Por eso el archivo `08-modelos-conciliacion.csv`.

## 3. Modelos de conciliación (v19)

> ⚠️ **Cambio de v19:** el campo `rule_type` desapareció. Ahora se usa **`trigger`**
> (`manual` / `auto_reconcile`) junto con los criterios `match_label`, `match_label_param`,
> `match_amount`, `match_journal_ids`, `match_partner_ids`.

Los 4 modelos cargados:

| Modelo | Criterio | Contrapartida | Automático |
|---|---|---|---|
| Comisiones bancarias | etiqueta contiene *"Comisión"* | 6532 Gastos bancarios | Sí |
| ITF | etiqueta contiene *"ITF"* | 6532 Gastos bancarios | Sí |
| Portes y mantenimiento | etiqueta contiene *"Portes"* | 6532 Gastos bancarios | Sí |
| Intereses bancarios | etiqueta contiene *"Intereses"* | 7761 Ingresos financieros | No (propuesta manual) |

**Ejercicio:** importa el extracto **antes** de crear los modelos, concilia 5 comisiones a mano y
cronométrate. Después crea los modelos, deshaz la conciliación y repite. La diferencia de tiempo,
multiplicada por 12 meses, es el argumento de venta.

## 4. El ejercicio completo (cronometrado)

1. Importa `07-extracto-bancario.csv`.
2. Importa `08-modelos-conciliacion.csv` y ejecuta la conciliación automática.
3. Concilia los cobros de clientes contra las facturas de las Fases 2 y 3.
4. Concilia los pagos a proveedores contra sus facturas.
5. Los 4 movimientos **no identificados**: decide qué hacer con cada uno y documéntalo.
6. Cierra el saldo del banco y compáralo con el saldo del extracto.

**Meta: menos de 10 minutos** para las 40 líneas, contando desde el paso 3.

## 5. Los casos difíciles (los que hacen la diferencia)

| Caso | Cómo se resuelve |
|---|---|
| Un depósito paga **3 facturas** | Se seleccionan las 3 en la conciliación; la suma debe cuadrar |
| El cliente pagó **de menos** (retención) | Se concilia parcialmente y el saldo queda abierto, o se registra la retención |
| El cliente pagó **de más** | El excedente queda como saldo a favor, aplicable a la siguiente factura |
| Un cobro sin factura emitida | Se registra como **anticipo de cliente** (cuenta de pasivo), no como ingreso |
| Transferencia entre cuentas propias | Se concilia contra la otra cuenta bancaria, **no** contra un cliente |
| Cheque devuelto | Se revierte el cobro; la factura vuelve a estar pendiente |

## 6. Preguntas para tu bitácora

1. ¿Qué es la cuenta de **pagos pendientes** (outstanding) y por qué el pago no toca directamente el banco?
2. ¿Qué diferencia hay entre *registrar un pago* y *conciliar*?
3. ¿Por qué el saldo contable del banco puede diferir del saldo del extracto y en qué casos es normal?
4. ¿Qué haces con un movimiento no identificado al cerrar el mes? ¿Puedes dejarlo sin conciliar?
5. ¿Cómo se relacionan las liquidaciones de POS del extracto con el cierre de caja del Punto de Venta?

## 7. Errores frecuentes

| Error | Consecuencia |
|---|---|
| Crear pagos manuales en vez de conciliar el extracto | Se duplican los movimientos y el banco nunca cuadra |
| Mandar lo no identificado a "otros gastos" para cerrar rápido | Se pierde el rastro de un cobro real de un cliente |
| No usar modelos de conciliación | 200 líneas al mes a mano: el contador abandona el sistema |
| Conciliar contra el cliente equivocado | La antigüedad de saldos miente y se reclama a quien ya pagó |
| Dejar la cuenta de pagos pendientes sin revisar | Saldo creciente que nadie entiende en el primer cierre |
