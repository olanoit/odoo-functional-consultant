# Soluciones — E2: ejercicios de búsqueda, agrupación y reportes

> Los números corresponden exactamente a los datos de `datos/02-clientes.csv`, `03-proveedores.csv`,
> `04-contactos-hijos.csv` y `06-productos.csv` recién importados, **sin datos demo**.
> Si tu resultado difiere, revisa primero si importaste todos los archivos y en el orden correcto.

---

## Parte A — Filtros y búsqueda

**1. Clientes fuera de Lima y Callao → 14 de 25.**
Cómo: *Contactos* → filtro **Clientes** → buscar por etiqueta *Zona Provincia*.
Alternativa: agrupar por Ciudad y sumar todas menos Lima y Callao.
La etiqueta existe justamente para no depender del texto de la ciudad (que un usuario escribirá
"LIMA", "lima" o "Lima Cercado"). **Lección de datos maestros: lo que se filtra, se etiqueta.**

**2. Mayoristas con línea de crédito → 13.**
Cómo: buscar por etiqueta *Mayorista* **y** añadir un segundo criterio por etiqueta *Con línea de crédito*.
Ojo: dos criterios en **la misma** categoría del buscador se combinan con **O**; en categorías distintas,
con **Y**. Es el error de búsqueda más frecuente de un usuario nuevo.

**3. Correos que contienen `bodega` → 2 registros:** *Bodega Doña Rosa* (la empresa) y
*Rosa Quispe Huamán* (la persona de contacto, hija de esa empresa).
Muestra que empresa y persona son **el mismo modelo** (`res.partner`) con distinto `type`.

**4. Direcciones de entrega → 5.**
Cómo: agrupar por **Tipo de dirección** (o filtrar por él). Las direcciones no aparecen por defecto en
la lista principal de Contactos: hay que quitar el filtro por defecto o agrupar.

**5. Cliente con más de una dirección de entrega → *Comercial Los Andes E.I.R.L.*** (Tienda Cayma y
Tienda Cerro Colorado). En la Fase 2 verás que al cotizar se elige **cuál** de las dos recibe la mercancía.

**6. Favorito compartido *"Clientes mayoristas de provincia"* → 9 clientes.**
Cómo: aplicar los dos filtros de etiqueta → *Favoritos → Guardar búsqueda actual* → marcar
**Compartir con todos los usuarios**. Verifica entrando con el usuario Ana: debe verlo.

## Parte B — Agrupaciones

**7. Top ciudades (clientes + proveedores):** Lima 18 · Arequipa 5 · Cusco 3 · Trujillo 2.

**8. Productos por categoría:**

| Categoría | Productos |
|---|---|
| Conservas | 15 |
| Snacks | 15 |
| Harinas y Granos | 12 |
| Envases y Embalajes | 12 |
| Materia Prima | 9 |
| Bebidas | 6 |
| Servicios | 6 |
| Aditivos | 4 |
| **Total** | **79** |

**9. Por unidad de medida:** 65 en Unidades · 13 en kg · 1 en litros.
Los servicios están en *Unidades* porque toda plantilla de producto necesita una unidad —
lo relevante en ellos no es la unidad, sino que `type = service` y que **no tienen stock**.

**10. Productos no vendibles (`sale_ok = False`) → 28:** Envases 12, Materia Prima 9, Aditivos 4,
Servicios 3. Tiene sentido de negocio: son cosas que **se compran** para producir, no que se venden.
Configurarlo así evita que un vendedor cotice "Tapa metálica twist-off" por error — es
**control por configuración**, no por capacitación. Ese razonamiento es el que vendes como consultor.

## Parte C — Pivote y gráfico

**11.** Diferencia entre la suma de precios de venta y la suma de costes, por categoría:

| Categoría | Σ Precio venta | Σ Coste | Diferencia |
|---|---|---|---|
| Servicios | 3 100.35 | 2 450.22 | 650.13 |
| Conservas | 213.49 | 113.79 | 99.70 |
| Harinas y Granos | 171.91 | 91.18 | 80.73 |
| Snacks | 121.47 | 55.97 | 65.50 |
| Bebidas | 42.12 | 19.44 | 22.68 |

**La respuesta de consultor no es "Servicios".** Es: *"esta cifra no significa nada"* — está sumando
precios unitarios de artículos distintos, sin cantidades vendidas. Sirve para aprender a manejar la
vista pivote, no para decidir. El margen real se mide sobre líneas de venta facturadas (Fase 2) y
sobre coste real de producción (Fase 5). **Saber cuándo un número no sirve es parte del oficio.**

**12.** Vista gráfico de barras → orden descendente → *Favoritos → Guardar búsqueda actual*
como *"Catálogo por categoría"*.

## Parte D — Preguntas de gerencia

**13. Proveedores por tipo de suministro:** insumos 5 · envases 5 · servicios 5.
**Plazo de entrega más largo: 12 días**, de *Insumos Químicos Alimentarios S.A.C.*
(pectina cítrica y sorbato de potasio).
Cómo: *Inventario/Compras → Productos*, agrupar por proveedor y ordenar por plazo, o revisar la
pestaña *Compra* del producto. En la Fase 3 ese plazo alimentará las reglas de reordenamiento.

**14. Insumos con cantidad mínima ≥ 1 000 → 8 productos:** frascos de vidrio 400 g y 200 g (1 000),
tapas de 63 y 82 mm (2 000), etiquetas frontal y posterior (5 000), bolsas metalizadas 50 g y 100 g (5 000).
**Impacto de negocio:** son compras grandes y poco frecuentes; condicionan el capital de trabajo y el
espacio de almacén. Es exactamente el tipo de dato que el cliente hoy no tiene a la mano.

**15. Productos sin código de barras → 6: los servicios.**
La pregunta de consultor —*¿por qué esos?*— tiene respuesta: un servicio no se escanea, no ocupa
un lugar en la góndola ni pasa por caja. Que el filtro devuelva **solo** servicios es señal de que
los datos maestros están **completos y coherentes**. Si aparecieran conservas en esa lista, tendrías
un problema de calidad de datos que resolver antes de operar.

---

## Cómo evaluarte

| Nivel | Señal |
|---|---|
| **Insuficiente** | Necesitas exportar a Excel para responder |
| **En camino** | Respondes todo, pero tardas más de 5 minutos por pregunta |
| **Listo para la Fase 2** | Respondes cualquiera en < 2 min y sabes explicar **por qué** el dato es o no confiable |
