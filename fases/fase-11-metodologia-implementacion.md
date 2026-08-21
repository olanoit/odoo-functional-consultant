# Fase 11 — Metodología de implementación y habilidades de consultoría

**Horas estimadas:** 30–35 h · **Prerrequisitos:** Fases 1 a 10 · **Base:** documental (poco Odoo, mucha práctica de consultoría)

> **Objetivo:** dejar de ser "alguien que sabe Odoo" y convertirte en **consultor**.
> El conocimiento del producto es la mitad del trabajo; la otra mitad es levantar requerimientos,
> decidir el alcance, gestionar expectativas, probar, capacitar y sostener el go-live.
> Los proyectos de ERP fracasan por esta mitad, casi nunca por el software.

---

## 📓 Cuaderno de ejemplos de esta fase

Material de práctica en **[`../ejemplos/fase-11/`](../ejemplos/fase-11/README.md)**: la
**transcripción completa de una entrevista de levantamiento** con 4 personas (con sus contradicciones
y sus silencios), 25 requerimientos para clasificar en la matriz GAP-FIT, 8 conversaciones difíciles
con respuestas modelo, el ejercicio guiado de entrevista → GAP-FIT → alcance → estimación, y la
checklist de go-live con plan de reversión.

## 1. Resultados de aprendizaje

1. Ejecutar un levantamiento de requerimientos estructurado, con preguntas que revelan el proceso real.
2. Documentar AS-IS y TO-BE, y construir una matriz **GAP-FIT** con decisiones justificadas.
3. Definir alcance, supuestos, exclusiones y criterios de aceptación de un proyecto.
4. Estimar horas y riesgos con un método repetible.
5. Preparar y ejecutar una demo orientada al dolor del cliente (no al catálogo de funciones).
6. Planificar y ejecutar UAT con casos de prueba y gestión de defectos.
7. Diseñar la capacitación y la documentación de usuario final.
8. Ejecutar el go-live y el soporte hiper-cuidado del primer mes (incluido el primer cierre contable).
9. Manejar conversaciones difíciles: cambios de alcance, expectativas irreales, decir "esto no lo hace".

## 2. Fuentes

La documentación oficial cubre el **producto**; la metodología se construye con práctica.
Fuentes recomendadas:

