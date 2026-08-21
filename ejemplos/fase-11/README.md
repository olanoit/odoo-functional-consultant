# Cuaderno de ejemplos — Fase 11: Metodología de implementación

Casos prácticos para [`../../fases/fase-11-metodologia-implementacion.md`](../../fases/fase-11-metodologia-implementacion.md).

> Este cuaderno no tiene CSV: aquí no se configura Odoo, se practica **consultoría**.
> Es la mitad del trabajo que hace fracasar o triunfar los proyectos, y la que casi nadie entrena.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `casos/C1-entrevista-transcrita.md` | **Transcripción completa** de una entrevista de levantamiento con 4 personas de ANDINA GOURMET |
| `casos/C2-requerimientos-para-clasificar.md` | 25 requerimientos reales para clasificar en la matriz GAP-FIT |
| `casos/C3-conversaciones-dificiles.md` | 8 situaciones incómodas con respuestas modelo |
| `guias/P1-de-la-entrevista-al-gap-fit.md` | El ejercicio central: de lo que el cliente dice a lo que hay que hacer |
| `guias/P2-checklist-go-live.md` | Checklist de salida a producción y estabilización (entregable) |
| `soluciones/` | 22 requerimientos extraídos, síntomas vs. causas, y los 25 clasificados |

---

## Ejemplo 1 — Leer una entrevista como consultor
*(Bloque 11.1 · 45 min)*

Lee [`casos/C1-entrevista-transcrita.md`](casos/C1-entrevista-transcrita.md) **una vez, sin tomar notas**.
Después contesta de memoria: ¿cuál es el problema más caro que tiene esta empresa?

Vuelve a leerla y extrae los requerimientos con
[`guias/P1-de-la-entrevista-al-gap-fit.md`](guias/P1-de-la-entrevista-al-gap-fit.md), parte 1.
La solución trae **22 requerimientos**; si sacaste menos de 15, estás leyendo como usuario.

## Ejemplo 2 — Síntomas, causas y lo que faltó preguntar
*(Bloque 11.1 · 45 min)*

Partes 2 y 3 de P1. El cliente describe síntomas ("14 notas de crédito al mes"); tú tienes que
identificar la causa ("se factura contra la proforma, no contra lo entregado").

Y lo más importante: **las 10 preguntas que la entrevista no hizo**. Un levantamiento se juzga por
lo que quedó sin preguntar.

> Dos números de esa entrevista sostienen toda la propuesta comercial: **el 11 % de las facturas
> termina en nota de crédito** y hay **un ajuste de inventario de S/ 15 000 que la gerente no conocía**.

## Ejemplo 3 — La matriz GAP-FIT
*(Bloque 11.2 · 90 min)*

Clasifica los 25 requerimientos de [`casos/C2-requerimientos-para-clasificar.md`](casos/C2-requerimientos-para-clasificar.md).

Lo que se evalúa no es la etiqueta, sino que detectes **los tres que no deben implementarse tal como
se pidieron** y que sepas cómo abordar esa conversación.

## Ejemplo 4 — Alcance, estimación y las malas noticias
*(Bloque 11.3 · 90 min)*

Partes 6 y 7 de P1: objetivo en el lenguaje del cliente, corte de alcance justificado por la fecha
límite de enero, exclusiones explícitas y estimación por bloques **con reserva de riesgo**.

Incluye preparar las dos conversaciones incómodas que salen de la entrevista: el ajuste de inventario
y lo que realmente implica "facturar electrónico".

## Ejemplo 5 — Conversaciones difíciles
*(Bloque 11.9 · 60 min)*

[`casos/C3-conversaciones-dificiles.md`](casos/C3-conversaciones-dificiles.md): escribe tu respuesta
a las 8 situaciones **antes** de leer la modelo. Léelas en voz alta: si no suena natural dicho, no
sirve escrito.

## Ejemplo 6 — Demo, UAT y capacitación
*(Bloques 11.4, 11.6 y 11.7 · 150 min)*

1. **Demo:** ejecuta el guion de la Fase 2 ([`../fase-02/guias/G4-guion-demo-comercial.md`](../fase-02/guias/G4-guion-demo-comercial.md))
   con los dolores reales de la entrevista. Grábate y autoevalúa.
2. **UAT:** escribe 20 casos con [`../../plantillas/06-casos-de-prueba-uat.md`](../../plantillas/06-casos-de-prueba-uat.md),
   ejecútalos sobre `LAB` y gestiona 3 defectos hasta el cierre.
3. **Capacitación:** una guía rápida de 1 página para el rol de almacenero y una sesión de 30 minutos
   donde **el usuario toma el teclado**.

## Ejemplo 7 — Go-live
*(Bloque 11.8 · 60 min)*

[`guias/P2-checklist-go-live.md`](guias/P2-checklist-go-live.md): 4 secciones, 30 verificaciones y el
**plan de reversión**, que es obligatorio.

Recuerda el criterio: el éxito no se mide el día del arranque, sino en el **primer cierre contable**.

---

## Cierre: el kit de consultoría completo

Al terminar debes tener los 10 artefactos, listos para usar con un cliente real:

- [ ] Guion de entrevista por área (6 áreas).
- [ ] AS-IS y TO-BE documentados con diagramas.
- [ ] Matriz GAP-FIT con 25 requerimientos clasificados y decididos.
- [ ] Documento de alcance con exclusiones y criterios de aceptación.
- [ ] Estimación por fase y rol, con supuestos y reserva de riesgo.
- [ ] Guion de demo + demo grabada de 20 minutos.
- [ ] Plan de migración de datos (Fase 9).
- [ ] 20 casos UAT ejecutados con gestión de defectos.
- [ ] Guías rápidas por rol (mínimo 3) y plan de capacitación.
- [ ] Checklist de go-live y plan de estabilización.
