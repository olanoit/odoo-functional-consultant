# Simulacro de certificación funcional — 60 preguntas

> **Formato del examen oficial:** ~120 preguntas · 90 minutos · mínimo 70 % para aprobar ·
> **respuesta incorrecta resta ½ punto**, no responder vale 0.
> Este simulacro tiene 60 preguntas: date **45 minutos**.
>
> Respuestas y explicaciones en [`respuestas.md`](respuestas.md). **No las mires antes de terminar.**
>
> Estrategia derivada de la penalización: responde solo si puedes descartar al menos la mitad de las
> opciones. Adivinar a ciegas entre 4 opciones tiene valor esperado negativo.

---

## Fundamentos (1–8)

**1.** Un usuario ve el menú de Ventas pero su lista de presupuestos aparece vacía, aunque hay
presupuestos creados. ¿Qué está pasando?
a) Le falta el grupo de Ventas b) Una regla de registro limita las filas que ve
c) Los presupuestos están archivados d) Necesita el modo desarrollador

**2.** ¿Para qué sirve el identificador externo (ID externo) al importar datos?
a) Para ordenar los registros b) Para que la importación actualice en vez de duplicar
c) Para traducir los nombres d) Para asignar permisos

**3.** En Odoo 19, un producto físico que se controla en inventario se configura como:
a) `type = product` b) `type = consu` con `is_storable = True`
c) `type = storable` d) `type = goods`

**4.** ¿Qué diferencia hay entre archivar y eliminar un registro?
a) Ninguna, son sinónimos b) Archivar lo oculta conservando historial; eliminar lo borra
c) Archivar solo funciona en contactos d) Eliminar requiere modo desarrollador

**5.** Al desinstalar un módulo:
a) Se conservan todos sus datos b) Se eliminan sus modelos, campos y datos propios
c) Solo se ocultan sus menús d) Se archivan sus registros

**6.** El chatter de un documento sirve principalmente para:
a) Chatear con otros usuarios b) Registrar la conversación y las actividades ligadas a ese registro
c) Enviar correos masivos d) Configurar permisos

**7.** ¿Cuál de estos es un motivo válido para elegir Odoo.sh sobre Odoo Online?
a) Necesitar Studio b) Necesitar módulos de terceros y entornos de prueba
c) Tener más de 10 usuarios d) Querer facturación electrónica

**8.** En una importación, la columna `country_id/id` con valor `base.pe` significa:
a) Que el país se llama base.pe b) Que se referencia el país por su ID externo
c) Que es un campo obligatorio d) Que se creará un país nuevo

## Ventas y CRM (9–18)

**9.** Un cliente pide 200 unidades, se entregan 120 y el producto tiene política *cantidades
entregadas*. Al facturar, la factura sale por:
a) 200 b) 120 c) 0 d) 80

**10.** En una lista de precios hay una regla global de −20 % y otra de producto con precio fijo de
S/ 10. Para ese producto, gana:
a) La que dé menor precio b) La regla de producto, por ser más específica
c) La global, por ser más antigua d) Depende de la cantidad

**11.** ¿Qué campo determina si una plantilla de cotización exige firma en línea?
a) `require_signature` b) `signature_required` c) `is_signed` d) `sign_ok`

**12.** En Odoo 19, los productos opcionales de una plantilla de cotización son:
a) Un modelo aparte (`sale.order.template.option`) b) Líneas de la plantilla con `is_optional = True`
c) Productos con `optional = True` d) No existen

**13.** El cierre de una sesión de punto de venta genera:
a) Una factura por cada ticket b) Un asiento contable resumen de la sesión
c) Nada, hasta que se facture d) Solo un reporte

**14.** ¿Qué es el MRR en Suscripciones?
a) El margen sobre ingreso recurrente b) El ingreso recurrente mensual normalizado
c) La tasa de renovación d) El costo de retención

**15.** Un pedido confirmado y facturado necesita una línea más. Lo correcto es:
a) Modificar la factura emitida b) Agregar la línea al pedido y generar factura adicional
c) Cancelar todo y rehacer d) No es posible

**16.** Las etapas del embudo de CRM en Odoo 19 se relacionan con los equipos mediante:
a) `team_id` (Many2one) b) `team_ids` (Many2many)
c) No se relacionan d) Un campo calculado

**17.** ¿Cuál es la diferencia entre un lead y una oportunidad?
a) Ninguna b) El lead es información sin calificar; la oportunidad es un negocio identificado
c) El lead es de marketing y la oportunidad de ventas d) El lead no tiene cliente asociado

