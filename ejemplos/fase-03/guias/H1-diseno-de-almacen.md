# H1 — Diseño del almacén: cuántos pasos y por qué

> La pregunta que hace todo consultor novato: *"¿activo 1, 2 o 3 pasos?"*.
> La respuesta correcta nunca es técnica: **cada paso extra es trabajo humano diario**.

---

## 1. Las opciones que da Odoo

**Recepciones** (`reception_steps`)

| Valor | Flujo | Cuándo se justifica |
|---|---|---|
| `one_step` | Recibir y almacenar de una vez | Volumen bajo, sin control de calidad, una sola persona |
| `two_steps` | Recibir → Almacenar | Hay zona de recepción física separada del almacén |
| `three_steps` | Recibir → Control de calidad → Almacenar | Hay inspección real que puede **rechazar** mercancía |

**Entregas** (`delivery_steps`)

| Valor | Flujo | Cuándo se justifica |
|---|---|---|
| `ship_only` | Enviar | Pocos pedidos, se preparan y salen |
| `pick_ship` | Recoger → Enviar | Preparación separada del despacho; varias personas |
| `pick_pack_ship` | Recoger → Empacar → Enviar | Embalaje real con verificación previa al transporte |

## 2. La decisión para ANDINA GOURMET

| Almacén | Recepción | Entrega | Razón |
|---|---|---|---|
| **Lima** (planta y centro de distribución) | **3 pasos** | **3 pasos** | Recibe materia prima perecible que se inspecciona (°Brix, estado sanitario) y puede rechazarse; despacha a distribuidores con embalaje verificado por lote |
| **Arequipa** (almacén de reparto) | **1 paso** | **1 paso** | Solo recibe producto terminado ya inspeccionado y despacha a clientes locales; 1 persona |

**Este contraste es intencional**: te obliga a configurar los dos extremos y a explicar la diferencia
al cliente en términos de costo operativo, no de funcionalidad.

## 3. Preguntas para decidir (úsalas en tu levantamiento)

1. ¿Alguien **inspecciona** lo que llega y puede rechazarlo? → si no, no hay 3 pasos que valgan.
2. ¿La persona que recibe es **distinta** de la que almacena? → si es la misma, 1 paso.
3. ¿Empacan y pesan antes de entregar al transportista? → si no, no hay paso de empaque.
4. ¿Cuántas recepciones/entregas hacen al día? Con 3 al día, cada paso extra son 3 registros más.
5. ¿Qué pasa hoy cuando llega mercancía en mal estado? La respuesta define si necesitas cuarentena.

## 4. Lo que Odoo crea al activar pasos

Al cambiar los pasos, Odoo **genera automáticamente**: ubicaciones (Entrada, Control de calidad,
Salida, Empaque), tipos de operación (una por paso) y las **reglas de la ruta** que los encadenan.
Míralo con modo desarrollador en *Inventario → Configuración → Rutas* después de cambiar el ajuste:
ver esas reglas creadas solas es la mejor forma de entender qué es una ruta.

## 5. Diagrama de los movimientos (Lima, 3 pasos)

**Entrada de una compra:**
```
Proveedor ──(recepción)──▶ WH/Entrada ──(control)──▶ WH/Control de calidad ──(almacenar)──▶ WH/Existencias
```

**Salida de una venta:**
```
WH/Existencias ──(recoger)──▶ WH/Empaque ──(empacar)──▶ WH/Salida ──(enviar)──▶ Cliente
```

Cada flecha es un **movimiento de stock** y cada uno genera una **transferencia** que alguien debe
validar. En un pedido: 3 documentos, no 1. Esa es la conversación que hay que tener con el cliente
antes de activar la opción, no después.

## 6. Ubicaciones internas (archivo `02-ubicaciones-lima.csv`)

Se crean 6 ubicaciones bajo *WH/Existencias*: estantes A (conservas), B (snacks), C (insumos),
cámara refrigerada, zona de despacho y **cuarentena**.

Reglas de diseño de ubicaciones:
- **Refleja la realidad física.** Si el almacenero no puede caminar hasta ahí, no es una ubicación.
- **No crees más de las que se van a usar.** Cada ubicación es una decisión al recibir y al preparar.
- **Usa códigos de barras** desde el inicio: es lo que hace viable el escaneo (Bloque 3.7).
- La **cuarentena** es interna, no virtual: la mercancía retenida existe y hay que contarla.

## 7. Errores típicos

| Error | Consecuencia |
|---|---|
| Activar 3 pasos "porque se ve profesional" | El cliente valida 3 transferencias por pedido y en 2 semanas empieza a saltárselas |
| Crear una ubicación por estante y por nivel desde el día 1 | Nadie las mantiene; el inventario se vuelve ficción |
| Poner la cuarentena como ubicación virtual | El stock retenido desaparece del conteo físico |
| Configurar los pasos después de operar | Las transferencias en curso quedan a medio flujo |
| No documentar quién valida cada paso | En UAT nadie sabe de quién es la tarea |
