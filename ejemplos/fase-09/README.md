# Cuaderno de ejemplos — Fase 9: Productividad, Studio y Datos

Casos prácticos para [`../../fases/fase-09-productividad-studio-datos.md`](../../fases/fase-09-productividad-studio-datos.md).

> Esta fase entrena las dos capacidades que multiplican el valor de un consultor funcional:
> **personalizar sin programar** y **dominar los datos**. Y, sobre todo, el criterio para saber
> cuándo **no** personalizar.

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-clientes-legado.csv` | **512 clientes** exportados de un sistema viejo, con duplicados, RUC inválidos, formatos rotos y campos vacíos |
| `guias/N1` | Migración de datos: perfilado, decisiones, mapeo, carga y validación |
| `guias/N2` | Studio: árbol de decisión, app propia, reportes y aprobaciones |
| `soluciones/respuestas-migracion.md` | Perfilado resuelto con las sumas de control exactas |

Studio, Documentos, Firma y Conocimiento son **Enterprise**.

---

## Ejemplo 1 — Herramientas de productividad
*(Bloque 9.1 · 60 min)*

1. **Conocimiento:** construye el manual interno de ANDINA GOURMET con artículos anidados y vistas
   de Odoo incrustadas. **Úsalo para tu propia documentación de estudio**: es la mejor forma de
   aprenderlo y te deja el material listo para la Fase 11.
2. **Documentos:** espacio de trabajo con reglas de clasificación y flujo de aprobación; conecta la
   digitalización de facturas de proveedor con la Fase 4.
3. **Firma:** plantilla de contrato de distribuidor con campos y dos firmantes en orden.
4. **Conversaciones y Calendario:** canales por equipo y agendamiento de citas en línea.

## Ejemplo 2 — El tablero gerencial
*(Bloque 9.2 · 60 min)*

Inserta vistas de Odoo en una **hoja de cálculo** y construye el tablero de dirección con 6
indicadores en vivo:

| Indicador | Fuente |
|---|---|
| Ventas del mes vs. objetivo | Fase 2 |
| Margen por línea de negocio | Analítica de la Fase 4 |
| Rotación de inventario | Fase 3 |
| Antigüedad de cobros | Fase 4 |
| Rentabilidad de proyectos | Fase 6 |
| Costo real de producción | Fase 5 |

**Requisito del ejercicio:** documenta de dónde sale **cada** dato. Un indicador que nadie puede
reproducir no sirve para decidir, por bonito que se vea.

## Ejemplo 3 — Migración de datos real
*(Bloque 9.5 · 120 min)* ← **el ejercicio central**

[`guias/N1-migracion-de-datos.md`](guias/N1-migracion-de-datos.md) con el archivo de 512 clientes.

Anticipo de lo que vas a encontrar: 13 nombres duplicados que afectan a 27 filas, 14 RUC inválidos,
78 clientes inactivos, 7 límites de crédito con formato roto y una suma de control de **S/ 3 776 000**.

El ejercicio no termina cuando importas: termina cuando **puedes demostrar** que la carga es correcta
y entregar el archivo de descartes con sus motivos.

## Ejemplo 4 — Studio y el árbol de decisión
*(Bloques 9.3 y 9.4 · 150 min)*

[`guias/N2-studio-y-arbol-de-decision.md`](guias/N2-studio-y-arbol-de-decision.md):

1. **Primero el criterio:** aplica el árbol de decisión a 6 requerimientos reales y argumenta cada uno.
2. **Después la herramienta:** construye la app *Visitas a distribuidores* con 12 campos, 6 vistas,
   3 automatizaciones y permisos por rol.
3. Personaliza la **factura PDF** y crea 2 **reglas de aprobación** (descuento > 20 %, compra > S/ 20 000).
4. Documenta el **costo oculto** de cada personalización: qué pasa al actualizar y quién la mantiene.

## Ejemplo 5 — Limpieza de datos
*(Bloque 9.5 · 45 min)*

Con los 512 clientes ya cargados:
1. Usa **Limpieza de datos** para detectar duplicados por nombre y por RUC.
2. Configura reglas de formato (mayúsculas, espacios, teléfonos).
3. Fusiona **un** par de duplicados y observa qué pasa con sus documentos asociados.
4. Escribe la regla de negocio: ¿cuándo se fusiona y cuándo no? *(Pista: dos sucursales del mismo
   grupo con RUC distinto **no** se fusionan.)*

---

## Cierre: entregables de la Fase 9

- [ ] App propia en Studio funcionando, con permisos por rol.
- [ ] Factura PDF personalizada y 2 reglas de aprobación.
- [ ] Tablero gerencial con 6 indicadores y su documentación de fuentes.
- [ ] Migración de los 512 clientes **validada con sumas de control** y archivo de descartes.
- [ ] Reimportación probada: modificar 5 registros y comprobar que no se duplican.
- [ ] **Entregable 1:** *"Árbol de decisión de personalización"* con los 6 casos resueltos.
- [ ] **Entregable 2:** *"Plan de migración de datos"* usando
      [`../../plantillas/05-plan-de-migracion-de-datos.md`](../../plantillas/05-plan-de-migracion-de-datos.md).
- [ ] Respaldo `LAB_fase09_AAAAMMDD.zip`.

---

## Para ampliar

Dos fuentes de comunidad que conviene tener abiertas durante toda la fase:

| Recurso | Para qué en esta fase |
|---|---|
| **[Odoo en Español](https://www.youtube.com/@OdooSpanish)** | Ver explicado en video Studio, migración de datos y hojas de cálculo — **después** de haberlo hecho tú con estos datos |
| **[Cybrosys](https://www.cybrosys.com)** | Artículos por módulo; útiles para profundizar en la personalización sin código y la limpieza de datos antes de importar |

> **Úsalas para el concepto, no para la configuración.** Buena parte de ese material está grabado o
> escrito para v15–v18, y en v19 cambiaron nombres de campo, valores de selección y modelos enteros.
> Contrasta siempre contra la documentación 19.4, contra [la tabla de cambios de v19](../fase-12/README.md#los-cambios-de-v19-que-hay-que-llevar-frescos-al-examen) y contra tu propia base.

El catálogo completo de recursos verificados está en [`../../recursos.md`](../../recursos.md).
