# Fase 10 — Localización peruana y administración de la plataforma

**Horas estimadas:** 30–35 h · **Prerrequisitos:** Fase 4 (obligatoria) · **Base:** `PE` (nueva) + `SANDBOX`

> **Objetivo:** poder implementar Odoo en Perú **de verdad**: comprobantes electrónicos ante SUNAT,
> plan contable local, retenciones/detracciones, libros electrónicos; y administrar la plataforma:
> hosting, respaldos, entornos, actualizaciones de versión y multiempresa.
>
> *(Si tu mercado no es Perú, sustituye la localización por la de tu país en el mismo índice de
> [localizaciones fiscales](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations.html);
> la estructura del estudio es idéntica.)*

---

## 📓 Cuaderno de ejemplos de esta fase

Datos y casos en **[`../ejemplos/fase-10/`](../ejemplos/fase-10/README.md)**: 12 clientes peruanos
con RUC y DNI usando los ID externos reales de la localización, 8 productos con casos tributarios
distintos (gravado, exonerado, gratuito, ICBPER), guía de instalación paso a paso, el
**manual de 10 errores de facturación electrónica** y la **matriz de hosting** con recomendación
por perfil de cliente.

## 1. Resultados de aprendizaje

1. Instalar y configurar la localización peruana **antes** de operar, y explicar qué trae.
2. Emitir factura, boleta, nota de crédito y nota de débito electrónicas en modo de prueba.
3. Configurar el proveedor de envío a SUNAT (PSE/OSE o IAP) y diagnosticar rechazos.
4. Manejar retenciones, detracciones, percepciones y tipos de cambio SUNAT.
5. Explicar el estado de los libros electrónicos (PLE/SIRE) y qué se resuelve fuera de Odoo.
6. Elegir hosting con criterio y gestionar respaldos, entornos y actualizaciones de versión.
7. Configurar y operar un escenario **multiempresa/multimoneda**.

## 2. Mapa de contenidos y fuentes

