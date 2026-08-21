# G1 — Diseño del embudo comercial

> Un embudo mal diseñado no es un problema estético: hace que el **pronóstico mienta**, y el gerente
> toma decisiones de compra, producción y caja con ese pronóstico. Esta guía es el razonamiento
> detrás de `datos/02-etapas-crm.csv`.

---

## 1. Las 5 etapas y su criterio de avance

La regla es una sola: **para pasar de etapa tiene que haber ocurrido un hecho verificable**,
no una sensación del vendedor.

| # | Etapa | Criterio para ENTRAR (hecho verificable) | Prob. sugerida | Días para alertar |
|---|---|---|---|---|
| 1 | **Nuevo** | Contacto registrado con empresa, persona y canal de origen | 10 % | 15 |
| 2 | **Calificado** | Confirmado: necesidad real, presupuesto estimado y **quién decide** | 25 % | 20 |
| 3 | **Propuesta enviada** | Cotización enviada desde Odoo y recibida por el cliente | 45 % | 15 |
| 4 | **Negociación** | El cliente respondió con objeciones concretas; hay contrapropuesta | 70 % | 10 |
| 5 | **Ganado** | Cotización firmada o pedido confirmado | 100 % | — |

**Perdido no es una etapa.** Es un estado (con motivo). Si lo pones como etapa, contaminas el
pronóstico y pierdes la estadística de motivos.

## 2. Las preguntas que definen cada etapa (para tu entrevista de levantamiento)

- ¿Qué tiene que pasar para que digas que esta oportunidad avanzó?
- ¿Quién decide de verdad? ¿Ya hablaste con esa persona?
- ¿Tienen presupuesto asignado o están explorando?
- ¿Cuándo necesitan tenerlo funcionando?
- ¿Contra quién estamos compitiendo?
- ¿Qué pasa si no compran nada?

Si el cliente no puede responder estas preguntas sobre sus propias oportunidades, el problema no
es el CRM: es el proceso comercial. **Decirlo es parte del trabajo de consultoría.**

## 3. Leads sí o leads no

| Situación | Recomendación |
|---|---|
| Entran muchos contactos de baja calidad (web, ferias, listas compradas) | **Activar leads**: se califica antes de ensuciar el embudo |
| Los contactos llegan filtrados (referidos, cartera conocida) | **Sin leads**: todo entra como oportunidad |
| Equipos distintos con realidades distintas | Se configura **por equipo** (`use_leads`), como en el archivo 01 |

En ANDINA GOURMET: B2B y Online usan leads; Retail no.

## 4. Reglas de higiene del embudo (acuerdo con el cliente, por escrito)

1. **Toda oportunidad abierta tiene una actividad siguiente.** Sin actividad, está muerta.
2. **Sin fecha de cierre esperada no hay pronóstico.** Es obligatoria desde la etapa *Calificado*.
3. **Perder es sano.** Un embudo sin pérdidas es un embudo con basura acumulada.
4. **La probabilidad la fija la etapa**, no el optimismo del vendedor (salvo excepción justificada).
5. **Revisión semanal del embudo**: 30 minutos, oportunidades estancadas primero.

Estas 5 reglas valen más que cualquier configuración. Van en el entregable de proceso TO-BE.

## 5. Indicadores que se leen desde el primer día

| Indicador | Dónde | Qué decisión dispara |
|---|---|---|
| Ingreso esperado ponderado por mes | Reporte de previsión | Compras y producción (Fases 3 y 5) |
| Oportunidades estancadas | Kanban con alerta de días | Reasignación o cierre |
| Tasa de conversión por etapa | Análisis del flujo | Dónde entrenar al equipo |
| Motivos de pérdida | Filtro Perdidas + agrupar | Precio, producto o argumentación |
| Actividades vencidas por vendedor | Vista de actividades | Gestión diaria del jefe de ventas |

## 6. Errores típicos al diseñar el embudo

| Error | Consecuencia |
|---|---|
| 9 etapas "para tener más detalle" | Nadie las mantiene; el vendedor deja todo en la primera |
| Etapas que describen tareas internas ("Esperando aprobación de crédito") | El embudo deja de reflejar al cliente y se vuelve un tablero de tareas |
| Probabilidades arbitrarias | El pronóstico ponderado no sirve para planificar caja |
| No configurar motivos de pérdida | Se pierde la única estadística que mejora el proceso |
| Copiar el embudo de otro cliente | Cada negocio compra distinto; el embudo se levanta, no se copia |
