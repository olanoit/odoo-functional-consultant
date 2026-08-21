# Fase 9 — Productividad, Studio y gestión de datos

**Horas estimadas:** 30–35 h · **Prerrequisitos:** Fases 1 a 4 (mínimo) · **Base:** `LAB` + `SANDBOX`

> **Objetivo:** adquirir las dos capacidades que multiplican el valor de un consultor funcional:
> **(a)** personalizar Odoo sin programar (Studio, automatizaciones, reportes) y
> **(b)** dominar los datos (importación masiva, hojas de cálculo, tableros).
> Aquí es donde dejas de "configurar apps" y empiezas a **diseñar soluciones**.

⚠️ Studio es **Enterprise**. Si trabajas en Community, esta fase requiere una prueba Enterprise u Odoo Online.

---

## 1. Resultados de aprendizaje

1. Usar Conversaciones, Calendario, Conocimiento, Documentos y Firma como herramientas de proceso.
2. Construir tableros ejecutivos con Hojas de cálculo conectadas en vivo a los datos de Odoo.
3. Crear con Studio: campos, vistas, filtros, menús, modelos nuevos y una app completa.
4. Diseñar reportes PDF personalizados (formato de factura, guía, etiqueta).
5. Configurar automatizaciones (acciones automatizadas) y reglas de aprobación sin código.
6. Ejecutar migraciones de datos complejas con relaciones, ID externos y validación posterior.
7. **Decidir con criterio** entre: configurar / Studio / módulo de terceros / desarrollo / cambiar el proceso.

## 2. Mapa de contenidos y fuentes

