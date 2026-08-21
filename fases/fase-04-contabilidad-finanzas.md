# Fase 4 — Contabilidad y Finanzas

**Horas estimadas:** 50–60 h · **Prerrequisitos:** Fases 1, 2 y 3 · **Base:** `LAB`

> **Objetivo:** convertirte en el consultor que **el contador respeta**. No se trata de ser contador,
> sino de saber traducir la contabilidad de la empresa al modelo de Odoo, configurarla con precisión
> y acompañar un cierre mensual. Esta es la fase que separa a un consultor junior de uno senior.

⚠️ **Es la fase más larga y la que no se salta.** Si algo no se entiende, se repite el bloque.

---

## 1. Resultados de aprendizaje

1. Explicar la partida doble en el modelo de Odoo: diario, asiento, apunte, cuenta, conciliación.
2. Configurar desde cero: plan de cuentas, diarios, impuestos, condiciones de pago, posiciones fiscales.
3. Ejecutar y explicar el ciclo completo cliente (facturar → cobrar → conciliar → seguimiento de deuda).
4. Ejecutar y explicar el ciclo proveedor (factura → pago → conciliación → antigüedad de saldos).
5. Configurar activos fijos, gastos e ingresos diferidos.
6. Implementar contabilidad analítica para medir rentabilidad por proyecto/línea/centro de costo.
7. Producir e interpretar: balance general, estado de resultados, libro mayor, balance de comprobación,
   antigüedad de saldos, flujo de efectivo, declaración de impuestos.
8. Ejecutar un **cierre de mes** y describir el **cierre de año**.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 4.1 | Contabilidad (índice general) | [finance/accounting.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting.html) |
| 4.2 | Primeros pasos / configuración inicial | [accounting/get_started.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/get_started.html) |
| 4.3 | **Hoja de trucos de contabilidad** (léela dos veces) | [get_started/cheat_sheet.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/get_started/cheat_sheet.html) |
| 4.4 | Plan de cuentas | [get_started/chart_of_accounts.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/get_started/chart_of_accounts.html) |
| 4.5 | Multimoneda | [get_started/multi_currency.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/get_started/multi_currency.html) |
| 4.6 | Facturas de cliente | [accounting/customer_invoices.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/customer_invoices.html) |
| 4.7 | Condiciones de pago | [customer_invoices/payment_terms.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/customer_invoices/payment_terms.html) |
| 4.8 | Notas de crédito y reembolsos | [customer_invoices/credit_notes.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/customer_invoices/credit_notes.html) |
| 4.9 | Facturación electrónica (marco general) | [customer_invoices/electronic_invoicing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/customer_invoices/electronic_invoicing.html) |
| 4.10 | Facturas de proveedor | [accounting/vendor_bills.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/vendor_bills.html) |
| 4.11 | Activos fijos | [vendor_bills/assets.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/vendor_bills/assets.html) |
| 4.12 | Gastos diferidos / Ingresos diferidos | [deferred_expenses.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/vendor_bills/deferred_expenses.html) · [deferred_revenues.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/customer_invoices/deferred_revenues.html) |
| 4.13 | Bancos y efectivo | [accounting/bank.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/bank.html) |
| 4.14 | Conciliación bancaria y modelos de conciliación | [bank/reconciliation.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/bank/reconciliation.html) |
| 4.15 | Sincronización bancaria | [bank/bank_synchronization.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/bank/bank_synchronization.html) |
| 4.16 | Pagos (registro, lotes, seguimiento de deuda) | [accounting/payments.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/payments.html) · [payments/batch.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/payments/batch.html) · [payments/follow_up.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/payments/follow_up.html) |
| 4.17 | Impuestos | [accounting/taxes.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/taxes.html) |
| 4.18 | Posiciones fiscales | [taxes/fiscal_positions.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/taxes/fiscal_positions.html) |
| 4.19 | Reportes contables | [accounting/reporting.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/reporting.html) |
| 4.20 | Contabilidad analítica | [reporting/analytic_accounting.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/reporting/analytic_accounting.html) |
| 4.21 | Presupuestos | [reporting/budget.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/reporting/budget.html) |
| 4.22 | Declaración de impuestos | [reporting/tax_returns.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/reporting/tax_returns.html) |
| 4.23 | Cierre de ejercicio | [reporting/year_end.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/reporting/year_end.html) |
| 4.24 | Gastos de empleados | [finance/expenses.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/expenses.html) |
| 4.25 | Proveedores de pago en línea | [finance/payment_providers.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/payment_providers.html) |
| 4.26 | Valoración por precio promedio (puente con Fase 3) | [get_started/avg_price_valuation.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/get_started/avg_price_valuation.html) |

