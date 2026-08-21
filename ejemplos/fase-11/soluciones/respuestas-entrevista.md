# Soluciones — P1: análisis de la entrevista

---

## Parte 1 — Requerimientos extraídos (22)

| ID | Requerimiento | Quién | Área | Prioridad |
|---|---|---|---|---|
| R-001 | Canal único de entrada de pedidos (hoy WhatsApp, correo, teléfono) | Sofía | Comercial | Alta |
| R-002 | Stock en línea y confiable al cotizar | Ana | Inventario | Alta |
| R-003 | Visibilidad de lo que está en producción | Ana / Rosa | Producción | Alta |
| R-004 | Facturar solo lo entregado (evitar notas de crédito) | Julio | Ventas/Contab. | Alta |
| R-005 | Listas de precios formalizadas (3 niveles) | Ana | Comercial | Alta |
| R-006 | Control de descuentos con aprobación | Sofía | Comercial | Alta |
| R-007 | Reposición sugerida por el sistema, no por memoria | Rosa | Compras | Alta |
| R-008 | Que la compra no dependa de una sola persona | Rosa | Compras | Media |
| R-009 | Trazabilidad de lotes hacia el cliente | Rosa | Inventario | **Alta** |
| R-010 | Control de fechas de vencimiento | Rosa | Inventario | Alta |
| R-011 | Cierre mensual en días, no en dos semanas | Julio | Contabilidad | Alta |
| R-012 | Cuadre entre inventario físico y contable | Julio | Contab./Inv. | **Alta** |
| R-013 | Costo real de producción por producto | Sofía | Producción | **Alta** |
| R-014 | Rentabilidad por producto y por cliente | Sofía | Gerencia | Alta |
| R-015 | Continuidad si el vendedor no está (información centralizada) | Sofía | Comercial | Alta |
| R-016 | Facturación electrónica integrada (evitar triple digitación) | Sofía / Julio | Contabilidad | **Alta** |
| R-017 | Entregas parciales gestionadas correctamente | Ana / Julio | Ventas/Almacén | Alta |
| R-018 | Registro de acuerdos con el cliente accesible a todos | Sofía | Comercial | Media |
| R-019 | Planificación de producción basada en pedidos reales | Rosa | Producción | Media |
| R-020 | Historial de compras por cliente | Ana | Comercial | Media |
| R-021 | Control de quién autoriza compras en ausencia del comprador | Sofía | Compras | Media |
| R-022 | Estar operativo antes de la campaña de febrero | Sofía | Proyecto | **Crítica** |

## Parte 2 — Síntomas y causas

| Síntoma | Causa real | Qué lo resuelve |
|---|---|---|
| 14 notas de crédito de ~125 facturas (11 %) | Se factura contra la proforma, no contra lo entregado | Política de facturación por **cantidades entregadas** (Fase 2) |
| Excel de stock actualizado 2 veces por semana | El stock no se actualiza con la operación, sino a mano | Inventario en tiempo real por movimientos (Fase 3) |
| 3 días para rastrear un lote | Lotes en cuaderno, no en sistema; guías en papel | Trazabilidad por lote (Fase 3) |
| Ajuste de inventario de S/ 15 000 | No hay valoración conectada a la contabilidad | Valoración perpetua + cuadre mensual (Fases 3 y 4) |
| Costo de hace dos años | No hay costeo de producción | LdM con costos reales (Fase 5) |
| "Si Ana no está, la empresa se para" | La información vive en una persona y en su Excel | CRM + historial en el sistema (Fase 2) |
| Triple digitación | Tres sistemas desconectados | Odoo con localización PE (Fase 10) |

> **El dato que hay que subrayar en la propuesta:** 11 % de las facturas terminan en nota de crédito,
> y hay un ajuste de inventario de S/ 15 000 que la gerente **no conocía**. Esos dos números,
> presentados juntos, justifican el proyecto mejor que cualquier lista de funcionalidades.

## Parte 3 — Las 10 preguntas que faltaron

1. ¿Cuántos SKU activos manejan?
2. ¿Cuántos clientes activos y cuántos compran al mes?
3. ¿Cuántas personas usarían el sistema y en qué roles?
4. ¿Cuál es el presupuesto y quién firma la decisión?
5. ¿Qué sistema contable usan hoy y se puede migrar de ahí?
6. ¿Cuántos proveedores y cuántas órdenes de compra al mes?
7. ¿Cuántas órdenes de producción por semana?
8. ¿Tienen certificado digital vigente para facturación electrónica?
9. ¿Quién será la contraparte del proyecto y cuánto tiempo puede dedicarle?
10. ¿Han intentado antes un proyecto así? ¿Qué pasó?

Las preguntas 4, 9 y 10 son las que más veces se olvidan y las que más determinan si el proyecto
sale bien. **La 10 es oro:** un cliente que ya fracasó con otro ERP trae miedos concretos que hay
que conocer antes de proponer.

## Parte 6 — Las dos conversaciones difíciles

**El ajuste de S/ 15 000.** Sofía se enteró **en la reunión** de que su contador venía ajustando el
inventario para poder cerrar. No es tu papel señalar a Julio; es tu papel explicar el mecanismo:

> *"Ese ajuste no significa que alguien haya hecho algo mal: significa que hoy no hay forma de que el
> inventario físico y el contable coincidan, porque no están conectados. Con la valoración conectada,
> ese número deja de ser un ajuste a ciegas y pasa a ser una diferencia que se puede explicar línea
> por línea. Va a ser incómodo el primer mes, porque van a ver de dónde viene."*

**"Que facture electrónico".** Para el cliente es un botón. Explica el alcance real sin asustar:

> *"Sí, Odoo emite y envía a SUNAT. Lo que hay detrás es: su certificado digital, las series que
> tienen autorizadas, y revisar producto por producto la afectación tributaria. Eso lo hacemos
> nosotros, pero necesitamos a Julio disponible unas horas y el certificado vigente. Si el
> certificado está vencido, ese es el primer trámite y no depende de nosotros."*

## Parte 7 — Nota sobre la estimación

La fecha límite (enero, por la campaña de febrero) es el condicionante más fuerte del proyecto.
Con ese corte, la respuesta profesional es **partir el alcance**:

- **Fase 1 (a enero):** comercial, inventario con lotes, compras, contabilidad, facturación electrónica.
- **Fase 2 (después de la campaña):** producción y costeo, rentabilidad por producto, tablero de gerencia.

Prometer las dos cosas para enero es lo que hace fracasar proyectos. Y el argumento para el cliente
es suyo, no tuyo: *"prefiero que en febrero facturen sin problemas a que estén aprendiendo a costear
en plena campaña"*.
