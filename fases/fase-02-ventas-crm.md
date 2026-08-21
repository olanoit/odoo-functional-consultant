# Fase 2 — Ventas y CRM (ciclo Order-to-Cash comercial)

**Horas estimadas:** 35–40 h · **Prerrequisitos:** Fase 1 · **Base:** `LAB`

> **Objetivo:** dominar el recorrido comercial completo —desde que entra un lead hasta que se
> factura y cobra— y saber configurarlo para tres modelos de negocio distintos: B2B mayorista,
> tienda física (PdV) y venta recurrente (suscripciones).

---

## 1. Resultados de aprendizaje

1. Diseñar un embudo de ventas (etapas, probabilidades, motivos de pérdida, reglas de asignación).
2. Configurar el flujo cotización → pedido → entrega → factura, con sus variantes.
3. Modelar precios: listas de precios, descuentos, precios por cantidad, promociones y cupones.
4. Explicar y configurar las políticas de facturación (cantidades pedidas vs. entregadas) y su impacto contable.
5. Poner en marcha un Punto de Venta operativo con métodos de pago y cierre de caja.
6. Configurar suscripciones (planes recurrentes, renovación, MRR) y alquiler.
7. Interpretar los reportes comerciales y construir el tablero del gerente comercial.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 2.1 | CRM (visión general) | [sales/crm.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/crm.html) |
| 2.2 | Captación de leads | [crm/acquire_leads.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/crm/acquire_leads.html) |
| 2.3 | Gestión del flujo/pipeline | [crm/pipeline.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/crm/pipeline.html) |
| 2.4 | Desempeño y reportes CRM | [crm/performance.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/crm/performance.html) |
| 2.5 | Ventas (visión general) | [sales/sales.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/sales.html) |
| 2.6 | Cotizaciones: envío, plantillas, firma y pago en línea | [sales/send_quotations.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/sales/send_quotations.html) |
| 2.7 | Productos y precios (variantes, listas de precios, descuentos) | [sales/products_prices.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/sales/products_prices.html) |
| 2.8 | Facturación de ventas (políticas, anticipos, prorrateo) | [sales/invoicing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/sales/invoicing.html) |
| 2.9 | Punto de venta | [sales/point_of_sale.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/point_of_sale.html) |
| 2.10 | Suscripciones | [sales/subscriptions.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/subscriptions.html) |
| 2.11 | Alquiler | [sales/rental.html](https://www.odoo.com/documentation/saas-19.4/es/applications/sales/rental.html) |
| 2.12 | Proveedores de pago (pago en línea) | [finance/payment_providers.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/payment_providers.html) |

**Refuerzo:** cursos de CRM, Sales y Point of Sale en <https://www.odoo.com/slides/all>.

## 3. Ruta de estudio paso a paso

### Bloque 2.1 — CRM: el embudo (6 h)
1. Instalar CRM. Definir **equipos de ventas** (Mayorista, Retail, Online) con sus miembros y alias de correo.
2. Diseñar etapas propias del embudo de ANDINA GOURMET, con probabilidad por etapa y criterio de avance
   escrito (¿qué debe ser cierto para pasar de etapa?).
3. Activar **leads** (además de oportunidades) y entender la diferencia lead → oportunidad → cliente.
4. Configurar **reglas de asignación** de leads por equipo/vendedor y ejecutarlas.
5. Registrar 20 oportunidades con distintos valores, fechas de cierre y vendedores.
6. Configurar **motivos de pérdida** y perder 6 oportunidades. Reactivar una.
7. Reportes: análisis del flujo, actividades siguientes, previsión (*forecast*) por mes.

> **Romper:** cerrar una oportunidad sin actividad programada y ver cómo el flujo pierde trazabilidad.
> Concepto que venderás siempre: *"si no hay actividad siguiente, la oportunidad está muerta"*.

### Bloque 2.2 — Cotizaciones y pedidos (6 h)
1. Convertir una oportunidad en cotización; entender el vínculo entre `crm.lead` y `sale.order`.
2. Crear **plantillas de cotización** con productos opcionales y secciones/notas.
3. Configurar términos y condiciones, validez, plazos de pago y **firma en línea** + **pago en línea**.
4. Flujo completo: enviar por correo → portal del cliente → firma → confirmación.
5. Entender el **portal del cliente**: qué ve, qué puede hacer, cómo se configura el acceso.
6. Modificar un pedido confirmado (agregar línea, cambiar cantidad) y observar el efecto en la entrega.

### Bloque 2.3 — Precios y catálogo comercial (6 h)
1. **Listas de precios**: por cliente, por moneda, por rango de fechas, por cantidad mínima,
   basadas en otra lista, con descuentos y redondeo. Crear 3 escenarios reales:
   - Mayorista con 15 % de descuento y precio escalonado por volumen.
   - Lista en USD para exportación.
   - Promoción de temporada con vigencia fechada.
2. **Variantes** de producto (sabor × presentación) y cómo afectan precio y código.
3. **Unidades de medida** y ventas por peso; conversión entre UdM de la misma categoría.
4. Descuentos por línea, descuento global, y por qué eso es distinto de una lista de precios.
5. Promociones y cupones (módulo de promociones): reglas, condiciones, códigos.

> **Prueba de dominio:** dado un cliente mayorista que compra 500 unidades en USD durante una
> promoción, explicar **qué precio sale y por qué** siguiendo la jerarquía de resolución.

### Bloque 2.4 — Facturación de ventas (5 h)
1. Política de facturación **cantidades pedidas** vs. **cantidades entregadas**: configurar ambos
   productos y comparar el resultado tras una entrega parcial.
2. **Anticipos** (porcentaje y monto fijo) y su tratamiento en la factura final.
3. Facturas parciales, notas de crédito y devoluciones desde el pedido.
4. Facturación por hitos (útil para servicios) y facturación de productos de servicio.
5. Enlace comercial→contable: qué cuenta usa cada línea, de dónde sale el impuesto,
   qué diario recibe la factura. (Se profundiza en la Fase 4; aquí basta con rastrear el camino.)

### Bloque 2.5 — Punto de Venta (6 h)
1. Configurar un PdV para la tienda de Lima: métodos de pago (efectivo, tarjeta), monedas,
   impresora de recibos, categorías de productos en pantalla.
2. Abrir sesión, registrar 10 ventas con distintos pagos, aplicar descuento, hacer una devolución,
   **cerrar sesión** y revisar las diferencias de caja.
3. Entender el asiento contable que genera el cierre de sesión (dónde mirarlo).
4. Configurar clientes en PdV, programas de fidelidad y notas de pedido.
5. Modo restaurante (mesas, pisos, división de cuenta) — al menos explorarlo, es pregunta frecuente.
6. Comportamiento **fuera de línea**: qué pasa si cae internet durante una sesión.

### Bloque 2.6 — Suscripciones y alquiler (5 h)
1. Crear **planes de suscripción** (mensual, anual) con facturación recurrente y renovación automática.
2. Entender **MRR**, tasa de cancelación (*churn*) y el reporte de análisis de suscripciones.
3. Ciclo completo: alta → renovación → cambio de plan (*upsell*) → cancelación.
4. Alquiler: configurar productos alquilables, tarifas por periodo, recogida/devolución y penalidades.

### Bloque 2.7 — Reportes comerciales (3 h)
1. Análisis de ventas: por vendedor, por producto, por cliente, por período, con comparativas.
2. Construir el tablero del gerente comercial: 5 indicadores que él realmente mira
   (ventas del mes vs. objetivo, pipeline ponderado, ticket promedio, margen por línea, top 10 clientes).
3. Exportar y guardar filtros compartidos.

## 4. Laboratorio integrador

**Encargo del cliente:** *"Vendemos a distribuidores con precios especiales, en tienda propia y
queremos empezar con un plan de suscripción de caja mensual. Muéstrame cómo se ve todo eso en Odoo."*

Construir en `LAB`:
1. 3 equipos de ventas con embudos y reglas de asignación distintas.
2. 3 listas de precios (mayorista escalonada, USD, promoción vigente) aplicadas correctamente.
3. Un flujo completo mayorista: oportunidad → cotización con productos opcionales → firma en portal →
   confirmación → entrega parcial → factura por cantidades entregadas → segunda entrega → segunda factura.
4. Un PdV con sesión abierta, 10 tickets, una devolución y un cierre con arqueo.
5. Un plan de suscripción con 3 clientes activos y una renovación ejecutada.
6. Un tablero comercial guardado.

## 5. Preguntas de comprensión (prueba B)

1. Un cliente entrega parcialmente y quiere facturar solo lo entregado. ¿Qué configuras y dónde?
2. ¿Cuál es el orden de precedencia entre lista de precios, descuento de línea y promoción?
3. Diferencia entre lead y oportunidad. ¿Cuándo recomiendas activar leads?
4. ¿Qué pasa contablemente cuando se cierra una sesión de PdV?
5. Un pedido confirmado necesita una línea adicional después de entregado. ¿Qué opciones tienes y qué implica cada una?
6. ¿Cómo cotizas un producto con variantes cuando cada variante tiene precio distinto?
7. Explica MRR y por qué un cliente de suscripciones lo pide desde el día 1.
8. ¿Qué diferencia hay entre una nota de crédito y una devolución de mercancía? ¿Se pueden dar por separado?
9. ¿Cómo garantizas que un vendedor no vea las oportunidades de otro equipo?
10. Cliente pide "aprobación del jefe si el descuento supera el 20 %". ¿Estándar, Studio o desarrollo?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (90 min):** configurar desde cero un equipo de ventas con embudo propio,
      una lista de precios escalonada, una plantilla de cotización con opcionales, y ejecutar
      el ciclo cotización→entrega parcial→factura por entregado.
- [ ] **B.** ≥ 8/10 en preguntas.
- [ ] **C. Entregable:** documento *"Proceso comercial TO-BE de ANDINA GOURMET"* con diagrama de
      flujo (usa [`../plantillas/02-mapa-de-procesos-bpd.md`](../plantillas/02-mapa-de-procesos-bpd.md)),
      roles, estados y puntos de control.
- [ ] **D. Demo:** grabar o ejecutar en vivo una demo de 15 minutos del ciclo comercial
      (guion en [`../plantillas/04-guion-de-demo.md`](../plantillas/04-guion-de-demo.md)).
- [ ] Respaldo `LAB_fase02`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Usar descuentos de línea en vez de listas de precios | Imposible de mantener y de auditar con 300 clientes. |
| No definir criterio de avance de etapa | El embudo se llena de oportunidades zombis y el reporte miente. |
| Facturar por "cantidades pedidas" sin avisar | Se factura lo no entregado; el problema aparece en la conciliación. |
| Prometer PdV sin probar el cierre de caja | El arqueo y la diferencia de efectivo son el 70 % de las quejas de tienda. |
| Confundir Suscripciones con "facturar todos los meses a mano" | Suscripciones es Enterprise y trae renovación, MRR y portal. |
