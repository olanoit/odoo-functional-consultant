# E2 — 12 ejercicios de búsqueda, agrupación y reportes

**Regla del ejercicio:** todo se responde **dentro de Odoo**, sin exportar a Excel y sin escribir código.
Cronométrate: al terminar la fase deberías resolver cualquiera de ellos en menos de 2 minutos.

Las respuestas están en [`../soluciones/respuestas-ejercicios-busqueda.md`](../soluciones/respuestas-ejercicios-busqueda.md)
— consúltalas **después** de intentarlo.

---

## Parte A — Filtros y búsqueda (Contactos)

**1.** ¿Cuántos clientes hay fuera de Lima y Callao?
*(Pista: las etiquetas del CSV ya traen la zona.)*

**2.** Lista los clientes que son **mayoristas con línea de crédito**. ¿Cuántos son?

**3.** Encuentra todos los contactos cuyo correo contiene `bodega`. ¿Qué tipo de registros son?

**4.** Muestra únicamente las **direcciones de entrega** (no las empresas ni las personas).
*(Pista: hay un filtro por tipo de dirección; si no lo encuentras, agrupa.)*

**5.** ¿Qué cliente tiene más de una dirección de entrega?

**6.** Guarda como **favorito compartido con todos los usuarios** un filtro llamado
*"Clientes mayoristas de provincia"*.

## Parte B — Agrupaciones (Contactos y Productos)

**7.** Agrupa los contactos por **ciudad** y ordena mentalmente: ¿cuáles son las 3 ciudades con más contactos?

**8.** Agrupa los productos por **categoría de producto**: ¿cuántos productos hay en *Envases y Embalajes*
y cuántos en *Materia Prima*?

**9.** Agrupa los productos por **unidad de medida**: ¿cuántos se manejan en kg y cuántos en unidades?
¿Por qué los servicios no aparecen en kg?

**10.** Agrupa por **dos niveles**: categoría de producto y luego si se puede vender (`sale_ok`).
¿Qué categorías tienen productos que **no** se venden y por qué tiene sentido?

## Parte C — Pivote y gráfico (Productos)

**11.** Construye una **vista pivote** de productos con:
- filas: categoría de producto,
- medida: **precio de venta** y **coste**.

Responde: ¿en qué categoría es mayor la diferencia entre precio y coste?
*(Nota: la vista pivote de productos suma valores; es un ejercicio de manejo de la herramienta,
no un análisis de margen real — el margen se mide sobre ventas, en la Fase 2.)*

**12.** Cambia a **vista gráfico** de barras, ordena de mayor a menor y **guarda el reporte como favorito**
con el nombre *"Catálogo por categoría"*.

## Parte D — Preguntas de gerencia (integradoras)

Estas son las que un gerente hace de verdad. Resuélvelas con la interfaz y anota **cuántos clics** te tomó:

**13.** "¿Cuántos proveedores tengo por tipo de suministro y quién me da el plazo de entrega más largo?"

**14.** "Dame la lista de insumos cuyo proveedor exige comprar 1 000 unidades o más."

**15.** "¿Qué productos no tienen código de barras?"
*(Y la pregunta de consultor: ¿por qué esos y no otros?)*

---

## Cierre del ejercicio

Guarda estos **3 favoritos compartidos** (los pide el laboratorio de la Fase 1):

- [ ] *Clientes mayoristas de provincia* (ejercicio 6)
- [ ] *Insumos con proveedor asignado*
- [ ] *Productos sin código de barras* (útil para control de calidad de datos maestros)

Y **1 reporte pivote guardado** que responda una pregunta de gerencia (ejercicio 11 o 13).

> **Reflexión para la bitácora:** los ejercicios 13–15 son preguntas que hoy el cliente responde
> con Excel y dos días de trabajo. Poder responderlas en 30 segundos delante de él es, literalmente,
> tu argumento de venta en la Fase 11.
