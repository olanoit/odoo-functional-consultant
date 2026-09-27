# L2 — Ausencias, asignaciones y asistencias

> El módulo que **todos** los clientes entienden y que más rápido genera adopción.
> También el que más se configura mal, porque los cálculos dependen de cosas que se definen antes.

---

## 1. El orden correcto de configuración

```
1. Horarios de trabajo (resource.calendar)
2. Empleados asignados a su horario
3. Días festivos globales
4. Tipos de ausencia
5. Planes de acumulación (si aplica)
6. Asignaciones a empleados
7. Recién entonces: solicitudes
```

**Saltarse el paso 1 es el error clásico**: si el horario está mal, todos los cálculos de días y
horas salen mal, y hay que rehacer las solicitudes ya aprobadas.

## 2. Los horarios de ANDINA GOURMET

| Horario | Uso | Horas/día | Total semanal |
|---|---|---|---|
| Administrativo | Oficina | 8 | 48 |
| Planta turno día | Producción y almacén | 8 | 48 |
| Planta turno tarde | Segundo turno | 8 | 48 |
| Medio tiempo | Contabilidad de apoyo | 5 | 25 |

**Ejercicio:** carga `04-horarios.csv`, luego **corrige a mano las franjas horarias**
(`attendance_ids`) de cada uno: al crear el horario, Odoo le copia las franjas del horario de la
empresa (por defecto L-V, 8 h/día), no las que indica su nombre.

> **Desde v19 (vigente en v20):** `resource.calendar` **no tiene campo `tz`**. La zona horaria se fija
> en cada empleado (`hr.employee.tz`, que se guarda en su versión, `hr.version`), no en el horario.
> Revisa que los 18 empleados queden en `America/Lima`: con la zona mal puesta, las horas de
> asistencia se desplazan 5 horas.

> **v20:** el horario tiene un **horario de referencia** (`reference_calendar_id`, por defecto el de la
> empresa) del que sale el *Equivalente a tiempo completo*. Si la empresa sigue con 40 h, el
> administrativo de 48 h aparecerá al 120 %: define bien la referencia antes de seguir.

Añade los feriados peruanos del segundo semestre: 28 y 29 de julio, 30 de agosto, 8 de octubre,
1 de noviembre, 8 y 25 de diciembre.

## 3. Los seis tipos de ausencia

Del archivo `03-tipos-ausencia.csv`, que se importa en el modelo **`hr.work.entry.type`**
(desde v19 `hr.leave.type` ya no existe: los tipos de ausencia y los tipos de entrada de trabajo
son el mismo modelo; en v20 sigue igual). Menú: *Ausencias → Configuración → Time Types*
(en es_419, «Tipos de permisos»).

| Tipo | ¿Requiere asignación? | Aprobación | Unidad | Documento |
|---|---|---|---|---|
| Vacaciones | Sí | Jefe | Día | No |
| Descanso médico | No | RR. HH. | Día | **Sí** |
| Permiso sin goce | No | **Doble** (jefe + RR. HH.) | Hora | No |
| Compensatorio | Sí | Jefe | Día | No |
| Licencia paternidad/maternidad | No | RR. HH. | Día | **Sí** |
| Capacitación externa | No | Jefe | Hora | No |

**Detalle que importa:** *Capacitación externa* tiene **`count_as = working_time`** (tiempo trabajado),
no `absence`. No es una ausencia: la persona está trabajando, solo que fuera. Confundirlo distorsiona
los reportes de ausentismo.

> **Desde v19:** el campo se llamaba `time_type` (`leave` / `other`) y ahora es **`count_as`**
> (`absence` / `working_time`). Además `code` es **obligatorio** —es el código de nómina— y
> `time_off_selectable = True` es lo que hace que el tipo aparezca en el menú de Ausencias.
>
> **Unidad, dos campos:** `unit_of_measure` (*Unidad*: en qué se asigna y acumula el saldo, días u
> horas; **por defecto, horas**) y `request_unit` (*Tipo de duración*: `day` día completo, `half_day`
> medio día, `hour` horas personalizadas). Si importas solo `request_unit = day`, las vacaciones se
> asignarían en horas: por eso el CSV trae las dos columnas.

