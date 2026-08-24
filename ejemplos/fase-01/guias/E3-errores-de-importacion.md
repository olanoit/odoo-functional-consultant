# E3 — Los 8 errores de `07-productos-con-errores.csv` (en 9 filas)

> **Léelo después de haber diagnosticado tú mismo el archivo.**
> Los mensajes exactos varían ligeramente según la versión y el idioma; lo que no varía es la **causa**.
>
> **Verificado importando el archivo en Odoo 19 (saas~19.4), interfaz en español.** El dato más
> importante del ejercicio está en la columna *¿Odoo avisa?*: **Odoo solo reporta 5 de los 8 errores**.
> Los otros 3 se importan mal **en silencio**. Si esperabas que el archivo fuera rechazado entero,
> ya aprendiste la lección principal de la fase.

---

## Resumen

| Fila | ID | Error | Categoría del error | ¿Odoo avisa? | Qué entra si no avisa |
|---|---|---|---|---|---|
| 1 | `andina.err_001` | `type` = `producto` | Valor de selección inválido | **Sí** | — |
| 2 | `andina.err_002` | `categ_id/id` = `andina.categ_mermeladas` (no existe) | Relación no encontrada | **Sí** | — |
| 3 | `andina.err_003` | `list_price` = `5,90` | Formato numérico | **No** | `590.00` — **cien veces** el precio |
| 4 y 5 | `andina.err_004` (×2) | Mismo ID externo en dos filas | ID externo duplicado | **No** | 1 registro en vez de 2: la fila 5 sobrescribe la 4 |
| 6 | `andina.err_006` | `name` vacío | Campo obligatorio ausente | **Sí** | — |
| 7 | `andina.err_007` | `uom_id` = `Unidad` | Many2one por nombre inexistente | **Sí** | — |
| 8 | `andina.err_008` | `barcode` repetido de `andina.prod_001` | Violación de unicidad | **Sí** | — |
| 9 | `andina.err_009` | `is_storable` = `sí` | Booleano no reconocido | **No** | `True` — cualquier texto no vacío se lee como verdadero |

**5 avisados, 3 silenciosos.** Y fíjate en cuáles son los silenciosos: un precio multiplicado por
100, un producto que desaparece y un booleano inventado. Los tres pasan la revisión visual.

---

## Detalle

### Fila 1 — Valor de selección inválido
- **Síntoma:** *"Valor '`producto`' no válido para el campo Tipo de producto"* y Odoo ofrece los valores admitidos.
- **Causa:** en Odoo 19 `type` solo acepta `consu`, `service` o `combo`. El valor `product`
  (producto almacenable) **desapareció en v18/v19**: ahora es `type=consu` + `is_storable=True`.
- **Solución:** `type` → `consu`, y asegurar `is_storable=True`.
- **Por qué importa:** es el error #1 al reutilizar plantillas de importación de versiones antiguas.

### Fila 2 — Relación no encontrada (Many2one)
- **Síntoma:** *"No se encontró ninguna coincidencia para el valor '`andina.categ_mermeladas`' en el campo Categoría de producto"*.
- **Causa:** el ID externo no existe: en `05-categorias-producto.csv` las mermeladas viven dentro de
  `andina.categ_conservas`. Se referenció una categoría que nunca se creó.
- **Solución:** usar `andina.categ_conservas`, **o** crear antes la categoría faltante.
- **Regla general:** un archivo de importación **nunca** puede referenciar algo que no se haya cargado antes.
  De ahí el orden de carga.

### Fila 3 — Formato numérico · **error silencioso**
- **Síntoma verificado en v19:** *ninguno*. No hay mensaje de error. El producto se crea con
  `list_price = 590.00` en lugar de 5.90.
- **Causa:** con las opciones de formato por defecto del diálogo de importación —**separador de
  miles = coma**, **separador decimal = punto**— Odoo lee `5,90` como *cinco mil novecientos… sin
  decimales*: **590**. No es un truncamiento, es una multiplicación por 100.
- **Solución:** escribir `5.90` en el archivo, **o** cambiar el separador decimal a coma en el
  diálogo de importación (pestaña de opciones de formato) **antes** de importar.
- **⚠️ Por qué es el error más caro del archivo:** un producto de S/ 5.90 que entra a S/ 590.00
  no rompe nada en la importación. Rompe la primera cotización que alguien envíe a un cliente.
  La única defensa es la validación post-carga con **sumas de control** (Fase 9): si la suma de
  precios del catálogo no cuadra con la del archivo, hay un decimal mal leído.

