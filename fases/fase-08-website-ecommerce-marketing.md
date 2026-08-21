# Fase 8 — Sitio web, eCommerce y Marketing

**Horas estimadas:** 30–35 h · **Prerrequisitos:** Fases 1, 2 y 3 · **Base:** `LAB`

> **Objetivo:** cerrar el círculo digital: atraer (marketing), convertir (sitio web y tienda) y
> retener (automatización, eventos, encuestas), todo conectado al mismo CRM, inventario y contabilidad
> que ya configuraste. Aquí se demuestra el argumento más fuerte de Odoo: **una sola base de datos**.

---

## 📓 Cuaderno de ejemplos de esta fase

Datos y casos en **[`../ejemplos/fase-08/`](../ejemplos/fase-08/README.md)**: 7 categorías de tienda,
20 productos publicados, 3 métodos de envío, listas y contactos de correo, la
**checklist de puesta en marcha de la tienda** (10 bloques) y las **4 campañas de automatización**
que todo negocio necesita, con sus condiciones de salida.

## 1. Resultados de aprendizaje

1. Construir un sitio web corporativo con el editor por bloques, sin código, y publicarlo.
2. Configurar una tienda en línea completa: catálogo, variantes, pagos, envíos, impuestos, checkout.
3. Conectar la tienda con inventario, precios y contabilidad ya configurados.
4. Diseñar campañas de correo/SMS segmentadas y medir su desempeño.
5. Automatizar recorridos de cliente (marketing automation) con condiciones y disparadores.
6. Gestionar eventos y encuestas, y usarlos como fuente de leads.
7. Explicar SEO básico, chat en vivo, blog, foro y eLearning como piezas de captación.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 8.1 | Sitio web | [websites/website.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/website.html) · [website/pages.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/website/pages.html) |
| 8.2 | Comercio electrónico | [websites/ecommerce.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/ecommerce.html) |
| 8.3 | Catálogo en línea | [ecommerce/products.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/ecommerce/products.html) |
| 8.4 | Pago, envío y finalización de compra | [ecommerce/checkout_payment_shipping.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/ecommerce/checkout_payment_shipping.html) |
| 8.5 | Proveedores de pago | [finance/payment_providers.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/payment_providers.html) |
| 8.6 | Chat en vivo | [websites/livechat.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/livechat.html) |
| 8.7 | Blog | [websites/blog.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/blog.html) |
| 8.8 | Foro | [websites/forum.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/forum.html) |
| 8.9 | eLearning | [websites/elearning.html](https://www.odoo.com/documentation/saas-19.4/es/applications/websites/elearning.html) |
| 8.10 | Marketing por correo | [marketing/email_marketing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/email_marketing.html) |
| 8.11 | Marketing por SMS | [marketing/sms_marketing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/sms_marketing.html) |
| 8.12 | Marketing social | [marketing/social_marketing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/social_marketing.html) |
| 8.13 | Automatización de marketing | [marketing/marketing_automation.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/marketing_automation.html) · [campaign_templates.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/marketing_automation/campaign_templates.html) |
| 8.14 | Eventos | [marketing/events.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/events.html) |
| 8.15 | Encuestas | [marketing/surveys.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/surveys.html) · [surveys/create.html](https://www.odoo.com/documentation/saas-19.4/es/applications/marketing/surveys/create.html) |

## 3. Ruta de estudio paso a paso

### Bloque 8.1 — Sitio web (5 h)
1. Crear el sitio de ANDINA GOURMET: tema, colores, fuentes, cabecera y pie.
2. Editor de bloques: construir Inicio, Nosotros, Contacto y una landing de campaña.
3. **Formulario web** que cree un lead en el CRM (enlace directo con la Fase 2).
4. Páginas, menús, versiones móviles, y **multisitio** (concepto y cuándo usarlo).
5. SEO: título, descripción, palabras clave, URL amigables, redirecciones, mapa del sitio.
6. Traducción del sitio y publicación por idioma.

### Bloque 8.2 — eCommerce (8 h)
1. Publicar productos: imágenes, descripción, variantes con atributos visibles, productos alternativos
   y **venta cruzada** (accesorios / sugeridos).
2. Categorías de tienda, filtros por atributo, buscador y orden de aparición.
3. **Precios en línea**: lista de precios pública, precios con impuesto incluido/excluido, promociones y cupones.
4. **Disponibilidad**: mostrar stock, permitir venta sin stock, avisos de "últimas unidades",
   y qué pasa con la reserva (Fase 3).
5. **Checkout**: pasos, campos obligatorios, registro vs. invitado, condiciones.
6. **Métodos de envío**: tarifa fija, por peso/precio, retiro en tienda, transportistas.
7. **Métodos de pago**: activar un proveedor en modo de prueba, transferencia bancaria y su conciliación (Fase 4).
8. Flujo completo real: cliente compra → pedido → factura → entrega → asiento. Rastrear los 4 documentos.
9. Carritos abandonados y correo de recuperación.

### Bloque 8.3 — Marketing por correo y SMS (5 h)
1. Listas de correo, suscripción/baja, y **segmentación por filtros** sobre cualquier modelo.
2. Diseño de un correo con bloques, personalización con campos dinámicos y prueba A/B.
3. Métricas: entregados, abiertos, clics, rebotes, bajas. Interpretarlas.
4. Reputación de envío: dominio propio, SPF/DKIM/DMARC (concepto), límites diarios, IAP de créditos.
5. Campaña de SMS y consideraciones de costo/consentimiento.

### Bloque 8.4 — Automatización de marketing (5 h)
1. Crear una campaña con público objetivo, disparadores y actividades encadenadas
   (correo → espera → condición → SMS → crear actividad para el vendedor).
2. Usar plantillas de campaña y adaptarlas.
3. Escenarios: bienvenida a nuevo cliente, recuperación de carrito, reactivación de cliente inactivo,
   nutrición de leads del formulario web.
4. Medición del embudo de la campaña y su impacto en oportunidades ganadas.

> **Puente clave:** la automatización de marketing actúa sobre **cualquier modelo** (contactos, leads,
> pedidos, suscripciones). Es la diferencia con una herramienta de correo masivo externa. Véndelo así.

### Bloque 8.5 — Eventos, encuestas y comunidad (5 h)
1. Evento con inscripción en línea, entradas de pago, agenda, correos automáticos y seguimiento post-evento.
2. Encuestas: tipos de pregunta, puntuación, condiciones, certificación y uso en reclutamiento (Fase 7)
   y satisfacción (Fase 6).
3. eLearning: curso con lecciones, cuestionarios y certificado — útil para **capacitar a los usuarios
   del cliente** (Fase 11).
4. Chat en vivo: canales, reglas por página, respuestas rápidas y conversión a ticket/lead.
5. Blog y foro: cuándo aportan y cuándo son mantenimiento muerto.

## 4. Laboratorio integrador

**Encargo:** *"Queremos vender en línea nuestras conservas, capturar leads del sitio y recuperar
los carritos abandonados."*

En `LAB`:
1. Sitio con 4 páginas y formulario que crea leads asignados al equipo Online.
2. Tienda con 15 productos publicados, 2 con variantes, categorías y filtros; venta cruzada configurada.
3. Lista de precios pública con impuesto incluido y un cupón de descuento vigente.
4. 2 métodos de envío y 2 de pago (uno en modo de prueba, uno por transferencia).
5. Una compra completa ejecutada de punta a punta, con los 4 documentos trazados y el asiento contable revisado.
6. Campaña automatizada de recuperación de carrito (3 pasos) y campaña de bienvenida.
7. Un evento con inscripción y una encuesta de satisfacción enviada a clientes.

## 5. Preguntas de comprensión (prueba B)

1. ¿Cómo se conecta un formulario web con el CRM y qué se configura para asignarlo a un equipo?
2. ¿Qué determina el precio que ve un visitante anónimo en la tienda?
3. ¿Se reserva el stock cuando alguien pone un producto en el carrito? ¿Qué opciones hay?
4. Diferencia entre venta cruzada y productos alternativos.
5. ¿Cómo se contabiliza una venta en línea pagada con transferencia bancaria?
6. ¿Qué es la segmentación por filtros y por qué es más potente que una lista estática?
7. ¿Qué elementos técnicos afectan la entregabilidad del correo y cuáles dependen del cliente?
8. Describe una campaña de automatización de 4 pasos para reactivar clientes inactivos.
9. ¿Cuándo recomiendas multisitio y qué implica en catálogo y precios?
10. ¿Cómo usarías eLearning dentro de un proyecto de implementación?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (90 min):** publicar 5 productos con variantes, configurar 1 envío + 1 pago,
      ejecutar una compra completa y mostrar pedido, factura, entrega y asiento.
- [ ] **B.** ≥ 8/10 en preguntas.
- [ ] **C. Entregable:** *"Plan digital de ANDINA GOURMET"*: mapa de captación → conversión → retención,
      con la app de Odoo responsable de cada paso y los indicadores de cada etapa.
- [ ] Respaldo `LAB_fase08`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Tratar el eCommerce como "un sitio bonito" | Es un canal de ventas conectado a stock, precios e impuestos: si el back-office está mal, la tienda vende mal. |
| No definir la política de stock en línea | Sobreventa y clientes molestos en la primera campaña. |
| Impuestos mal configurados en el sitio | Precios distintos entre tienda y factura: reclamo garantizado. |
| Prometer entregabilidad de correo masivo | Depende del dominio y la reputación del cliente, no de Odoo. |
| Automatizaciones sin criterio de salida | Clientes recibiendo correos eternos; siempre define la condición de fin. |