**Ejercicio de diseño:** ¿por qué el permiso sin goce lleva **doble** aprobación y el descanso médico
solo una? Escribe la razón de negocio, no la técnica.

## 4. Asignaciones y acumulación

Dos formas de dar saldo:

| Forma | Cómo funciona | Cuándo usarla |
|---|---|---|
| **Manual** | Se asignan N días de una vez | Vacaciones asignadas por año completo |
| **Acumulación** (accrual) | Se devengan por período trabajado | Cuando la ley o la política devengan mes a mes |

**Ejercicio:** crea un plan de acumulación que otorgue **2.5 días al mes** (30 al año) y aplícalo a
los 18 empleados. Después responde:
1. ¿Qué pasa con el saldo de alguien que entró en septiembre?
2. ¿El saldo se pierde a fin de año o se arrastra? ¿Dónde se configura? (Pista: en cada nivel del
   plan, *acción con las acumulaciones no usadas* y el tope de arrastre `max_carriedover_duration`.)
3. ¿Puede pedirse vacaciones a cuenta de días no devengados todavía?

## 5. El ciclo completo (ejecutar)

1. Asigna saldos a los 18 empleados.
2. Procesa 10 solicitudes: 6 aprobadas, 2 rechazadas, 1 con doble aprobación, 1 con documento adjunto.
3. Mira el **calendario del equipo**: ¿hay dos operarios del mismo turno de vacaciones a la vez?
4. Aprueba unas vacaciones que se solapan con un turno **planificado** (Fase 6) y observa el conflicto.
5. Revisa el reporte de saldos y el de ausentismo por departamento.

## 6. Rompe a propósito

| Prueba | Qué observar |
|---|---|
| Solicitar vacaciones sin saldo | El mensaje exacto y si permite forzarlo |
| Solicitar sobre un feriado | ¿Cuenta el día o no? Depende del horario configurado |
| Solicitar medio día en un tipo configurado por días | Qué permite la unidad de solicitud |
| Cambiar el horario de un empleado con ausencias aprobadas | Si se recalculan los días o quedan como estaban |
| Aprobar dos ausencias solapadas del mismo empleado | Si Odoo lo detecta |

Cada resultado va a tu bitácora: son las preguntas literales que hará RR. HH. la primera semana.

## 7. Asistencias

1. Configura el **modo kiosco** con PIN para los 8 operarios y almaceneros.
2. Registra una semana de entradas y salidas, incluyendo una jornada con horas extra.
3. Revisa cómo se calculan las horas extra contra el horario configurado. **v20:** se definen como
   **reglas de tiempo** en *Asistencias → Configuración → Automatic Rules* (`hr.time.rule`; reemplazan
   a las reglas de horas extra de v19): umbral por día o semana, tolerancias, tipo de entrada de
   trabajo para el exceso y, si quieres, abono a *Compensatorio por horas extra* (*Allocate to*).
   Si en los ajustes exiges aprobación de asistencias (`attendance_validation`), valida las
   pendientes (estado *Borrador → Validado*); por defecto se aprueban solas.
4. Compara el reporte de asistencias con las **hojas de horas** de la Fase 6 y explica la diferencia:
   asistencia = *cuándo estuvo*; hoja de horas = *en qué trabajó*. Un cliente puede necesitar ambas,
   una o ninguna.

## 8. Errores frecuentes

| Error | Consecuencia |
|---|---|
| Configurar ausencias antes que los horarios | Todos los cálculos de días salen mal |
| No cargar los feriados | Se descuentan días de vacaciones en días no laborables |
| Tipos de ausencia sin definir quién aprueba | Solicitudes atascadas y usuarios frustrados |
| Confundir tiempo trabajado con ausencia | El reporte de ausentismo pierde sentido |
| Dar acceso a datos de RR. HH. a todos los usuarios | Problema legal y de confianza; se configura el día 1 |
