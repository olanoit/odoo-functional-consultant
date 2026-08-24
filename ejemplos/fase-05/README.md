# Cuaderno de ejemplos — Fase 5: Manufactura, Calidad y Mantenimiento

Casos prácticos para [`../../fases/fase-05-manufactura-calidad.md`](../../fases/fase-05-manufactura-calidad.md).
Usa los insumos y envases cargados en la Fase 1, el inventario de la Fase 3 y las cuentas de la Fase 4.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-productos-produccion.csv` | 3 semielaborados con ruta de fabricación y lote, más un kit |
| `datos/02-centros-trabajo.csv` | 5 centros con costo/hora, tiempos de preparación y limpieza, OEE |
| `datos/03-listas-materiales.csv` | 4 LdM: pulpa, almíbar, conserva (3 niveles) y un **kit** |
| `guias/J1` | **Laboratorio de costeo**: calcula el costo real antes que Odoo |
| `guias/J2` | Producción, subcontratación, calidad, mantenimiento y PLM |
| `soluciones/` | Costeo resuelto con el análisis de negocio |

> **IDs externos de esta fase:** `01-productos-produccion.csv` crea plantilla (`andina.prod_sem_*`,
> `andina.prod_kit_navidad`) **y** variante (`andina.var_sem_*`, `andina.var_kit_navidad`) mediante la
> columna `product_variant_ids/id`. En `03-listas-materiales.csv`, `product_tmpl_id/id` usa el ID de
> **plantilla** y `bom_line_ids/product_id/id` el de **variante**: no son intercambiables.

## Antes de empezar

Apps: **Fabricación** (y en Enterprise, **Calidad**, **Mantenimiento** y **PLM**).
En *Fabricación → Configuración* activa: **Órdenes de trabajo**, **Listas de materiales multinivel**,
**Subcontratación**, **Programa maestro de producción** y **Lotes/series**.

---

## Ejemplo 1 — La estructura de producto
*(Bloque 5.1 · 60 min)*

Importa en orden: `01-productos-produccion.csv` → `02-centros-trabajo.csv` → `03-listas-materiales.csv`.

El archivo de LdM usa el patrón de **filas de continuación**: la primera fila lleva los datos de la
lista y la primera línea de componente y de operación; las siguientes solo las líneas hijas.
Es la forma de importar One2many anidados en un único archivo.

**Verificaciones:**
1. La LdM de la conserva tiene 7 componentes y 2 operaciones.
2. La pulpa y el almíbar tienen su propia LdM → estructura de **3 niveles**.
3. El Kit Navideño es de tipo **kit (phantom)**: comprueba que no genera orden de fabricación.
4. Abre el reporte **Estructura y costo** de la conserva y compáralo con tu cálculo de J1.

## Ejemplo 2 — Laboratorio de costeo
*(Bloque 5.3 · 90 min)* ← **el ejercicio central**

[`guias/J1-laboratorio-de-costeo.md`](guias/J1-laboratorio-de-costeo.md): calcula a mano el costo de
la pulpa, del almíbar y de la conserva, incluyendo tiempos de preparación y limpieza.

Anticipo del hallazgo: el costo real es **S/ 5.50** frente al estándar de **S/ 6.80** que la empresa
venía usando. Estaba subestimando su margen en S/ 1.30 por unidad. Ese tipo de número es lo que
convierte una implementación en un proyecto que el gerente defiende.

## Ejemplo 3 — Fabricar de verdad
*(Bloque 5.2 · 90 min)*

Sigue [`guias/J2-produccion-y-calidad.md`](guias/J2-produccion-y-calidad.md), secciones 1 a 5:
producción con y sin órdenes de trabajo, cadena multinivel, consumo flexible y mermas, lotes,
desecho, sobreproducción y desmontaje.

**El ejercicio que más enseña:** lanza 1 000 conservas sin stock de pulpa ni almíbar y dibuja la
cadena completa de documentos que Odoo genera solo.

## Ejemplo 4 — Costo real vs. teórico
*(Bloque 5.3 · 45 min)*

Dos órdenes idénticas, una perfecta y otra con desviaciones (20 kg de merma de pulpa, 60 minutos
extra de envasado, 15 unidades desechadas). Produce el **análisis de varianza**: cuánto se desvió
por material, cuánto por tiempo y cuánto por desecho.

Escribe el asiento contable de la orden **antes** de mirarlo en Odoo.

## Ejemplo 5 — Planificación
*(Bloque 5.4 · 45 min)*

1. Configura plazos de fabricación y planifica **hacia atrás** desde una fecha de entrega comprometida.
2. Usa el **MPS** con una demanda prevista de 4 000 conservas mensuales y compáralo con las reglas
   de reordenamiento de la Fase 3: ¿cuándo conviene cada uno?
3. Provoca un cuello de botella: dos órdenes que necesitan la línea de envasado el mismo día.
   Míralo en la vista de planificación de centros de trabajo.

## Ejemplo 6 — Subcontratación
*(Bloque 5.5 · 45 min)*

Guía J2, sección 6: etiquetado tercerizado con y sin envío de componentes.
La pregunta que debes poder responder: **¿de quién es la mercancía mientras está en la planta del
subcontratista?** Tiene consecuencias contables y de seguro.

## Ejemplo 7 — Calidad, mantenimiento y PLM
*(Bloques 5.6 y 5.7 · 90 min · Enterprise)*

Guía J2, secciones 7 a 9: control de °Brix con tolerancias, alerta de calidad, mantenimiento
preventivo y correctivo de la línea de envasado, y una ECO que cambia el diámetro de la tapa.

---

## Cierre: entregables de la Fase 5

- [ ] LdM de 3 niveles funcionando, con operaciones y costos.
- [ ] Laboratorio de costeo resuelto y contrastado con Odoo.
- [ ] Análisis de varianza de dos órdenes documentado.
- [ ] Trazabilidad demostrada: lote de aguaymanto → lote de pulpa → lote de conserva → cliente.
- [ ] **Entregable C:** *"Diseño del proceso productivo de ANDINA GOURMET"* con el diagrama de
      estructura, las operaciones, los puntos de control y el modelo de costeo.
- [ ] **Entregable D:** demo de 15 minutos "de la materia prima al cliente, con trazabilidad y costo".
- [ ] Respaldo `LAB_fase05_AAAAMMDD.zip`.

---

## Para ampliar

Dos fuentes de comunidad que conviene tener abiertas durante toda la fase:

| Recurso | Para qué en esta fase |
|---|---|
| **[Odoo en Español](https://www.youtube.com/@OdooSpanish)** | Ver explicado en video listas de materiales, órdenes de trabajo y subcontratación — **después** de haberlo hecho tú con estos datos |
| **[Cybrosys](https://www.cybrosys.com)** | Artículos por módulo; útiles para profundizar en el costeo de fabricación, la planificación y los flujos de calidad |

> **Úsalas para el concepto, no para la configuración.** Buena parte de ese material está grabado o
> escrito para v15–v18, y en v19 cambiaron nombres de campo, valores de selección y modelos enteros.
> Contrasta siempre contra la documentación 19.4, contra [la tabla de cambios de v19](../fase-12/README.md#los-cambios-de-v19-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