| # | Tema | Fuente |
|---|---|---|
| 10.1 | Localizaciones fiscales (marco) | [finance/fiscal_localizations.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations.html) |
| 10.2 | **Localización de Perú** | [fiscal_localizations/peru.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations/peru.html) |
| 10.3 | Facturación electrónica (marco general) | [customer_invoices/electronic_invoicing.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/customer_invoices/electronic_invoicing.html) |
| 10.4 | Multimoneda (repaso Fase 4) | [get_started/multi_currency.html](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/accounting/get_started/multi_currency.html) |
| 10.5 | Multiempresa | [general/companies/multi_company.html](https://www.odoo.com/documentation/saas-19.4/es/applications/general/companies/multi_company.html) |
| 10.6 | Administración e implementación | [administration.html](https://www.odoo.com/documentation/saas-19.4/es/administration.html) · [hosting.html](https://www.odoo.com/documentation/saas-19.4/es/administration/hosting.html) |
| 10.7 | Odoo Online | [administration/odoo_online.html](https://www.odoo.com/documentation/saas-19.4/es/administration/odoo_online.html) |
| 10.8 | Odoo.sh | [administration/odoo_sh.html](https://www.odoo.com/documentation/saas-19.4/es/administration/odoo_sh.html) · [odoo_sh/getting_started.html](https://www.odoo.com/documentation/saas-19.4/es/administration/odoo_sh/getting_started.html) |
| 10.9 | Local (on-premise) | [administration/on_premise.html](https://www.odoo.com/documentation/saas-19.4/es/administration/on_premise.html) |
| 10.10 | Actualización de versión | [administration/upgrade.html](https://www.odoo.com/documentation/saas-19.4/es/administration/upgrade.html) |
| 10.11 | Versiones soportadas | [administration/supported_versions.html](https://www.odoo.com/documentation/saas-19.4/es/administration/supported_versions.html) |
| 10.12 | Base neutralizada | [administration/neutralized_database.html](https://www.odoo.com/documentation/saas-19.4/es/administration/neutralized_database.html) |
| 10.13 | Normativa (fuente externa obligatoria) | <https://www.sunat.gob.pe> — comprobantes electrónicos, detracciones, SIRE |
| 10.14 | Módulos de comunidad y terceros | <https://apps.odoo.com/apps/modules> · <https://github.com/OCA> |

## 3. Ruta de estudio paso a paso

### Bloque 10.1 — Marco normativo peruano (5 h) *(estudio fuera de Odoo)*
Antes de configurar, entiende qué exige la SUNAT. Resume en tu bitácora:
1. **Tipos de comprobante**: factura, boleta, nota de crédito, nota de débito, guía de remisión,
   recibo por honorarios; y su serie/correlativo.
2. **Identificación**: RUC, DNI, CE, pasaporte; validación del documento del cliente.
3. **Tributos**: IGV 18 %, exonerado, inafecto, gratuito, ISC, ICBPER (bolsas plásticas).
4. **Detracciones**, **retenciones** y **percepciones**: cuándo aplican y quién las declara.
5. **Envío a SUNAT**: modelo OSE/PSE, CDR (constancia de recepción), estados y plazos.
6. **Libros electrónicos**: PLE/SIRE — qué exige, con qué frecuencia.
7. **Tipo de cambio SUNAT**: compra/venta, qué tipo usa cada operación.

> Este bloque es lo que te diferencia de un consultor genérico. Un cliente peruano detecta en
> 5 minutos si entiendes su realidad tributaria.

### Bloque 10.2 — Instalación y configuración de la localización (6 h)
1. Crear la base `PE` **nueva**, con país Perú y **antes de cualquier asiento** instalar el paquete
   de localización peruana + facturación electrónica.
2. Revisar qué trajo la instalación: plan contable local, impuestos, tipos de documento de identidad,
   tipos de comprobante, diarios, catálogos SUNAT.
3. Configurar la compañía: RUC, dirección con ubigeo, tipo de contribuyente, datos del certificado.
4. Configurar **diarios por tipo de comprobante** con sus series y correlativos.
5. Configurar clientes con tipo de documento y validación de RUC/DNI.
6. Configurar productos con sus códigos de tributo y unidades de medida SUNAT.

### Bloque 10.3 — Emisión electrónica en modo de prueba (7 h)
1. Configurar el modo de **prueba/certificación** y las credenciales del proveedor de envío.
2. Emitir y enviar: **factura**, **boleta**, **nota de crédito** (por anulación y por descuento),
   **nota de débito**. Verificar el estado y la respuesta (CDR).
3. Provocar rechazos a propósito y resolverlos: RUC inválido, tipo de documento incorrecto,
   impuesto mal configurado, serie no autorizada, monto que no cuadra con el detalle.
   **Documentar cada error y su solución** — este será tu manual de soporte.
4. Manejo de contingencia: qué hacer cuando SUNAT no responde; reenvío y consulta de estado.
5. Anulación / comunicación de baja.
6. Factura en **USD** con tipo de cambio: qué tipo se usa y cómo se refleja el monto en soles.

### Bloque 10.4 — Detracciones, retenciones y percepciones (4 h)
1. Configurar los impuestos y cuentas correspondientes.
2. Emitir una factura afecta a detracción y registrar su pago con depósito en cuenta de detracciones.
3. Registrar una retención de un cliente agente de retención y su efecto en el saldo por cobrar.
4. Reportes y control: qué se declara, dónde se consulta.

### Bloque 10.5 — Reportes, libros y cierre local (4 h)
1. Reportes de la localización disponibles en el estándar y su alcance real.
2. Evaluar la brecha para PLE/SIRE: ¿qué cubre Odoo, qué requiere módulo adicional, qué se hace fuera?
   **Escribir la respuesta comercial honesta.**
3. Cierre mensual peruano: IGV por pagar, renta, conciliación de comprobantes emitidos vs. contabilizados.

### Bloque 10.6 — Multiempresa y multimoneda (4 h)
1. Crear una segunda compañía (ANDINA GOURMET Chile) y configurar:
   plan de cuentas propio, moneda propia, usuarios con acceso a una o ambas.
2. Reglas de visibilidad de datos maestros compartidos (contactos, productos) vs. datos por compañía.
3. **Operaciones interempresa**: venta de una compañía a otra y su documento espejo.
4. Consolidación de reportes y sus límites.
5. Riesgos típicos: registros creados en la compañía equivocada, diarios cruzados, secuencias compartidas.

### Bloque 10.7 — Administración de la plataforma (5 h)
1. **Elegir hosting**: matriz Odoo Online / Odoo.sh / On-premise por criterio
   (módulos de terceros, acceso a datos, costo, equipo técnico disponible, cumplimiento).
2. **Respaldos**: frecuencia, restauración probada (un respaldo no probado no existe), retención.
3. **Entornos** en Odoo.sh: producción, preproducción (*staging*), desarrollo; qué se prueba en cada uno.
4. **Actualización de versión**: proceso, base de prueba, qué se rompe (personalizaciones y módulos de
   terceros), plan de pruebas y ventana de corte. Leer [upgrade.html](https://www.odoo.com/documentation/saas-19.4/es/administration/upgrade.html)
   y [supported_versions.html](https://www.odoo.com/documentation/saas-19.4/es/administration/supported_versions.html).
5. **Bases neutralizadas** para pruebas seguras (sin correos ni pagos reales).
6. Gestión de usuarios y costos de licencia: cómo se cuentan, qué es un usuario de portal, IAP.

## 4. Laboratorio integrador

**Encargo:** *"Somos una empresa peruana. Necesitamos facturar electrónicamente y que el contador
tenga sus libros."*

En la base `PE`:
1. Localización instalada y compañía configurada con RUC y datos completos.
2. 4 diarios con series por tipo de comprobante.
3. 10 clientes con RUC/DNI validados; 10 productos con configuración tributaria (gravado, exonerado, gratuito).
4. Emisión en modo de prueba de: 5 facturas, 5 boletas, 2 notas de crédito, 1 nota de débito — todas aceptadas.
5. **Bitácora de 8 rechazos provocados** con causa y solución.
6. 1 factura con detracción y 1 con retención, pagadas y conciliadas.
7. 1 factura en USD con tipo de cambio del día.
8. Segunda compañía creada con usuarios de acceso diferenciado y una operación interempresa.
9. Respaldo hecho **y restaurado** en otra base (probado, no solo descargado).

## 5. Preguntas de comprensión (prueba B)

1. ¿Por qué la localización debe instalarse antes de cualquier asiento?
2. Diferencia entre factura y boleta, y cómo se refleja en la configuración de diarios y clientes.
3. ¿Qué es el CDR y qué haces si nunca llega?
4. Un cliente exonerado en zona de selva compra un producto gravado. ¿Cómo lo configuras?
5. ¿Cómo se registra el pago de una factura afecta a detracción?
6. ¿Qué tipo de cambio usas para una factura de venta en USD y de dónde lo obtienes?
7. ¿Qué cubre Odoo de PLE/SIRE y qué no? Respuesta comercial honesta en 5 líneas.
8. Compara Odoo Online, Odoo.sh y on-premise para una empresa peruana de 25 usuarios con 2 módulos de terceros.
9. ¿Qué pasa con las personalizaciones de Studio y los módulos de terceros al actualizar de versión?
10. ¿Cómo pruebas una actualización sin arriesgar la producción?
11. En multiempresa, ¿qué datos se comparten y cuáles no? Da un ejemplo de error típico.
12. ¿Qué es una base neutralizada y cuándo la usas?

## 6. Criterios de validación (gate)

- [ ] **A. A ciegas (120 min):** base nueva peruana — localización, compañía, diarios con series,
      3 clientes, 3 productos; emitir factura y boleta aceptadas en prueba, y una nota de crédito.
- [ ] **B.** ≥ 10/12 en preguntas.
- [ ] **C. Entregable 1:** *"Manual de errores de facturación electrónica"* (mínimo 8 casos: síntoma,
      causa, solución) — herramienta de soporte reutilizable en todos tus proyectos.
- [ ] **C. Entregable 2:** *"Matriz de decisión de hosting"* con recomendación argumentada para 3 perfiles de cliente.
- [ ] **D.** Respaldo restaurado exitosamente en otra base (evidencia).
- [ ] Respaldos `PE_fase10` y `LAB_fase10`.

## 7. Trampas frecuentes

| Trampa | Realidad |
|---|---|
| Instalar la localización tarde | Obliga a recrear la base. Error clásico y caro. |
| Prometer "SUNAT sale automático" | Depende del proveedor de envío, certificado, series autorizadas y configuración tributaria. |
| Ignorar detracciones y retenciones en la preventa | Aparecen en UAT y descarrilan el cronograma. |
| No probar la restauración del respaldo | Se descubre en la emergencia que el respaldo no servía. |
| Actualizar de versión sin base de prueba | Producción caída y personalizaciones rotas. |
| Multiempresa "por si acaso" | Duplica la complejidad de permisos y reportes; se justifica o no se activa. |