**18.** Para que un descuento mayor al 20 % requiera aprobación del jefe, lo más adecuado es:
a) Desarrollo a medida b) Una regla de aprobación en Studio
c) Quitar el permiso de descuento d) Una lista de precios nueva

## Inventario y Compras (19–30)

**19.** En Odoo, un ajuste de inventario positivo genera un movimiento desde:
a) La nada b) La ubicación virtual de inventario (pérdidas/ganancias)
c) El proveedor d) La ubicación de producción

**20.** Una regla *pull* se dispara por:
a) Una llegada de mercancía b) Una necesidad en la ubicación de destino
c) El planificador nocturno d) Una orden de compra

**21.** Con recepción en 3 pasos, al confirmar una orden de compra se crea inicialmente:
a) Las 3 transferencias b) Solo la recepción (proveedor → entrada)
c) Solo el movimiento final d) Ninguna hasta recibir

**22.** Un producto tiene 1 500 unidades a mano y 3 000 reservadas. La regla de reordenamiento es
mín. 2 000 / máx. 10 000. Odoo propone comprar:
a) 8 500 b) 11 500 c) 10 000 d) 500

**23.** FEFO ordena la salida de mercancía por:
a) Fecha de entrada b) Fecha de caducidad c) Costo d) Ubicación

**24.** En Odoo 19, el modelo de lotes se llama:
a) `stock.production.lot` b) `stock.lot` c) `stock.serial` d) `product.lot`

**25.** En Odoo 19, con valoración perpetua (*Perpetual (at invoicing)*) y PEPS, **validar la
recepción** de la mercancía:
a) Debita valoración de existencias y acredita entrada de existencias
b) No genera ningún asiento: la contabilidad espera a la factura de compra
c) Debita gasto y acredita proveedores d) Genera el asiento solo si la categoría tiene diario de existencias

**26.** Los costos en destino (landed costs) se pueden distribuir por:
a) Solo por cantidad b) Cantidad, peso, volumen, valor o a partes iguales
c) Solo por valor d) Solo manualmente

**27.** El control de facturas de compra por "cantidades recibidas" implica:
a) Facturar todo lo pedido b) Facturar solo lo que efectivamente llegó
c) No poder facturar hasta cerrar la orden d) Facturar automáticamente

**28.** Una transferencia interna entre dos ubicaciones del mismo almacén:
a) Cambia el valor del inventario b) No cambia el valor total del inventario
c) Genera un asiento de gasto d) Requiere aprobación

**29.** ¿Qué método de costo recalcula el costo unitario de todo el stock en cada compra?
a) Estándar b) PEPS c) Promedio ponderado (AVCO) d) UEPS

**30.** En Odoo 19, la valoración de una categoría puede ser:
a) `manual_periodic` o `real_time` b) `periodic` o `real_time`
c) `manual` o `automatic` d) `fifo` o `average`

## Contabilidad (31–42)

**31.** ¿Qué determina si una cuenta arrastra saldo al ejercicio siguiente?
a) Su código b) Su tipo de cuenta (`account_type`) c) Su diario d) Su moneda

**32.** El bloqueo de fecha "para todos":
a) Impide registrar antes de esa fecha, incluso al administrador
b) Solo afecta a usuarios normales c) Solo afecta a facturas d) Es reversible sin permisos

**33.** Un cliente exonerado compra un producto gravado. La forma correcta de resolverlo es:
a) Cambiar el impuesto del producto b) Asignarle una posición fiscal
c) Editar el impuesto en cada factura d) Crear un producto duplicado

**34.** En Odoo 19, el mapeo de impuestos de una posición fiscal se define:
a) En líneas de la posición (`account.fiscal.position.tax`)
b) En el impuesto destino, con `original_tax_ids` y `fiscal_position_ids`
c) En el producto d) En el cliente

**35.** Al registrar un pago de cliente antes de conciliar el banco, el asiento acredita la cuenta
por cobrar y debita:
a) Directamente el banco b) Una cuenta transitoria de pagos pendientes
c) Ingresos d) Caja

**36.** Un modelo de conciliación sirve para:
a) Importar extractos b) Reconocer automáticamente líneas repetitivas y crear su contrapartida
c) Cerrar el período d) Generar reportes

**37.** La distribución analítica en Odoo permite:
a) Una sola cuenta analítica por apunte b) Repartir un apunte entre varias cuentas por porcentaje
c) Solo aplicarse a gastos d) Solo aplicarse manualmente

**38.** El valor del inventario no coincide con la cuenta contable de existencias. Causa **poco**
probable:
a) Recepciones sin factura b) Asientos manuales a la cuenta
c) Costos en destino sin aplicar d) Que el almacén tenga varias ubicaciones

