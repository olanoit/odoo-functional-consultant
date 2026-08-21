# M1 — Checklist de puesta en marcha de una tienda en línea

> Una tienda en línea en Odoo **no es un sitio web con productos**: es un canal de ventas conectado
> al mismo inventario, precios, impuestos y contabilidad que ya configuraste. Si el back-office está
> mal, la tienda vende mal — y en público.

---

## 1. Catálogo

- [ ] Productos **publicados** (`is_published`) y con orden definido (`website_sequence`).
- [ ] Cada producto con **imagen** de calidad y descripción de venta.
- [ ] **Categorías de tienda** (`product.public.category`) creadas — son distintas de las categorías
      internas de producto, que sirven para costeo e inventario.
- [ ] Atributos publicados para que funcionen los **filtros** de la izquierda.
- [ ] Variantes con imagen propia cuando el color o la presentación importan.
- [ ] Productos **alternativos** y de **venta cruzada** configurados en los más vendidos.

> **Diferencia que hay que explicar al cliente:** `categ_id` (categoría interna) manda en la
> contabilidad y la valoración; `public_categ_ids` (categoría de tienda) manda en cómo navega el
> comprador. Son dos árboles distintos, con propósitos distintos.

## 2. Precios e impuestos

- [ ] Lista de precios **pública** definida y asignada al sitio.
- [ ] Decisión tomada y aplicada: precios **con IGV incluido** o sin él.
- [ ] Coherencia verificada: el precio del sitio = el precio de la factura.
- [ ] Promociones y cupones probados con fecha de vigencia.
- [ ] Precio mostrado a un visitante **anónimo** verificado (no es el del cliente mayorista).

## 3. Stock y disponibilidad

- [ ] Decidido si se **muestra** el stock disponible y con qué umbral.
- [ ] Decidido si se permite **vender sin stock** (`allow_out_of_stock_order`) y con qué mensaje.
- [ ] Comprobado qué pasa con la **reserva**: el carrito no reserva; la reserva ocurre al confirmar.
- [ ] Probada la sobreventa: dos compradores, una unidad disponible.

> Este bloque es el que provoca la primera crisis real de una tienda: la campaña sale, entran 40
> pedidos y el almacén tiene 12 unidades.

## 4. Envíos

- [ ] Métodos de envío creados con su **producto de servicio** asociado.
- [ ] Tarifas probadas: fija, por peso o por importe.
- [ ] **Envío gratis** sobre cierto monto (configurado y probado en el límite exacto).
- [ ] Retiro en tienda como opción, si aplica.
- [ ] Zonas no cubiertas: qué ve el comprador de una zona a la que no se llega.

## 5. Pagos

- [ ] Al menos un proveedor de pago en **modo de prueba** funcionando.
- [ ] **Transferencia bancaria** con instrucciones claras y su circuito de conciliación (Fase 4).
- [ ] Probado el flujo completo de pago fallido y de pago pendiente.
- [ ] Definido quién confirma los pedidos con pago pendiente y en cuánto tiempo.

## 6. Checkout y cuenta

- [ ] Campos obligatorios revisados (¿de verdad necesitas el RUC de un consumidor final?).
- [ ] Compra como invitado permitida o no, decidido con criterio.
- [ ] **Términos y condiciones** publicados y aceptados en el checkout.
- [ ] Correos transaccionales revisados: confirmación, envío, factura.
- [ ] Portal del cliente probado: ¿puede ver sus pedidos y descargar su factura?

## 7. Contenido y SEO

- [ ] Páginas mínimas: Inicio, Nosotros, Contacto, Preguntas frecuentes, Políticas.
- [ ] **Formulario de contacto que crea un lead** en el CRM (Fase 2), asignado a un equipo.
- [ ] Títulos, descripciones y URL amigables por página y por producto.
- [ ] Versión móvil revisada en un teléfono real, no solo en el simulador.
- [ ] Velocidad de carga con imágenes optimizadas.

## 8. Post-venta y recuperación

- [ ] Correo de **carrito abandonado** configurado con su tiempo de espera.
- [ ] Campaña de bienvenida a nuevos clientes.
- [ ] Encuesta de satisfacción tras la entrega.
- [ ] Definido el proceso de **devoluciones** desde la tienda (Fases 2 y 3).

## 9. La prueba final antes de publicar

Ejecuta una compra completa **como cliente real**, con un correo propio, y verifica los cinco
documentos que se generan:

```
Pedido de venta  →  Factura  →  Entrega  →  Pago  →  Asiento contable
```

Si alguno no aparece o aparece con datos raros, la tienda **no está lista**, por bonita que se vea.

## 10. Errores frecuentes

| Error | Consecuencia |
|---|---|
| Publicar sin decidir la política de stock | Sobreventa en la primera campaña |
| Impuestos distintos entre tienda y factura | Reclamo del cliente y problema tributario |
| No probar el checkout en móvil | La mayoría del tráfico compra desde el teléfono |
| Formulario de contacto que solo manda correo | Se pierden los leads y nadie mide la conversión |
| Prometer entregabilidad de correo masivo | Depende del dominio y la reputación del cliente, no de Odoo |
| Tratar la tienda como proyecto de diseño | El 80 % del trabajo real está en catálogo, precios y stock |
