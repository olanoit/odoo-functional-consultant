# O0 — Guía completa de la localización peruana (Odoo 19 · saas~19.4)

> **Qué es esta guía.** La referencia de consulta de la Fase 10: todo lo que la localización
> peruana trae, cómo se configura y qué se rompe. Las otras tres guías de la fase son de trabajo:
> [O1](O1-instalacion-localizacion-pe.md) es el paso a paso del laboratorio,
> [O2](O2-manual-de-errores-sunat.md) el manual de errores y
> [O3](O3-hosting-y-administracion.md) la matriz de hosting.
>
> **Cómo se escribió.** Partiendo de la
> [documentación oficial de saas-19.4](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations/peru.html)
> y **contrastando cada dato contra una base real** con los diez módulos `l10n_pe*` instalados
> (Odoo 19 saas~19.4, CE + EE, empresa peruana con plan contable `pe`). Los nombres de campo,
> las listas de valores y los conteos que aparecen abajo **salen de la base, no de la documentación**.
> Donde ambas fuentes discrepan se dice cuál gana y por qué.
>
> Los enlaces externos se comprobaron uno a uno el **24 de agosto de 2026**.

---

## 1. El vocabulario, antes de tocar nada

Si no puedes explicar estos seis términos en una reunión, no configures todavía.

