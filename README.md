# Plan de Estudios — Consultor Funcional Odoo 19 (saas-19.4)

Ruta de aprendizaje completa, por fases, para pasar de "usuario que conoce Odoo"
a **consultor funcional capaz de levantar, diseñar, configurar, probar, capacitar
y poner en marcha** una implementación Odoo.

- **Documentación base:** <https://www.odoo.com/documentation/saas-19.4/es/>
- **Idioma de estudio:** español (la doc oficial en ES es la fuente primaria; cuando
  una página no esté traducida, se usa la versión EN cambiando `/es/` por `/en/`).
- **Versión objetivo:** Odoo 19 / saas-19.4.

---

## 1. Cómo está organizado este plan

| Archivo | Para qué sirve |
|---|---|
| [`00-metodo-y-entorno.md`](00-metodo-y-entorno.md) | **Léelo primero.** Método de estudio, entorno de práctica, reglas del juego, cómo se valida cada fase. |
| [`fases/`](fases/) | Una carpeta con las 12 fases. Cada fase es autocontenida: qué estudiar, dónde, qué laboratorio hacer, cómo validar y cuándo avanzar. |
| [`ejemplos/`](ejemplos/) | Cuadernos de casos prácticos por fase: datos listos para importar, laboratorios guiados y soluciones. Se construyen fase a fase. **Disponibles: Fases 1 a 11.** |
| [`plantillas/`](plantillas/) | Documentos de trabajo reales de consultoría (levantamiento, GAP-FIT, UAT, demo, migración de datos, bitácora). Se usan **desde la Fase 1**, no al final. |
| [`recursos.md`](recursos.md) | Catálogo de recursos verificados: doc, eLearning oficial, YouTube, foro, apps, certificación. |
| [`seguimiento.md`](seguimiento.md) | Tablero de progreso con casillas por fase y registro de horas. |

## 2. Mapa de fases

| # | Fase | Foco | Horas (est.) | Entregable |
|---|---|---|---|---|
| 1 | [Fundamentos y base de datos](fases/fase-01-fundamentos.md) | Interfaz, modelo de datos, usuarios, permisos, importación, ajustes generales | 25–30 h | DB base configurada + guía de navegación |
| 2 | [Ventas y CRM](fases/fase-02-ventas-crm.md) | CRM, cotizaciones, listas de precios, facturación de ventas, suscripciones, alquiler, PdV | 35–40 h | Ciclo Order-to-Cash documentado |
| 3 | [Compras e Inventario](fases/fase-03-compras-inventario.md) | Compras, almacenes, rutas, lotes/series, reabastecimiento, valoración | 45–50 h | Ciclo Procure-to-Pay + diseño de almacén multi-etapa |
| 4 | [Contabilidad y Finanzas](fases/fase-04-contabilidad-finanzas.md) | Plan contable, impuestos, conciliación, activos, analítica, reportes | 50–60 h | Cierre mensual simulado + juego de reportes |
| 5 | [Manufactura, Calidad, Mantenimiento](fases/fase-05-manufactura-calidad.md) | LdM, órdenes de trabajo, subcontratación, MPS, PLM, calidad | 35–40 h | Caso de planta con 3 niveles de LdM |
| 6 | [Servicios: Proyectos, Hojas de horas, Soporte](fases/fase-06-servicios-proyectos.md) | Proyecto, timesheets, helpdesk, servicio de campo, planeación | 25–30 h | Modelo de negocio de servicios facturables |
| 7 | [Recursos Humanos](fases/fase-07-rrhh.md) | Empleados, asistencias, ausencias, reclutamiento, evaluaciones, nómina | 25–30 h | Ciclo Hire-to-Retire |
| 8 | [Sitio web, eCommerce y Marketing](fases/fase-08-website-ecommerce-marketing.md) | Website, eCommerce, eLearning, email/SMS/social, automatización, eventos, encuestas | 30–35 h | Tienda funcional + campaña automatizada |
| 9 | [Productividad, Studio y Datos](fases/fase-09-productividad-studio-datos.md) | Conversaciones, Documentos, Firma, Conocimiento, Hojas de cálculo, Studio, importación masiva | 30–35 h | App a medida sin código + tablero ejecutivo |
| 10 | [Localización PE y Administración](fases/fase-10-localizacion-pe-administracion.md) | Localización peruana, facturación electrónica, hosting, actualizaciones, multiempresa | 30–35 h | DB peruana emitiendo comprobantes en modo prueba |
| 11 | [Metodología de implementación](fases/fase-11-metodologia-implementacion.md) | Levantamiento, GAP-FIT, demo, migración de datos, UAT, go-live, soporte | 30–35 h | Kit de consultoría completo |
| 12 | [Capstone y certificación](fases/fase-12-capstone-certificacion.md) | Proyecto integral de punta a punta + examen funcional oficial | 40–60 h | Implementación simulada + certificación |