### Filas 4 y 5 — ID externo duplicado · **error silencioso**
- **Síntoma verificado en v19:** *ninguno*. Se importa **una sola fila**: la 5 (*Harina de Maca 1 kg*)
  **sobrescribe** a la 4 (*Harina de Maca 500 g*), que desaparece sin dejar rastro.
- **Causa:** `andina.err_004` aparece dos veces con productos distintos (Harina de Maca 500 g y 1 kg).
- **Solución:** un ID externo único por registro (`andina.err_004` y `andina.err_005`).
- **Por qué es grave:** en una migración real esto no rompe nada visiblemente; simplemente **pierdes registros**
  en silencio. Se detecta contando filas del archivo contra registros creados.

### Fila 6 — Campo obligatorio ausente
- **Síntoma:** *"El campo Nombre es obligatorio"* / *"No se puede crear el registro"*.
- **Causa:** `name` vacío. En `product.template` es `required=True`.
- **Solución:** completar el nombre (*Snack de Cañihua Horneada 50 g*).
- **Variante frecuente en la vida real:** filas vacías al final del archivo que Excel arrastra.
  Siempre revisa el número de filas antes de importar.

### Fila 7 — Many2one por nombre que no existe
- **Síntoma:** *"No se encontró ninguna coincidencia para el valor '`Unidad`' en el campo Unidad"*.
- **Causa:** la unidad se llama *Unidades* (o *Units* si la base está en inglés). Se importó **por nombre**,
  no por ID externo, y el nombre depende del idioma de la base.
- **Solución:** usar la columna `uom_id/id` con `uom.product_uom_unit` — así funciona en cualquier idioma.
- **Esta es la lección más transferible del ejercicio:** en migraciones, **siempre `/id`**.

### Fila 8 — Violación de unicidad
- **Síntoma:** *"Ya existe un producto con este código de barras"* / error de restricción única.
- **Causa:** el código `7750000000014` ya pertenece a *Conserva de Aguaymanto 200 g*.
- **Solución:** asignar un EAN-13 propio y válido.
- **En el cliente real:** el catálogo trae códigos repetidos con mucha frecuencia. Se detectan **antes**
  de importar, con un contador de duplicados en la hoja de cálculo, no después con los errores de Odoo.

### Fila 9 — Booleano no reconocido · **error silencioso**
- **Síntoma verificado en v19:** *ninguno*. El campo entra como **`True`**.
- **Causa:** el importador trata **cualquier texto no vacío** como verdadero. `sí`, `no`, `falso`,
  `quizá` y `0.0` entran todos como **verdadero**. Solo la cadena vacía y los valores reconocidos
  (`True`/`False`, `1`/`0`, `VERDADERO`/`FALSO` según idioma) se interpretan como es debido.
- **Solución:** `True` / `False`, o `1` / `0`.
- **Consecuencia si pasa desapercibido:** aquí el azar juega a favor —`sí` significa verdadero y
  verdadero es lo que se quería—, pero escribe **`no`** en esa celda y el producto seguirá siendo
  almacenable. Ese es el caso que rompe la Fase 3: un producto marcado como *no almacenable* en el
  archivo que entra como almacenable, o al revés, y el almacenero reporta "faltan productos" sin que
  nadie entienda por qué.

---

## Checklist personal de importación (borrador para la Fase 11)

Antes de importar cualquier archivo en cualquier cliente:

- [ ] ¿El archivo está en UTF-8 y con el separador correcto?
- [ ] ¿Cada registro tiene un **ID externo** único y con prefijo propio?
- [ ] ¿Conté las filas del archivo para compararlas después con los registros creados?
- [ ] ¿Todas las relaciones (`/id`) apuntan a algo **ya cargado**?
- [ ] ¿Los campos de selección usan valores técnicos válidos **de esta versión**?
- [ ] ¿Los decimales usan el separador que espera la base?
- [ ] ¿Revisé duplicados en las columnas únicas (código de barras, referencia, RUC)?
- [ ] ¿Los booleanos son `True`/`False`?
- [ ] ¿Ejecuté **Probar importación** y leí *todos* los mensajes?
- [ ] Tras importar: ¿conté registros y validé con al menos una **suma de control**?

> **Los errores que Odoo reporta son los fáciles.** Los caros son los tres que **no** reporta y que
> este archivo demuestra en vivo: el **precio multiplicado por 100**, el **producto que desaparece**
> por un ID externo repetido y el **booleano inventado** que entra como verdadero.
>
> Odoo avisó de 5 de 8. Tu checklist tiene que cubrir los otros 3.