**39.** La depreciación mensual de un activo genera:
a) Debe gasto de depreciación, haber depreciación acumulada
b) Debe activo, haber banco c) Debe gasto, haber proveedores d) No genera asiento

**40.** Una factura en USD cobrada cuando el tipo de cambio subió genera:
a) Nada b) Una diferencia de cambio realizada
c) Un ajuste de inventario d) Una nota de crédito

**41.** ¿Qué reporte muestra cuánto deben los clientes agrupado por antigüedad?
a) Balance general b) Antigüedad de saldos por cobrar
c) Libro mayor d) Estado de resultados

**42.** Un impuesto configurado como "incluido en el precio" implica que:
a) El precio mostrado ya contiene el impuesto b) El impuesto no se declara
c) Se calcula sobre el total d) No aparece en la factura

## Manufactura (43–48)

**43.** Una lista de materiales tipo **kit** (phantom):
a) Genera una orden de fabricación b) Reemplaza el producto por sus componentes en la entrega
c) Requiere centros de trabajo d) Solo funciona con un componente

**44.** El costo real de una orden de fabricación con órdenes de trabajo incluye:
a) Solo los materiales b) Materiales más el costo de los centros de trabajo por tiempo
c) Solo la mano de obra d) El precio de venta menos el margen

**45.** En subcontratación **con** envío de componentes:
a) El subcontratista compra los materiales b) Los componentes se envían y siguen siendo de la empresa
c) No hay control de stock d) No se puede trazar

**46.** Los componentes consumidos en una fabricación se mueven hacia:
a) La ubicación del cliente b) La ubicación virtual de producción
c) La chatarra d) El proveedor

**47.** Una ECO (orden de cambio de ingeniería) en PLM sirve para:
a) Cancelar órdenes b) Versionar y aprobar cambios en listas de materiales u operaciones
c) Calcular costos d) Planificar la capacidad

**48.** El MPS (programa maestro de producción) se usa cuando:
a) Se fabrica solo bajo pedido b) Hay demanda prevista que planificar por período
c) No hay stock d) Se subcontrata todo

## Servicios y RR. HH. (49–54)

**49.** Para que la rentabilidad de un proyecto sea real, es imprescindible:
a) Facturar por hitos b) Cargar el costo por hora de los empleados
c) Usar el portal del cliente d) Tener tareas con fecha límite

**50.** El campo `service_tracking` de un producto de servicio define:
a) Su precio b) Qué crea al confirmar la venta (tarea, proyecto o nada)
c) Su impuesto d) Su unidad de medida

**51.** Una política SLA vencida en la mesa de ayuda:
a) Cierra el ticket b) Marca el incumplimiento y aparece en el reporte
c) Reasigna el ticket automáticamente d) Notifica al cliente

**52.** Diferencia entre asistencia y hoja de horas:
a) Son lo mismo b) Asistencia registra cuándo estuvo; la hoja de horas, en qué trabajó
c) La asistencia es para obreros d) La hoja de horas no se puede facturar

**53.** En Odoo 19, los datos laborales del empleado (salario, horario, fechas de contrato) viven en:
a) `hr.contract` b) `hr.version` c) `hr.employee` directamente d) `hr.job`

**54.** Una asignación de ausencias por acumulación (accrual):
a) Da todos los días de golpe b) Devenga días según el período trabajado
c) No requiere configuración d) Solo aplica a vacaciones

## Web, Studio y datos (55–60)

**55.** La categoría que determina cómo navega el comprador en la tienda en línea es:
a) `categ_id` b) `public_categ_ids` c) `product_tag_ids` d) `pos_categ_id`

**56.** Un carrito de compra en la tienda en línea:
a) Reserva el stock inmediatamente b) No reserva; la reserva ocurre al confirmar el pedido
c) Descuenta el inventario d) Genera una factura

**57.** Una automatización de marketing sin condición de salida:
a) Se detiene sola b) Puede mantener contactos recibiendo mensajes indefinidamente
c) No se puede guardar d) Solo envía un mensaje

**58.** El primer paso ante un requerimiento que el estándar no cubre es:
a) Cotizar desarrollo b) Preguntarse si el requerimiento es real o costumbre del proceso anterior
c) Buscar un módulo de terceros d) Usar Studio

**59.** Al importar productos con variantes en Odoo 19 se puede usar la columna:
a) `attribute_line_ids` b) `import_attribute_values` con formato `Atributo:Valor`
c) `variant_ids` d) No se pueden importar variantes

**60.** La validación de una migración de datos se demuestra con:
a) Revisar visualmente algunos registros b) Sumas de control (conteos e importes) contra el origen
c) Confiar en que Odoo no dio error d) El número de filas del archivo
