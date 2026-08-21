# Soluciones — C2: clasificación de los 25 requerimientos

> La clasificación depende del contexto; lo que se evalúa es el **argumento**, no la etiqueta exacta.
> Si tu respuesta difiere pero tu justificación es sólida, está bien.

| # | Requerimiento | Clasificación | Por qué |
|---|---|---|---|
| 1 | Vendedor ve solo sus clientes | **CONFIG** | Grupo de Ventas "solo documentos propios" + regla de registro estándar |
| 2 | Precios por tipo de cliente | **FIT** | Listas de precios: es funcionalidad núcleo (Fase 2) |
| 3 | Factura con logo y diseño | **STUDIO** | Editor de reportes PDF; sin código |
| 4 | No vender por debajo del costo | **STUDIO** | Regla de aprobación o automatización sobre el margen de la línea |
| 5 | Rentabilidad por producto | **CONFIG** | Requiere costeo correcto (Fases 3 y 5) y analítica (Fase 4); el reporte ya existe |
| 6 | Que el sistema diga cuándo comprar | **FIT** | Reglas de reordenamiento y reporte de reabastecimiento |
| 7 | Almacenero no cambia cantidades tras despachar | **CONFIG** | Permisos + bloqueo de transferencias validadas |
| 8 | Facturación electrónica SUNAT | **FIT** (Enterprise) | `l10n_pe_edi`; requiere certificado y series autorizadas |
| 9 | Kardex valorizado SUNAT | **TERCEROS** o **FIT** según edición | `l10n_pe_reports_stock` en Enterprise; verificar cobertura del formato exigido |
| 10 | Aviso por WhatsApp al despachar | **TERCEROS / DEV** | Requiere el módulo de WhatsApp y una plantilla aprobada; hay costo por mensaje |
| 11 | Campo "color de la tapa" | **STUDIO** — o mejor, **PROCESO** | Antes de crear el campo: ¿no es un atributo de variante? Preguntar para qué se usará |
| 12 | Comisión por margen | **DEV** | El cálculo de comisiones con reglas propias no es estándar; especificar y estimar |
| 13 | Clientes afectados por un lote | **FIT** | Trazabilidad de lotes (Fase 3): es el argumento de venta, no un desarrollo |
| 14 | Aprobación de descuentos > 20 % | **STUDIO** | Regla de aprobación |
| 15 | Pedidos que entran por WhatsApp | **DEV** + **PROCESO** | Técnicamente posible con integración, pero la pregunta real es si conviene: un pedido debe entrar por un canal estructurado |
| 16 | Balance y estado de resultados | **FIT** | Reportes contables estándar |
| 17 | Inventario por sucursal | **CONFIG** | Múltiples almacenes (Fase 3); **no** requiere multiempresa |
| 18 | Registro de visitas a distribuidores | **STUDIO** | App propia (Fase 9) |
| 19 | Planilla con PLAME y CTS | **OUT** (recomendado) o **DEV** | Ver el análisis completo en la Fase 7 |
| 20 | Aviso de lote por vencer | **CONFIG** | Fechas de caducidad + días de alerta (Fase 3) |
| 21 | Seguir usando el Excel en paralelo | **PROCESO** | Es el requerimiento más peligroso: garantiza doble digitación y datos que nunca cuadran. Se conversa, no se implementa |
| 22 | Integrar balanza electrónica | **TERCEROS / DEV** | Vía IoT Box o desarrollo; requiere prueba con el hardware real antes de cotizar |
| 23 | Guía de remisión electrónica | **FIT** (Enterprise) | `l10n_pe_edi_stock` |
| 24 | Tablero de ventas del día en pantalla | **CONFIG** | Vista de tablero o panel; sin desarrollo |
| 25 | Tienda funcionando sin internet | **FIT parcial** | El PdV opera fuera de línea y sincroniza al reconectar; hay que explicar los límites reales |

---

## Los tres que hay que conversar, no clasificar

**#21 — "Quiero seguir usando mi Excel en paralelo".**
No es un requerimiento técnico: es **miedo al cambio** y desconfianza en el sistema nuevo. Si lo
implementas, el proyecto está muerto: habrá dos verdades, la gente confiará en el Excel y el ERP
quedará como "el sistema que hay que llenar además".
Cómo se aborda: reconocer el miedo, acordar un período de convivencia **corto y con fecha de fin**,
y comprometerse a que el sistema entregue el reporte que hoy le da el Excel. La respuesta no es "no";
es "sí, durante seis semanas, y aquí está el plan para dejarlo".

**#15 — "Pedidos que entran por WhatsApp automáticamente".**
Técnicamente hay opciones, pero el problema de fondo es que **el pedido llega sin estructura**: sin
producto codificado, sin cantidad clara, sin precio. Automatizar la entrada de texto libre traslada
el caos al sistema.
Cómo se aborda: proponer el **portal del cliente** o un formulario, y usar WhatsApp para avisos
salientes (confirmación, despacho), donde sí aporta. Es un cambio de proceso disfrazado de requerimiento técnico.

**#19 — "Planilla con PLAME y CTS".**
Es la conversación de la Fase 7. No se clasifica sin antes explicar el alcance, el costo de
mantenimiento anual y el riesgo legal de un cálculo incorrecto. La recomendación por defecto es
dejar la planilla fuera del alcance de la primera fase.

---

## El criterio que se está evaluando

Un consultor junior clasifica los 25 y los cotiza.
Un consultor senior **detecta los tres que no deben implementarse tal como se pidieron**, y tiene la
conversación antes de que estén en el contrato. Esa conversación, hecha a tiempo, es lo que separa un
proyecto exitoso de uno que se pelea en la UAT.