**Total:** ~400–480 h de trabajo efectivo.

## 3. Dos velocidades

| Ritmo | Dedicación | Duración | Perfil |
|---|---|---|---|
| **Intensivo** | 25–30 h/semana | 16–18 semanas (~4 meses) | Dedicación casi exclusiva |
| **Sostenido** | 10–12 h/semana | 36–40 semanas (~9 meses) | Estudio en paralelo al trabajo |

Regla: **nunca avanzar de fase por calendario, solo por criterio de validación cumplido.**
Si una fase toma el doble de lo estimado, se toma el doble. El calendario es una
estimación; el *gate* de salida es el contrato.

## 4. Orden y dependencias

```
Fase 1 (obligatoria, base de todo)
   │
   ├── Fase 2 ──┐
   ├── Fase 3 ──┼──► Fase 4  (Contabilidad necesita ver ventas, compras e inventario primero)
   │            │
   │            └──► Fase 5  (Manufactura necesita Inventario)
   │
   ├── Fase 6, 7, 8   (independientes entre sí; pueden reordenarse según el mercado objetivo)
   │
   └── Fase 9 ──► Fase 10 ──► Fase 11 ──► Fase 12
```

Reordenamientos permitidos:
- Si el objetivo inmediato es **retail/comercio**, adelantar Fase 3 antes que Fase 2.
- Si el objetivo es **empresa de servicios**, adelantar Fase 6 antes que Fase 3.
- Las Fases 1, 4, 9, 11 y 12 **no se saltan nunca**: son el núcleo del perfil funcional.

## 5. Qué significa "consultor funcional" en este plan

No es "saber usar Odoo". Al terminar debes poder, frente a un cliente real:

1. **Entrevistar** y levantar el proceso actual (AS-IS) sin sesgo de producto.
2. **Traducir** ese proceso al modelo de datos y flujos estándar de Odoo (TO-BE).
3. **Identificar el GAP** y decidir: configuración → Studio → desarrollo → cambio de proceso.
4. **Configurar** el estándar con criterio (y saber *por qué* cada casilla).
5. **Demostrar** el flujo con datos del cliente, no con datos demo.
6. **Migrar** los datos maestros e históricos con integridad.
7. **Probar** (UAT) con casos escritos y trazabilidad de defectos.
8. **Capacitar** al usuario final y dejar documentación.
9. **Acompañar** el go-live y el cierre contable del primer mes.
10. **Estimar y comunicar**: horas, riesgos, alcance, lo que Odoo NO hace.

Cada fase entrena una parte de esa lista; la Fase 11 y la 12 las integran.

## 6. Cómo empezar hoy

1. Leer completo [`00-metodo-y-entorno.md`](00-metodo-y-entorno.md) (~30 min).
2. Montar el entorno de práctica que ahí se describe (~1–2 h).
3. Copiar [`plantillas/07-bitacora-de-estudio.md`](plantillas/07-bitacora-de-estudio.md) como `bitacora.md`.
4. Abrir [`fases/fase-01-fundamentos.md`](fases/fase-01-fundamentos.md) y ejecutar el Bloque 1.1.
5. Marcar avances en [`seguimiento.md`](seguimiento.md).

> **Cuadernos de ejemplos:** cada fase tendrá el suyo en [`ejemplos/`](ejemplos/) —datos de ejemplo
> listos para importar, configuración paso a paso, errores provocados a propósito y soluciones.
> **Ya disponibles:** [`fase-01`](ejemplos/fase-01/README.md), [`fase-02`](ejemplos/fase-02/README.md) [`fase-03`](ejemplos/fase-03/README.md) [`fase-04`](ejemplos/fase-04/README.md) [`fase-05`](ejemplos/fase-05/README.md) [`fase-06`](ejemplos/fase-06/README.md) [`fase-07`](ejemplos/fase-07/README.md) [`fase-08`](ejemplos/fase-08/README.md) [`fase-09`](ejemplos/fase-09/README.md) [`fase-10`](ejemplos/fase-10/README.md) y [`fase-11`](ejemplos/fase-11/README.md). Los demás se generan a medida
> que avanzas: se planifican de uno en uno, cuando llegues a la fase.
