# K2 — Mesa de ayuda, SLA y servicio de campo

> Configuración guiada de la operación de soporte de ANDINA GOURMET.
> Helpdesk, Servicio de campo y Planeación son **Enterprise**.

---

## 1. El equipo de soporte

**Escenario:** los distribuidores llaman, escriben por WhatsApp y mandan correos cuando un lote llega
dañado, falta mercancía o necesitan documentación sanitaria. Hoy todo eso vive en el celular del
jefe de ventas.

Configura un equipo *Atención a distribuidores* con:

| Elemento | Valor |
|---|---|
| Etapas | Nuevo · En análisis · Esperando al cliente · Resuelto · Cancelado |
| Asignación | Equilibrada entre 2 agentes |
| Canales de entrada | Correo (alias `soporte@`), formulario web, chat en vivo |
| Visibilidad | Miembros del equipo |

## 2. Políticas SLA

| Política | Prioridad | Objetivo | Se aplica a |
|---|---|---|---|
| Crítico | Urgente | **4 horas** hábiles hasta la primera respuesta | Mercancía dañada o faltante |
| Normal | Media | **2 días** hábiles hasta la resolución | Consultas y documentación |
| Bajo | Baja | **5 días** | Sugerencias y mejoras |

**Ejercicio:**
1. Crea las tres políticas y 10 tickets repartidos.
2. Deja vencer uno a propósito: observa dónde aparece el incumplimiento y quién lo ve.
3. Revisa el reporte de cumplimiento de SLA y responde: *¿el problema es el equipo o el objetivo?*

> **Advertencia de consultor:** los SLA copiados del folleto comercial ("respuesta en 1 hora, 24/7")
> vuelven el tablero rojo desde la primera semana y el equipo deja de mirarlo. Se pactan objetivos
> **alcanzables** con el horario y el personal reales, y se ajustan cuando el equipo crezca.

## 3. Tickets facturables

1. Vende la **bolsa de 20 horas de soporte** (`SRV-BOL-20`) a un distribuidor.
2. Registra horas en un ticket contra esa bolsa.
3. Comprueba el consumo y el saldo restante.
4. Convierte un ticket no cubierto en una venta nueva.

## 4. Base de conocimiento y respuestas rápidas

1. Crea 5 artículos con las preguntas frecuentes reales del negocio (documentación sanitaria,
   condiciones de devolución, plazos de entrega, lista de precios vigente, política de lotes).
2. Configura respuestas predefinidas y úsalas al responder un ticket.
3. Publica dos artículos en el portal para que el cliente se autoatienda.

**Medición:** ¿cuántos tickets se evitarían si esos dos artículos estuvieran publicados?
Esa estimación es lo que justifica el tiempo de escribirlos.

## 5. Servicio de campo

**Escenario:** un distribuidor reporta que la exhibidora refrigerada cedida en comodato no enfría.

1. Escala el ticket a una **tarea de campo** asignada a Pedro Quiroz.
2. Planifica la visita en su calendario.
3. En sitio: registra tiempo, consume un repuesto del inventario del vehículo, completa la hoja de
   trabajo y captura la **firma del cliente**.
4. Factura la intervención (tiempo + materiales).
5. Relaciona el caso con **Mantenimiento** (Fase 5): ¿el equipo debía estar en un plan preventivo?

## 6. Planeación de recursos

1. Crea plantillas de turno para los 2 agentes de soporte y el técnico de campo.
2. Publica el horario de la semana; deja un turno **abierto** para que alguien lo tome.
3. Cruza la planificación con las **ausencias** (Fase 7) y observa qué pasa al aprobar unas vacaciones
   sobre un turno publicado.
4. Compara horas planificadas contra horas registradas al final de la semana.

## 7. Preguntas de diseño

**A.** ¿Cuándo un pedido del cliente debe ser un **ticket**, cuándo una **tarea de proyecto** y cuándo
una **tarea de campo**? Define el criterio en una frase para cada uno.

**B.** El cliente quiere que sus distribuidores vean el estado de sus tickets. ¿Qué configuras y qué
información **no** debe ver?

**C.** ¿Cómo evitas que el equipo cierre tickets sin resolverlos para cumplir el SLA?
(Pista: la respuesta no es técnica.)

**D.** ¿Qué indicadores mira el jefe de soporte cada mañana? Elige 4 y construye su tablero.
