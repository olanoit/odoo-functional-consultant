# Cuaderno de ejemplos — Fase 6: Servicios, Proyectos y Soporte

Casos prácticos para [`../../fases/fase-06-servicios-proyectos.md`](../../fases/fase-06-servicios-proyectos.md).

> **Nota v19 importante:** el modelo `hr.contract` fue reemplazado por **`hr.version`** (versiones
> del empleado). Los datos laborales —salario, horario, puesto, fechas de contrato— viven ahora en la
> versión, no en un contrato aparte. Aquí solo se usan empleados con `hourly_cost`; el detalle
> completo está en la Fase 7.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-empleados-servicios.csv` | 6 empleados **con costo por hora** (sin esto, la rentabilidad no existe) |
| `datos/02-productos-servicio.csv` | 5 servicios con las tres políticas de facturación |
| `datos/03-proyectos.csv` | 4 proyectos: 2 de cliente (portal), 1 de soporte, 1 interno |
| `datos/04-tareas.csv` | 12 tareas con horas asignadas y fechas límite |
| `guias/K1` | **Laboratorio de rentabilidad**: calcula el margen antes que Odoo |
| `guias/K2` | Mesa de ayuda, SLA, servicio de campo y planeación |
| `soluciones/` | Rentabilidad resuelta con el análisis de negocio |

## Antes de empezar

Apps: **Proyecto**, **Hojas de horas**, **Ventas** (y en Enterprise: **Servicio de asistencia**,
**Servicio de campo**, **Planeación**).
Activa en Ventas: **Facturación por hojas de horas** e **Hitos de facturación**.

---

## Ejemplo 1 — Catálogo de servicios y creación automática de proyectos
*(Bloque 6.2 · 60 min)*

Importa `01-empleados-servicios.csv` → `02-productos-servicio.csv` → `03-proyectos.csv` → `04-tareas.csv`.

Fíjate en la columna **`service_tracking`** de los productos: define qué crea Odoo al confirmar la venta.

| Valor | Qué crea |
|---|---|
| `no` | Nada |
| `task_global_project` | Una tarea en un proyecto existente |
| `task_in_project` | Un proyecto nuevo **y** una tarea dentro |
| `project_only` | Solo el proyecto |

**Ejercicio:** vende cada uno de los 5 servicios a un cliente distinto y comprueba qué se creó en
cada caso. Es la diferencia entre "vender servicios" y "vender servicios que se ejecutan solos".

## Ejemplo 2 — Rentabilidad
*(Bloque 6.2 · 90 min)* ← **el ejercicio central**

[`guias/K1-rentabilidad-de-servicios.md`](guias/K1-rentabilidad-de-servicios.md): registra las horas
del proyecto Sol de Oro (108 h entre 4 personas con costos distintos) y de la bolsa de soporte, y
calcula el margen **antes** de abrir el reporte.

Hallazgo que verás: las 12 horas del gerente cuestan más que las 18 de la jefa de ventas.
Ese dato cambia cómo se arman los equipos de proyecto.

## Ejemplo 3 — Las tres políticas en acción
*(Bloque 6.2 · 60 min)*

1. **Precio fijo:** vende la implantación (S/ 4 800), registra 40 horas y factura. ¿Cambió el importe?
2. **Por horas:** vende asesoría, registra 12 horas y factura. ¿Qué se factura exactamente?
3. **Por hitos:** vende el desarrollo de marca propia (S/ 18 000) con 4 hitos, marca 2 como
   alcanzados y factura el avance.
4. **Reventa de gastos:** registra un gasto de viaje reembolsable y factúraselo al cliente.

## Ejemplo 4 — Gestión del proyecto
*(Bloque 6.1 · 45 min)*

Con los 4 proyectos y 12 tareas cargadas:
1. Define etapas propias y criterios de avance (como el embudo de la Fase 2).
2. Crea dependencias entre tareas y mira el **gantt**: ¿qué pasa si la primera se retrasa una semana?
3. Reparte las tareas entre personas y revisa la **planificación de carga**: ¿alguien está sobrecargado?
4. Abre el **portal del cliente** de un proyecto: define qué ve y qué no debe ver.

## Ejemplo 5 — Soporte, SLA y campo
*(Bloques 6.3 a 6.5 · 90 min · Enterprise)*

[`guias/K2-helpdesk-sla-y-campo.md`](guias/K2-helpdesk-sla-y-campo.md): equipo de soporte con canales
de entrada, tres políticas SLA, tickets facturables contra bolsa de horas, base de conocimiento,
escalamiento a visita de campo con firma del cliente y planificación de turnos.

---

## Cierre: entregables de la Fase 6

- [ ] Los 5 servicios vendidos, cada uno creando lo que corresponde.
- [ ] Rentabilidad calculada a mano y contrastada con Odoo.
- [ ] Bolsa de horas vendida, consumida, excedida y renovada.
- [ ] Equipo de soporte con 2 SLA y reporte de cumplimiento.
- [ ] Un ticket escalado a campo, ejecutado, firmado y facturado.
- [ ] **Entregable C:** *"Modelo de negocio de servicios"*: catálogo, política de facturación por
      tipo, flujo de soporte e indicadores de rentabilidad.
- [ ] Respaldo `LAB_fase06_AAAAMMDD.zip`.
