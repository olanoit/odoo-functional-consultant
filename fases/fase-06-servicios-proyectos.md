# Fase 6 — Servicios: Proyectos, Hojas de horas, Soporte y Campo

**Horas estimadas:** 25–30 h · **Prerrequisitos:** Fases 1, 2 y 4 · **Base:** `LAB`

> **Objetivo:** implementar el modelo de negocio de servicios: vender horas o proyectos,
> registrarlos, facturarlos y medir su rentabilidad. Es el escenario más común en empresas
> de consultoría, agencias, estudios y soporte técnico — probablemente el de tu propio empleador.

---

## 📓 Cuaderno de ejemplos de esta fase

Datos y casos en **[`../ejemplos/fase-06/`](../ejemplos/fase-06/README.md)**: 6 empleados con costo
por hora, 5 servicios con las tres políticas de facturación, 4 proyectos y 12 tareas,
**laboratorio de rentabilidad** con el margen calculado a mano, y guía de mesa de ayuda, SLA,
servicio de campo y planeación.

## 1. Resultados de aprendizaje

1. Configurar proyectos con etapas, subtareas, dependencias y planificación.
2. Vender servicios en tres modalidades: precio fijo, por hora (tiempo y materiales) y por hitos.
3. Registrar horas y facturarlas automáticamente, controlando lo vendido vs. lo entregado.
4. Medir rentabilidad de proyecto usando contabilidad analítica (Fase 4).
5. Configurar una mesa de ayuda con SLA, equipos, canales de entrada y base de conocimiento.
6. Gestionar servicio de campo: intervención, materiales usados, firma en sitio y facturación.
7. Planificar turnos y asignación de recursos.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 6.1 | Proyecto | [services/project.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/project.html) · [project/tasks.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/project/tasks.html) |
| 6.2 | Hojas de horas | [services/timesheets.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/timesheets.html) |
| 6.3 | Servicio de asistencia (Helpdesk) | [services/helpdesk.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/helpdesk.html) · [helpdesk/overview.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/helpdesk/overview.html) |
| 6.4 | Servicio de campo | [services/field_service.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/field_service.html) |
| 6.5 | Planeación (turnos y recursos) | [services/planning.html](https://www.odoo.com/documentation/saas-19.4/es/applications/services/planning.html) |
| 6.6 | Facturación de servicios (repaso desde Ventas) | [sales/invoicing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/sales/invoicing.html) |

## 3. Ruta de estudio paso a paso

### Bloque 6.1 — Proyecto (6 h)
1. Crear proyectos con etapas propias, subtareas, dependencias y fechas planificadas.
2. Plantillas de proyecto y de tareas recurrentes.
3. Vistas: kanban, lista, gantt, calendario, mapa; **planificación de carga** por persona.
4. Colaboración: seguidores, actividades, adjuntos, portal del cliente (¿qué ve el cliente?).
5. Etiquetas, prioridades, campos de proyecto y control de acceso (proyecto privado, portal, público).

### Bloque 6.2 — Servicios facturables (7 h)
1. Configurar productos de servicio con las tres políticas:
   - **Precio fijo** (factura al pedido),
   - **Basado en hojas de horas** (factura lo registrado),
   - **Por hitos** (factura por avance porcentual).
2. Vincular producto de servicio → proyecto/tarea creado automáticamente al confirmar la venta.
3. Registrar horas contra la tarea (desde escritorio y desde móvil/temporizador) y **facturarlas**.
4. Control de sobreconsumo: horas vendidas vs. registradas, alertas y qué hacer al excederse.
5. Reventa de gastos: gasto de viaje reembolsable facturado al cliente.
6. **Rentabilidad del proyecto**: ingresos, costo de horas (costo/hora del empleado), gastos, margen.

### Bloque 6.3 — Mesa de ayuda (5 h)
1. Equipos de asistencia con etapas, asignación (manual, equilibrada, aleatoria) y visibilidad.
2. Canales de entrada: correo (alias), formulario web, chat en vivo, teléfono.
3. **Políticas SLA**: definición, prioridad, tiempo objetivo, escalamiento e informe de cumplimiento.
4. Tickets facturables: convertir ticket → hoja de horas → factura; y venta de bonos de horas
   (contratos de soporte prepagado).
5. Base de conocimiento asociada y respuestas predefinidas.
6. Encuesta de satisfacción y reporte de desempeño del equipo.

### Bloque 6.4 — Servicio de campo (4 h)
1. Tareas de campo: planificación, asignación a técnicos, ruta y calendario.
2. En sitio: registrar tiempo, consumir productos del inventario del vehículo, hoja de trabajo, firma del cliente.
3. Facturar la intervención (tiempo + materiales) y cerrar.
4. Relación con Mantenimiento (Fase 5) y con Helpdesk (escalamiento de ticket a visita).

### Bloque 6.5 — Planeación de recursos (3 h)
1. Crear plantillas de turno, publicar horarios, asignaciones abiertas que los empleados toman.
2. Planificación por rol/habilidad y control de disponibilidad (integración con Ausencias, Fase 7).
3. Comparar horas planificadas vs. registradas.

## 4. Laboratorio integrador

**Encargo:** *"Vendemos implementaciones a precio fijo y soporte por bolsa de horas. Necesito saber
si gano o pierdo en cada proyecto y responder los tickets con un SLA de 4 horas."*

En `LAB`:
1. 3 productos de servicio (fijo, por horas, por hitos) con creación automática de proyecto/tarea.
2. Un proyecto vendido a precio fijo con 40 h presupuestadas, 6 tareas y horas registradas por 2 empleados
   con costo/hora distinto → reporte de rentabilidad con margen real.
3. Una bolsa de 20 horas de soporte vendida, consumida por tickets y renovada al agotarse.
4. Equipo de mesa de ayuda con 2 SLA (crítico 4 h, normal 2 días) y reporte de cumplimiento.
5. Un ticket escalado a visita de campo, con materiales consumidos y firma, facturado.
6. Planificación semanal de 3 técnicos publicada.

## 5. Preguntas de comprensión (prueba B)

1. ¿Qué políticas de facturación de servicio existen y cuándo se usa cada una?
2. ¿Cómo se crea automáticamente un proyecto al confirmar una venta y qué se configura para ello?
3. ¿Cómo se calcula el costo de una hora registrada y de dónde sale ese dato?
4. Un proyecto a precio fijo lleva 60 h consumidas de 40 vendidas. ¿Qué muestra Odoo y qué recomiendas al cliente?
5. ¿Qué es una política SLA y qué ocurre al vencerse?
6. Diferencia entre tarea de proyecto, ticket de helpdesk y tarea de campo. ¿Cuándo usar cada una?
7. ¿Cómo vendes y controlas una bolsa de horas prepagada?
8. ¿Qué ve un cliente en el portal de un proyecto y cómo se limita?
9. ¿Cómo se factura un gasto reembolsable al cliente?
10. ¿Cómo mides la rentabilidad real de un proyecto y qué relación tiene con la contabilidad analítica?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (75 min):** configurar producto de servicio facturado por hojas de horas con
      creación automática de proyecto, registrar horas de 2 empleados, facturar y mostrar rentabilidad.
- [ ] **B.** ≥ 8/10 en preguntas.
- [ ] **C. Entregable:** *"Modelo de negocio de servicios"*: catálogo de servicios, política de
      facturación por tipo, flujo de soporte con SLA e indicadores de rentabilidad.
- [ ] Respaldo `LAB_fase06`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Vender "por horas" sin configurar costo/hora del empleado | La rentabilidad muestra margen del 100 % y no sirve. |
| Usar tareas de proyecto como tickets | Sin SLA ni canales de entrada, el soporte se vuelve ingobernable. |
| SLA irreales copiados del folleto comercial | El reporte se vuelve rojo permanente y el equipo lo ignora. |
| No definir qué ve el cliente en el portal | Fuga de información interna (costos, notas internas). |
| Olvidar que las horas alimentan la analítica | Se pierde el puente con la contabilidad de la Fase 4. |
