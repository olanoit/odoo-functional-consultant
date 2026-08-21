# Fase 12 — Proyecto integrador (capstone) y certificación oficial

**Horas estimadas:** 40–60 h · **Prerrequisitos:** Fases 1 a 11 completas y validadas · **Base:** `CAPSTONE` (nueva, desde cero)

> **Objetivo:** demostrar —con evidencia— que puedes implementar Odoo de punta a punta, y obtener
> la credencial que lo respalda frente al mercado.

---

## 📓 Cuaderno de ejemplos de esta fase

Material en **[`../ejemplos/fase-12/`](../ejemplos/fase-12/README.md)**: guion día a día de las
4 semanas del capstone con sus gates, y un **simulacro de 60 preguntas** con clave, explicaciones de
las más falladas y mapa de repaso por fase. Incluye el resumen de **todos los cambios de v19**
documentados a lo largo del plan, para llevarlos frescos al examen.

## Parte A — Proyecto integrador

### A.1 El encargo

Implementas **ANDINA GOURMET S.A.C.** completa, en una base nueva llamada `CAPSTONE`,
**sin copiar `LAB`**: se construye desde cero, contra reloj, como si fuera un cliente real.

Alcance obligatorio:

| Área | Debe quedar operativo |
|---|---|
| Base | Compañía peruana, usuarios por rol con permisos probados, correo configurado |
| Comercial | CRM con embudo, listas de precios (mayorista, USD, promoción), portal de cliente |
| Ventas | Ciclo completo con entregas parciales y facturación por entregado |
| PdV | Tienda con sesión, arqueo y contabilización |
| Compras | Ciclo P2P con control a tres bandas y acuerdos con 2 proveedores |
| Inventario | 2 almacenes, entrega en 2 pasos, lotes con vencimiento, FEFO, reglas de reordenamiento |
| Producción | LdM de 2 niveles, 1 centro de trabajo con costo, 1 subcontratación, 1 control de calidad |
| Contabilidad | Localización PE, impuestos, posiciones fiscales, conciliación con modelos, analítica de 2 dimensiones, activos |
| Facturación electrónica | Factura, boleta y nota de crédito aceptadas en modo de prueba |
| Servicios | 1 servicio facturable por horas con rentabilidad de proyecto |
| RR. HH. | Empleados con horarios, asistencias, ausencias con acumulación |
| Digital | Sitio + tienda en línea con 10 productos y 1 compra completa trazada |
| Personalización | 1 app propia en Studio, 2 automatizaciones, 1 regla de aprobación, factura PDF con marca |
| Datos | Migración de 500+ registros por importación, con validación documentada |
| Analítica | Tablero gerencial en hoja de cálculo con 6 indicadores en vivo |

### A.2 Entregables del proyecto

1. **Base `CAPSTONE`** funcionando + respaldo.
2. **Documento de proyecto** (20–35 páginas) con: alcance, AS-IS/TO-BE, matriz GAP-FIT, diseño de
   configuración por área, plan de migración, plan de pruebas y plan de capacitación.
3. **Casos de prueba UAT ejecutados** (mínimo 30) con evidencia y gestión de defectos.
4. **Guías rápidas** por rol (mínimo 4 roles).
5. **Demo grabada de 30 minutos** cubriendo el flujo integral: venta → producción → entrega →
   factura electrónica → cobro → conciliación → reporte de rentabilidad.
6. **Estimación y cronograma** del proyecto como si fuera a venderse.
7. **Documento de lecciones aprendidas** y lista de lo que Odoo **no** resuelve en este caso.

### A.3 Cronograma sugerido (4 semanas a tiempo parcial)

| Semana | Trabajo |
|---|---|
| 1 | Alcance + AS-IS/TO-BE + GAP-FIT + base, compañía, usuarios, datos maestros migrados |
| 2 | Comercial + compras + inventario + producción operando de punta a punta |
| 3 | Contabilidad + localización PE + facturación electrónica + servicios + RR. HH. |
| 4 | Web/eCommerce + Studio + tablero + UAT + guías + demo grabada + documento final |

### A.4 Rúbrica de evaluación (autoevaluación honesta, 100 puntos)

