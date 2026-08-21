# Plantilla — Matriz GAP-FIT

**Cliente:** ____________ · **Proyecto:** ____________ · **Versión:** ____ · **Fecha:** ____

---

## 1. Clasificación usada

| Código | Significado | Costo relativo | Riesgo en actualizaciones |
|---|---|---|---|
| **FIT** | El estándar lo hace tal cual | Nulo | Nulo |
| **CONFIG** | Se resuelve configurando | Bajo | Nulo |
| **STUDIO** | Campos/vistas/automatizaciones sin código | Medio | Bajo-medio |
| **TERCEROS** | Módulo de Apps Store / OCA | Medio | Medio (depende del mantenedor) |
| **DEV** | Desarrollo a medida | Alto | Alto (mantenimiento por versión) |
| **PROCESO** | Se ajusta el proceso del cliente | Bajo | Nulo |
| **OUT** | Fuera de alcance / otro sistema | — | — |

## 2. Matriz

| ID | Requerimiento | Área | Prio | Clasificación | Solución propuesta | Est. (h) | Decisión del cliente | Fecha |
|---|---|---|---|---|---|---|---|---|
| R-001 | | | Alta | FIT | | 0 | Aceptado | |
| R-002 | | | Alta | CONFIG | | | | |
| R-003 | | | Media | STUDIO | | | | |
| R-004 | | | Alta | DEV | | | | |
| R-005 | | | Baja | OUT | | — | | |

## 3. Detalle de cada GAP (uno por brecha real)

### GAP R-0XX — <título>

- **Necesidad de negocio:** ____________
- **Por qué el estándar no lo cubre:** ____________
- **Opciones evaluadas:**
  | Opción | Costo (h) | Ventajas | Desventajas | Riesgo de actualización |
  |---|---|---|---|---|
  | A. Cambiar el proceso | | | | |
  | B. Studio | | | | |
  | C. Módulo de terceros | | | | |
  | D. Desarrollo | | | | |
- **Recomendación del consultor:** ____________
- **Impacto si NO se implementa:** ____________
- **Decisión del cliente (con nombre y fecha):** ____________
- **Criterio de aceptación:** ____________

## 4. Resumen ejecutivo

| Clasificación | Cantidad | Horas estimadas |
|---|---|---|
| FIT | | 0 |
| CONFIG | | |
| STUDIO | | |
| TERCEROS | | |
| DEV | | |
| PROCESO | | |
| OUT | | — |
| **Total** | | |

**Alertas para el cliente:**
- Cada elemento DEV y STUDIO añade costo permanente en cada actualización de versión.
- Los elementos OUT no se implementarán; requieren decisión explícita de aceptación.
