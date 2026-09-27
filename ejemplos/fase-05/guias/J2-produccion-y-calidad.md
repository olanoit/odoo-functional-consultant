# J2 — Producción, calidad y mantenimiento en la planta

> Guía de ejecución: qué configurar, qué probar y qué romper en el taller virtual de ANDINA GOURMET.

---

## 1. Órdenes de fabricación: los dos modos

| Modo | Cuándo | Qué registra el operario |
|---|---|---|
| **Sin órdenes de trabajo** | Producción simple, sin control de tiempos | Solo cantidades producidas y consumidas |
| **Con órdenes de trabajo** | Hay centros de trabajo, tiempos y capacidad que planificar | Inicio/fin de cada operación, en la vista de taller |

**Ejercicio:** fabrica 1 000 conservas de las dos formas y compara: número de clics, información
obtenida y costo calculado. Luego decide, con argumentos, cuál recomendarías a ANDINA GOURMET.

## 2. La cadena multinivel

Al lanzar una orden de 1 000 conservas sin stock de pulpa ni almíbar, con los semielaborados
con LdM propia (en v20 la ruta de **fabricación** es del almacén y se les aplica sola por tener LdM):

1. Odoo crea la orden de la conserva (en espera de componentes).
2. **No** crea por sí solo las órdenes de **pulpa** y **almíbar**: los componentes de una orden se
   piden *bajo existencias* y la orden se queda esperando. Las órdenes hijas (240 kg de pulpa y 180 L
   de almíbar) aparecen de dos maneras, verificadas en v20:
   - marcando en la pulpa y el almíbar la ruta **Reabastecer sobre pedido (MTO)** —viene archivada:
     desarchívala en *Inventario → Configuración → Rutas*—: se crean al **confirmar** la orden;
   - o desde *Inventario → Operaciones → Reabastecimiento*, que propone esas cantidades y las crea
     con **Pedir** (o sola, con una regla de reordenamiento automática).
3. Si tampoco hay aguaymanto, dispara la **compra** (si el insumo tiene regla o ruta de compra).

**Ejercicio:** ejecútalo y dibuja la cadena completa de documentos. Después responde:
¿en qué orden hay que terminarlas? ¿Qué pasa si terminas la conserva antes que la pulpa?

## 3. Consumo distinto de la LdM y mermas

> ⚠️ **Cambio respecto de v19.0:** el campo `consumption` de la LdM (`strict` / `warning` /
> `flexible`) **ya no existe en v20** (desapareció en las versiones saas-19.x). Ya no se elige por LdM
> si se bloquea o se permite: cuando el consumo registrado difiere del de la LdM, Odoo **siempre**
> muestra la *Advertencia de consumo* al marcar la orden como hecha, con tres salidas: **Confirmar**
> (acepta lo consumido), **Update Quantities & Validate** (vuelve a las cantidades de la LdM) o
> **Descartar** (`mrp/wizard/mrp_consumption_warning.py`).

**Ejercicio:** consume 260 kg de pulpa en vez de 240, observa el aviso, confírmalo y mira el efecto en
el costo real. Anota qué le dirías a un jefe de planta que pide "que no salga ese aviso, para no
perder tiempo": qué gana y qué pierde (pista: el aviso es el único control de mermas que queda en la
orden).

## 4. Lotes y trazabilidad completa

1. Asigna lote a la pulpa producida.
2. Consúmela en la conserva y asigna lote al producto terminado.
3. Desde el lote de conserva, usa **Trazabilidad** hacia atrás: debe llegar hasta el lote de
   aguaymanto comprado al proveedor.

> Esta es la cadena que se corta si los componentes no llevan lote. Compruébalo: quita el seguimiento
> a la pulpa y repite. Verás exactamente dónde muere la trazabilidad.

## 5. Desecho, sobreproducción y desmontaje

