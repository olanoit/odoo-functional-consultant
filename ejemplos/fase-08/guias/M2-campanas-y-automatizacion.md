# M2 — Campañas de marketing y automatización

> Lo que diferencia a Odoo de una herramienta de correo masivo externa: la automatización actúa
> sobre **cualquier modelo** de la base —contactos, leads, pedidos, suscripciones— y lo que hace
> queda registrado en el mismo CRM donde trabaja el vendedor.

---

## 1. Las listas cargadas

| Lista | Pública | Uso |
|---|---|---|
| Clientes de tienda en línea | Sí | Compradores del canal web |
| Distribuidores mayoristas | No | Comunicación B2B, no promocional |
| Boletín Vida Andina | Sí | Captación y contenido |

`05-contactos-correo.csv` trae 12 contactos repartidos entre las tres.

> **Segmentación estática vs. dinámica:** una lista es un conjunto fijo de contactos. Un **filtro
> sobre un modelo** ("clientes que compraron conservas en los últimos 90 días y no han vuelto")
> se recalcula solo. Para campañas de negocio, casi siempre quieres lo segundo.

## 2. Campaña de correo (ejercicio)

1. Diseña un correo con bloques para el lanzamiento de la **línea de aguaymanto**.
2. Personalízalo con campos dinámicos (nombre, empresa).
3. Haz una **prueba A/B** con dos asuntos distintos.
4. Envíalo a la lista del boletín y revisa las métricas: entregados, abiertos, clics, rebotes, bajas.
5. Explica cada métrica en una frase apta para un gerente.

**Sobre entregabilidad:** dominio propio, SPF, DKIM y DMARC configurados por el cliente; límites
diarios de envío; y créditos IAP si se usa el servidor de Odoo. **Nunca prometas tasas de entrega:**
dependen de la reputación del dominio del cliente, no del software.

## 3. Las cuatro campañas que todo negocio necesita

Diseña estas cuatro en *Automatización de marketing*, cada una con su condición de **salida**:

### A. Bienvenida a nuevo cliente
```
Disparador: primer pedido confirmado
 → Día 0  : correo de agradecimiento + cómo contactar soporte
 → Día 3  : ¿recibiste tu pedido? (encuesta corta)
 → Día 10 : contenido de valor (recetas con aguaymanto)
 → Día 20 : cupón de segunda compra
 → Salida : realizó una segunda compra
```

### B. Recuperación de carrito abandonado
```
Disparador: carrito sin confirmar por 4 horas
 → 4 h    : "tu carrito te espera"
 → 24 h   : mismo carrito + envío gratis sobre S/ 250
 → 72 h   : último aviso
 → Salida : compró, o pasaron 7 días
```

### C. Reactivación de cliente inactivo
```
Disparador: sin pedidos en 120 días
 → Día 0  : "te extrañamos" + novedades
 → Día 7  : condición → ¿abrió el correo?
             Sí  → crear actividad para su vendedor (llamar)
             No  → SMS con oferta puntual
 → Día 21 : si no hubo respuesta, marcar como inactivo para depuración
 → Salida : hizo un pedido
```

### D. Nutrición de leads del formulario web
```
Disparador: lead creado desde el formulario del sitio
 → Día 0  : ficha de producto + lista de precios mayorista
 → Día 2  : condición → ¿abrió?
             Sí  → asignar a vendedor y crear actividad
             No  → segundo correo con caso de éxito
 → Día 10 : si sigue sin interacción, marcar el lead como frío
 → Salida : se convirtió en oportunidad
```

**Regla que no se negocia:** toda automatización necesita **condición de salida**. Sin ella, los
clientes reciben correos para siempre y la marca se quema.

## 4. Medición

| Indicador | Dónde | Qué decisión dispara |
|---|---|---|
| Tasa de apertura por campaña | Marketing por correo | Cambiar asuntos o segmentación |
| Clics → visitas → pedidos | Campaña + Ventas | Si convierte, se repite y se amplía |
| Carritos recuperados | Automatización | Justifica el canal por sí solo |
| Leads del formulario → oportunidades | CRM | Calidad del tráfico del sitio |
| Bajas por campaña | Marketing por correo | Señal de exceso de frecuencia |

## 5. Eventos y encuestas

1. Crea un **evento**: degustación para distribuidores, con inscripción en línea, aforo y
   correos automáticos de confirmación y recordatorio.
2. Los inscritos deben generar **leads** en el equipo B2B.
3. Crea una **encuesta** de satisfacción post-entrega y envíala a los clientes de la Fase 2.
4. Reutiliza el módulo de encuestas para las **entrevistas de reclutamiento** de la Fase 7:
   es el mismo motor, otro uso.

## 6. Preguntas de diseño

**A.** ¿Cuándo una campaña debe segmentar por lista y cuándo por filtro dinámico sobre el modelo?

**B.** El gerente quiere enviar el boletín a **todos** los contactos de la base. ¿Qué le respondes?
(Pista: consentimiento, reputación del dominio y tasa de bajas.)

**C.** ¿Cómo evitas que un mismo cliente entre en tres campañas a la vez y reciba cinco correos por semana?

**D.** ¿Qué campaña de las cuatro tiene el retorno más medible y por qué la propondrías primero?
