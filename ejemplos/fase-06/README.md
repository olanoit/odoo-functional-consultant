# Cuaderno de ejemplos — Fase 6: Servicios, Proyectos y Soporte

Casos prácticos para [`../../fases/fase-06-servicios-proyectos.md`](../../fases/fase-06-servicios-proyectos.md).

> **Nota importante (desde v19, vigente en v20):** el modelo `hr.contract` fue reemplazado por
> **`hr.version`** (versiones del empleado). Los datos laborales —salario, horario, puesto, fechas de contrato— viven ahora en la
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
**Planeación** y **Servicio de campo**, que en v20 es una extensión de Planeación).
La facturación por hojas de horas (`sale_timesheet`) se instala sola al tener Ventas + Hojas de horas;
no hay un ajuste global en Ventas. Los **hitos** tampoco: se activan **en cada proyecto** con la casilla
*Hitos* (`allow_milestones`; en es_419 se traduce «Objetivos»), y eso habilita la política *Basada en hitos*.

---

## Ejemplo 1 — Catálogo de servicios y creación automática de proyectos
*(Bloque 6.2 · 60 min)*

Importa `01-empleados-servicios.csv` → `02-productos-servicio.csv` → `03-proyectos.csv` → `04-tareas.csv`.

Fíjate en dos columnas de los productos. La primera, **`service_tracking`**, define qué crea Odoo al
confirmar la venta:

| Valor | Qué crea |
|---|---|
| `no` | Nada |
| `task_global_project` | Una tarea en un proyecto existente |
| `task_in_project` | Un proyecto nuevo **y** una tarea dentro |
| `project_only` | Solo el proyecto |

La segunda, **`service_type`**, combinada con `invoice_policy`, fija la **política de facturación del
servicio** (`service_policy`, campo calculado que es lo que muestra el formulario):

| `invoice_policy` + `service_type` | Política que ve el usuario | Productos del CSV |
|---|---|---|
| `order` + `manual` / `timesheet` | *Precio fijo o de prepago* | Implantación, bolsa de horas |
| `delivery` + `timesheet` | *Según el registro de horas* | Asesoría por hora |
| `delivery` + `milestones` | *Basada en hitos* (es_419: «objetivos») | Marca propia |
| `delivery` + `manual` | *Basado en la entrega (manual)* | Capacitación |

> **Cuidado al importar:** si solo pones `invoice_policy = delivery`, `service_type` queda en `manual`
> y el producto sale como *Basado en la entrega (manual)*, no como facturado por horas ni por hitos.
> La bolsa de horas se vende **por hora** (S/ 110 × 20 h = S/ 2 200), con unidad *Horas*, para que
> Odoo compare lo registrado contra lo vendido. Y como crea la tarea en un proyecto existente
> (`task_global_project`), después de importar `03-proyectos.csv` asígnale en el producto el proyecto
> *Soporte a distribuidores 2026*.

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



---

## Para ampliar

### Cybrosys — libro de Odoo 19 y artículos

Enlaces verificados uno a uno. Todos están **en inglés**.

**Capítulos del [libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)**: [Project](https://www.cybrosys.com/odoo/odoo-books/v19/project/) · [Timesheet](https://www.cybrosys.com/odoo/odoo-books/v19/timesheet/) · [Helpdesk](https://www.cybrosys.com/odoo/odoo-books/v19/helpdesk/)

| Artículo | Para qué en esta fase | Fecha |
|---|---|---|
| [How to Use Timesheet-Based Billing for Projects in Odoo 19](https://www.cybrosys.com/blog/how-to-use-timesheet-based-billing-for-projects-in-odoo-19) | Facturación por horas — las tres políticas del Ejemplo 3 | *may 2026* |

### Odoo en Español — YouTube

[**Buscar «proyectos hoja de horas» en el canal**](https://www.youtube.com/@OdooSpanish/search?query=proyectos+hoja+de+horas) — vídeos en español sobre proyectos y hojas de horas.

> El canal no publica un índice enlazable por tema, así que el enlace abre la **búsqueda dentro del
> canal**: siempre devuelve lo que haya publicado sobre el tema, aunque renombre o reordene sus
> vídeos. El canal completo está en <https://www.youtube.com/@OdooSpanish>.

> **Úsalos para el concepto, no para la configuración.** Todo lo marcado con ⚠️ es de una versión
> anterior, y aun en los artículos de v19 conviene contrastar los nombres de campo: verifica contra
> la documentación 20.0, contra [la tabla de cambios de v20](../fase-12/README.md#los-cambios-de-v20-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