| Operación | Qué probar | Qué observar |
|---|---|---|
| **Desecho** | Desechar 15 unidades durante la orden | Ubicación virtual de desecho; hay asiento inmediato solo si esa ubicación tiene cuenta de valoración (si no, llega con el cierre de existencias) |
| **Sobreproducción** | Producir 1 020 en vez de 1 000 | Cómo se reparte el costo entre más unidades |
| **Desmontaje** | Deshacer una orden terminada | Los componentes vuelven al stock; ¿a qué costo? |

## 6. Subcontratación del etiquetado

1. Crea una LdM de **subcontratación** con *Maquilas Alimentarias del Norte* para la conserva etiquetada.
2. Prueba las dos variantes:
   - **Sin envío de componentes**: el subcontratista pone todo; tú solo compras el producto terminado.
   - **Con envío de componentes**: le envías frascos y etiquetas; su ubicación aparece en tu inventario.
3. Compara la propiedad del stock en cada caso: **¿de quién es la mercancía mientras está en su planta?**
   Esa pregunta tiene consecuencias contables y de seguro.

## 7. Calidad (Enterprise)

Configura dos puntos de control con `measure_on`, `norm` y tolerancias:

| Punto | Cuándo | Tipo | Criterio |
|---|---|---|---|
| °Brix de la pulpa | Al terminar la orden de pulpa | **Medición** | Norma 14, tolerancia 12–16 |
| Sellado de la conserva | Al terminar la orden de conserva | Aprobar / Rechazar | Inspección visual del vacío |

**Ejercicio:** provoca un fallo (mide 10 °Brix) y sigue el flujo de la **alerta de calidad**:
quién la recibe, qué acción correctiva se registra, qué pasa con la orden.

## 8. Mantenimiento

1. Registra la **línea de envasado** como equipo, con responsable, categoría, centro de trabajo, costo
   y *Fecha efectiva* (la base del cálculo del MTBF). El equipo **no tiene campo de criticidad**: se
   modela con una **propiedad** definida en la categoría del equipo o con la **prioridad** de cada
   solicitud.
2. Crea un mantenimiento **preventivo** recurrente cada 3 meses (*Recurrente*, *Repetir cada* 3
   meses). El estándar de v20 programa por **calendario**, no por horas de uso: un plan "cada 500
   horas" hay que convertirlo a una frecuencia equivalente o resolverlo fuera del estándar (dato para
   tu análisis GAP).
3. Genera una solicitud **correctiva** desde el taller (la selladora falla a mitad de una orden).
4. Observa el efecto en la planificación del centro de trabajo mientras el equipo está en
   mantenimiento (con *Bloquear centro de trabajo* activado en la solicitud, Enterprise).
5. Revisa los indicadores MTBF y MTTR del equipo (se calculan con los mantenimientos **correctivos**
   terminados) y explica qué decisión de negocio dispara cada uno.

## 9. PLM: cambio de ingeniería (Enterprise)

**Escenario:** el proveedor de frascos cambia el diseño y ahora la tapa es de 70 mm.

1. Crea una **ECO** sobre la LdM de la conserva.
2. Cambia el componente en la revisión, revisa las diferencias contra la versión vigente.
3. Aprueba y aplica. Comprueba que las órdenes ya lanzadas mantienen la versión anterior.
4. Revisa el historial: quién pidió el cambio, quién lo aprobó y cuándo entró en vigor.

> **El argumento de venta:** en una empresa de alimentos, cambiar una fórmula sin control de versiones
> es un riesgo sanitario y legal. El PLM deja rastro de quién cambió qué y desde cuándo.

## 10. Errores frecuentes en la implantación de manufactura

| Error | Consecuencia |
|---|---|
| Usar kits para productos que sí se arman y almacenan | Sin stock del padre, sin costo de producción y sin trazabilidad |
| Configurar órdenes de trabajo sin necesidad real | Registro manual diario que el operario terminará saltándose |
| No declarar mermas en la LdM | El costo real siempre se desvía y nadie confía en el sistema |
| Olvidar el costo/hora del centro de trabajo | El costo real sale idéntico al teórico y la varianza no existe |
| Poner lote solo al producto terminado | La trazabilidad muere en el primer eslabón |
| Lanzar producción sin haber cuadrado el inventario | Los negativos de stock aparecen multiplicados |