| Criterio | Puntos | Qué se evalúa |
|---|---|---|
| Flujo integral funcionando | 25 | El caso corre de punta a punta sin trabas manuales |
| Corrección contable | 20 | Cuadre inventario↔contabilidad, impuestos correctos, cierre posible |
| Trazabilidad y control | 10 | Lotes, permisos, aprobaciones, auditoría |
| Calidad de la documentación | 15 | Un tercero podría continuar el proyecto con ella |
| Migración y calidad de datos | 10 | Cargada por importación, validada con sumas de control |
| Personalización con criterio | 10 | Se personalizó solo lo justificado y está documentado |
| Demo | 10 | Clara, orientada al negocio, sin improvisar |

**Aprobado ≥ 80.** Por debajo: identificar el área débil, volver a esa fase y repetir el bloque.

---

## Parte B — Certificación oficial de Odoo

### B.1 Qué es

Odoo ofrece una **certificación funcional** oficial, en línea, que valida el conocimiento del producto
a nivel transversal. Es el aval reconocido por partners y clientes.

- Certificación funcional de Odoo 19: <https://www.odoo.com/slides/odoo-19-functional-certification-502>
- Listado de certificaciones: <https://www.odoo.com/slides?slide_category=certification>
- **Examen de muestra (gratuito, hazlo antes)**: <https://www.odoo.com/slides/odoo-functional-certification-sample-test-50>

### B.2 Formato del examen (verifícalo siempre en la página oficial antes de inscribirte)

- ~120 preguntas · 1 h 30 min · **mínimo 70 % para aprobar**.
- Puntuación con penalización: respuesta correcta +1, **incorrecta −½**, sin responder 0.
  → **Estrategia: no adivines a ciegas**; responde solo si puedes descartar al menos la mitad de las opciones.
- Cubre transversalmente: Sitio web, eCommerce, Encuestas, Marketing, CRM, Ventas, Compras, Proyecto,
  Hojas de horas, Contabilidad, Inventario, MRP, RR. HH., Hojas de cálculo, Conocimiento, PdV y Studio.
- Es nominativa y no transferible; una vez enviada, no se puede volver atrás.

### B.3 Plan de preparación (2–3 semanas)

| Día | Actividad |
|---|---|
| 1–3 | Repasar todos los cuestionarios B de las 12 fases en una sola pasada. Marcar los fallos. |
| 4–6 | Rehacer los laboratorios de las áreas falladas (solo esas). |
| 7 | **Examen de muestra oficial.** Anotar cada error y su tema. |
| 8–12 | Recorrer los cursos oficiales de las áreas débiles en <https://www.odoo.com/slides/all>. |
| 13–15 | Repaso de configuración: cada app, sus 5 opciones de configuración más importantes. |
| 16–18 | Simulacros cronometrados: responder 120 preguntas propias en 90 min (usa tus cuestionarios). |
| 19–20 | Repaso ligero, descanso y examen. |

### B.4 Temas que más se fallan (refuérzalos sí o sí)

1. Diferencias sutiles de configuración entre apps (políticas de facturación, métodos de reserva).
2. Inventario: rutas multi-etapa, reglas push/pull, estrategias de remoción.
3. Contabilidad: tipos de cuenta, posiciones fiscales, conciliación, analítica.
4. Manufactura: kits vs. LdM, subcontratación, costos.
5. Studio: qué se puede y qué no se puede hacer sin código.
6. Website/eCommerce: precios, variantes publicadas, checkout.
7. Opciones que **solo aparecen tras activar otra opción** (dependencias de configuración).

### B.5 Después de la certificación

- Publicar la credencial (perfil profesional, CV, firma de correo).
- Mantenerla: cada versión mayor trae cambios; la doc de
  [versiones soportadas](https://www.odoo.com/documentation/saas-19.4/es/administration/supported_versions.html)
  te dice cuándo conviene recertificar.
- Siguiente paso natural: especializarte (contabilidad + localización, manufactura, o retail/PdV)
  y/o dar el salto técnico con los [tutoriales de desarrollador](https://www.odoo.com/documentation/saas-19.4/es/developer/tutorials.html).

---

## Criterios de validación final del plan completo

- [ ] Proyecto capstone con rúbrica ≥ 80 puntos.
- [ ] Demo integral de 30 min grabada.
- [ ] Documento de proyecto completo.
- [ ] Examen de muestra oficial aprobado.
- [ ] **Certificación funcional oficial obtenida.**
- [ ] Bitácora completa de las 12 fases (tu activo más valioso: es tu manual personal).

> **A partir de aquí**, el aprendizaje continúa con clientes reales. La regla no cambia:
> leer la documentación, configurar, romper a propósito, explicar. Y documentar todo.
