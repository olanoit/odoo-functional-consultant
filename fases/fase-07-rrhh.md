# Fase 7 — Recursos Humanos (ciclo Hire-to-Retire)

**Horas estimadas:** 25–30 h · **Prerrequisitos:** Fases 1 y 4 · **Base:** `LAB`

> **Objetivo:** cubrir el ciclo de vida del empleado en Odoo y —clave para un consultor en
> Latinoamérica— entender **hasta dónde llega la nómina estándar** y dónde empieza la localización
> o el desarrollo. Es una de las áreas donde más se sobrevende y peor se estima.

---

## 1. Resultados de aprendizaje

1. Configurar el expediente del empleado, la estructura organizacional y los contratos.
2. Implementar asistencias (kiosco, PIN, geolocalización) y su relación con horarios de trabajo.
3. Configurar tipos de ausencia, asignaciones, aprobaciones y calendario del equipo.
4. Ejecutar un proceso de reclutamiento completo, desde la publicación hasta la contratación.
5. Configurar evaluaciones de desempeño y planes de carrera.
6. Explicar el motor de nómina de Odoo (estructuras, reglas salariales) y evaluar su viabilidad en Perú.
7. Gestionar flota, comedor y referidos como beneficios (módulos complementarios).

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 7.1 | Empleados | [hr/employees.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/employees.html) · [employees/new_employee.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/employees/new_employee.html) |
| 7.2 | Asistencias | [hr/attendances.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/attendances.html) |
| 7.3 | Tiempo personal / Ausencias | [hr/time_off.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/time_off.html) |
| 7.4 | Reclutamiento | [hr/recruitment.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/recruitment.html) · [recruitment/new_job.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/recruitment/new_job.html) |
| 7.5 | Evaluaciones | [hr/appraisals.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/appraisals.html) |
| 7.6 | Nómina | [hr/payroll.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/payroll.html) · [payroll/contracts.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/payroll/contracts.html) |
| 7.7 | Flota | [hr/fleet.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/fleet.html) |
| 7.8 | Recepción (Frontdesk) | [hr/frontdesk.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/frontdesk.html) |
| 7.9 | Almuerzo | [hr/lunch.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/lunch.html) |
| 7.10 | Referencias de empleados | [hr/referrals.html](https://www.odoo.com/documentation/saas-19.4/es/applications/hr/referrals.html) |
| 7.11 | Gastos de empleados (repaso Fase 4) | [finance/expenses.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/expenses.html) |

## 3. Ruta de estudio paso a paso

### Bloque 7.1 — Empleados y organización (5 h)
1. Crear los 18 empleados de ANDINA GOURMET con departamentos, puestos, jerarquía y responsables.
2. Expediente: datos personales, documentos (identidad, certificados), información de RR. HH.
   (horario de trabajo, zona horaria, costo/hora ← alimenta la Fase 6).
3. **Horarios de trabajo**: crear turnos (administrativo 8×5, planta 6×6, medio tiempo) y días festivos globales.
4. Relación empleado ↔ usuario de Odoo (y qué pasa si no la hay).
5. Organigrama y directorio; privacidad de datos personales y control de acceso a RR. HH.

### Bloque 7.2 — Asistencias (3 h)
1. Modos de registro: desde el perfil, desde **kiosco** (tablet con PIN o código de barras), desde móvil.
2. Reglas de horas extra, tolerancias y aprobación de asistencias.
3. Reporte de asistencia y su comparación con las hojas de horas (Fase 6): **no son lo mismo**.

### Bloque 7.3 — Ausencias (4 h)
1. **Tipos de ausencia**: vacaciones, enfermedad, permiso sin goce, compensatorio. Configurar unidad
   (días/horas), aprobación (jefe/RR. HH./doble), documento de respaldo, efecto en nómina.
2. **Asignaciones**: manual, por acumulación (*accrual*) con reglas de devengo, y sus fechas de corte.
3. Flujo de solicitud → aprobación → efecto en calendario y en planificación (Fase 6).
4. Reportes: saldo por empleado, calendario del equipo, ausentismo.

> **Romper:** solicitar vacaciones sin saldo y con solapamiento de turno planificado. Documentar qué avisa Odoo.

### Bloque 7.4 — Reclutamiento (4 h)
1. Publicar un puesto (vinculado al sitio web, Fase 8), definir el embudo de selección y los entrevistadores.
2. Entrada de candidatos: formulario web, correo con alias, referidos.
3. Flujo: candidato → entrevistas (con encuestas de evaluación) → propuesta de contrato →
   **enlace de contratación** firmado en línea (Firma) → creación del empleado.
4. Indicadores: tiempo de contratación, fuente de candidatos, tasa de conversión por etapa.

### Bloque 7.5 — Evaluaciones y desarrollo (3 h)
1. Plantillas de evaluación, periodicidad, autoevaluación y evaluación del jefe.
2. Objetivos, plan de carrera y competencias.
3. Reporte de evaluaciones y su uso en decisiones salariales.

### Bloque 7.6 — Nómina: alcance real (5 h) ← *criterio de consultor*
1. Entender la arquitectura: **estructura salarial** → **reglas salariales** (con condiciones y
   fórmulas Python) → **categorías** → **recibo de nómina** → asiento contable.
2. Crear una estructura simple con: sueldo básico, asignación familiar, descuento de pensión,
   renta de quinta categoría (simplificada), aportes del empleador. Generar recibos de un mes.
3. Configurar contratos: tipo, salario, horario, fechas, estructura aplicable.
4. Lotes de nómina, generación masiva y contabilización.
5. **Evaluación crítica:** listar qué exige la legislación peruana (PLAME, T-Registro, CTS, gratificaciones,
   utilidades, quinta categoría con proyección anual, boletas electrónicas) y decidir por cada punto:
   ¿estándar, localización, módulo de terceros o sistema externo?
6. Escribir la recomendación que darías a un cliente peruano sobre nómina en Odoo — con argumentos.

> **Este bloque no busca que implementes nómina peruana**, sino que sepas **estimar y responder**
> cuando el cliente pregunte "¿Odoo hace mi planilla?". La respuesta honesta vale más que la venta.

### Bloque 7.7 — Beneficios y complementos (2 h)
Recorrer y saber demostrar: Flota (vehículos, contratos, costos), Almuerzo, Recepción, Referencias.
No profundizar: son módulos de refuerzo comercial.

## 4. Laboratorio integrador

**Encargo:** *"Queremos controlar asistencia y vacaciones de 18 personas, y dejar de reclutar por WhatsApp."*

En `LAB`:
1. 18 empleados con 3 horarios de trabajo distintos y organigrama completo.
2. Kiosco de asistencia con PIN funcionando y reporte de horas extra de una semana.
3. 4 tipos de ausencia, uno con acumulación mensual y doble aprobación; saldos cargados y 10 solicitudes procesadas.
4. 1 puesto publicado con embudo de 5 etapas y 8 candidatos, uno llevado hasta empleado creado.
5. Ciclo de evaluación configurado para el semestre.
6. 1 estructura salarial simple con 5 reglas y un lote de nómina de 5 empleados contabilizado.
7. Documento de recomendación sobre nómina en Perú (§7.6.6).

## 5. Preguntas de comprensión (prueba B)

1. Diferencia entre **asistencia** y **hoja de horas**. ¿Puede una empresa usar ambas?
2. ¿Cómo funciona una asignación de ausencias por acumulación y cuándo se devenga?
3. ¿Qué relación hay entre empleado, usuario y contacto en el modelo de datos?
4. ¿Dónde se define el costo por hora de un empleado y qué módulos lo consumen?
5. ¿Qué pasa con las tareas planificadas de alguien que pide vacaciones aprobadas?
6. Describe el camino de un candidato hasta convertirse en empleado.
7. ¿Cómo se compone una regla salarial y qué determina si aplica?
8. ¿Qué asiento contable genera un lote de nómina?
9. Un cliente peruano pide PLAME y CTS. ¿Qué le respondes y cómo estimas el trabajo?
10. ¿Cómo proteges la privacidad de los datos personales de empleados dentro de Odoo?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (75 min):** crear 5 empleados con 2 horarios, un tipo de ausencia con acumulación
      y doble aprobación, procesar 3 solicitudes y sacar el reporte de saldos.
- [ ] **B.** ≥ 8/10 en preguntas.
- [ ] **C. Entregable:** *"Alcance de RR. HH. y nómina para un cliente peruano"*: qué cubre el estándar,
      qué requiere localización/terceros, qué queda fuera, y una estimación en horas por bloque.
- [ ] Respaldo `LAB_fase07`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Vender "Odoo hace tu planilla" sin analizar la localización | Es la causa #1 de proyectos de RR. HH. fallidos en LATAM. |
| Confundir asistencia con hojas de horas | Son dos modelos distintos con dos propósitos distintos. |
| No configurar horarios de trabajo antes que ausencias | Todos los cálculos de días/horas salen mal. |
| Olvidar el costo/hora del empleado | Rompe la rentabilidad de proyectos (Fase 6) y el costeo de producción (Fase 5). |
| Dejar los datos de RR. HH. visibles para todos | Problema legal y de confianza; se configura desde el día 1. |