## 3. Ruta de estudio paso a paso

### Bloque 4.0 — Nivelación contable (5 h) *(saltar solo si eres contador)*
Antes de tocar Odoo, asegura estos conceptos con la *hoja de trucos* (4.3) y cualquier curso básico:
- Partida doble, debe/haber, cuentas de balance vs. de resultado.
- Ecuación contable y su reflejo en el Balance General.
- Devengado vs. percibido, provisión, depreciación, diferido.
- Qué es conciliar (emparejar un apunte pendiente con un pago).
- IGV/IVA: débito fiscal, crédito fiscal, base imponible, retención, percepción.

**Autoevaluación:** escribe a mano los asientos de: venta al crédito con IGV, cobro, compra de
activo, depreciación mensual, nómina simplificada. Si no salen, no sigas.

### Bloque 4.1 — Configuración contable inicial (7 h)
1. Instalar Contabilidad en `LAB`. Ejecutar el asistente de configuración.
2. **Plan de cuentas**: tipos de cuenta (¿por qué el tipo importa más que el número?), cuentas de
   conciliación, cuentas por defecto de la compañía. Crear/ajustar 15 cuentas propias.
3. **Diarios**: ventas, compras, banco, efectivo, misceláneos. Secuencias, cuentas por defecto,
   control de acceso por diario, diarios en moneda extranjera.
4. **Períodos fiscales**: bloqueos de fecha (bloqueo para todos, bloqueo para no asesores, bloqueo fiscal)
   y por qué son la herramienta antifraude más importante.
5. **Multimoneda**: activar USD, configurar tasas manuales y automáticas, y provocar una
   diferencia de cambio (realizada y no realizada).
6. Saldos iniciales: cargar el balance de apertura por asiento de diario misceláneo.

### Bloque 4.2 — Impuestos y posiciones fiscales (6 h)
1. Anatomía de un impuesto: cálculo (porcentaje, fijo, grupo), alcance, incluido en precio,
   afecta base de impuestos posteriores, distribución en factura y en nota de crédito
   (cuentas de impuesto y etiquetas de reporte).
2. Crear: IGV 18 %, exonerado, inafecto, impuesto incluido en precio, retención, un impuesto de grupo.
3. **Posiciones fiscales**: mapear impuestos y cuentas según el tipo de cliente
   (exportación, régimen especial, cliente exonerado). Detección automática por país/grupo.
4. Comprobar el efecto: mismo producto, tres clientes con posiciones distintas → tres facturas distintas.
5. Reporte de impuestos y cierre del período fiscal.

> **Romper:** cambiar la cuenta de un impuesto **después** de emitir facturas y observar qué pasa
> con el reporte. Concepto: la configuración fiscal se define antes de operar.

### Bloque 4.3 — Ciclo de ingresos (6 h)
1. Facturar desde pedido y facturar directo. Facturas en borrador vs. publicadas (asentadas):
   qué se puede editar en cada estado y por qué.
2. **Condiciones de pago**: contado, 30 días, pagos parciales (30/70), descuento por pronto pago.
   Ver cómo se generan varias líneas de vencimiento en un mismo asiento.
