# L1 — Alcance real de RR. HH. y nómina en Perú

> **Entregable C de la Fase 7** y una de las piezas más valiosas de tu kit: la respuesta honesta a
> *"¿Odoo hace mi planilla?"*. Contestar bien esta pregunta evita el tipo de proyecto que termina en
> juicio; contestarla mal es la causa número uno de implantaciones de RR. HH. fallidas en LATAM.

---

## 1. Lo que exige la legislación peruana

| Obligación | Qué es | Periodicidad |
|---|---|---|
| **T-Registro** | Registro de trabajadores ante SUNAT | Al alta/baja |
| **PLAME** | Planilla mensual electrónica | Mensual |
| **Boletas de pago electrónicas** | Comprobante de remuneración | Mensual |
| **CTS** | Compensación por tiempo de servicios | Mayo y noviembre |
| **Gratificaciones** | Julio y diciembre, más bonificación extraordinaria | Semestral |
| **Vacaciones** | 30 días por año, con reglas de récord y adelantos | Anual |
| **Quinta categoría** | Retención de renta con **proyección anual** y regularización | Mensual |
| **Aportes** | ESSALUD, SCTR, EPS | Mensual |
| **Descuentos** | ONP o AFP (con comisión sobre flujo o sobre saldo) | Mensual |
| **Utilidades** | Reparto según giro y planilla | Anual |
| **Liquidación de beneficios** | Al cese del trabajador | Puntual |

## 2. Qué cubre Odoo estándar

| Área | Estado en Odoo estándar | Comentario |
|---|---|---|
| Expediente del empleado | ✅ Completo | Datos, documentos, organigrama |
| **Versiones del empleado** (`hr.version`) | ✅ | Reemplaza a los contratos: salario, horario, puesto, fechas |
| Horarios de trabajo | ✅ | Turnos, festivos, medio tiempo |
| Asistencias | ✅ | Kiosco, PIN, móvil, horas extra |
| Ausencias | ✅ | Tipos, asignaciones, acumulación, aprobaciones |
| Reclutamiento | ✅ | Embudo, portal de empleo, firma de contrato |
| Evaluaciones | ✅ (Enterprise) | Plantillas, objetivos, periodicidad |
| Gastos de empleados | ✅ | Aprobación y reembolso |
| **Motor de nómina** | ⚠️ Existe (Enterprise) | Estructuras y reglas salariales genéricas |
| **Localización peruana de nómina** | ❌ **No incluida en el estándar** | No hay estructura peruana oficial |
| PLAME / T-Registro / boletas electrónicas | ❌ | Requiere desarrollo o sistema externo |
| CTS, gratificaciones, utilidades | ❌ | Requieren reglas salariales a medida |
| Quinta categoría con proyección | ❌ | Cálculo específico peruano |

> **Verifica siempre el estado actual** en el índice de
> [localizaciones fiscales](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations.html)
> y en [apps.odoo.com](https://apps.odoo.com/apps/modules) antes de responderle a un cliente: la
> disponibilidad de localizaciones cambia entre versiones.

## 3. Las cuatro opciones que puedes ofrecer

| Opción | Cuándo tiene sentido | Riesgo | Esfuerzo estimado |
|---|---|---|---|
| **A. RR. HH. sí, nómina fuera** | La empresa ya tiene un software de planilla que funciona | Doble registro de novedades | 40–80 h |
| **B. Módulo de terceros** (Apps Store / partner peruano) | Existe uno mantenido para la versión objetivo | Depende del mantenedor; puede frenar actualizaciones | 60–120 h + licencia |
| **C. Desarrollo a medida** sobre el motor de nómina | Empresa grande, con presupuesto y equipo técnico | Alto costo de mantenimiento por versión y por cambio normativo | 300–600 h |
| **D. No hacer nómina** | La mayoría de los casos | Ninguno; se gana credibilidad | 0 |

**La recomendación por defecto es la A.** Odoo aporta muchísimo valor en expediente, asistencias,
ausencias, reclutamiento y gastos; la planilla peruana es un problema normativo que cambia cada año
y que no conviene asumir sin un compromiso claro de mantenimiento.

## 4. Cómo se dice esto en una reunión

> *"Odoo va a manejar muy bien todo el ciclo del trabajador: su expediente, su horario, sus
> asistencias, sus vacaciones, el reclutamiento y sus gastos. La planilla peruana —PLAME, CTS,
> gratificaciones, quinta categoría— no viene resuelta de fábrica: eso o lo dejamos en el sistema
> que ya usan, o lo evaluamos como un proyecto aparte con su propio costo y su propio mantenimiento
> anual, porque la norma cambia todos los años. Mi recomendación para esta primera etapa es
> integrarnos con lo que ya tienen y no meter riesgo en el arranque."*

Esa respuesta, dicha **en la preventa** y no en la UAT, es la diferencia entre un cliente que confía
y un proyecto que se descarrila.

## 5. Si aun así el cliente insiste (opción C)

Preguntas obligatorias antes de estimar:

1. ¿Cuántos trabajadores y de cuántos regímenes (general, agrario, MYPE, construcción civil)?
2. ¿Cuántos conceptos remunerativos y descuentos distintos usan hoy? Pide la boleta real.
3. ¿Quién valida el cálculo? ¿Hay un contador de planillas que firme la conformidad?
4. ¿Cómo se generan hoy PLAME y T-Registro? ¿Puede seguir haciéndose fuera?
5. ¿Quién mantiene el módulo cuando cambie la UIT, la RMV o el tope de AFP en enero?
6. ¿Qué pasa si un cálculo sale mal? (La respuesta correcta es: multas y reclamos laborales.)

Si el cliente no puede responder 3 y 5, **la respuesta es no**.

## 6. Plantilla del entregable

| Sección | Contenido |
|---|---|
| 1. Alcance cubierto por el estándar | Lista de módulos y funciones, con lo que resuelve cada uno |
| 2. Brechas identificadas | Cada obligación legal no cubierta, con su impacto |
| 3. Opciones evaluadas | Las cuatro opciones con costo, riesgo y recomendación |
| 4. Recomendación argumentada | Una opción, con las razones y los supuestos |
| 5. Estimación por bloque | Horas de configuración, migración, pruebas y capacitación |
| 6. Riesgos y responsabilidades | Quién mantiene qué; qué pasa ante un cambio normativo |
| 7. Decisión del cliente | Firmada y fechada |
