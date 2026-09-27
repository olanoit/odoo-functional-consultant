# K1 — Rentabilidad de servicios: las tres políticas y su margen

> El negocio de servicios se gana o se pierde en el registro de horas. Este laboratorio te obliga a
> calcular el margen antes de que Odoo te lo muestre.
> Soluciones en [`../soluciones/respuestas-rentabilidad.md`](../soluciones/respuestas-rentabilidad.md).

---

## 1. Las tres políticas de facturación de servicios

| Producto del catálogo | Política (`invoice_policy` + `service_type`) | Cuándo se factura | Riesgo |
|---|---|---|---|
| Implantación en punto de venta (S/ 4 800) | **Precio fijo o de prepago** (`order` + `manual`) | Al confirmar el pedido | Si el trabajo se pasa de horas, el margen lo absorbe la empresa |
| Asesoría por hora (S/ 120/h) | **Según el registro de horas** (`delivery` + `timesheet`) | Según hojas de horas | Si nadie registra, no se factura |
| Desarrollo de marca propia (S/ 18 000) | **Basada en hitos** (`delivery` + `milestones`) | Según avance aprobado | Requiere hitos definidos y aceptados por escrito |

> En el formulario del producto las dos columnas se ven como un solo campo, *Política de facturación
> de servicios* (`service_policy`). La opción de hitos solo aparece cuando algún proyecto tiene
> activada la casilla *Hitos*.

**Ejercicio previo:** para cada uno, escribe qué pasa si el trabajo toma el doble de lo previsto.
Esa respuesta es la que define el precio que debes cotizar.

## 2. El caso: proyecto Sol de Oro (precio fijo)

Se vendió el desarrollo de **marca propia** a *Distribuidora Sol de Oro* por **S/ 18 000**,
presupuestando **120 horas**. El equipo registró:

| Persona | Costo/hora | Horas registradas |
|---|---|---|
| Lucía Ferrer (nutricionista) | 45.00 | 52 |
| Ana Vílchez (jefa de ventas) | 32.00 | 18 |
| Sofía Reátegui (gerente) | 65.00 | 12 |
| Pedro Quiroz (técnico) | 24.00 | 26 |

Además se gastaron **S/ 1 850** en viajes y muestras, reembolsables **no** facturados al cliente.

**Calcula antes de mirar Odoo:**

| # | Pregunta | Tu respuesta |
|---|---|---|
| 1 | Horas totales registradas | |
| 2 | Costo total de mano de obra | |
| 3 | Costo total del proyecto (con gastos) | |
| 4 | Margen en soles y en % | |
| 5 | Desvío frente a las 120 horas presupuestadas | |
| 6 | ¿Quién consumió más costo: quien puso más horas o quien cuesta más por hora? | |

## 3. El caso: bolsa de 20 horas de soporte

Se vendió una **bolsa de 20 horas** por S/ 2 200 (20 h × S/ 110, política *Precio fijo o de prepago*). Se consumieron: 6 h de Lucía, 9 h de Ana y 7 h de Pedro.

| # | Pregunta | Tu respuesta |
|---|---|---|
| 7 | Horas consumidas y horas restantes | |
| 8 | Costo real de esas horas | |
| 9 | Margen de la bolsa | |
| 10 | ¿Qué debería hacer el sistema al superar las 20 horas? | |

## 4. Configuración que hace posible el cálculo

1. **Costo por hora del empleado** (`hourly_cost`) — sin esto, el margen sale del 100 % y no sirve.
   Está en el archivo `01-empleados-servicios.csv`.
2. **Proyecto facturable** (`allow_billable`) y con hojas de horas (`allow_timesheets`).
3. **Cuenta analítica** del proyecto: es el puente con la contabilidad de la Fase 4.
4. El producto de servicio con `service_tracking` que crea el proyecto o la tarea automáticamente.

**Ejercicio:** quita el `hourly_cost` de un empleado, recarga el reporte de rentabilidad y observa
qué muestra. Ese es exactamente el estado en el que llegan la mayoría de las implementaciones a
producción: con márgenes ficticios.

## 5. El reporte que hay que saber leer

En v20 el proyecto **ya no tiene un panel lateral de «Rentabilidad»** (tampoco estaba en saas-19.4).
La rentabilidad se lee en dos lugares:

| Dónde | Qué muestra |
|---|---|
| Proyecto → botón *Estado* (tablero de *Actualizaciones*) → acción *Apuntes analíticos* | Todo lo cargado a la cuenta analítica del proyecto: ingresos facturados, costo de horas (horas × costo/hora), gastos, compras y materiales |
| *Hojas de horas → Reportes → Registro de horas → Por tipo de facturación* | Por proyecto y empleado: *Ingresos de la hoja de horas*, costo y **Margen** de las horas |

Arma con ellos el cuadro de siempre:

| Bloque | Qué incluye |
|---|---|
| Ingresos | Facturado + por facturar (según política) |
| Costos de horas | Horas × costo/hora del empleado |
| Otros costos | Gastos, compras y materiales asignados al proyecto |
| Margen | Diferencia y porcentaje |

> La acción *Apuntes analíticos* solo aparece si está activa la **contabilidad analítica**
> (grupo `analytic.group_analytic_accounting`).

**Preguntas para la bitácora:**
- ¿Por qué las horas del gerente encarecen tanto un proyecto? ¿Conviene que participe?
- ¿Qué haces cuando el margen es negativo a mitad de proyecto? ¿Se avisa al cliente o se absorbe?
- ¿Cómo se refleja este margen en la contabilidad (Fase 4)?

## 6. Sobreconsumo: el momento de la verdad

1. Registra horas hasta superar las vendidas en el proyecto de precio fijo.
2. Observa qué avisa Odoo y **dónde** lo avisa (¿lo ve el jefe de proyecto o solo el gerente?).
3. Define el procedimiento de negocio: ¿se para el trabajo? ¿se pide ampliación? ¿se absorbe?
   **Escríbelo**: forma parte del proceso TO-BE de una empresa de servicios.

## 7. Errores frecuentes

| Error | Consecuencia |
|---|---|
| No cargar el costo/hora | Todos los proyectos parecen 100 % rentables |
| Registrar horas al final del mes "de memoria" | Los datos no sirven ni para facturar ni para medir |
| Vender precio fijo sin histórico de horas | Se cotiza a ciegas y se pierde dinero en los proyectos grandes |
| No definir hitos por escrito en la modalidad por hitos | Discusión con el cliente en cada cobro |
| Facturar bolsas de horas sin controlar el saldo | Se regala trabajo sin que nadie lo note |