3. Notas de crédito: reversión total, parcial y "modificar factura". Diferencia entre las tres.
4. Cobros: registrar pago, pago parcial, pago agrupado, pago en exceso y su cuenta transitoria.
5. **Seguimiento de deuda (follow-up)**: niveles de recordatorio, correos automáticos, reporte de
   antigüedad de saldos por cobrar.
6. Portal del cliente: ver facturas y pagar en línea (proveedores de pago en modo de prueba).

### Bloque 4.4 — Ciclo de egresos (5 h)
1. Facturas de proveedor: creación manual, desde orden de compra, y por **carga de PDF/digitalización**.
2. Coincidencia a tres bandas: orden de compra ↔ recepción ↔ factura. Diferencias de precio y cantidad.
3. Pagos: individuales, en lote, parciales, con retenciones.
4. Antigüedad de saldos por pagar y previsión de flujo de caja.
5. **Gastos de empleados**: reporte de gastos, aprobación, contabilización y reembolso.

### Bloque 4.5 — Banco y conciliación (6 h)
1. Configurar diarios de banco; importar extracto (CSV/OFX) y crear extractos manuales.
2. Ejecutar la conciliación: emparejar con factura, con pago, dividir un apunte, conciliar parcialmente.
3. **Modelos de conciliación**: reglas automáticas para comisiones bancarias, redondeos y cobros recurrentes.
4. Conciliar diferencias de cambio en cuentas en USD.
5. Cerrar el saldo del banco y cuadrarlo con el extracto real.
6. Caja chica: diario de efectivo, arqueo, y su relación con el cierre de PdV (Fase 2).

> **Prueba de dominio:** conciliar 30 líneas de extracto en menos de 10 minutos usando modelos.
> Es la tarea diaria del contador; si tu configuración no lo permite, el cliente odiará Odoo.

### Bloque 4.6 — Activos, diferidos y analítica (7 h)
1. **Activos fijos**: modelos de activo, generación desde factura de proveedor, depreciación lineal/degresiva,
   venta/baja de activo y su asiento.
2. **Gastos e ingresos diferidos**: seguro anual pagado por adelantado, suscripción cobrada por adelantado.
3. **Contabilidad analítica**: planes analíticos, cuentas y **distribución analítica** automática por
   posición/producto. Aplicar a: línea de negocio (conservas vs. snacks), canal (mayorista/tienda/online)
   y proyecto.
4. Reporte analítico: rentabilidad por línea y por canal.
5. **Presupuestos**: crear presupuesto por cuenta analítica y comparar real vs. presupuestado.

### Bloque 4.7 — Reportes y cierre (6 h)
1. Recorrer todos los reportes: Balance General, Estado de Resultados, Flujo de Efectivo, Libro Mayor,
   Balance de Comprobación, Libro Mayor de Socios, Antigüedad de Saldos, Reporte de Impuestos.
2. Aprender el manejo del motor de reportes: comparativos entre períodos, filtro por diario/analítica,
   desglose (*drill-down*) hasta el apunte, anotaciones, exportación a Excel/PDF.
3. **Cierre de mes** simulado sobre los datos de las Fases 2 y 3:
   conciliar bancos → revisar cuentas transitorias → validar impuestos → revisar valoración de
   inventario vs. cuenta contable → depreciaciones → bloquear fechas → emitir estados.
4. Leer y resumir el proceso de **cierre de ejercicio** (asiento de cierre, cuenta de resultados acumulados).
5. Construir el **tablero financiero** del gerente: 6 indicadores y su fuente.

### Bloque 4.8 — Puente inventario ↔ contabilidad (4 h)
1. Verificar que el valor del inventario (reporte de valoración) cuadre con la cuenta contable de existencias.
2. Explicar cada diferencia posible: ajustes, chatarra, costos en destino, facturas sin recepción,
   recepciones sin factura (cuenta de entrada de stock / mercancía en tránsito).
3. Documentar el **procedimiento mensual de cuadre inventario-contabilidad** (entregable reutilizable).

