# E3 — Los 9 errores de `07-productos-con-errores.csv`

> **Léelo después de haber diagnosticado tú mismo el archivo.**
> Los mensajes exactos varían ligeramente según la versión y el idioma; lo que no varía es la **causa**.

---

## Resumen

| Fila | ID | Error | Categoría del error |
|---|---|---|---|
| 1 | `andina.err_001` | `type` = `producto` | Valor de selección inválido |
| 2 | `andina.err_002` | `categ_id/id` = `andina.categ_mermeladas` (no existe) | Relación no encontrada |
| 3 | `andina.err_003` | `list_price` = `5,90` | Formato numérico |
| 4 y 5 | `andina.err_004` (×2) | Mismo ID externo en dos filas | ID externo duplicado |
| 6 | `andina.err_006` | `name` vacío | Campo obligatorio ausente |
| 7 | `andina.err_007` | `uom_id` = `Unidad` | Many2one por nombre inexistente |
| 8 | `andina.err_008` | `barcode` repetido de `andina.prod_001` | Violación de unicidad |
| 9 | `andina.err_009` | `is_storable` = `sí` | Booleano no reconocido |

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

### Fila 3 — Formato numérico
- **Síntoma:** *"No se pudo convertir '`5,90`' a número"* (o el precio entra como `5`, que es peor porque **no falla**).
- **Causa:** separador decimal coma en una base configurada con punto. Típico de archivos exportados
  desde Excel en configuración regional española/latinoamericana.
- **Solución:** `5.90`, o ajustar la opción de formato numérico en el diálogo de importación.
- **⚠️ El caso peligroso:** cuando el valor se importa **truncado en vez de fallar**. Por eso la validación
  post-carga con sumas de control (Fase 9) no es opcional.

### Filas 4 y 5 — ID externo duplicado
- **Síntoma:** *"Se encontró más de un registro con el mismo identificador externo"*, o —según el caso—
  se importa **una sola fila**: la segunda **sobrescribe** a la primera.
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

### Fila 9 — Booleano no reconocido
- **Síntoma:** el campo entra como **falso** sin avisar, o error de conversión.
- **Causa:** `sí` no es un valor booleano reconocido.
- **Solución:** `True` / `False`, o `1` / `0`.
- **Consecuencia si pasa desapercibido:** el producto no es almacenable → no aparece en inventario →
  el almacenero reporta "faltan productos" en la Fase 3 y nadie entiende por qué.

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

> **Los errores que Odoo reporta son los fáciles.** Los caros son los que **no** reporta:
> el precio truncado, el booleano en falso y la fila sobrescrita por un ID duplicado.
