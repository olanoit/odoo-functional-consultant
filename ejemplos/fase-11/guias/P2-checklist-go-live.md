# P2 — Checklist de go-live y estabilización

> **Entregable de la Fase 11.** Se adapta a cada cliente, pero la estructura no cambia.
> La regla: **nada sale a producción sin que las cuatro secciones estén completas.**

**Cliente:** ____________ · **Fecha de salida:** ____________ · **Responsable:** ____________

---

## A. Dos semanas antes

| # | Verificación | Responsable | ✔ |
|---|---|---|---|
| A1 | UAT cerrada: 100 % de casos críticos aprobados | Cliente | ☐ |
| A2 | Cero defectos críticos abiertos; los altos con plan y fecha | Consultor | ☐ |
| A3 | Acta de aceptación firmada | Ambos | ☐ |
| A4 | Ensayo de migración completo y cronometrado | Consultor | ☐ |
| A5 | Usuarios creados con sus permisos y **probados uno por uno** | Consultor | ☐ |
| A6 | Capacitación ejecutada por rol, con acta firmada | Ambos | ☐ |
| A7 | Guías rápidas entregadas (1 página por rol) | Consultor | ☐ |
| A8 | Fecha de corte comunicada a **toda** la empresa | Cliente | ☐ |
| A9 | Plan de reversión escrito y acordado | Ambos | ☐ |

## B. La semana previa

| # | Verificación | Responsable | ✔ |
|---|---|---|---|
| B1 | Datos maestros cargados y validados con sumas de control | Consultor | ☐ |
| B2 | Saldos contables de apertura cuadrados y aprobados por el contador | Cliente | ☐ |
| B3 | Stock inicial contado físicamente y cargado | Cliente | ☐ |
| B4 | Documentos abiertos migrados (cobrar, pagar, pedidos pendientes) | Consultor | ☐ |
| B5 | Secuencias y series configuradas y **autorizadas** | Consultor | ☐ |
| B6 | Correo saliente configurado y probado con un envío real | Consultor | ☐ |
| B7 | Facturación electrónica probada en producción con **un** documento real | Ambos | ☐ |
| B8 | Respaldo automático activado y **restauración probada** | Consultor | ☐ |
| B9 | Base de preproducción sincronizada para consultas | Consultor | ☐ |
| B10 | Canal único de incidencias definido y comunicado | Ambos | ☐ |

## C. El día del arranque

| # | Verificación | Responsable | ✔ |
|---|---|---|---|
| C1 | Respaldo previo al arranque | Consultor | ☐ |
| C2 | Carga final de saldos y stock a la fecha de corte | Consultor | ☐ |
| C3 | Validación de las sumas de control finales | Ambos | ☐ |
| C4 | Sistema anterior en **solo lectura** | Cliente | ☐ |
| C5 | Primer documento real de cada tipo emitido y verificado | Ambos | ☐ |
| C6 | Consultor presente (o disponible en línea) toda la jornada | Consultor | ☐ |
| C7 | Bitácora de incidencias abierta | Consultor | ☐ |

## D. Los primeros 30 días

| # | Actividad | Cuándo | ✔ |
|---|---|---|---|
| D1 | Soporte dedicado, presencial o en línea | Días 1 a 5 | ☐ |
| D2 | Revisión diaria de incidencias con el líder del cliente | Días 1 a 10 | ☐ |
| D3 | Verificación de que **nadie** siga usando el sistema viejo | Día 7 | ☐ |
| D4 | Revisión de datos: negativos de stock, documentos en borrador, transferencias en espera | Día 10 | ☐ |
| D5 | Refuerzo de capacitación en lo que más falla | Día 15 | ☐ |
| D6 | **Acompañamiento del primer cierre contable** | Fin de mes | ☐ |
| D7 | Cuadre inventario ↔ contabilidad del primer mes | Fin de mes | ☐ |
| D8 | Reunión de cierre de proyecto y lecciones aprendidas | Día 30 | ☐ |
| D9 | Traspaso formal a soporte, con alcance y tiempos | Día 30 | ☐ |

---

## El plan de reversión (obligatorio)

| Escenario | Señal de alarma | Acción | Quién decide | Plazo máximo |
|---|---|---|---|---|
| Carga masiva con errores | Sumas de control no cuadran | Restaurar respaldo y reprogramar | Consultor + líder cliente | 2 h |
| Facturación electrónica no funciona | Rechazos sistemáticos | Emitir por el sistema anterior ese día | Contador | 4 h |
| Los usuarios no pueden operar | Más de X incidencias bloqueantes | Volver al sistema anterior por 48 h | Patrocinador | 1 día |

**Sin este cuadro completo, no hay go-live.** Un problema grave sin salida atrás destruye la
confianza del proyecto entero, aunque después se resuelva.

---

## El indicador real de éxito

No es el día del arranque. Es el **primer cierre contable**: cuando el contador emite sus estados
financieros desde el sistema nuevo, el inventario cuadra con la contabilidad y puede explicar cada
diferencia. Hasta ese momento, el proyecto está en curso — aunque todos estén usando el sistema.
