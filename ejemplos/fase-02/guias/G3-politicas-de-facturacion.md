# G3 — Políticas de facturación: 6 escenarios

> Cada escenario se ejecuta completo en la base `LAB` y se compara con el **resultado esperado**.
> Si tu resultado difiere, no sigas: encuentra la causa. Este es el tema que más disputas genera
> entre el cliente y el consultor después del go-live.

**Preparación:**
- Producto A = *Conserva de Aguaymanto 400 g* → política **Cantidades entregadas**.
- Producto B = *Asesoría nutricional para cliente* (servicio) → política **Cantidades pedidas**.
- Cliente = *Comercial Los Andes E.I.R.L.* con lista Mayorista B2B.
- Se configura en el producto, pestaña *Ventas* → *Política de facturación*.

---

## Escenario 1 — Entrega parcial con política "entregadas"

**Pasos:** pedido de 200 unidades de A → confirmar → entregar 120 → facturar.

**Resultado esperado:**
- La factura sale por **120 unidades**, no 200.
- El pedido queda con estado de facturación *Por facturar parcialmente*.
- Al entregar las 80 restantes y volver a facturar, sale una **segunda factura** por 80.

**Pregunta:** ¿qué ve el cliente en su portal entre la primera y la segunda factura?

## Escenario 2 — El mismo caso con política "pedidas"

**Pasos:** cambia A a *Cantidades pedidas*, repite el pedido de 200 y entrega solo 120 → facturar.

**Resultado esperado:**
- La factura sale por **200 unidades**, aunque solo entregaste 120.
- El pedido queda *Totalmente facturado* con mercancía pendiente de entregar.

**La conversación con el cliente:** esto no es un error de Odoo, es una decisión de negocio.
Se factura por adelantado lo comprometido. El riesgo: si nunca entregas las 80, tienes una factura
emitida sin respaldo de entrega — problema contable y, en Perú, tributario.

## Escenario 3 — Anticipo del 30 %

**Pasos:** pedido de 200 unidades de A (política entregadas) → *Crear factura* → **Anticipo (porcentaje) 30 %**.

**Resultado esperado:**
- Se emite una factura de anticipo por el 30 % del total del pedido.
- Aparece una línea de anticipo en el pedido.
- Al facturar la entrega real, el anticipo se **descuenta** de la factura final.

**Verificación clave:** el total facturado al final (anticipo + factura final) debe ser exactamente
el total del pedido. Si no cuadra, revisa el producto de anticipo y sus impuestos.

## Escenario 4 — Servicio facturado por adelantado

**Pasos:** pedido con 1 unidad de B (servicio, política pedidas) + 50 unidades de A → confirmar → facturar sin entregar nada.

**Resultado esperado:**
- La factura incluye **solo el servicio B**; A no aparece porque no se ha entregado.
- Es el comportamiento correcto y es el argumento para mezclar políticas en un mismo pedido.

## Escenario 5 — Devolución y nota de crédito

**Pasos:** sobre el pedido del escenario 1 ya facturado, devuelve 20 unidades por el almacén y emite
la nota de crédito correspondiente.

**Resultado esperado:**
- La devolución **no genera** la nota de crédito automáticamente: son dos hechos distintos
  (uno logístico, uno contable).
- La nota de crédito se emite desde la factura, por 20 unidades.
- El pedido refleja cantidades entregadas netas.

**Pregunta de consultor:** ¿puede existir una devolución sin nota de crédito? ¿Y una nota de crédito
sin devolución? Da un caso real de cada una. (Sí a ambas: mercancía cambiada por otra igual;
descuento comercial posterior.)

## Escenario 6 — Cambio del pedido después de facturar

**Pasos:** sobre un pedido confirmado y facturado parcialmente, intenta:
a) agregar una línea nueva, b) cambiar la cantidad de una línea ya facturada,
c) cambiar el precio de una línea ya facturada.

**Resultado esperado y aprendizaje:** Odoo permite algunas cosas y bloquea otras según el estado
del pedido y si está *bloqueado* (`locked`). Anota **exactamente** qué permitió y qué no, porque
esa será la pregunta del cliente la primera semana de operación.

---

## Tabla resumen para el entregable

| Tipo de producto en ANDINA GOURMET | Política recomendada | Motivo |
|---|---|---|
| Conservas, snacks, harinas, bebidas | Cantidades entregadas | Hay riesgo de faltante, lote y merma; se factura lo que salió del almacén |
| Fletes y servicios | Cantidades pedidas | No hay entrega física que registrar |
| Productos bajo pedido especial (marca propia) | Cantidades pedidas + anticipo | Protege el capital de trabajo de una producción dedicada |

## Errores frecuentes

| Error | Consecuencia |
|---|---|
| Dejar la política global por defecto sin revisarla producto por producto | Se factura lo no entregado y el cliente reclama |
| Facturar por "pedidas" con productos que se entregan en varias veces | El pedido queda facturado y el almacén sin control |
| No usar anticipos en producciones dedicadas | La empresa financia al cliente sin saberlo |
| Emitir nota de crédito para "corregir" en lugar de devolver mercancía | El inventario queda descuadrado (lo verás en la Fase 3) |
