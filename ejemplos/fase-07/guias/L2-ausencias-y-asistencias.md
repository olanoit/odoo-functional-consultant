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

**Ejercicio:** carga `04-horarios.csv`, luego **completa a mano las franjas horarias**
(`attendance_ids`) de cada uno; el CSV solo crea la cabecera. Añade los feriados peruanos del
segundo semestre: 28 y 29 de julio, 30 de agosto, 8 de octubre, 1 de noviembre, 8 y 25 de diciembre.

## 3. Los seis tipos de ausencia

Del archivo `03-tipos-ausencia.csv`:

| Tipo | ¿Requiere asignación? | Aprobación | Unidad | Documento |
|---|---|---|---|---|
| Vacaciones | Sí | Jefe | Día | No |
| Descanso médico | No | RR. HH. | Día | **Sí** |
| Permiso sin goce | No | **Doble** (jefe + RR. HH.) | Hora | No |
| Compensatorio | Sí | Jefe | Día | No |
| Licencia paternidad/maternidad | No | RR. HH. | Día | **Sí** |
| Capacitación externa | No | Jefe | Hora | No |

**Detalle que importa:** *Capacitación externa* tiene `time_type = other` (tiempo trabajado), no
`leave`. No es una ausencia: la persona está trabajando, solo que fuera. Confundirlo distorsiona los
reportes de ausentismo.

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
2. ¿El saldo se pierde a fin de año o se arrastra? ¿Dónde se configura?
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
3. Revisa cómo se calculan las horas extra contra el horario configurado.
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
