# Cuaderno de ejemplos — Fase 8: Sitio web, eCommerce y Marketing

Casos prácticos para [`../../fases/fase-08-website-ecommerce-marketing.md`](../../fases/fase-08-website-ecommerce-marketing.md).
Se apoya en el catálogo de la Fase 1, las listas de precios de la Fase 2 y el inventario de la Fase 3.

> **El argumento central de esta fase:** la tienda en línea no es un sitio web con productos, es un
> canal de ventas conectado a la misma base. Todo lo que configuraste mal en las fases anteriores
> se hace público aquí.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-categorias-tienda.csv` | 7 categorías de tienda (distintas de las internas) |
| `datos/02-productos-publicados.csv` | Publica 20 productos con su orden y categoría web |
| `datos/03-metodos-envio.csv` | 3 métodos: reparto Lima (gratis sobre S/ 250), agencia, retiro |
| `datos/04-listas-correo.csv` | 3 listas de correo |
| `datos/05-contactos-correo.csv` | 12 contactos repartidos entre las listas |
| `guias/M1` | **Checklist de puesta en marcha de la tienda** (10 bloques) |
| `guias/M2` | Campañas de correo y **las 4 automatizaciones** que todo negocio necesita |

## Antes de empezar

Apps: **Sitio web**, **Comercio electrónico**, **Marketing por correo electrónico**,
**Automatización de marketing** (Enterprise), **Eventos**, **Encuestas**.
Configura la **base neutralizada** o desactiva el envío real de correos antes de probar campañas.

---

## Ejemplo 1 — El sitio y el formulario que captura leads
*(Bloque 8.1 · 60 min)*

1. Elige tema, colores y tipografías coherentes con una marca de alimentos andinos.
2. Construye 4 páginas: Inicio, Nosotros, Contacto y una landing de la línea de aguaymanto.
3. Crea el **formulario de contacto que genera un lead** en el CRM, asignado al equipo Online.
4. Configura SEO por página y revisa el resultado en móvil.
5. Prueba: envía el formulario y comprueba que la oportunidad aparece en el embudo de la Fase 2.

## Ejemplo 2 — Montar la tienda
*(Bloque 8.2 · 120 min)*

Importa `01-categorias-tienda.csv` → `02-productos-publicados.csv` → `03-metodos-envio.csv`.

Fíjate en la diferencia entre los dos árboles de categorías:

| Campo | Para qué sirve |
|---|---|
| `categ_id` (Fase 1) | Costeo, valoración y cuentas contables |
| `public_categ_ids` (aquí) | Navegación del comprador en la tienda |

Luego sigue [`guias/M1-checklist-tienda-en-linea.md`](guias/M1-checklist-tienda-en-linea.md)
bloque por bloque: catálogo, precios, stock, envíos, pagos, checkout, contenido y post-venta.

**El ejercicio decisivo (bloque 3 de la checklist):** decide la política de stock y **prueba la
sobreventa** con dos compradores y una unidad. Lo que decidas ahí se nota el día de la primera campaña.

## Ejemplo 3 — La compra completa, trazada
*(Bloque 8.2 · 45 min)*

Compra como cliente real y sigue los cinco documentos:

```
Pedido de venta → Factura → Entrega → Pago → Asiento contable
```

Verifica que el precio de la tienda coincide con el de la factura, que la entrega descuenta del
almacén correcto y que el asiento usa las cuentas de la Fase 4. **Si algo no cuadra, la tienda no
está lista** — y el problema casi nunca está en el sitio web, sino en el back-office.

## Ejemplo 4 — Campañas de correo
*(Bloque 8.3 · 60 min)*

Importa `04-listas-correo.csv` y `05-contactos-correo.csv`, y sigue
[`guias/M2-campanas-y-automatizacion.md`](guias/M2-campanas-y-automatizacion.md), secciones 1 y 2:
diseño del correo, personalización, prueba A/B y lectura de métricas.

Aprende a explicar en una frase cada métrica y a **no prometer entregabilidad**: depende del dominio
y la reputación del cliente.

## Ejemplo 5 — Las cuatro automatizaciones
*(Bloque 8.4 · 90 min · Enterprise)*

Guía M2, sección 3: bienvenida, recuperación de carrito, reactivación de inactivos y nutrición de
leads. Cada una con su disparador, sus pasos, sus condiciones y —obligatorio— su **condición de salida**.

Implementa al menos dos completas y ejecútalas contra datos reales de tu base.

## Ejemplo 6 — Eventos, encuestas y comunidad
*(Bloque 8.5 · 60 min)*

1. **Evento:** degustación para distribuidores con inscripción en línea, aforo, correos automáticos
   y generación de leads en el equipo B2B.
2. **Encuesta:** satisfacción post-entrega enviada a los clientes de la Fase 2.
3. **eLearning:** un curso corto de "cómo exhibir la línea andina" para el personal de tus
   distribuidores. Guarda la idea: en la Fase 11 lo usarás para **capacitar a los usuarios del cliente**.
4. **Chat en vivo:** canal con reglas por página y conversión de conversación a ticket o lead.

---

## Cierre: entregables de la Fase 8

- [ ] Sitio con 4 páginas y formulario que genera leads asignados.
- [ ] Tienda con 20 productos publicados, categorías, filtros y venta cruzada.
- [ ] 3 métodos de envío y 2 de pago probados, incluido el umbral de envío gratis.
- [ ] Una compra completa trazada en sus cinco documentos.
- [ ] 2 campañas automatizadas funcionando con condición de salida.
- [ ] Un evento con inscripciones y una encuesta enviada.
- [ ] **Entregable C:** *"Plan digital de ANDINA GOURMET"*: mapa captación → conversión → retención,
      con la app responsable de cada paso y los indicadores de cada etapa.
- [ ] Respaldo `LAB_fase08_AAAAMMDD.zip`.
