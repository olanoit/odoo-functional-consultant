# I4 — Checklist de cierre mensual

> **Entregable C de la Fase 4** y una de las piezas más reutilizables de tu kit de consultoría:
> se entrega a todos los clientes, adaptando cuentas y responsables.

**Empresa:** ANDINA GOURMET S.A.C. · **Período:** ____________ · **Responsable del cierre:** ____________

---

## Bloque 1 — Ventas e ingresos

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 1.1 | Todas las entregas del mes están facturadas | Pedidos con estado *Por facturar* = 0 | Facturación | ☐ |
| 1.2 | No hay facturas en borrador con fecha del período | Filtro estado *Borrador* | Facturación | ☐ |
| 1.3 | Las sesiones de PdV del mes están cerradas y contabilizadas | PdV → Sesiones, ninguna abierta | Tienda | ☐ |
| 1.4 | Notas de crédito del mes revisadas y con motivo | Listado de notas de crédito | Facturación | ☐ |
| 1.5 | Numeración de comprobantes sin huecos | Reporte por diario y secuencia | Contabilidad | ☐ |

## Bloque 2 — Compras y gastos

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 2.1 | Todas las recepciones del mes tienen factura registrada | Compras: *Por facturar* | Compras | ☐ |
| 2.2 | Coincidencia a tres bandas revisada (orden ↔ recepción ↔ factura) | Diferencias de precio y cantidad | Compras | ☐ |
| 2.3 | Gastos de empleados aprobados y contabilizados | Gastos → *Por aprobar* = 0 | RR. HH. | ☐ |
| 2.4 | Facturas de proveedor en borrador = 0 | Filtro estado | Contabilidad | ☐ |

## Bloque 3 — Bancos y caja

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 3.1 | Extractos de todas las cuentas importados hasta fin de mes | Un extracto por cuenta | Tesorería | ☐ |
| 3.2 | Conciliación al 100 %; sin líneas pendientes | Panel de conciliación en 0 | Tesorería | ☐ |
| 3.3 | Saldo contable = saldo del extracto, por cuenta | Comparación directa | Tesorería | ☐ |
| 3.4 | Cuenta de **pagos pendientes** (outstanding) revisada y explicada | Mayor de la cuenta | Contabilidad | ☐ |
| 3.5 | Arqueo de caja chica realizado | Diario de efectivo | Administración | ☐ |

## Bloque 4 — Inventario

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 4.1 | Todas las transferencias del mes validadas (nada *En espera* de fecha anterior) | Inventario → Transferencias | Almacén | ☐ |
| 4.2 | Ajustes de inventario del mes aplicados y justificados | Historial de ajustes | Almacén | ☐ |
| 4.3 | **Valor del inventario = saldo de la cuenta de existencias** | Ver guía de cuadre (§ siguiente) | Contabilidad | ☐ |
| 4.4 | Cuenta de **entrada de existencias** revisada (recepciones sin factura) | Mayor de la cuenta | Contabilidad | ☐ |
| 4.5 | Costos en destino del mes aplicados | Listado de costos en destino | Contabilidad | ☐ |

## Bloque 5 — Impuestos

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 5.1 | Reporte de impuestos cuadra con la contabilidad (IGV por pagar y crédito fiscal) | Reporte vs. mayor | Contabilidad | ☐ |
| 5.2 | Facturas sin impuesto revisadas una por una | Filtro por importe de impuesto = 0 | Contabilidad | ☐ |
| 5.3 | Detracciones y retenciones del período registradas | Cuentas específicas | Contabilidad | ☐ |
| 5.4 | Declaración presentada y pago registrado | Comprobante de pago | Contador | ☐ |

## Bloque 6 — Ajustes y cierre

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 6.1 | Depreciaciones del mes generadas y contabilizadas | Activos → asientos del período | Contabilidad | ☐ |
| 6.2 | Gastos e ingresos diferidos del mes registrados | Listado de diferidos | Contabilidad | ☐ |
| 6.3 | Diferencias de cambio (realizadas y no realizadas) calculadas | Asistente de diferencia de cambio | Contabilidad | ☐ |
| 6.4 | Provisiones del mes (planilla, servicios) registradas | Asientos misceláneos | Contabilidad | ☐ |
| 6.5 | Distribución analítica completa en ingresos y gastos | Apuntes sin analítica = 0 | Contabilidad | ☐ |

## Bloque 7 — Emisión y bloqueo

| # | Tarea | Cómo se verifica | Responsable | ✔ |
|---|---|---|---|---|
| 7.1 | Balance de comprobación revisado (sin saldos anómalos) | Reporte | Contador | ☐ |
| 7.2 | Estado de resultados y balance general emitidos | PDF/Excel archivado | Contador | ☐ |
| 7.3 | Antigüedad de saldos por cobrar y pagar emitida | Reportes | Cobranzas | ☐ |
| 7.4 | **Fecha de bloqueo** establecida | Ajustes → Bloqueos de fecha | Contador | ☐ |
| 7.5 | Respaldo de la base de datos del cierre | Archivo guardado | TI | ☐ |

---

## Anexo — Procedimiento de cuadre inventario ↔ contabilidad

1. **Inventario → Reportes → Valoración**: anotar el valor total a la fecha de cierre.
2. **Contabilidad → Mayor**: saldo de la(s) cuenta(s) de valoración de existencias a la misma fecha.
3. Si coinciden, documentar y cerrar. Si no, revisar en este orden:

| Causa probable | Cómo detectarla |
|---|---|
| Categorías con valoración **periódica** mezcladas con **perpetua** | Revisar el método por categoría |
| Asientos manuales directos a la cuenta de existencias | Filtrar el mayor por diario *Operaciones diversas* |
| Recepciones sin factura (cuenta de entrada de existencias) | Saldo de la cuenta transitoria |
| Costos en destino registrados y no aplicados | Listado de costos en destino en borrador |
| Ajustes de inventario del último día no contabilizados | Fecha de los asientos vs. fecha del ajuste |
| Cambio de método de costo durante el período | Historial del campo en la categoría |
| Desechos no registrados contablemente | Movimientos a la ubicación de chatarra |

4. Documentar **cada** diferencia con su causa y su corrección. Una diferencia sin explicación es
   una diferencia que volverá el mes siguiente, más grande.

> **Regla de oro del primer cierre:** el objetivo no es que cuadre por casualidad, sino que el
> cliente **sepa por qué cuadra**. Ese es el momento en que el proyecto se considera exitoso.