| # | Tema | Documentación |
|---|---|---|
| 9.1 | Conversaciones (Discuss) | [productivity/discuss.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/discuss.html) |
| 9.2 | Calendario | [productivity/calendar.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/calendar.html) |
| 9.3 | Conocimiento | [productivity/knowledge.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/knowledge.html) |
| 9.4 | Documentos | [productivity/documents.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/documents.html) |
| 9.5 | Firma electrónica | [productivity/sign.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/sign.html) |
| 9.6 | Hojas de cálculo | [productivity/spreadsheet.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/spreadsheet.html) · [spreadsheet/insert.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/spreadsheet/insert.html) |
| 9.7 | VoIP | [productivity/voip.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/voip.html) |
| 9.8 | WhatsApp | [productivity/whatsapp.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/whatsapp.html) |
| 9.9 | Limpieza de datos | [productivity/data_cleaning.html](https://www.odoo.com/documentation/saas-19.4/es/applications/productivity/data_cleaning.html) |
| 9.10 | **Studio** (índice) | [applications/studio.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio.html) |
| 9.11 | Studio · Campos | [studio/fields.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio/fields.html) |
| 9.12 | Studio · Vistas | [studio/views.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio/views.html) |
| 9.13 | Studio · Modelos, módulos y apps | [studio/models_modules_apps.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio/models_modules_apps.html) |
| 9.14 | Studio · Acciones automatizadas | [studio/automated_actions.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio/automated_actions.html) |
| 9.15 | Studio · Reportes PDF | [studio/pdf_reports.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio/pdf_reports.html) |
| 9.16 | Studio · Reglas de aprobación | [studio/approval_rules.html](https://www.odoo.com/documentation/saas-19.4/es/applications/studio/approval_rules.html) |
| 9.17 | Importación/exportación (repaso profundo) | [essentials/export_import_data.html](https://www.odoo.com/documentation/saas-19.4/es/applications/essentials/export_import_data.html) |
| 9.18 | Integraciones y IoT | [general/integrations.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/integrations.html) · [general/iot.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/iot.html) |
| 9.19 | Derechos de acceso y usuarios de portal | [users/access_rights.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/users/access_rights.html) · [users/portal.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/users/portal.html) |

## 3. Ruta de estudio paso a paso

### Bloque 9.1 — Herramientas de productividad (5 h)
1. **Conversaciones**: canales por equipo/proyecto, mensajes directos, integración con el chatter.
2. **Calendario**: sincronización, tipos de reunión, disponibilidad y agendamiento en línea (citas).
3. **Conocimiento**: construir el manual interno de ANDINA GOURMET con artículos anidados, plantillas,
   vistas incrustadas de Odoo y artículos compartidos con el cliente. **Úsalo para tu propia documentación.**
4. **Documentos**: espacios de trabajo, etiquetas, reglas de clasificación, flujos de aprobación,
   digitalización de facturas de proveedor (enlace con Fase 4).
5. **Firma**: plantillas con campos, roles de firmantes, orden de firma, validez y trazabilidad.
   Caso: contrato de distribuidor y contrato de trabajo (Fase 7).

### Bloque 9.2 — Hojas de cálculo y tableros (6 h)
1. Insertar una lista/pivote de Odoo en una hoja de cálculo y ver la **actualización en vivo**.
2. Funciones de Odoo dentro de la hoja (lectura de datos del modelo) y filtros dinámicos por período.
3. Construir el **tablero gerencial de ANDINA GOURMET**: ventas vs. objetivo, margen por línea,
   rotación de inventario, antigüedad de cobros, rentabilidad de proyectos.
4. Tableros compartidos, permisos y exportación.
5. Comparar: ¿cuándo un reporte nativo, cuándo una hoja de cálculo, cuándo una herramienta BI externa?

### Bloque 9.3 — Studio: personalización sin código (10 h)
1. **Campos**: agregar campos de todos los tipos (texto, selección, relacional, calculado con fórmula,
   relacionado, monetario, binario). Entender qué implica cada uno en la base de datos.
2. **Vistas**: modificar formularios (pestañas, grupos, invisibilidad condicional, obligatoriedad condicional,
   solo lectura), listas, kanban, calendario, gantt, pivote, gráfico, cohorte y mapa.
3. **Filtros y agrupaciones** por defecto; ordenar y colorear registros por condición.
4. **Modelos nuevos**: crear una app propia desde cero. Caso: *"Registro de visitas a distribuidores"*
   con estados, responsable, relación con contactos y reporte.
5. **Menús y accesos**: dónde aparece, quién lo ve, permisos por grupo.
6. **Reportes PDF**: personalizar la factura (logo, datos fiscales, términos), crear una etiqueta de
   producto y una guía de remisión simple.
7. **Acciones automatizadas**: al crear/actualizar/eliminar, con dominio de filtro y acción
   (actualizar campo, crear actividad, enviar correo, ejecutar código). Casos:
   - avisar al gerente cuando una oportunidad supera S/ 50 000,
   - crear una actividad de seguimiento al confirmar una venta a un cliente nuevo,
   - bloquear el paso de etapa si falta un dato.
8. **Reglas de aprobación**: descuentos mayores al 20 %, órdenes de compra sobre cierto monto.
9. **Exportar la personalización** como módulo (concepto) y por qué importa para migrar entre bases.

> **Romper:** agregar un campo obligatorio en un modelo con datos existentes y ver qué ocurre.
> Después, hacerlo obligatorio *condicionalmente*. Diferencia entre "obligatorio" y "obligatorio si".

### Bloque 9.4 — El criterio: configurar vs. Studio vs. desarrollar (4 h)
Construye tu **árbol de decisión** y escríbelo (será entregable):

```
¿El estándar ya lo hace?
 ├── Sí → configurar. Documentar la configuración.
 └── No → ¿el requerimiento es real o es costumbre del proceso viejo?
      ├── Costumbre → proponer cambio de proceso (opción más barata y la que menos se ofrece)
      └── Real → ¿se resuelve con campos/vistas/automatizaciones simples?
           ├── Sí → Studio. Riesgo: mantenimiento y actualizaciones.
           └── No → ¿existe módulo de terceros confiable (apps.odoo.com)?
                ├── Sí → evaluar: versión, mantenedor, código, soporte, costo
                └── No → desarrollo a medida: especificar, estimar, y advertir el costo de actualización
```
Reglas prácticas:
- Toda personalización tiene **costo de por vida** (cada actualización de versión).
- Studio no es gratis: es deuda técnica ligera. Documenta cada cambio.
- El desarrollo se especifica por escrito **antes** de cotizar, con criterios de aceptación.

### Bloque 9.5 — Datos: migración y calidad (6 h)
1. Diseñar el **plan de migración** de ANDINA GOURMET: qué migrar (maestros, saldos, históricos),
   qué no migrar y por qué, en qué orden (dependencias), con qué corte.
2. Orden canónico de carga: compañías → contactos → categorías/UdM → productos → listas de precios →
   plan de cuentas → saldos iniciales → stock inicial → documentos abiertos (facturas por cobrar/pagar,
   pedidos y órdenes pendientes).
3. Ejecutar una migración real de prueba con 500+ registros y relaciones cruzadas.
4. **Validación post-carga**: conteos, sumas de control (total por cobrar, valor de inventario),
   muestreo manual y reporte de discrepancias.
5. **Limpieza de datos**: duplicados, formatos, reglas de deduplicación y fusión de contactos.
6. Estrategia de reversión: qué haces si la carga sale mal a 2 días del go-live.

## 4. Laboratorio integrador

**Encargo:** *"Necesitamos registrar las visitas de nuestros vendedores a distribuidores, que el
gerente apruebe descuentos altos, tener nuestra factura con nuestro diseño y un tablero de dirección."*

En `LAB`:
1. App nueva con Studio: *Visitas a distribuidores* (modelo propio, 8 campos, kanban por estado,
   vista calendario y mapa, reporte pivote, menú propio con permisos).
2. Regla de aprobación para descuentos > 20 % en pedidos de venta.
3. 3 acciones automatizadas útiles y documentadas.
4. Factura PDF personalizada con identidad de ANDINA GOURMET.
5. Tablero gerencial en hoja de cálculo con 6 indicadores en vivo.
6. Migración de 500 registros con validación documentada (sumas de control incluidas).
7. Árbol de decisión de personalización, escrito con 3 ejemplos reales del propio LAB.

## 5. Preguntas de comprensión (prueba B)

1. ¿Qué diferencia hay entre un campo relacionado y uno calculado? Ejemplo de cada uno.
2. ¿Cuándo un campo debe ser "invisible condicional" en vez de eliminarse de la vista?
3. ¿Qué riesgos tiene una personalización de Studio al actualizar de versión?
4. Describe una acción automatizada que evite un error humano frecuente en ventas.
5. ¿Cómo se comparte un tablero con la gerencia sin darles acceso a todo Odoo?
6. ¿Cuál es el orden correcto de carga de datos y por qué importa?
7. ¿Qué sumas de control usarías para validar una migración contable?
8. Un cliente pide un campo obligatorio nuevo con 10 000 registros ya cargados. ¿Qué haces?
9. ¿Cómo evalúas un módulo de terceros antes de recomendarlo?
10. Un requerimiento no lo hace el estándar y el cliente insiste. Explica cómo lo abordas paso a paso.

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (90 min):** crear con Studio un modelo nuevo con 6 campos, 3 vistas, un menú,
      una acción automatizada y un reporte PDF, funcionando.
- [ ] **B.** ≥ 8/10 en preguntas.
- [ ] **C. Entregable 1:** *"Árbol de decisión de personalización"* con 3 casos resueltos.
- [ ] **C. Entregable 2:** *"Plan de migración de datos"* usando
      [`../plantillas/05-plan-de-migracion-de-datos.md`](../plantillas/05-plan-de-migracion-de-datos.md).
- [ ] Respaldo `LAB_fase09`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Usar Studio como primera respuesta | El 60 % de los "requerimientos" se resuelven configurando o ajustando el proceso. |
| Personalizar sin documentar | En la siguiente versión nadie sabe por qué existe ese campo. |
| Migrar históricos completos "por si acaso" | Multiplica el costo y el riesgo. Se migra lo que se usa, el resto se archiva. |
| Validar la migración "a ojo" | Sin sumas de control, los errores aparecen en el primer cierre contable. |
| Prometer tableros sin definir la fuente del dato | Indicadores que nadie puede reproducir ni auditar. |