| Término | Qué es | Por qué te importa como consultor |
|---|---|---|
| **SUNAT** | Superintendencia Nacional de Aduanas y de Administración Tributaria | La autoridad. Valida o rechaza cada comprobante |
| **CPE** | Comprobante de Pago Electrónico | El documento (factura, boleta, NC, ND) en formato XML firmado |
| **OSE** | Operador de Servicios Electrónicos | Un tercero autorizado que valida el CPE **en nombre de** SUNAT ([definición oficial](https://cpe.sunat.gob.pe/aliados/ose)) |
| **PSE** | Proveedor de Servicios Electrónicos | Un tercero que **emite por ti**; se registra ante SUNAT ([padrón oficial en PDF](https://www.sunat.gob.pe/orientacion/padrones/pse/ProveedoresServiciosElectronicos-PSE.pdf)) |
| **CDR** | Constancia de Recepción | El XML que devuelve SUNAT/OSE. **Es la prueba legal** de que el comprobante existe |
| **Credenciales SOL** | SUNAT Operaciones en Línea: usuario y clave | Sin ellas no hay envío directo ni GRE |

> **La confusión que más caro se paga.** OSE y PSE no son lo mismo y un cliente puede necesitar
> ambos. Con el servicio IAP de Odoo el OSE es **Estela (antes Digiflow)** y hay que **afiliarlo en
> el portal de SUNAT**: si el cliente no hace ese trámite, Odoo firma correctamente y SUNAT
> rechaza igual. No es un problema de Odoo y no se resuelve desde Odoo.

---

## 2. Los módulos: lo que hay de verdad

Verificado sobre la instalación: **diez** módulos `l10n_pe*`, no cinco.

| Módulo | Edición | Qué aporta |
|---|---|---|
| `l10n_pe` | **Community** | Plan de cuentas PCGE, impuestos, tipos de identificación, tipos de documento, distritos |
| `l10n_pe_edi` | Enterprise | Firma y envío a OSE/SUNAT, CDR, anulaciones. **El corazón de la localización** |
| `l10n_pe_edi_stock` | Enterprise | Guía de Remisión Electrónica (GRE) |
| `l10n_pe_edi_withholding` | Enterprise | Comprobantes de **retención** |
| `l10n_pe_reports` | Enterprise | RVIE 14.4, RCE 8.4 y 8.5, PLE 5.1 / 5.3 / 6.1 / 1.1 / 1.2 |
| `l10n_pe_reports_lib` | Enterprise | Base de los informes de inventario y balances |
| `l10n_pe_reports_stock` | Enterprise | PLE 12.1 y 13.1 (inventario permanente) |
| `l10n_pe_reports_stock_landed_costs` | Enterprise | PLE de inventario con costos en destino |
| `l10n_pe_pos` | **Community** | Documentos peruanos en Punto de Venta |
| `l10n_pe_edi_pos` | Enterprise | Emisión electrónica desde el Punto de Venta |

**Solo `l10n_pe` y `l10n_pe_pos` son Community.** Todo lo demás —incluida la facturación
electrónica— exige Enterprise. Es el primer dato que va en una propuesta económica, antes que
cualquier estimación de horas.

### ⚠️ Dos módulos que la documentación cita y **no existen** en saas-19.4

Comprobado en el código fuente de esta versión:

| La documentación dice | Realidad en saas~19.4 |
|---|---|
| Instalar `l10n_pe_edi_stock_20` para la GRE 2.0 | **No existe.** La GRE 2.0 está dentro de `l10n_pe_edi_stock`: los campos de credenciales de la API GRE (`l10n_pe_edi_stock_client_id`, `_client_secret`, `_client_username`, `_client_password`) ya están en `res.company` con solo ese módulo |
| Instalar `l10n_pe_website_sale` para el eCommerce peruano | **No existe** en esta versión |

Si sigues la documentación al pie de la letra buscarás en Aplicaciones dos módulos que no aparecen
y perderás una tarde. Este es exactamente el motivo por el que el método de este plan es
*"documentación primero, base de datos después, y gana la base de datos"*.

---

## 3. Configuración

### 3.1 Empresa

| Campo (técnico) | Etiqueta | Nota |
|---|---|---|
| `country_id` | País | **Perú**. Determina qué localización instala Odoo |
| `vat` | NIF | Con formato **RUC** (11 dígitos) |
| `l10n_pe_edi_address_type_code` | Address Type Code | Código de establecimiento que SUNAT asigna al registrar el RUC. Si se desconoce: `0000` |

**No existe** un campo «tipo de contribuyente»: si lo buscas por un tutorial antiguo, perderás el
rato. Lo que sí hay, y casi nadie configura, son otros dos campos de reporte:

| Campo | Para qué |
|---|---|
| `l10n_pe_financial_statement_type` | Tipo de estado financiero para el PLE. **9 valores** según el organismo supervisor (SMV sector diverso, seguros, banca, AFP, agentes de intermediación, fondos de inversión, fideicomisos, ICLV, otros). El habitual en una empresa no supervisada es `09 - Otros` |
| `l10n_pe_shareholder_ids` | Accionistas *(lo aporta `l10n_pe_reports_lib`)*, necesarios para algunos reportes societarios |

> Un `address_type_code` incorrecto **no falla al guardar**: falla al validar el comprobante, días
> después, con un error que no menciona el campo. Confírmalo con el cliente en el levantamiento.

### 3.2 Plan de cuentas

Se instala solo, basado en el **PCGE** vigente y compatible con NIIF. En la base de referencia:
**1 268 cuentas** con la localización limpia.

**Paso que casi todos se saltan:** el tipo de plan para el PLE 5.3 no viene definido. Ve a
*Contabilidad → Ajustes → Facturación electrónica peruana* y rellena `l10n_pe_chart_of_accounts`.
Las ocho opciones reales son:

| Valor | Plan |
|---|---|
| `1` | Plan contable general empresarial *(el habitual)* |
| `2` | Plan contable revisado |
| `3` | Empresas del sistema financiero (SBS) |
| `4` | Prestadoras de servicios de salud (SBS) |
| `5` | Empresas del sistema de seguros (SBS) |
| `6` | Administradoras privadas de fondos de pensiones (SBS) |
| `7` | Plan contable gubernamental |
| `99` | Otros |

Sin este dato los reportes PLE salen vacíos o mal formados.

### 3.3 Proveedor de firma: la decisión que define el proyecto

El campo es `res.company.l10n_pe_edi_provider` y tiene **tres** valores:

| Valor | Etiqueta en v19 | Certificado | Credenciales SOL | Cuándo elegirlo |
|---|---|---|---|---|
| `iap` | IAP | **Lo pone Odoo** | No | Por defecto. La vía rápida: sin certificado propio ni contrato con un OSE |
| `digiflow` | **Estela (formerly Digiflow)** | Propio (`.pfx`) | Sí | El cliente ya tiene contrato con Estela |
| `sunat` | SUNAT | Propio (`.pfx`) | Sí | Envío directo, sin OSE. Exige superar la **certificación SUNAT** |

> **Ojo al nombre.** En Odoo 19 la etiqueta es **«Estela (formerly Digiflow)»**: Estela compró
> Digiflow y la interfaz ya recoge el cambio, pero la documentación oficial y casi todos los
> tutoriales siguen diciendo «Digiflow». Es el mismo proveedor. El valor técnico sigue siendo
> `digiflow`.

**Sobre IAP.** Odoo regala **1 000 créditos** en bases nuevas; después se compran por paquetes
(1 000 / 5 000 / 10 000 / 20 000, tarificados en EUR). Se consume **un crédito por envío**, y un
reenvío tras un rechazo **consume otro**. Dicho de otro modo: los errores de datos maestros se
pagan en dinero, no solo en tiempo. Eso justifica el laboratorio [O2](O2-manual-de-errores-sunat.md)
ante el cliente mejor que cualquier argumento técnico.

Con IAP quedan **dos trámites del cliente en el portal de SUNAT**, que Odoo no puede hacer por él:
afiliar a Estela/Digiflow como su **OSE** y registrarlo como **PSE** autorizado.

**Si el cliente pone su propio certificado**, necesita un `.pfx` con su contraseña, comprado a una
entidad del registro oficial. La lista de proveedores autorizados está en
[certificados digitales de SUNAT](https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/),
que remite al registro ROPS de INDECOPI.

> **Formato del usuario SOL con conexión directa a SUNAT:** RUC **pegado** al usuario, sin espacios
> ni separadores — `20121888549JOHNSMITH`. Es causa de error frecuente y silenciosa.

### 3.4 Entorno de prueba

`l10n_pe_edi_test_env` es un **booleano**, no una lista. Y el valor por defecto es **producción**:
una base recién instalada emite en real salvo que marques la casilla.

Con entorno de prueba + IAP, las transacciones se validan solas y **no gastan créditos**.

> **La GRE no tiene entorno de prueba.** SUNAT no lo ofrece. Las guías de remisión que generes por
> error se emiten de verdad y hay que darlas de baja **desde el portal de SUNAT**, no desde Odoo.
> Avísalo por escrito antes de que el usuario clave empiece a probar.

### 3.5 Multimoneda

El tipo de cambio oficial lo publica SUNAT y Odoo puede descargarlo automáticamente. Actívalo
antes de la primera factura en dólares: el importe en soles del comprobante se calcula con ese
tipo de cambio y es lo que SUNAT contrasta.

---

## 4. Datos maestros

### 4.1 Tipos de identificación — los 11 reales

`l10n_latam_identification_type_id` en el contacto. Verificados con su código SUNAT y su ID externo:

| ID externo | Código | Documento |
|---|---|---|
| `l10n_pe.it_RUC` | 6 | RUC |
| `l10n_pe.it_DNI` | 1 | DNI |
| `l10n_pe.it_NDTD` | 0 | Documento tributario no domiciliado |
| `l10n_pe.it_DIC` | A | Carné de identidad diplomática |
| `l10n_pe.it_IDCR` | B | Documento del país de residencia |
| `l10n_pe.it_TIN` | C | Tax Identification Number |
| `l10n_pe.it_IN` | D | Identification Number |
| `l10n_pe.it_TAM` | E | TAM |
| `l10n_pe.it_PTP` | F | PTP |
| `l10n_pe.it_SP` | G | Salvoconducto |
| `l10n_pe.it_CPP` | H | Permiso temporal / permanente |

**No hay «carné de extranjería»** en la lista peruana de v19, y el **pasaporte** no pertenece a esta
localización: es `l10n_latam_base.it_pass`, genérico latinoamericano y **sin país asignado**. Para un
extranjero domiciliado se usa `it_IDCR` (documento del país de residencia) o `it_CPP`.

> **Consecuencia de v19 que hay que tener presente:** `res.partner.company_type` desapareció e
> `is_company` es **calculado**. Quien decide si el contacto es empresa o persona es, en la
> práctica, el **tipo de identificación**. En un CSV de migración se importa
> `l10n_latam_identification_type_id/id`, nunca `is_company`. Está en
> [`../datos/01-clientes-pe.csv`](../datos/01-clientes-pe.csv).

### 4.2 Tipos de documento

**60 tipos** cargados para Perú. Los que se usan a diario:

| Código | Documento | `internal_type` |
|---|---|---|
| `01` | Factura | `invoice` |
| `03` | Boleta | `invoice` |
| `07` | Nota de Crédito *(y Nota de Crédito Boleta)* | `credit_note` |
| `08` | Nota de Débito *(y Nota de Débito Boleta)* | `debit_note` |
| `20` | Comprobante de retención | — |
| `09` | Guía de Remisión Remitente | *(GRE)* |
| `31` | Guía de Remisión Transportista | *(GRE)* |

> Odoo solo soporta en facturación de cliente: **factura, boleta, nota de crédito y nota de
> débito**. Los otros 56 existen como catálogo —para clasificar documentos de proveedor— pero no
> los emite. Si el cliente pide emitir una liquidación de compra (`04`), la respuesta es *no de
> serie*, y hay que decirlo en el GAP-FIT, no en la UAT.

Los códigos `07` y `08` aparecen **dos veces** cada uno (versión factura y versión boleta). No es
un error de datos: la serie es distinta según el comprobante que rectifican.

### 4.3 Impuestos y sus campos EDI

La documentación habla de «tres nuevos campos». En v19 son **cinco** en `account.tax`:

| Campo | Para qué |
|---|---|
| `l10n_pe_edi_tax_code` | Código de tributo SUNAT (`1000` IGV, `9996` gratuito, `9997` exonerado, `9998` inafecto, `9995` exportación) |
| `l10n_pe_edi_unece_category` | Categoría UNECE (`S` gravado, `E` exento, `Z` tasa cero) |
| `l10n_pe_edi_affectation_reason` | Motivo de afectación por defecto |
| `l10n_pe_edi_international_code` | `VAT` / `FRE` |
| `l10n_pe_edi_isc_type` | Tipo de ISC (impuesto selectivo al consumo) |

Los impuestos que instala la localización ya los traen. Los verificados:

| Impuesto | Tributo | UNECE | Afectación |
|---|---|---|---|
| VAT 18% | 1000 | S | 10 |
| 0% Exo *(exonerado)* | 9997 | E | 20 |
| 0% Ina *(inafecto)* | 9998 | Z | 30 |
| 0% Gra *(gratuito)* | 9996 | E | 11 |
| 0% Exp *(exportación)* | 9995 | S | 40 |

> **⚠️ El impuesto que creas a mano no sirve para facturar.** Un impuesto nuevo sin estos campos se
> aplica bien en el asiento y **se rechaza en SUNAT**. Es una trampa real de este cuaderno: los
> impuestos de [`../../fase-04/datos/03-impuestos.csv`](../../fase-04/datos/03-impuestos.csv) están
> pensados para la base `LAB` y **no** llevan configuración EDI. Sirven para aprender contabilidad,
> no para emitir. En la base `PE` usa los de la localización.

### 4.4 Posiciones fiscales

Dos, creadas por la localización y ambas con aplicación automática:

- **LOCAL PERU** — clientes locales.
- **FOREIGN - EXPORT** — exportación.

### 4.5 Diarios y series

Al crear un diario de ventas:

| Campo | Valor |
|---|---|
| `l10n_latam_use_documents` | **Activado** (viene así por defecto en ventas) |
| Flujo EDI | **Peru UBL 2.1** |

> **Desmarca `Factur-X (FR)` a mano.** Aparece siempre por defecto, es el estándar francés, y no
> tiene nada que hacer en una base peruana. La propia documentación lo advierte.

**Un diario por serie.** Cada tipo de documento tiene su secuencia dentro del diario donde se
asigna. La correspondencia serie ↔ diario ↔ tipo de documento se acuerda con el contador **antes**
de emitir, porque cambiarla después obliga a dar de baja comprobantes.

### 4.6 Contactos: el ubigeo

`l10n_pe` carga **196 ciudades** y **1 874 distritos** peruanos (modelo
`l10n_pe.res.city.district`, campo `res.partner.l10n_pe_district`).

El **distrito no es decorativo**: forma parte del ubigeo que viaja en el XML. Una dirección con
«Lima» y sin distrito genera rechazo. En una migración de contactos es el campo que más trabajo de
limpieza exige, porque en el sistema antiguo casi nunca viene normalizado.

> **Cambio de v19 que afecta a los datos bancarios:** el modelo `res.bank` **ya no existe**. Las
> cuentas bancarias viven en `res.partner.bank`. Un script de migración de proveedores que cree
> bancos con el modelo antiguo falla con `KeyError`.

### 4.7 Productos

| Campo | Cuándo es obligatorio |
|---|---|
| Código UNSPSC | Facturación electrónica |
| `l10n_pe_edi_tariff_fraction` (partida arancelaria) | GRE |
| `l10n_pe_type_of_existence` | Reportes PLE 12.1 / 13.1 (tabla 5 de SUNAT) |
| `l10n_pe_withhold_code`, `l10n_pe_withhold_percentage` | Retenciones |
| `weight` | GRE — un peso `0.00` **rompe la guía** (error 2325) |

---

## 5. Emitir un comprobante

### 5.1 Los tres campos EDI de la factura

| Campo | Dónde | Nota |
|---|---|---|
| Tipo de documento | Cabecera | Por defecto factura; cámbialo a boleta cuando toque |
| `l10n_pe_edi_operation_type` | Cabecera | **21 opciones**. Por defecto `0101` venta interna; `0200` exportación de bienes; `1001` detracciones |
| `l10n_pe_edi_affectation_reason` | **Línea** | **19 opciones**, heredadas del impuesto. Aquí se distingue gravado / exonerado / inafecto / gratuito / exportación |

Los motivos de afectación agrupan así: `10–17` gravado, `20–21` exonerado, `30–37` inafecto,
`40` exportación. Los retiros (bonificación, donación, premio, muestras médicas) tienen código
propio dentro de cada grupo: **no es lo mismo regalar que vender a cero**, y SUNAT lo distingue.

### 5.2 El ciclo

Validar la factura registra el asiento **y** dispara el flujo electrónico. `l10n_pe_edi_status`
tiene tres estados:

| Estado | Significado |
|---|---|
| `to_send` | Listo para enviar. Lo manda un cron **cada hora**, o tú con *Enviar ahora* |
| `sent` | Aceptado. Se descarga el ZIP y el CDR queda en el chatter |
| `cancelled` | Baja aceptada |

Es **asíncrono**: contabilizar no es enviar. Un rechazo deja el estado en `to_send`, con el error
en la parte superior del documento.

> **Cómo corregir, según dónde esté el error:** si está en un dato maestro (cliente, impuesto),
> corrige el registro y pulsa **Reintentar**. Si está en la factura (tipo de operación, líneas),
> hay que **restablecer a borrador**, corregir y reenviar. Confundir los dos caminos es la causa
> número uno de créditos IAP quemados.

Una vez aceptado, el PDF sale con **código QR**: es la marca de documento fiscal válido.

### 5.3 Anulación

Botón **Solicitar cancelación** con un motivo obligatorio. Genera un ticket, y el CDR de la baja
queda en el chatter. **Consume un crédito.**

---

## 6. Casos especiales

| Caso | Lo que hay que hacer |
|---|---|
| **Exportación** | Cliente con identificación extranjera + tipo de operación de exportación + impuestos EXP. Los tres a la vez |
| **Detracción** | Tipo de operación **`1001`** y los campos de detracción del producto configurados. En la factura: `l10n_pe_detraction_date` y `l10n_pe_detraction_number` |
| **Anticipos** | SUNAT **no admite negativos** en las declaraciones. Odoo documenta un rodeo largo: facturar el anticipo, crear la factura final sin la línea de anticipo, emitir una nota de crédito con una línea manual descriptiva y conciliarla contra la factura final |
| **Gratuitas** | Impuesto `0% Gra` **y** motivo de afectación de retiro (`11`–`16` según el motivo). Solo el impuesto no basta |

> El caso de los **anticipos** es el que más se subestima. No es un clic: son siete pasos manuales
> y hay que documentárselos al usuario clave con capturas, o no lo hará bien ni una vez.

---

## 7. Guía de Remisión Electrónica (GRE 2.0)

Obligatoria para trasladar bienes, salvo régimen RUS.

**Odoo emite la guía de *remitente*. La de *transportista* no está soportada.** Si el cliente mueve
mercancía con transporte público necesita **las dos**, y la segunda tendrá que salir de otro
sistema. Esto se pregunta en el levantamiento, no en el go-live.

| Tipo de transporte | Valor | Guías necesarias |
|---|---|---|
| Público | `01` | Remitente **+ transportista** *(esta última fuera de Odoo)* |
| Privado | `02` | Solo remitente |

**La GRE va siempre directa a SUNAT**, use el cliente IAP, Estela o SUNAT como proveedor de firma.
Por eso necesita credenciales propias, configuradas en *Inventario → Configuración → Ajustes*:

| Campo | Contenido |
|---|---|
| `l10n_pe_edi_stock_client_id` | Client ID de la API GRE, generado en el portal SUNAT |
| `l10n_pe_edi_stock_client_secret` | Client Secret |
| `l10n_pe_edi_stock_client_username` | **RUC + usuario SOL** pegados (`20557912879USUARIOSOL`) |
| `l10n_pe_edi_stock_client_password` | Clave del usuario SOL |

El procedimiento para obtenerlas está en el
[manual de servicios web de la plataforma GRE (PDF de SUNAT)](https://cpe.sunat.gob.pe/sites/default/files/inline-files/Manual_Servicios_GRE%20%281%29.pdf).
Suele hacer falta **un segundo usuario SOL**, con permisos distintos a los de la facturación.

**Motivos de traslado** (`l10n_pe_edi_reason_for_transfer`), los 8 reales: `01` venta ·
`03` venta con entrega a terceros · `04` traslado entre establecimientos de la misma empresa ·
`05` consignación · `13` otros · `14` venta sujeta a confirmación · `17` traslado para
transformación · `18` traslado de emisor itinerante.

> **Trampa documentada:** los motivos `03` y `12` fallan en Odoo porque exigen un cliente que el
> flujo deja vacío. Y `13` (otros) provoca el error `cac:BuyerCustomerParty`. En la práctica se
> trabaja con `01` y `04`.

**Lo demás que hay que dar de alta:** el *operador* (conductor, contacto tipo persona con licencia
y distrito), el *transportista* (contacto tipo empresa con número MTC, entidad emisora y número de
autorización), y los *vehículos* en *Inventario → Configuración → Vehículos* (modelo
`l10n_pe_edi.vehicle`: matrícula, marca M1/L, autorización especial, operador por defecto).

Marca **¿Es M1 o L?** si el vehículo tiene menos de cuatro ruedas u ocho asientos — motos y
mototaxis, que en reparto urbano peruano son la norma.

Para generar la guía, el albarán debe estar **Listo**; entonces aparece *Generar Guía de Remisión*.

> **Vocabulario de SUNAT:** las guías **no se anulan, se «dan de baja»**. Y solo si el envío no ha
> empezado, o cambiando el destinatario antes del destino final.

---

## 8. Retenciones — lo que la documentación no cuenta

`l10n_pe_edi_withholding` **existe y funciona**, y la página oficial de la localización no lo
menciona. Añade el comprobante de retención (documento `20`) y, en `account.payment`, los campos
`withhold`, `withholding_line_ids`, `withholding_amount` y `withholding_net_amount`.

Si el cliente es **agente de retención** designado por SUNAT, este módulo es obligatorio y no
aparecerá en ninguna estimación hecha leyendo solo la documentación. Pregunta siempre por él en el
levantamiento.

---

## 9. Reportes

### 9.1 SIRE: RVIE y RCE

El **SIRE** es el sistema con el que SUNAT genera los registros de ventas y compras a partir de
los comprobantes electrónicos. Odoo produce, verificados en la base:

| Informe | Qué es |
|---|---|
| VAT Report (RVIE Sales 14.4) | Registro de Ventas e Ingresos |
| VAT Report (RCE Purchase 8.4) | Registro de Compras |
| VAT Report (RCE Purchase 8.5) | Compras con sujetos no domiciliados |

SUNAT publica un cronograma de incorporación **por fases** —julio 2023, octubre 2023, agosto 2024,
enero 2025 y julio 2025— que a día de hoy alcanza a todos los obligados a llevar registro de
ventas y compras, principales contribuyentes incluidos
([cronograma oficial](https://emprender.sunat.gob.pe/comprobantes-libros/registros-libros-electronicos/sistema-integrado-registros-electronicos-sire)).

> **Verifica siempre el estado vigente.** Ha habido prórrogas y periodos de regularización sin
> sanción, y las fechas se mueven. Antes de comprometer un alcance, consulta el
> [portal del SIRE](https://sire.sunat.gob.pe/) y las páginas de
> [RVIE](https://emprender.sunat.gob.pe/comprobantes-libros/registros-libros-electronicos/registro-ventas-e-ingresos-electronico-rvie)
> y [RCE](https://emprender.sunat.gob.pe/comprobantes-libros/registros-libros-electronicos/registro-compras-electronico-rce).
> Un plan de estudios no es fuente normativa; SUNAT sí.

### 9.2 PLE

`l10n_pe_reports` genera **PLE 5.1** (diario), **5.3** (plan de cuentas), **6.1** (mayor),
**1.1** (caja) y **1.2** (bancos). Recuerda el ajuste de la §3.2.

### 9.3 PLE 12.1 y 13.1 — inventario permanente

Los da `l10n_pe_reports_stock`. **12.1** lleva unidades físicas; **13.1**, unidades y valores.
Semestrales (enero–junio y julio–diciembre) con detalle mensual; presentación el **1 de octubre**
y el **1 de abril** respectivamente (R. S. N° 169-2015).

Tres requisitos que hay que dejar cerrados **antes** de operar, porque son retroactivos y no se
arreglan al cierre:

1. **Producto** → `l10n_pe_type_of_existence` según la tabla 5 de SUNAT.
2. **Valoración automática** y **método de costo distinto de estándar** — los reportes se
   alimentan de los asientos que generan los movimientos de stock. Con precio estándar no hay nada
   que leer.
3. **Almacén** → `l10n_pe_anexo_establishment_code`, numérico de 4 a 7 dígitos.

Y en cada transferencia hay que elegir el **tipo de operación PE** (`l10n_pe_operation_type`,
**47 valores** de la tabla 12 de SUNAT: venta nacional, compra nacional, consignación recibida y
entregada, devoluciones, bonificación, premio, donación, salida de producción, traslado entre
almacenes, retiro, merma, deterioro, destrucción, saldo inicial…).

Los libros se descargan en **.txt** desde el informe de valoración de inventario, botón *PLE
Reports*, y se cargan en el software PLE de SUNAT. **No hay vista previa dentro de Odoo**: se
descarga a ciegas.

> Enlaza esto con la Fase 3: el método de costo que se eligió allí **determina** si el cliente
> puede cumplir con el PLE 13.1. Si alguien configuró precio estándar «porque es más simple»,
> el incumplimiento aparece meses después.

---

## 10. Punto de venta y comercio electrónico

**PdV.** `l10n_pe_pos` (Community) permite editar los datos fiscales del cliente desde el TPV;
`l10n_pe_edi_pos` (Enterprise) emite el comprobante electrónico. El tipo de documento sale del
identificador: **RUC → factura, DNI → boleta**.

**eCommerce.** El módulo `l10n_pe_website_sale` que cita la documentación **no existe en
saas-19.4** (§2). Lo que sí aplica del flujo documentado, y conviene comprobar en la versión que
tengas delante:

- Política de facturación **Cantidades pedidas** en los productos.
- Métodos de envío con proveedor **Precio fijo** y precio **mayor que cero**: el envío entra como
  línea de factura. Para envío gratis, no dejes 0.00 — usa **0.01** o quita el producto de envío,
  o SUNAT rechaza la factura.
- Un **precio de venta** definido en el producto de envío.

> Ese detalle del céntimo conecta con la corrección que este cuaderno ya aplicó en la Fase 8:
> los métodos de envío necesitan **su propio producto de servicio**, no reciclar uno del catálogo.

---

## 11. Checklist de puesta en marcha

Orden real. Cada punto bloquea al siguiente.

- [ ] Base **nueva** con país Perú *(la localización va antes que el primer asiento)*
- [ ] RUC en el NIF de la empresa y `address_type_code` confirmado con el cliente
- [ ] Tipo de plan de cuentas para PLE 5.3 seleccionado
- [ ] Proveedor de firma decidido, con su coste en la propuesta
- [ ] Si no es IAP: certificado `.pfx` cargado y credenciales SOL con el formato RUC+usuario
- [ ] Si es IAP: **el cliente** afilió a Estela/Digiflow como OSE y lo registró como PSE
- [ ] **Entorno de prueba activado** *(por defecto está en producción)*
- [ ] Tipo de cambio SUNAT conectado
- [ ] Diarios con documentos activados y flujo **Peru UBL 2.1**; `Factur-X` desmarcado
- [ ] Series acordadas por escrito con el contador
- [ ] Clientes con tipo de identificación cargado
- [ ] Productos con UNSPSC; con partida arancelaria y **peso ≠ 0** si habrá GRE
- [ ] Si habrá PLE de inventario: tipo de existencia, valoración automática, costo ≠ estándar y código de establecimiento
- [ ] Si es agente de retención: `l10n_pe_edi_withholding` instalado
- [ ] Primera factura de prueba **aceptada con CDR** antes de tocar producción
- [ ] Prueba de anulación completada
- [ ] Créditos IAP suficientes para el primer mes

---

## 12. Fuentes

Comprobadas el **24 de agosto de 2026**.

### Oficiales de Odoo

| Recurso | Enlace |
|---|---|
| Localización de Perú (saas-19.4, la versión de este plan) | <https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations/peru.html> |
| Localización de Perú (19.0) | <https://www.odoo.com/documentation/19.0/es/applications/finance/fiscal_localizations/peru.html> |
| Smart Tutorial — Localización de Perú *(15 lecciones en español)* | <https://www.odoo.com/slides/smart-tutorial-localizacion-de-peru-133> |
| App Tour — Localización de Perú *(vídeo)* | <https://youtu.be/Ic3mGovkf8Y> |

### Oficiales de SUNAT

| Recurso | Enlace |
|---|---|
| Portal principal | <https://www.sunat.gob.pe> |
| Comprobantes de Pago Electrónicos (CPE) | <https://cpe.sunat.gob.pe/> |
| Qué es un OSE | <https://cpe.sunat.gob.pe/aliados/ose> |
| Certificados digitales autorizados | <https://cpe.sunat.gob.pe/informacion_general/certificados_digitales/> |
| Padrón de PSE *(PDF)* | <https://www.sunat.gob.pe/orientacion/padrones/pse/ProveedoresServiciosElectronicos-PSE.pdf> |
| Manual de servicios web GRE *(PDF)* | <https://cpe.sunat.gob.pe/sites/default/files/inline-files/Manual_Servicios_GRE%20%281%29.pdf> |
| Guía de remisión | <https://www.gob.pe/7899-guia-de-remision> |
| SIRE — portal | <https://sire.sunat.gob.pe/> |
| SIRE — qué es y cronograma | <https://emprender.sunat.gob.pe/comprobantes-libros/registros-libros-electronicos/sistema-integrado-registros-electronicos-sire> |
| RVIE | <https://emprender.sunat.gob.pe/comprobantes-libros/registros-libros-electronicos/registro-ventas-e-ingresos-electronico-rvie> |
| RCE | <https://emprender.sunat.gob.pe/comprobantes-libros/registros-libros-electronicos/registro-compras-electronico-rce> |

### Proveedores y utilidades

| Recurso | Enlace |
|---|---|
| Estela *(antes Digiflow)* — OSE/PSE del servicio IAP | <https://www.digiflow.pe/> |
| Consulta de validez de comprobante — Estela OSE | <https://consulta.ose.pe/> |
| Catálogo de códigos de error SUNAT/OSE *(~1 000 códigos)* | <https://www.nubefact.com/codigos-error-sunat/> |

> El catálogo de errores es de un proveedor privado (Nubefact), no de SUNAT, pero es la lista más
> completa y consultable que existe. Úsalo para **diagnosticar**; para citar normativa, SUNAT.

---

## 13. Qué hacer ahora

1. Monta la base `PE` con [O1](O1-instalacion-localizacion-pe.md) y esta guía al lado.
2. Emite, rechaza y anula a propósito con [O2](O2-manual-de-errores-sunat.md).
3. Contrasta **cada dato de esta guía** contra tu propia base. Si algo no coincide, gana tu base:
   la localización se actualiza con cada versión y esta guía se escribió contra saas~19.4 en
   agosto de 2026.

> Lo que llevarte a un cliente: **la documentación oficial de una localización va siempre un poco
> por detrás del código**. Aquí eran dos módulos inexistentes y un proveedor renombrado. Verificar
> antes de prometer no es desconfianza; es el trabajo.
