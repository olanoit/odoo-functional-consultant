# Cuaderno de ejemplos — Fase 4: Contabilidad y Finanzas

Casos prácticos para [`../../fases/fase-04-contabilidad-finanzas.md`](../../fases/fase-04-contabilidad-finanzas.md).
Trabaja sobre la base `LAB` con las ventas de la Fase 2, las compras y el inventario de la Fase 3.
**Aquí se cierra el mes de verdad**, no como ejercicio teórico.

> **Versión objetivo:** Odoo 20. Cuatro cambios recientes afectan todo lo que sepas de antes: desde
> v19 el **mapeo de impuestos de las posiciones fiscales** vive en el impuesto destino y el
> **inventario se contabiliza al facturar**; en v20 los **modelos de conciliación** recuperan
> `rule_type` con un significado nuevo (reglas de coincidencia) y el **informe de valoración** pasa al
> módulo `account` con sección de devengos. Detalle en
> [`guias/I5-campos-tecnicos-v20-contabilidad.md`](guias/I5-campos-tecnicos-v20-contabilidad.md).

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-cuentas.csv` | 25 cuentas con nomenclatura tipo PCGE peruano y su `account_type` |
| `datos/02-diarios.csv` | 7 diarios: facturas, boletas, compras, 2 bancos, caja y diversos |
| `datos/03-impuestos.csv` | IGV 18 % (venta/compra/incluido), exonerado, inafecto, gratuito |
| `datos/04-posiciones-fiscales.csv` | 4 posiciones (local, exonerado, inafecto, exportación) con el **mecanismo de mapeo vigente desde v19** |
| `datos/05-planes-analiticos.csv` | 2 planes: línea de negocio y canal de venta |
| `datos/06-cuentas-analiticas.csv` | 8 cuentas analíticas |
| `datos/07-extracto-bancario.csv` | **40 líneas** de extracto de agosto 2026 |
| `datos/08-modelos-conciliacion.csv` | 4 modelos de conciliación automática |
| `guias/I1` | **Laboratorio de asientos**: predice 12 asientos antes de ejecutarlos |
| `guias/I2` | Configuración fiscal e impuestos en v20 |
| `guias/I3` | Conciliación bancaria: 40 líneas en menos de 10 minutos |
| `guias/I4` | **Checklist de cierre mensual** + cuadre inventario ↔ contabilidad (entregables) |
| `guias/I5` | Chuleta de campos v20 de Contabilidad |
| `soluciones/` | Asientos resueltos y cuestionario |

## Antes de empezar

1. App **Contabilidad** instalada (en Community, *Facturación*; varias funciones son Enterprise).
2. Ejecuta el asistente de configuración contable: período fiscal, moneda, cuentas por defecto.
3. Multimoneda activada con la tasa **1 USD = 3.75 PEN**.
4. **Nivelación previa:** si no dominas partida doble, haz el Bloque 4.0 de la fase antes de seguir.
   Este cuaderno asume que sabes qué es debe, haber y devengado.

> **Codificación:** en el diálogo de importación elige **`utf-8`** a mano. Odoo adivina la
> codificación y con `02-diarios.csv`, `05-planes-analiticos.csv` y `06-cuentas-analiticas.csv` se equivoca (verificado en v20): se detectan como otra codificación y
> los acentos entran rotos sin ningún aviso. Detalle en la [Fase 1](../fase-01/README.md#antes-de-empezar).

---

## Ejemplo 1 — Plan de cuentas y diarios
*(Bloque 4.1 · 60 min)*

Importa `01-cuentas.csv` y `02-diarios.csv`.

> **El código de diario es único por compañía.** El diario *Operaciones diversas* del CSV usa el código
> **`OPDIV`**, no `MISC`: todo plan contable estándar (el genérico y el peruano) ya trae un diario `MISC`
> y el import fallaría entero con *«Journal codes must be unique per company»* — un solo código repetido
> tumba el archivo completo, no solo su fila. Antes de importar diarios en un cliente real, exporta los
> códigos existentes y compáralos.

Mira con atención la columna **`account_type`**: es lo que determina el comportamiento de la cuenta,
no el número. Ejercicio: explica por qué `4017 IGV crédito fiscal` está como `asset_current` y no
como `liability_current`, y qué pasaría si estuviera mal clasificada.

Luego, a mano:
1. **Condiciones de pago**: contado, 30 días, y **30/70** (30 % a 15 días, 70 % a 45 días).
   Se crean a mano porque las líneas deben sumar 100 % (ver guía I5, §10).
2. **Fechas de bloqueo**: prueba la global, la de declaración de impuestos y las de ventas/compras, y
   comprueba qué permite cada una. El **bloqueo permanente** no se puede deshacer: pruébalo solo en
   una copia de la base.
3. **Saldos de apertura**: un asiento en el diario *Operaciones diversas* que cuadre.

## Ejemplo 2 — Impuestos y posiciones fiscales
*(Bloque 4.2 · 90 min)*

Importa `03-impuestos.csv` y `04-posiciones-fiscales.csv`, y sigue
[`guias/I2-configuracion-fiscal.md`](guias/I2-configuracion-fiscal.md).

**Lo importante de este ejemplo:** desde v19 (y sigue así en v20), el impuesto *Exonerado* declara a
quién reemplaza (`original_tax_ids`) y en qué posición (`fiscal_position_ids`). El modelo
`account.fiscal.position.tax` de versiones anteriores **ya no existe**.

**La posición *Local Perú* no es decorativa:** la *Exportación* se detecta automáticamente sin país
(aplica a cualquier cliente con país), así que necesita una posición local con país Perú y
secuencia menor que la gane para los clientes peruanos. Es el mismo patrón que usa el plan contable
peruano (`LOCAL PERU` / `EXTRANJERO - EXPORTACIÓN`).

> **Con el plan contable peruano ya instalado (la base `LAB` tiene país Perú)**, esas dos posiciones
> existen antes de importar: *LOCAL PERÚ* (secuencia 10, país Perú) y *EXTRANJERO - EXPORTACIÓN*
> (secuencia 20, sin país). Verificado en v20: para un cliente peruano la detección automática elige
> *LOCAL PERÚ* (empata en secuencia con *Local Perú* y gana la que ya existía) y para un cliente
> extranjero, *EXTRANJERO - EXPORTACIÓN*; la *Exportación* del CSV (secuencia 40) nunca se aplica sola.
> Para que actúen las posiciones del CSV, **archiva las dos del plan** (o dale a las del CSV una
> secuencia menor). Es exactamente el tipo de duplicado que hay que detectar antes de un go-live.

**Prueba de fuego:** el mismo producto facturado a tres clientes con posiciones distintas produce
tres facturas distintas, sin tocar el producto.

**No olvides** configurar a mano las **líneas de repartición** de cada impuesto con las cuentas
4011 y 4017: sin eso, el reporte de impuestos no cuadra con el mayor.

## Ejemplo 3 — Laboratorio de asientos
*(Bloques 4.3, 4.4 y 4.8 · 120 min)* ← **el ejercicio central de la fase**

[`guias/I1-laboratorio-de-asientos.md`](guias/I1-laboratorio-de-asientos.md): 12 operaciones
(venta, entrega valorada, cobro, compra, recepción, pago, ajuste de inventario, depreciación,
comisión bancaria, factura en USD, diferencia de cambio, cierre de PdV) que debes **escribir a mano
antes** de ejecutarlas en Odoo.

Es el ejercicio que convierte "sé usar Odoo" en "entiendo qué hace Odoo con la contabilidad".

## Ejemplo 4 — Conciliación bancaria
*(Bloque 4.5 · 90 min)*

Importa `07-extracto-bancario.csv` (40 líneas, saldo neto S/ 8 401.85) y sigue
[`guias/I3-conciliacion-bancaria.md`](guias/I3-conciliacion-bancaria.md).

El extracto incluye a propósito **4 movimientos no identificados**: la realidad siempre los tiene, y
saber qué hacer con ellos es parte del trabajo.

Cronométrate antes y después de cargar los modelos de conciliación: esa diferencia es tu argumento
de venta cuando el cliente pregunte "¿y esto en qué me ahorra tiempo?".

## Ejemplo 5 — Analítica y rentabilidad
*(Bloque 4.6 · 60 min)*

1. Importa `05-planes-analiticos.csv` y `06-cuentas-analiticas.csv`: dos dimensiones
   (**línea de negocio** y **canal de venta**) que se aplican simultáneamente.
2. Configura **modelos de distribución analítica** para que se apliquen solos según el producto y el
   canal, en vez de que alguien los teclee factura por factura.
3. Aplica analítica a las ventas y compras del período.
4. Emite el reporte analítico: **¿qué línea de negocio deja más margen? ¿Qué canal?**
5. Crea un presupuesto por cuenta analítica y compara real vs. presupuestado.

> **Advertencia de consultor:** la analítica se configura **al inicio**, no cuando el gerente la pide.
> Sin distribución analítica en los apuntes históricos, no hay comparativo posible y hay que esperar
> un año entero.

## Ejemplo 6 — Activos y diferidos
*(Bloque 4.6 · 45 min · Enterprise)*

1. Compra de una **despulpadora industrial** por S/ 36 000 + IGV, depreciación lineal a 5 años.
   Genera el activo desde la factura y revisa el cuadro de depreciación.
2. Registra la depreciación del mes y busca su asiento.
3. **Gasto diferido:** seguro anual de S/ 12 000 pagado en agosto; reparte en 12 meses.
4. **Ingreso diferido:** cobro por adelantado de un alquiler de góndola anual.
5. Vende (o da de baja) el activo y analiza el asiento resultante.

## Ejemplo 7 — El cierre de mes
*(Bloque 4.7 · 120 min)* ← **el entregable de la fase**

Ejecuta el cierre completo de agosto de 2026 con
[`guias/I4-checklist-cierre-mensual.md`](guias/I4-checklist-cierre-mensual.md): 7 bloques,
30 controles y el **procedimiento de cuadre inventario ↔ contabilidad**.

Al terminar debes tener:
- Balance general y estado de resultados emitidos.
- Reporte de impuestos cuadrado con el mayor.
- Valor de inventario = saldo de la cuenta de existencias (o diferencias explicadas una por una),
  con el asiento de cierre de existencias y los devengos generados desde el informe de valoración.
- Fecha de bloqueo puesta.
- Respaldo del cierre.

## Ejemplo 8 — Reportes y tablero financiero
*(Bloque 4.7 · 45 min)*

1. Recorre los 8 reportes principales y aprende el motor: comparativos, filtros por analítica,
   desglose hasta el apunte, anotaciones y exportación.
2. Construye el **tablero financiero del gerente** con 6 indicadores: margen bruto, gastos por línea,
   antigüedad de cobros, días de cobro promedio, flujo de caja proyectado, rentabilidad por canal.
3. Documenta, para cada indicador, **de dónde sale el dato**. Un indicador que nadie puede reproducir
   no sirve para decidir.

---

## Cierre: entregables de la Fase 4

- [ ] Laboratorio de asientos ≥ 8/12 (Ejemplo 3).
- [ ] 40 líneas conciliadas en menos de 10 minutos (Ejemplo 4).
- [ ] **Entregable 1:** checklist de cierre mensual ejecutada y firmada.
- [ ] **Entregable 2:** procedimiento de cuadre inventario ↔ contabilidad, con las diferencias
      reales de tu base explicadas.
- [ ] Balance y estado de resultados de agosto emitidos y archivados.
- [ ] Explicación grabada (10 min) del flujo factura → cobro → conciliación, apta para un contador.
- [ ] Respaldo `LAB_fase04_AAAAMMDD.zip`.

## Lo que las fases siguientes necesitan de aquí

La Fase 5 (Manufactura) usa las cuentas y la valoración para calcular el **costo real de producción**;
la Fase 6 usa la **analítica** para la rentabilidad de proyectos; y la Fase 10 monta la localización
peruana sobre esta misma lógica fiscal. Si algo quedó sin cuadrar, se arrastra hasta el final.



---

## Para ampliar

### Cybrosys — libro de Odoo 19 y artículos

Enlaces verificados uno a uno. Todos están **en inglés**.

**Capítulos del [libro de Odoo 19](https://www.cybrosys.com/odoo/odoo-books/v19/)**: [Invoicing & Accounting](https://www.cybrosys.com/odoo/odoo-books/v19/invoicing-and-accounting/) · [· Reconciliation](https://www.cybrosys.com/odoo/odoo-books/v19/invoicing-and-accounting/reconciliation/) · [· Tax Returns](https://www.cybrosys.com/odoo/odoo-books/v19/invoicing-and-accounting/tax-returns/)

| Artículo | Para qué en esta fase | Fecha |
|---|---|---|
| [The Ultimate Guide to Journal Items and Entries in Odoo 19 Accounting](https://www.cybrosys.com/blog/the-ultimate-guide-to-journal-items-and-entries-in-odoo-19-accounting) | Apuntes y asientos — el laboratorio I1 | *may 2026* |
| [A Complete Guide to Inventory Valuation in Odoo 19](https://www.cybrosys.com/blog/a-complete-guide-to-inventory-valuation-in-odoo-19) | **Léelo antes del laboratorio I1**: explica por qué la recepción ya no genera asiento | *may 2026* |

### Odoo en Español — YouTube

[**Buscar «contabilidad conciliación» en el canal**](https://www.youtube.com/@OdooSpanish/search?query=contabilidad+conciliaci%C3%B3n) — vídeos en español sobre contabilidad, impuestos y conciliación.

> El canal no publica un índice enlazable por tema, así que el enlace abre la **búsqueda dentro del
> canal**: siempre devuelve lo que haya publicado sobre el tema, aunque renombre o reordene sus
> vídeos. El canal completo está en <https://www.youtube.com/@OdooSpanish>.

> **Úsalos para el concepto, no para la configuración.** Todo lo marcado con ⚠️ es de una versión
> anterior, y los artículos de v19 no recogen los cambios de v20 (reglas de coincidencia, informe de
> valoración con devengos, cierre de PdV con factura resumen): verifica contra la documentación 20.0,
> contra [la tabla de cambios de v20](../fase-12/README.md#los-cambios-de-v20-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