- **Odoo eLearning** — cursos de implementación/consultoría: <https://www.odoo.com/slides/all>
  (ver el track funcional: <https://www.odoo.com/slides/functional-24>).
- **Foro oficial** — casos reales y problemas de implementación: <https://www.odoo.com/forum/ayuda-1>
- **Documentación de administración** (entornos, actualizaciones, respaldos): [administration.html](https://www.odoo.com/documentation/saas-19.4/es/administration.html)
- **apps.odoo.com** y **OCA** para el análisis de brechas: <https://apps.odoo.com/apps/modules> · <https://github.com/OCA>
- Todas las plantillas de este plan: [`../plantillas/`](../plantillas/)

## 3. Ruta de estudio paso a paso

### Bloque 11.1 — Levantamiento de requerimientos (6 h)
1. Estudiar la plantilla [`01-levantamiento-de-requerimientos.md`](../plantillas/01-levantamiento-de-requerimientos.md)
   y construir tu **guion de entrevista** por área (ventas, compras, almacén, producción, contabilidad, RR. HH.).
2. Técnicas: pregunta abierta → concreta → contraejemplo → excepción.
   La pregunta más valiosa: *"¿qué pasa cuando esto sale mal?"*.
3. Reglas de oro:
   - Pedir **documentos reales** (factura, guía, reporte que usan hoy), no descripciones.
   - Preguntar **volúmenes** (¿cuántas facturas al mes? ¿cuántos SKU? ¿cuántos usuarios?).
   - Identificar al **dueño de cada decisión** y al usuario que sufrirá el cambio.
   - Separar *lo que dicen que hacen* de *lo que realmente hacen* (mirar la operación).
4. **Práctica:** entrevista simulada de 45 min con alguien que interprete al gerente de ANDINA GOURMET;
   grabarla y transcribir los requerimientos.

### Bloque 11.2 — AS-IS, TO-BE y GAP-FIT (6 h)
1. Documentar el AS-IS con la plantilla [`02-mapa-de-procesos-bpd.md`](../plantillas/02-mapa-de-procesos-bpd.md):
   actores, pasos, sistemas, documentos, puntos de dolor.
2. Diseñar el TO-BE en Odoo: mismo diagrama, con apps y objetos de Odoo en cada paso.
3. Llenar la matriz [`03-matriz-gap-fit.md`](../plantillas/03-matriz-gap-fit.md) clasificando cada requerimiento:
   **FIT** (estándar) · **CONFIG** · **STUDIO** · **DEV** · **TERCEROS** · **PROCESO** · **FUERA DE ALCANCE**.
4. Para cada GAP: impacto si no se hace, alternativa, estimación y decisión del cliente por escrito.
5. **Práctica:** convertir la entrevista del bloque anterior en un TO-BE y una matriz GAP-FIT completa.

### Bloque 11.3 — Alcance, estimación y propuesta (5 h)
1. Redactar el documento de alcance: objetivos, procesos incluidos, **exclusiones explícitas**, supuestos,
   entregables, hitos, responsabilidades del cliente, criterios de aceptación.
2. Método de estimación por bloques: configuración por app + migración por entidad + personalizaciones +
   pruebas + capacitación + acompañamiento + gestión (%) + **reserva de riesgo**.
3. Riesgos típicos y su mitigación: datos sucios, usuario clave no disponible, alcance creciente,
   localización, integraciones, resistencia al cambio.
4. **Práctica:** estimar el proyecto de ANDINA GOURMET completo en horas, por fase y por rol,
   con supuestos escritos.

> **Regla profesional:** todo lo que no está escrito como incluido, está excluido — y se dice desde el principio,
> amablemente, por escrito.

### Bloque 11.4 — La demo (4 h)
1. Estructura de una demo que vende: dolor del cliente → flujo en Odoo con **sus datos** →
   el número que le importa → siguiente paso.
2. Preparar la base demo: datos del cliente, nombres reales, productos reales, sin registros "Test 123".
3. Ensayar el guion de [`04-guion-de-demo.md`](../plantillas/04-guion-de-demo.md), cronometrado.
4. Manejo de preguntas: cuando no sabes, cuando la respuesta es "no lo hace", cuando piden algo fuera de alcance.
5. **Práctica:** demo de 20 minutos grabada del proceso completo de ANDINA GOURMET (ventas → almacén → factura),
   revisada contra una lista de errores comunes (hablar de menús en vez de negocio, perderse, improvisar datos).

### Bloque 11.5 — Migración de datos (4 h)
Repasar y aplicar [`05-plan-de-migracion-de-datos.md`](../plantillas/05-plan-de-migracion-de-datos.md)
con lo aprendido en la Fase 9: inventario de fuentes, mapeo campo a campo, reglas de limpieza,
orden de carga, ensayos, validación con sumas de control, fecha de corte y plan de reversión.

### Bloque 11.6 — Pruebas de aceptación (UAT) (5 h)
1. Escribir casos de prueba con [`06-casos-de-prueba-uat.md`](../plantillas/06-casos-de-prueba-uat.md):
   precondición, pasos, dato de prueba, resultado esperado, responsable.
2. Cubrir: caminos felices, excepciones, permisos por rol, reportes y cierres.
3. Gestión de defectos: registro, severidad, prioridad, responsable, reprueba, criterio de cierre.
4. **Acta de aceptación**: qué se firma y qué significa (fin de la etapa, inicio de garantía).
5. **Práctica:** 20 casos de prueba sobre el LAB, ejecutados y con al menos 3 defectos gestionados hasta el cierre.

### Bloque 11.7 — Capacitación y documentación (4 h)
1. Diseñar la capacitación por **rol**, no por app: qué hace el almacenero, qué hace el facturador.
2. Materiales: guía rápida de 1 página por rol, video corto por proceso, base de conocimiento
   dentro de Odoo (app Conocimiento, Fase 9) o curso en eLearning (Fase 8).
3. Ejecutar sesiones prácticas: el usuario hace, tú miras. Nunca al revés.
4. [`08-acta-de-capacitacion.md`](../plantillas/08-acta-de-capacitacion.md) firmada por asistentes.
5. **Práctica:** una guía rápida de 1 página para el rol "almacenero" y una sesión de 30 min ejecutada.

### Bloque 11.8 — Go-live y estabilización (4 h)
1. **Checklist de go-live**: datos cargados y validados, usuarios creados, permisos probados, secuencias
   y series correctas, correo configurado, respaldos activos, fecha de corte comunicada, plan de reversión.
2. Los primeros 5 días: soporte presencial/dedicado, canal único de incidencias, bitácora de problemas.
3. El **primer cierre contable** post go-live: es el verdadero examen del proyecto (Fase 4).
4. Traspaso a soporte: acuerdo de servicio, canal, tiempos, alcance de la garantía.
5. Revisión post-proyecto: qué funcionó, qué no, lecciones para el siguiente.

### Bloque 11.9 — Habilidades blandas del consultor (3 h)
Casos de práctica escritos (redacta tu respuesta a cada uno, en 5–8 líneas):
1. El cliente pide una funcionalidad que Odoo no hace y ya la prometió a su directorio.
2. El usuario clave sabotea el proyecto porque el sistema hace visible su ineficiencia.
3. A mitad del proyecto piden agregar tres módulos "que son rapidito".
4. La migración de datos revela que la información del cliente está mal desde hace años.
5. El gerente quiere reportes que su propio proceso no permite alimentar.
6. Descubres en UAT un error tuyo de configuración que costará 3 días.

> Principios: **transparencia temprana** (el problema comunicado a tiempo es un tema; comunicado tarde,
> una crisis), **todo por escrito**, **nunca prometer lo que no has probado**, y **el cliente decide,
> tú informas las consecuencias**.

## 4. Laboratorio integrador

Producir el **kit de consultoría completo** de ANDINA GOURMET, listo para usar con un cliente real:

1. Guion de entrevista por área (6 áreas).
2. Documento AS-IS + TO-BE con diagramas.
3. Matriz GAP-FIT con al menos 25 requerimientos clasificados y decididos.
4. Documento de alcance con exclusiones y criterios de aceptación.
5. Estimación en horas por fase y rol, con supuestos y reserva de riesgo.
6. Guion de demo + demo grabada de 20 min.
7. Plan de migración de datos.
8. 20 casos de prueba UAT ejecutados con gestión de defectos.
9. Guía rápida por rol (mínimo 3 roles) y plan de capacitación.
10. Checklist de go-live y plan de estabilización.

## 5. Preguntas de comprensión (prueba B)

1. ¿Cuáles son las 5 preguntas que nunca omites en un levantamiento y por qué?
2. Diferencia entre AS-IS y TO-BE. ¿Por qué documentar el AS-IS si vamos a cambiarlo?
3. ¿Cómo clasificas un requerimiento en la matriz GAP-FIT y quién toma la decisión final?
4. ¿Qué debe contener obligatoriamente un documento de alcance?
5. ¿Cómo estimas la migración de datos de un cliente con 3 sistemas y 8 000 productos?
6. ¿Qué hace que una demo funcione y qué la arruina?
7. ¿Qué diferencia hay entre una prueba funcional y una UAT?
8. ¿Cuándo se considera cerrado un defecto?
9. ¿Cómo capacitas a un usuario que se resiste al cambio?
10. Enumera 10 puntos del checklist de go-live.
11. ¿Por qué el primer cierre contable es el hito real de éxito?
12. Un cliente pide un cambio de alcance a 5 días del go-live. ¿Cómo lo manejas?

## 6. Criterios de validación (gate)

- [ ] **A. Simulación (2 h):** entrevista de levantamiento con un tercero interpretando al cliente
      → producir en el momento el TO-BE resumido y la matriz GAP-FIT inicial.
- [ ] **B.** ≥ 10/12 en preguntas, con respuestas argumentadas (no de memoria).
- [ ] **C. Entregable:** kit de consultoría completo (los 10 artefactos del §4).
- [ ] **D.** Demo de 20 min grabada y autoevaluada contra la lista de errores comunes.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Levantar requerimientos por correo | Se obtiene la versión oficial del proceso, no la real. |
| Demostrar funciones en vez de resolver dolores | El cliente no compra "Odoo tiene 80 apps", compra "dejo de perder plata en X". |
| Aceptar "hazlo como lo hacemos hoy" | Se replica en el ERP un proceso malo, con más costo y menos flexibilidad. |
| Dejar la migración para el final | Es la tarea más larga y la que más sorpresas trae. Empieza en la semana 2. |
| UAT hecha por el consultor | La prueba de aceptación la ejecuta **el usuario**, o no es aceptación. |
| Capacitar mostrando la pantalla | Se aprende haciendo. El usuario toma el teclado. |
| Ir a producción sin plan de reversión | Un problema grave sin salida atrás destruye la confianza del proyecto. |
