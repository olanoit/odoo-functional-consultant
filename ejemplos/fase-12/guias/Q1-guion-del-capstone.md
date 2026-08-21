# Q1 — Guion de ejecución del capstone

> Plan de trabajo día a día para construir `CAPSTONE` desde cero en 4 semanas.
> **No se copia `LAB`**: se reconstruye, contra reloj, como si fuera un cliente real.

---

## Regla del capstone

Trabajas **como consultor, no como estudiante**: cada configuración se documenta mientras se hace,
cada decisión se justifica y cada problema se registra. Al final, el entregable no es la base de
datos: es el **expediente del proyecto**.

## Semana 1 — Análisis y base

| Día | Trabajo | Entregable parcial |
|---|---|---|
| 1 | Releer la entrevista de la Fase 11 y redactar alcance, supuestos y exclusiones | Documento de alcance |
| 2 | AS-IS y TO-BE de los 5 procesos principales | Diagramas |
| 3 | Matriz GAP-FIT con decisiones y estimación por bloques | Matriz + estimación |
| 4 | Base nueva con localización PE, compañía, usuarios y permisos probados | Base inicial |
| 5 | Migración de datos maestros por importación, con validación | Sumas de control |

**Gate de la semana:** un tercero podría entender qué se va a implementar y por qué, leyendo tus documentos.

## Semana 2 — Cadena de suministro y comercial

| Día | Trabajo |
|---|---|
| 6 | Almacenes, ubicaciones, rutas multi-etapa, stock inicial con lotes |
| 7 | Compras: proveedores, plazos, reglas de reordenamiento, ciclo P2P completo |
| 8 | Comercial: equipos, embudo, listas de precios, plantilla de cotización |
| 9 | Ciclo O2C completo con entrega parcial y facturación por entregado |
| 10 | Producción: LdM de 2 niveles, centro de trabajo, una orden completada con lotes |

**Gate:** un pedido puede recorrer venta → producción → entrega sin intervención manual fuera de proceso.

## Semana 3 — Finanzas y localización

| Día | Trabajo |
|---|---|
| 11 | Plan de cuentas, diarios, impuestos, posiciones fiscales, condiciones de pago |
| 12 | Valoración de inventario con cuentas; verificar el asiento de una recepción |
| 13 | Facturación electrónica en modo prueba: factura, boleta, nota de crédito aceptadas |
| 14 | Conciliación bancaria con modelos; analítica de 2 dimensiones aplicada |
| 15 | Servicios y RR. HH.: 1 servicio facturable, empleados con horario y ausencias |

**Gate:** el mes cierra y el inventario cuadra con la contabilidad (o las diferencias están explicadas).

## Semana 4 — Digital, personalización y cierre

| Día | Trabajo |
|---|---|
| 16 | Sitio web y tienda con 10 productos; una compra completa trazada |
| 17 | Studio: app propia, 2 automatizaciones, 1 regla de aprobación, factura PDF |
| 18 | Tablero gerencial con 6 indicadores documentados |
| 19 | UAT: ejecutar los 30 casos y gestionar los defectos |
| 20 | Guías por rol, demo grabada de 30 min, documento final y lecciones aprendidas |

**Gate final:** rúbrica ≥ 80 puntos.

---

## Los errores que arruinan un capstone

| Error | Cómo evitarlo |
|---|---|
| Configurar sin documentar y "documentar al final" | Documenta el mismo día; al final no te acordarás de por qué |
| Saltarse la migración y cargar a mano | La migración **es** parte de la evaluación |
| Dejar la contabilidad para el último día | Es la que revela todos los errores anteriores |
| Grabar la demo sin ensayar | Se nota, y es el entregable que más se ve |
| No registrar los problemas encontrados | Las lecciones aprendidas son la mitad del valor del ejercicio |

## Checklist de entrega

- [ ] Base `CAPSTONE` funcionando + respaldo restaurado y probado.
- [ ] Documento de proyecto (20–35 páginas).
- [ ] 30 casos UAT ejecutados con evidencia y defectos gestionados.
- [ ] 4 guías rápidas por rol.
- [ ] Demo grabada de 30 minutos.
- [ ] Estimación y cronograma como si fuera a venderse.
- [ ] Lecciones aprendidas + lista de lo que Odoo **no** resuelve en este caso.
- [ ] Autoevaluación con la rúbrica de 100 puntos.
