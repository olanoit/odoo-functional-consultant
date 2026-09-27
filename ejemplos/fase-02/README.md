# Cuaderno de ejemplos — Fase 2: Ventas y CRM

Casos prácticos ejecutables para [`../../fases/fase-02-ventas-crm.md`](../../fases/fase-02-ventas-crm.md).
Continúa sobre la base `LAB` que dejaste lista en la [Fase 1](../fase-01/README.md): los 25 clientes
y los 79 productos de ANDINA GOURMET son la materia prima de todo lo que sigue.

> **Versión objetivo:** Odoo 20 (20.0). Campos verificados contra el código fuente
> ([`guias/G5-campos-tecnicos-v20-ventas.md`](guias/G5-campos-tecnicos-v20-ventas.md)).
> Desde v19 las etapas de CRM se comparten entre equipos (`team_ids` es Many2many), los productos
> opcionales de una plantilla de cotización son líneas normales (en v20, las de una sección con
> `is_optional`) y existe un mecanismo para **importar variantes**. En v20 se suman tres cambios más que rompen material de v19: las reglas
> de lista de precios pasan a ser **Descuento / Recargo / Precio fijo** (`percent_price` y el tipo
> *Fórmula* desaparecen), `require_payment` ya no existe (el pago en línea se exige cuando el
> porcentaje de anticipo es mayor que cero) y el cierre del PdV emite una **factura resumen**.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-equipos-ventas.csv` | 3 equipos: Mayorista B2B, Tienda Retail, Canal Online |
| `datos/02-etapas-crm.csv` | 5 etapas del embudo, con **criterio de avance escrito** y días de estancamiento |
| `datos/03-motivos-perdida.csv` | 6 motivos de pérdida reales del negocio |
| `datos/04-etiquetas-crm.csv` | 6 etiquetas de oportunidad |
| `datos/05-oportunidades.csv` | 20 oportunidades repartidas por etapa, equipo y valor |
| `datos/06-listas-precios.csv` | 4 listas: Mayorista, Exportación USD, Promoción, Tienda |
| `datos/07-reglas-precios.csv` | 8 reglas: global, por categoría, escalonadas, precio fijo y con vigencia |
| `datos/08-plantilla-cotizacion.csv` | 2 plantillas con secciones, notas y **productos opcionales** |
| `datos/09-variantes.csv` | 7 filas que crean 2 productos con variantes (atributos incluidos) |
| `datos/10-pedidos-borrador.csv` | 12 pedidos para poblar los reportes comerciales |
| `guias/G1` | Diseño del embudo: criterio de avance por etapa y reglas del juego |
| `guias/G2` | **Laboratorio de listas de precios**: 18 casos a predecir antes de probar |
| `guias/G3` | Políticas de facturación: 6 escenarios con su resultado esperado |
| `guias/G4` | Guion de la demo comercial de 15 minutos (entregable D de la fase) |
| `guias/G5` | Chuleta de campos técnicos de Ventas/CRM en v20 |
| `soluciones/` | Respuestas del laboratorio de precios y del cuestionario |

## Antes de empezar

1. Base `LAB` con la Fase 1 terminada (respaldo `LAB_fase01` restaurado si hiciste otras pruebas).
2. Apps instaladas: **CRM**, **Ventas**, **Inventario**, **Compras**, **Contactos**.
3. En *Ventas → Configuración → Ajustes*, activa: **Listas de precios**, **Descuentos**,
   **Variantes** y **Unidades y embalajes**. Las plantillas de cotización no tienen ajuste:
   vienen activas con la app Ventas (*Ventas → Configuración → Plantillas de cotización*).
4. En *Ajustes → Configuración general*, activa **Múltiples monedas** y crea la tasa
   **1 USD = 3.75 PEN** (fecha de hoy). Sin esa tasa, la lista de exportación no calcula.

> **Sobre las fechas:** los datos usan el segundo semestre de **2026**. Si estudias en otro año,
> abre los CSV y desplaza el año — o acepta ver las oportunidades como vencidas, que también
> es un escenario didáctico (así se ve un embudo mal mantenido).

> **Codificación:** en el diálogo de importación elige **`utf-8`** a mano. Odoo adivina la
> codificación y con `02-etapas-crm.csv` se equivoca (verificado en v20): se detecta como otra codificación y
> los acentos entran rotos sin ningún aviso. Detalle en la [Fase 1](../fase-01/README.md#antes-de-empezar).

---

## Ejemplo 1 — Montar el embudo comercial
*(Bloque 2.1 · 60 min)*

**Orden de carga:**
```
01-equipos-ventas.csv → 02-etapas-crm.csv → 03-motivos-perdida.csv → 04-etiquetas-crm.csv → 05-oportunidades.csv
```

Cosas que mirar mientras importas:

**Equipos** (`crm.team`). Fíjate en `use_leads`: el equipo B2B y el Online usan **leads** (hay que
calificar antes de crear oportunidad); Retail no (todo entra directo como oportunidad).
Esa decisión no es técnica: depende de cuánta basura entra por el canal.

**Etapas** (`crm.stage`). La columna `requirements` es el **criterio de avance** — se ve como tooltip
sobre el nombre de la etapa en el kanban. Es la diferencia entre un embudo que sirve y uno decorativo:
sin criterio escrito, cada vendedor mueve las tarjetas con su propio criterio y el pronóstico miente.

La columna `rotting_threshold_days` (existe desde v19; en la interfaz, *Días hasta la inactividad*) marca en el kanban las oportunidades que llevan
demasiados días sin moverse. Configuramos 15 días en *Nuevo* y 10 en *Negociación*: una negociación
parada 10 días está muerta y hay que saberlo.

> **Desde v19** las etapas ya no pertenecen a un equipo (`team_id`), sino que se comparten
> (`team_ids`, Many2many). Dejamos la columna vacía a propósito → las 5 etapas quedan disponibles
> para todos los equipos. Si un equipo necesitara un embudo distinto, se asignan ahí.
>
> **Novedad de v20:** el kanban del flujo trae un **selector de equipo** junto a la ruta de navegación
> (aparece cuando hay al menos 2 equipos con flujo). Al elegir un equipo se ven sus oportunidades, las
> que no tienen equipo, y solo las etapas de ese equipo más las compartidas.
>
> **Ojo con las etapas de fábrica:** la app CRM ya trae 4 etapas compartidas (*Nuevo*, *Calificado*,
> *Propuesta*, *Ganado*), y el CSV no las reemplaza: crea las suyas con otro ID externo. Tras importar,
> el kanban muestra **9 columnas**, tres con el nombre repetido (verificado en v20). Elimina las 4 de
> fábrica —no tienen oportunidades— para quedarte con el embudo de 5 etapas que diseñaste: las etapas
> de CRM **no se pueden archivar** (en v20 `crm.stage` no tiene campo *Activo*); si prefieres no
> borrarlas, pliégalas (`fold`) para que no estorben en el kanban.

**Oportunidades** (`crm.lead`). Observa que traen `expected_revenue`, `probability` y `date_deadline`:
son las tres columnas de las que vive el **pronóstico**. `priority` es la estrella (0–3).

**Verificaciones:**
1. Kanban del equipo B2B (elígelo en el selector de equipo) agrupado por etapa: **12 oportunidades** que suman **S/ 810 700** de ingreso
   esperado (S/ 310 000 ponderado por probabilidad). El embudo completo son 20 oportunidades y S/ 906 200.
2. Reporte de **previsión**: en septiembre vencen 8 cierres por S/ 167 300 (S/ 106 985 ponderados).
   ¿Coincide tu lectura del reporte con esos números?
3. Cambia la probabilidad de una oportunidad y observa cómo cambia el ingreso prorrateado.

**Rompe a propósito:** mueve una oportunidad a *Ganado* sin actividad programada ni cotización asociada.
Pregúntate qué pasó con el pronóstico y quién se dará cuenta. Después, revisa cuántas de las 20
oportunidades importadas **no tienen actividad siguiente**: esa lista es el verdadero estado del embudo.

---

## Ejemplo 2 — Perder bien
*(Bloque 2.1 · 20 min)*

1. Marca como perdidas 6 oportunidades, una con cada motivo del archivo 03.
2. Filtra por **Perdidas** y agrupa por **Motivo de pérdida**.
3. Reactiva una (*Restaurar*) y observa qué pasa con la probabilidad y la etapa.

**La pregunta de consultor:** si el 40 % de tus pérdidas son *"Precio por encima de la competencia"*,
¿es un problema de precios, de segmentación de clientes o de argumentación del vendedor?
Odoo te da el dato; el análisis lo pones tú. Anótalo en la bitácora: es material de demo.

---

## Ejemplo 3 — Listas de precios: el laboratorio
*(Bloque 2.3 · 90 min)* ← **el ejercicio central de esta fase**

Importa `06-listas-precios.csv` y luego `07-reglas-precios.csv`.

Las 4 listas modelan situaciones reales distintas:

| Lista | Moneda | Qué modela |
|---|---|---|
| **Mayorista B2B** | PEN | Descuento base 15 %, escalonado por volumen en conservas (22 % desde 100, 28 % desde 500) y snacks (25 % desde 200), más un **precio fijo negociado** de S/ 8.50 para la conserva estrella desde 1 000 unidades |
| **Exportación USD** | USD | 5 % de descuento y conversión automática por tipo de cambio |
| **Promoción Fin de Año** | PEN | 20 % en snacks y 15 % en bebidas, **solo del 1 al 31 de diciembre de 2026** |
| **Tienda / Público** | PEN | Sin reglas: precio de lista tal cual |

Ahora ve a [`guias/G2-laboratorio-listas-de-precios.md`](guias/G2-laboratorio-listas-de-precios.md):
**predice el precio de los 18 casos antes de abrir Odoo**, anótalo, y solo después comprueba.
Las respuestas están en [`soluciones/respuestas-laboratorio-precios.md`](soluciones/respuestas-laboratorio-precios.md).

Si aciertas menos de 14 de 18, no has entendido la precedencia de reglas — y ese es el motivo #1
por el que un cliente dice *"Odoo me pone mal los precios"*.

**Asignación al cliente:** pon *Mayorista B2B* como lista de los clientes con etiqueta *Mayorista*,
y *Tienda / Público* al resto. Comprueba en una cotización que el precio sale solo.

---

## Ejemplo 4 — Variantes de producto (y cómo importarlas)
*(Bloque 2.3 · 40 min)*

Importa `09-variantes.csv` sobre el modelo **Productos**.

Este archivo usa un mecanismo que existe desde Odoo 19 y sigue igual en v20: la columna **`import_attribute_values`** con el
formato `Atributo:Valor` (varios separados por coma). Al importar:

- Las filas con el **mismo `name`** se agrupan en **una sola plantilla de producto**.
- Los atributos y valores que no existan **se crean solos**: aquí, **Presentación** y **Sabor**.
  **Tamaño** no se crea: el módulo `product` ya trae ese atributo (*Size* / *Tamaño*, junto con
  *Marca*, *Color*, *Material* y *Patrón*) y el importador lo reutiliza por nombre, añadiéndole los
  valores *Pequeña*, *Mediana* y *Grande*.
- Cada fila se convierte en una **variante** con su propia referencia, coste **y precio de venta**:
  en v20 el precio de venta de la variante (`lst_price`) se guarda en la propia variante, así que
  la canasta queda a 45.00 / 78.00 / 135.00 y el pack a 4.50 / 4.20 / 7.88 / 7.35, tal como vienen
  en el archivo. El `list_price` de la **plantilla** se queda con el de la última fila del grupo
  (135.00 y 7.35), y el **precio extra** de cada variante es la diferencia entre ambos.

Resultado esperado: 2 plantillas — *Canasta Andina de Regalo* (3 variantes por tamaño) y
*Pack Degustación Snacks* (4 variantes: 2 presentaciones × 2 sabores).

**Verificaciones:**
1. Abre *Canasta Andina de Regalo* → pestaña **Atributos y variantes** → botón *Variantes*: 3.
2. Cotiza una *Canasta Pequeña* y una *Canasta Grande* con la lista *Tienda / Público*: deben salir a
   S/ 45.00 y S/ 135.00, el precio de cada fila del archivo. Con la lista *Mayorista B2B* salen con el
   15 % de descuento aplicado sobre el precio de **cada variante**.
3. Revisa *Ventas → Configuración → Atributos*: los atributos creados por la importación
   (*Presentación* y *Sabor*) quedaron como **"Creación de variantes: De forma dinámica"**; *Tamaño*,
   que ya existía, sigue **"Al instante"**. Entiende qué significa y cuándo cambiar uno por otro.

**La pregunta que decide el diseño:** ¿variantes o productos separados?
Regla práctica: variantes cuando comparten descripción, imagen y proceso de venta y solo cambia un
atributo; productos separados cuando tienen costo, proveedor o proceso de producción distinto.
Equivocarse aquí se paga en la Fase 3 (inventario) y en la Fase 8 (tienda en línea).

---

## Ejemplo 5 — Plantillas de cotización con opcionales
*(Bloque 2.2 · 45 min)*

Importa `08-plantilla-cotizacion.csv` en *Ventas → Configuración → Plantillas de cotización*.

`andina.sot_distribuidor` (*Kit de arranque distribuidor*) trae:
- **Secciones** (`display_type = line_section`): agrupan visualmente la cotización.
- **Una nota** (`line_note`) visible para el cliente.
- **Una sección de opcionales** (la sección *OPCIONALES* con `is_optional = True`) con 3 productos:
  flete, góndola y asesoría, **con cantidad 0**. **No suman al total** hasta que el cliente los agrega
  desde el portal y elige la cantidad.
- `require_signature` y `prepayment_percent = 0.30`: firma en línea y **30 % de anticipo**.
  En v20 el campo `require_payment` ya no existe: el pago en línea se exige cuando el anticipo es
  mayor que cero, y la plantilla *Pack degustación retail* (anticipo 0) no pide pago.
- `number_of_days = 15`: validez de la oferta.

> **Desde v19** los opcionales ya no viven en un modelo aparte (`sale.order.template.option`):
> son líneas normales. **En v20 lo opcional es la sección:** `is_optional` se marca en la línea de
> sección y vuelve opcionales en el portal todos los productos que cuelgan de ella; esos productos van
> con cantidad 0 para no sumar al total. Un producto con `is_optional = True` fuera de una sección
> opcional **suma al total como cualquier otro** y el cliente no puede quitarlo (verificado en v20).
> Además, las líneas de plantilla admiten atributos configurables y cantidad por sección.

**Ejecuta el flujo completo** con *Distribuidora Sol de Oro S.A.C.*:
1. Nueva cotización → aplicar la plantilla → verificar que el precio sale de la lista Mayorista.
2. Enviar por correo → abrir el **portal del cliente** desde el enlace del chatter.
3. Como cliente: agregar el flete opcional, **firmar** y **pagar el 30 %**
   (proveedor de pago en modo de prueba, o transferencia bancaria).
4. Como vendedor: ver la cotización convertida en pedido y el anticipo registrado.

**Rompe a propósito:** intenta enviar la cotización a un cliente sin correo. Y modifica el precio de
una línea después de que el cliente firmó. Anota qué permite Odoo y qué no.

---

## Ejemplo 6 — Facturar lo pedido vs. lo entregado
*(Bloque 2.4 · 60 min)* ← **el concepto que más problemas causa en producción**

Sigue [`guias/G3-politicas-de-facturacion.md`](guias/G3-politicas-de-facturacion.md): 6 escenarios
con entregas parciales, anticipos y devoluciones, cada uno con el resultado que **debe** dar.

Resumen del concepto, para tu bitácora:

| Política | Cuándo facturar | Riesgo si eliges mal |
|---|---|---|
| **Cantidades pedidas** | Al confirmar el pedido | Facturas lo que aún no entregaste: el cliente reclama y el almacén queda descuadrado |
| **Cantidades entregadas** | Después de la entrega | Si el almacén no registra a tiempo, no se puede facturar y se retrasa la cobranza |

La decisión es **por producto**, no global. En ANDINA GOURMET: los bienes van por *entregadas*
(hay riesgo de faltantes y lotes), los servicios por *pedidas* (no hay entrega física).

---

## Ejemplo 7 — Poblar y leer los reportes comerciales
*(Bloque 2.7 · 45 min)*

Importa `10-pedidos-borrador.csv`: 12 pedidos repartidos entre junio y agosto de 2026, con distintas
listas de precios y equipos.

> **Verificación importante al importar:** el archivo **no trae precios**, a propósito.
> Odoo debe calcularlos con la lista de precios de cada pedido. Abre `andina.so_010`
> (1 200 conservas de aguaymanto para Piura): el precio unitario debe ser **S/ 8.50**, el precio fijo
> negociado. Si aparece 12.50 o 0.00, la lista de precios no se aplicó — asigna la lista
> *Mayorista B2B* al pedido: en v20 cambiar la lista **recalcula al instante** los precios de todas
> las líneas (el botón *Actualizar precios* de v19 desapareció).

Confirma al menos 8 de los 12 pedidos (los reportes de ventas solo cuentan pedidos confirmados)
y responde con la interfaz:

> **Ojo con la fecha al confirmar:** en v20 (como antes) confirmar un pedido reescribe su *Fecha de
> la orden* con la fecha y hora actuales, así que los 12 pedidos pasan al mes en curso y la pregunta 1
> deja de tener sentido. Para recuperar las fechas del archivo, **vuelve a importar
> `10-pedidos-borrador.csv` dejando sin importar todas las columnas salvo `id` y `date_order`**
> (en el diálogo, *No importar* en las demás): el ID externo actualiza la fecha sin duplicar líneas
> (verificado en v20).

1. ¿Cuál fue el mes de mayor venta y por cuánto?
2. ¿Qué equipo vendió más y cuál tiene el **ticket promedio** más alto?
3. ¿Cuáles son los 5 productos más vendidos por importe? ¿Y por cantidad? ¿Por qué no coinciden?
4. ¿Qué cliente concentra más facturación? ¿Qué riesgo de negocio implica eso?
5. Construye el **tablero del gerente comercial** con 5 indicadores y guárdalo como favorito.

---

## Ejemplo 8 — Punto de Venta de la tienda de Lima
*(Bloque 2.5 · 60 min · configuración manual, sin CSV)*

El PdV se configura a mano porque casi todo son opciones de sesión y hardware:

1. **Configuración:** PdV *Tienda Lima*, lista de precios *Tienda / Público*, métodos de pago
   **Efectivo** y **Tarjeta**, categorías de producto visibles en pantalla.
2. **Sesión:** abre con S/ 200 de fondo de caja. Registra:
   - 6 ventas en efectivo,
   - 3 con tarjeta,
   - 1 con pago mixto,
   - 1 devolución de un producto vendido antes.
3. Aplica un descuento manual en un ticket y observa cómo se refleja.
4. **Cierra la sesión** declarando un efectivo **distinto** al teórico (por ejemplo S/ 10 menos):
   ese es el momento que más quejas genera en tienda. Anota qué muestra Odoo y dónde queda la diferencia
   (pista: una línea de corrección en el extracto de caja, contra la cuenta de pérdidas del diario de efectivo).
5. Busca la contabilización que generó el cierre. En v20 no es un asiento suelto: es una **factura
   resumen** al *Cliente por defecto* del PdV en su *Diario de cierre* (y una nota de crédito aparte
   por la devolución). Por defecto el PdV la genera **cada día a las 04:00** aunque la sesión siga
   abierta. Aún no hace falta entenderla del todo — la desarmarás en la Fase 4 —, pero localízala hoy.

**Para la bitácora:** ¿qué pasa si se cae internet a mitad de sesión? Pruébalo desconectando la red
del navegador unos minutos y siguiendo con las ventas.

---

## Ejemplo 9 — Suscripciones (Enterprise)
*(Bloque 2.6 · 45 min · requiere Odoo Enterprise)*

ANDINA GOURMET quiere vender una **caja mensual de suscripción**.

1. Crea un **plan de suscripción** mensual (facturación recurrente cada 1 mes, con renovación automática)
   y otro anual con 2 meses de descuento.
2. Crea el producto *Caja Andina Mensual* (S/ 89.00) asociado al plan.
3. Da de alta 3 suscriptores entre tus clientes retail y confirma sus suscripciones.
4. Ejecuta una **renovación** y un **cambio de plan** (mensual → anual).
5. Cancela una y observa el efecto en el reporte.
6. Lee el tablero: **MRR**, tasa de cancelación, ingreso recurrente por cliente.

**Si trabajas en Community:** no podrás hacerlo. Igual debes saber explicar qué es el MRR y por qué
un cliente de suscripciones lo pide desde el primer día — es pregunta de preventa y de certificación.

---

## Cierre: entregables de la Fase 2

- [ ] Embudo con criterio de avance escrito y 20 oportunidades vivas (Ejemplos 1 y 2).
- [ ] 3 listas de precios funcionando y verificadas con los 18 casos (Ejemplo 3).
- [ ] Flujo completo cotización → firma → anticipo → pedido (Ejemplo 5).
- [ ] Los 6 escenarios de facturación resueltos (Ejemplo 6).
- [ ] PdV con sesión cerrada y arqueo con diferencia explicada (Ejemplo 8).
- [ ] Tablero comercial guardado (Ejemplo 7).
- [ ] **Entregable C:** *"Proceso comercial TO-BE de ANDINA GOURMET"* con
      [`../../plantillas/02-mapa-de-procesos-bpd.md`](../../plantillas/02-mapa-de-procesos-bpd.md).
- [ ] **Entregable D:** demo de 15 minutos con [`guias/G4-guion-demo-comercial.md`](guias/G4-guion-demo-comercial.md).
- [ ] Respaldo `LAB_fase02_AAAAMMDD.zip`.

## Lo que la Fase 3 va a necesitar de aquí

Los 12 pedidos confirmados generarán **entregas pendientes**. No las valides todavía: en la Fase 3
las usarás para estudiar reservas, entregas parciales y rutas multi-etapa. Ese "desorden" es
intencional y es exactamente lo que encontrarás en un cliente real.



---

## Para ampliar

### Cybrosys — libro de Odoo 19 y artículos

Enlaces verificados uno a uno. Todos están **en inglés**.

**Capítulos del [libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)**: [CRM](https://www.cybrosys.com/odoo/odoo-books/v19/crm/) · [Sales](https://www.cybrosys.com/odoo/odoo-books/v19/sales/)

| Artículo | Para qué en esta fase | Fecha |
|---|---|---|
| [How to Configure & Optimize Pricelists in Odoo 19](https://www.cybrosys.com/blog/how-to-configure-and-optimize-pricelists-in-odoo-19) | Reglas de precio por producto, categoría, cantidad y fecha — el laboratorio G2 | *nov 2025* |
| [How to Design Professional Quotation Templates in Odoo 19](https://www.cybrosys.com/blog/how-to-design-professional-quotation-templates-in-odoo-19) | Plantillas de cotización, el archivo `08-plantilla-cotizacion.csv` | *dic 2025* |

### Odoo en Español — YouTube

[**Buscar «lista de precios ventas» en el canal**](https://www.youtube.com/@OdooSpanish/search?query=lista+de+precios+ventas) — vídeos en español sobre el embudo de CRM y las listas de precios.

> El canal no publica un índice enlazable por tema, así que el enlace abre la **búsqueda dentro del
> canal**: siempre devuelve lo que haya publicado sobre el tema, aunque renombre o reordene sus
> vídeos. El canal completo está en <https://www.youtube.com/@OdooSpanish>.

> **Úsalos para el concepto, no para la configuración.** Todo lo marcado con ⚠️ es de una versión
> anterior, y los artículos de Cybrosys son de v19: contrasta los nombres de campo contra
> la documentación 20.0, contra [la tabla de cambios de v20](../fase-12/README.md#los-cambios-de-v20-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
