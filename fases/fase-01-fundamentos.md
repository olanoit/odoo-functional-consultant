# Fase 1 — Fundamentos de Odoo y base de datos

**Horas estimadas:** 25–30 h · **Prerrequisitos:** ninguno · **Base de datos:** `SANDBOX` (exploración) + `LAB` (construcción)

> **Objetivo de la fase:** dejar de ser un usuario que "adivina dónde está el botón" y pasar a
> entender Odoo como un **modelo de datos con flujos de estado**. Todo lo demás del plan
> se apoya aquí. Esta es la única fase que, mal hecha, se paga en las once siguientes.

---

## 📓 Cuaderno de ejemplos de esta fase

Los laboratorios de abajo tienen sus datos y casos ya preparados en
**[`../ejemplos/fase-01/`](../ejemplos/fase-01/README.md)**:

| Recurso | Contenido |
|---|---|
| `datos/` | 25 clientes, 15 proveedores, 10 contactos hijos, 11 categorías y **79 productos** listos para importar, más un archivo con **9 errores de importación a propósito** |
| `guias/E1` | Los 4 usuarios con su matriz de permisos y **12 pruebas de acceso** |
| `guias/E2` | 15 ejercicios de filtros, agrupación y pivote |
| `guias/E3` | Diagnóstico de cada error de importación: síntoma → causa → solución |
| `guias/E4` | **Chuleta de nombres técnicos verificados en v19** (varios cambiaron: `uom_po_id` eliminado, `type=product` ya no existe, `mobile` eliminado, `groups_id`→`group_ids`) |
| `soluciones/` | Respuestas de los ejercicios y del cuestionario |

Trabaja los 8 ejemplos guiados en orden: cubren los bloques 1.1 a 1.7 y dejan el laboratorio
integrador prácticamente terminado.

## 1. Resultados de aprendizaje

Al terminar debes poder:

1. Explicar la arquitectura funcional: aplicaciones ↔ módulos ↔ modelos ↔ vistas ↔ menús.
2. Navegar cualquier app desconocida en < 5 minutos usando filtros, agrupaciones y vistas.
3. Crear una empresa desde cero: compañía, usuarios, permisos, idiomas, monedas, correo.
4. Importar datos maestros desde Excel/CSV con relaciones (Many2one) resueltas.
5. Explicar el chatter, actividades, seguidores y por qué son el corazón de la trazabilidad.
6. Construir un reporte con vista pivote y gráfico, y guardarlo como favorito compartido.
7. Distinguir Community vs. Enterprise, y Odoo Online vs. Odoo.sh vs. On-premise.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación oficial |
|---|---|---|
| 1.1 | Panorama general de la documentación de usuario | [applications.html](https://www.odoo.com/documentation/saas-19.4/es/applications.html) |
| 1.2 | Fundamentos de Odoo (esenciales) | [essentials.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials.html) |
| 1.3 | Búsqueda, filtros y agrupaciones | [essentials/search.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/search.html) |
| 1.4 | Reportes y vistas de análisis | [essentials/reporting.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/reporting.html) |
| 1.5 | Actividades y chatter | [essentials/activities.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/activities.html) |
| 1.6 | Contactos | [essentials/contacts.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/contacts.html) |
| 1.7 | Exportar e importar datos | [essentials/export_import_data.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/export_import_data.html) |
| 1.8 | Compras dentro de la aplicación (IAP) | [essentials/in_app_purchase.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/in_app_purchase.html) |
| 1.9 | Ajustes generales | [general.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general.html) |
| 1.10 | Usuarios y grupos de acceso | [general/users.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/users.html) |
| 1.11 | Compañías y multiempresa | [general/companies.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/companies.html) · [multi_company.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/companies/multi_company.html) |
| 1.12 | Aplicaciones y módulos (instalar/desinstalar) | [general/apps_modules.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/apps_modules.html) |
| 1.13 | Comunicación por correo (servidores, alias, plantillas) | [general/email_communication.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/email_communication.html) |
| 1.14 | Modo desarrollador | [general/developer_mode.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/developer_mode.html) |
| 1.15 | Hosting: Online, Odoo.sh, On-premise | [administration.html](https://www.odoo.com/documentation/saas-19.4/es/administration.html) · [hosting.html](https://www.odoo.com/documentation/saas-19.4/es/administration/hosting.html) |

**Refuerzo audiovisual:** curso *Odoo Essentials / Getting Started* en <https://www.odoo.com/slides/all>
y el canal oficial <https://www.youtube.com/@odoo>. Máximo 1 h de video por cada 3 h de configuración.

## 3. Ruta de estudio paso a paso

### Bloque 1.1 — Reconocimiento del terreno (3 h)
1. Crear la base `SANDBOX` **con** datos demo.
2. Recorrer *todas* las apps disponibles sin instalar nada nuevo: abrir cada una, mirar sus menús
   de nivel 1 y su menú **Configuración**. Anotar en la bitácora, por app, una frase: *"sirve para…"*.
3. Instalar y desinstalar un módulo (p. ej. **Encuestas**). Observar qué menús aparecen y desaparecen.
   Anotar: ¿qué pasó con los datos al desinstalar?

> **Concepto clave:** en Odoo *instalar una app instala módulos*, y los módulos *añaden campos y
> menús a modelos existentes*. Por eso instalar Contabilidad cambia la vista de Producto.

### Bloque 1.2 — La interfaz como herramienta de análisis (4 h)
1. En la lista de Contactos: aplicar filtros, agrupar por dos niveles, usar el buscador con
   varios criterios, y **guardar un filtro favorito** compartido con todos los usuarios.
2. Alternar entre vistas: lista, kanban, formulario, mapa, actividad.
3. En Ventas → Reportes: construir una **vista pivote** con medidas y dimensiones, invertir ejes,
   expandir subgrupos y **descargar a Excel**. Repetir con **vista gráfico** (barras, líneas, circular).
4. Personalizar columnas de una vista de lista (botón de ajustes de columnas) y ordenar por varios campos.

> **Prueba de dominio:** en 5 minutos, responder con la interfaz "¿cuáles fueron mis 3 clientes con
> mayor facturación este año y qué producto les vendí más?" — sin salir de Odoo y sin Excel.

### Bloque 1.3 — Chatter, actividades y trazabilidad (2 h)
1. En un pedido de venta: escribir un mensaje interno (nota) vs. enviar mensaje al cliente.
   Entender la diferencia de destinatarios.
2. Agregar/quitar seguidores y ajustar sus suscripciones por tipo de subtipo.
3. Programar actividades (llamada, reunión, tarea), reasignarlas y marcarlas como hechas.
4. Ver el **log de cambios** en modo desarrollador y el historial de campos rastreados.

> **Para el cliente:** el chatter es la razón por la que Odoo reemplaza cadenas de correo y
> hojas de "seguimiento". Aprende a venderlo así.

### Bloque 1.4 — Configuración inicial de una empresa (6 h) — base `LAB`
1. Crear la base `LAB` **sin datos demo**. Instalar solo: Contactos, Ventas, Inventario, Compras.
2. Configurar la compañía **ANDINA GOURMET S.A.C.**: nombre, RUC/identificación, dirección, logo,
   moneda PEN, zona horaria, idioma español.
3. Activar idiomas adicionales y **traducir** un término de la interfaz para ver cómo funciona.
4. Crear 4 usuarios con perfiles distintos (vendedor, comprador, almacenero, gerente) y asignar
   grupos de acceso. Entrar con cada uno (usar navegación privada) y **documentar qué ve y qué no**.
5. Configurar formatos: separador de miles, formato de fecha, primer día de la semana.
6. Revisar Ajustes → Técnico (modo desarrollador): secuencias, plantillas de correo, acciones planificadas.

> **Romper a propósito:** quitar a un usuario el grupo *Ventas: Ver solo lo propio* → *Ver todo*
> y observar cómo cambia su lista de pedidos. Documentar la diferencia entre **grupos** (qué menús ve)
> y **reglas de registro** (qué filas ve).

### Bloque 1.5 — Datos maestros y contactos (4 h)
1. Modelar contactos: empresa vs. contacto individual, **direcciones de entrega/facturación**,
   contactos hijos, etiquetas, campos de venta/compra/contabilidad.
2. Crear 15 clientes y 10 proveedores de ANDINA GOURMET (nombres inventados, RUC/DNI ficticios).
3. Crear 25 productos: 10 terminados, 10 insumos, 5 servicios. Definir categorías, unidades de medida,
   referencias internas, códigos de barras.
4. Diferenciar **tipo de producto** (bienes con/sin seguimiento de inventario, servicio, combo) y
   **variantes** vs. productos distintos.

### Bloque 1.6 — Importación y exportación de datos (5 h) ← *el súperpoder del consultor funcional*
1. Exportar los contactos creados con la opción **"Quiero actualizar datos (importación compatible)"**
   y observar la columna `id` (**XML ID / identificador externo**).
2. Modificar el Excel exportado y reimportar: comprobar que **actualiza** en vez de duplicar.
3. Importar un archivo nuevo de 50 productos con: categoría, unidad de medida, proveedor y etiquetas
   → resolver relaciones Many2one por nombre y por ID externo.
4. Provocar y resolver los 5 errores clásicos de importación:
   - valor de selección inválido,
   - Many2one no encontrado,
   - formato de fecha/decimal incorrecto,
   - duplicado por ID externo repetido,
   - campo obligatorio ausente.
5. Documentar en la bitácora tu **checklist personal de importación** (será entregable en la Fase 11).

> **Regla de oro:** siempre importar con ID externo propio (`prefijo.codigo_cliente`) para poder
> reimportar y corregir. Sin ID externo, cada corrección crea duplicados.

### Bloque 1.7 — Ediciones, hosting y ciclo de vida (2 h)
1. Leer [hosting.html](https://www.odoo.com/documentation/saas-19.4/es/administration/hosting.html)
   y comparar Odoo Online / Odoo.sh / On-premise en una tabla propia:
   control, costo, módulos de terceros, acceso a base de datos, actualizaciones.
2. Entender qué es una **base neutralizada** ([neutralized_database.html](https://www.odoo.com/documentation/saas-19.4/es/administration/neutralized_database.html))
   y por qué importa antes de probar en una copia (no se envían correos ni pagos reales).
3. Anotar la diferencia Community vs. Enterprise y hacer la **lista de apps que solo existen en Enterprise**
   (te la preguntarán en cada preventa).

## 4. Laboratorio integrador de la fase

**Encargo:** "Necesitamos la base de Odoo lista para empezar a trabajar el lunes."

Entregar en la base `LAB`:
- Compañía configurada (datos fiscales, moneda, logo, formatos).
- 4 usuarios con permisos diferenciados y verificados uno por uno.
- 25 clientes, 15 proveedores, 79 productos importados desde archivo (no a mano).
- 3 filtros favoritos compartidos útiles para gerencia.
- 1 reporte pivote guardado que responda una pregunta de negocio.
- Respaldo `LAB_fase01_AAAAMMDD.zip`.

## 5. Preguntas de comprensión (prueba B)

1. ¿Cuál es la diferencia entre un **grupo de acceso** y una **regla de registro**? Da un ejemplo de negocio de cada uno.
2. ¿Qué es un **ID externo** y por qué es imprescindible en una migración de datos?
3. Un cliente pide "que el vendedor solo vea sus propios clientes". ¿Es configuración, Studio o desarrollo? ¿Por qué?
4. ¿Qué diferencia hay entre **archivar** y **eliminar** un registro? ¿Cuál recomiendas a un cliente y por qué?
5. ¿Por qué al instalar Contabilidad cambian campos en el formulario de Producto?
6. ¿Qué información se pierde y qué se conserva al **desinstalar** un módulo?
7. Explica el chatter a un gerente que hoy usa cadenas de correo. Máximo 6 líneas.
8. ¿Cuándo recomendarías Odoo.sh en lugar de Odoo Online? Dos criterios concretos.
9. ¿Qué es una **secuencia** y qué pasa si un cliente exige que su numeración de facturas empiece en 0001 cada año?
10. Diferencia entre **unidad de medida** y **unidad de medida de compra**. Ejemplo con un insumo de ANDINA GOURMET.

## 6. Criterios de validación (gate de salida)

- [ ] **A. A ciegas (60 min):** en una base nueva sin demo — crear compañía, 3 usuarios con permisos
      distintos, importar 20 productos desde CSV con categoría y proveedor, y dejar un reporte pivote guardado.
- [ ] **B.** ≥ 8/10 en las preguntas, sin consultar.
- [ ] **C. Entregable:** documento *"Guía de navegación y datos maestros de ANDINA GOURMET"*
      (2–4 páginas) que un usuario nuevo pueda seguir para dar de alta un cliente y un producto.
- [ ] Glosario del §10 de [`../00-metodo-y-entorno.md`](../00-metodo-y-entorno.md) escrito con tus palabras.
- [ ] Bitácora al día y respaldo `LAB_fase01` guardado.

**Cuándo avanzar:** cuando puedas abrir una app que nunca has visto y, en 5 minutos, describir
qué objetos maneja, qué estados tienen y cómo se reporta sobre ellos.

## 7. Trampas frecuentes de esta fase

| Trampa | Realidad |
|---|---|
| "Los permisos se configuran al final" | Se configuran al principio: definen qué demos y qué prueba cada usuario en UAT. |
| Cargar datos maestros a mano | Un cliente real trae 4 000 productos. Si no importas, no implementas. |
| Ignorar el ID externo | Toda corrección posterior duplica datos. Es la causa #1 de migraciones fallidas. |
| Confundir producto y variante | Rompe inventario, precios y eCommerce tres fases más adelante. |
| Estudiar solo con demo | Nunca ves los campos vacíos ni los errores de configuración inicial. |
