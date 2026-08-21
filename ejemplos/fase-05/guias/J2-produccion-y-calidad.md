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
configurados con ruta de **fabricación**:

1. Odoo crea la orden de la conserva (en espera de componentes).
2. Crea las órdenes de fabricación de **pulpa** y **almíbar**.
3. Si tampoco hay aguaymanto, dispara la **compra** (si el insumo tiene regla o ruta de compra).

**Ejercicio:** ejecútalo y dibuja la cadena completa de documentos. Después responde:
¿en qué orden hay que terminarlas? ¿Qué pasa si terminas la conserva antes que la pulpa?

## 3. Consumo flexible y mermas

En la LdM, `consumption` controla si el operario puede consumir **más o menos** de lo previsto:
`strict` (bloquea), `warning` (avisa) o `flexible` (permite).

**Ejercicio:** configura `warning`, consume 260 kg de pulpa en vez de 240 y observa el aviso y el
efecto en el costo real. Anota qué le dirías a un jefe de planta que pide `flexible` "para no perder
tiempo": qué gana y qué pierde.

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
| **Desecho** | Desechar 15 unidades durante la orden | Ubicación virtual de chatarra y su asiento |
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

1. Registra la **línea de envasado** como equipo, con responsable, criticidad y fecha de compra.
2. Crea un mantenimiento **preventivo** cada 500 horas de uso o cada 3 meses.
3. Genera una solicitud **correctiva** desde el taller (la selladora falla a mitad de una orden).
4. Observa el efecto en la planificación del centro de trabajo mientras el equipo está en mantenimiento.
5. Revisa los indicadores MTBF y MTTR y explica qué decisión de negocio dispara cada uno.

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
