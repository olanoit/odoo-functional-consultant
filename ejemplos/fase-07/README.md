# Cuaderno de ejemplos — Fase 7: Recursos Humanos

Casos prácticos para [`../../fases/fase-07-rrhh.md`](../../fases/fase-07-rrhh.md).

> ⚠️ **Cambios mayores de v19 en RR. HH.**
>
> 1. El modelo **`hr.leave.type` desapareció**: los tipos de ausencia ahora son **`hr.work.entry.type`**
>    (el mismo modelo que los tipos de entrada de trabajo de nómina). Campos nuevos obligatorios/relevantes:
>    **`code`** (obligatorio), **`count_as`** (`absence` / `working_time`, sustituye a `time_type`)
>    y **`time_off_selectable`** (que aparezca en el menú de Ausencias). El campo `time_type` ya no existe.
> 2. **`resource.calendar` ya no tiene `tz`**: la zona horaria vive en el empleado
>    (`hr.employee.tz`, vía `resource.resource`). Una columna `tz` en el CSV de horarios falla.
> 3. El modelo `hr.contract` **desapareció**. Ahora existe **`hr.version`**:
> cada empleado tiene versiones fechadas donde viven el salario (`wage`), el horario
> (`resource_calendar_id`), el puesto, el departamento y las fechas de contrato
> (`contract_date_start` / `contract_date_end`). Todo material anterior a v19 sobre contratos de
> Odoo está obsoleto, y los CSV de contratos de v16–v18 **no se pueden importar**.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-departamentos.csv` | 6 departamentos en jerarquía de 3 niveles |
| `datos/02-puestos.csv` | 10 puestos, algunos con vacantes abiertas |
| `datos/03-tipos-ausencia.csv` | 6 tipos con distintas reglas de aprobación y unidad → se importa en **`hr.work.entry.type`** |
| `datos/04-horarios.csv` | 4 horarios: administrativo, dos turnos de planta y medio tiempo (sin `tz`: se fija por empleado) |
| `datos/05-empleados.csv` | **18 empleados** con departamento, puesto, horario y costo/hora |
| `guias/L1` | **Alcance real de RR. HH. y nómina en Perú** (entregable de la fase) |
| `guias/L2` | Ausencias, asignaciones, acumulación y asistencias |

## Antes de empezar

Apps: **Empleados**, **Ausencias**, **Asistencias**, **Reclutamiento**, **Evaluaciones** (Enterprise).
Los 6 empleados de la Fase 6 se reutilizan: el archivo `05-empleados.csv` usa los mismos ID externos
y **actualiza** sus datos añadiendo departamento, puesto y horario. Los otros 12 se crean nuevos.

---

## Ejemplo 1 — La organización
*(Bloque 7.1 · 60 min)*

**Orden:** `01-departamentos.csv` → `02-puestos.csv` → `04-horarios.csv` → `05-empleados.csv`.

**Después de importar, a mano:**
1. Completa las **franjas horarias** de cada horario (el CSV solo crea la cabecera).
2. Carga los feriados peruanos del semestre.
3. Asigna responsables de departamento y revisa el **organigrama**.
4. Vincula empleados con usuarios de Odoo donde corresponda (no todos los operarios necesitan usuario).
5. Explora la pestaña de **versiones** (`hr.version`) de un empleado: es donde vive su salario,
   su horario y sus fechas de contrato en v19.

**Verificación:** 18 empleados, 6 departamentos, 4 horarios; el costo/hora cargado en la Fase 6 sigue ahí
(compruébalo: si se perdió, la rentabilidad de proyectos deja de funcionar).

## Ejemplo 2 — Ausencias de punta a punta
*(Bloque 7.3 · 90 min)*

[`guias/L2-ausencias-y-asistencias.md`](guias/L2-ausencias-y-asistencias.md), secciones 3 a 6:
seis tipos de ausencia con reglas distintas, plan de acumulación de 2.5 días al mes, 10 solicitudes
procesadas y cinco pruebas de ruptura deliberada.

**El ejercicio que más enseña:** aprobar vacaciones que chocan con un turno planificado de la Fase 6,
y ver qué avisa (o no avisa) el sistema.

## Ejemplo 3 — Asistencias
*(Bloque 7.2 · 45 min)*

Guía L2, sección 7: kiosco con PIN para los operarios, una semana de marcaciones con horas extra, y
la comparación con las hojas de horas. Debes poder explicar en una frase la diferencia entre ambas.

## Ejemplo 4 — Reclutamiento
*(Bloque 7.4 · 60 min)*

Los puestos del archivo `02-puestos.csv` ya traen vacantes abiertas (2 ejecutivos comerciales,
1 almacenero, 3 operarios).

1. Publica el puesto de *Ejecutivo Comercial* y define el embudo de selección.
2. Crea 8 candidatos por distintas vías: formulario web, alias de correo y referido interno.
3. Lleva uno hasta el final: entrevistas → propuesta → **firma del contrato en línea** →
   creación del empleado con su versión inicial.
4. Revisa los indicadores: tiempo de contratación y fuente de los candidatos.

## Ejemplo 5 — Evaluaciones y beneficios
*(Bloques 7.5 y 7.7 · 45 min · Enterprise)*

1. Configura un ciclo de evaluación semestral con autoevaluación y evaluación del jefe.
2. Lanza la evaluación de 3 empleados y revisa el reporte.
3. Recorre **Flota**, **Almuerzo** y **Recepción** lo suficiente para demostrarlos en una preventa.

## Ejemplo 6 — Nómina: el análisis de alcance
*(Bloque 7.6 · 90 min)* ← **el entregable de la fase**

[`guias/L1-alcance-nomina-peru.md`](guias/L1-alcance-nomina-peru.md): qué cubre el estándar, qué exige
la legislación peruana, las cuatro opciones que puedes ofrecer y cómo se dice todo esto en una reunión.

Si tienes Enterprise, complementa creando una estructura salarial simple (básico, asignación familiar,
descuento de pensión, aporte del empleador) y generando un lote de 5 recibos, **solo para entender el
motor**. No para prometer una planilla peruana.

---

## Cierre: entregables de la Fase 7

- [ ] 18 empleados con horario, departamento, puesto y costo/hora.
- [ ] Kiosco de asistencia funcionando y reporte de horas extra de una semana.
- [ ] 6 tipos de ausencia, uno con acumulación y doble aprobación; 10 solicitudes procesadas.
- [ ] Un puesto publicado, 8 candidatos y uno convertido en empleado.
- [ ] **Entregable C:** *"Alcance de RR. HH. y nómina para un cliente peruano"*, con recomendación
      argumentada y estimación por bloque.
- [ ] Respaldo `LAB_fase07_AAAAMMDD.zip`.