## 4. Laboratorio integrador

**Encargo:** *"Queremos cerrar el mes en Odoo y que el balance cuadre con el inventario."*

Sobre los datos que ya existen en `LAB` (ventas de la Fase 2, compras de la Fase 3):
1. Configuración fiscal completa (IGV, exonerado, retención, 2 posiciones fiscales).
2. 3 condiciones de pago incluyendo una en dos armadas (30/70).
3. Extracto bancario de 40 líneas conciliado con al menos 3 modelos de conciliación automáticos.
4. 1 activo fijo depreciándose y 1 gasto diferido.
5. Plan analítico de 2 dimensiones aplicado a todas las ventas y compras del mes.
6. Presupuesto anual cargado y comparado.
7. **Cierre de mes ejecutado** con checklist firmada y fechas bloqueadas.
8. Cuadre documentado entre valoración de inventario y cuenta contable.

## 5. Preguntas de comprensión (prueba B)

1. ¿Por qué el **tipo** de cuenta importa más que su número en Odoo?
2. ¿Qué diferencia hay entre bloqueo de fecha "para todos", "para no asesores" y bloqueo fiscal?
3. Cliente exonerado de IGV compra un producto gravado. ¿Cómo lo resuelves sin tocar el producto?
4. ¿Qué es un modelo de conciliación y qué problema resuelve?
5. Se pagó una factura de más. ¿Dónde queda el excedente y cómo se aplica a la siguiente factura?
6. Explica la diferencia entre nota de crédito por reversión y por "modificar factura".
7. ¿Qué asientos genera la depreciación mensual de un activo y quién los dispara?
8. ¿Para qué sirve la distribución analítica y cómo se automatiza?
9. El inventario vale 120 000 y la cuenta contable dice 118 500. Enumera 5 causas posibles.
10. ¿Qué es la coincidencia a tres bandas y qué controla?
11. ¿Cómo se maneja una factura en USD cuando la moneda de la compañía es PEN, y dónde aparece la diferencia de cambio?
12. ¿Qué pasa si publicas una factura con fecha dentro de un período bloqueado?
13. ¿Cuándo un impuesto debe configurarse como "incluido en el precio" y qué efecto tiene en el margen?
14. Describe el cierre de ejercicio en Odoo en 6 pasos.

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (150 min):** base nueva — configurar plan de cuentas mínimo, 3 diarios, 3 impuestos,
      1 posición fiscal, 2 condiciones de pago; emitir 5 facturas, registrar cobros, importar y conciliar
      un extracto con 1 modelo automático, y emitir Balance y Estado de Resultados correctos.
- [ ] **B.** ≥ 12/14 en preguntas.
- [ ] **C. Entregable 1:** *"Checklist de cierre mensual"* (procedimiento paso a paso, con responsables y evidencias).
- [ ] **C. Entregable 2:** *"Procedimiento de cuadre inventario ↔ contabilidad"*.
- [ ] **D.** Explicar a un contador real (o grabarte explicando) el flujo factura→cobro→conciliación
      en 10 minutos, sin errores conceptuales.
- [ ] Respaldo `LAB_fase04`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| "El contador configura la contabilidad" | El contador define reglas; **tú** configuras. Si no entiendes, se configura mal. |
| Empezar a facturar antes de definir impuestos y posiciones fiscales | Rehacer facturas emitidas es imposible; se corrige con notas de crédito y desconfianza. |
| No usar analítica desde el inicio | Al año siguiente el cliente pide rentabilidad por línea y no hay datos históricos. |
| Ignorar las cuentas transitorias (pagos pendientes, entrada de stock) | Son el 90 % de los descuadres del primer cierre. |
| Conciliar a mano sin modelos | 200 líneas/mes a mano = el cliente vuelve a Excel. |
| Prometer "el balance cuadra solo" | Cuadra si la configuración y el proceso son correctos; hay que demostrarlo, no prometerlo. |
