# O1 — Instalación y configuración de la localización peruana

> **La regla que no se negocia:** la localización se instala en una base **nueva**, antes de
> registrar cualquier asiento. Instalarla tarde obliga a recrear la base. Es el error más caro
> y más frecuente en implantaciones peruanas.

---

## 1. Los módulos y qué aporta cada uno

| Módulo | Edición | Qué aporta |
|---|---|---|
| `l10n_pe` | Community | Plan contable peruano, impuestos, **tipos de identificación** (RUC, DNI, CE, pasaporte), tipos de documento, catálogo de ciudades y **distritos** (ubigeo), bancos |
| `l10n_pe_edi` | Enterprise | Facturación electrónica: envío a SUNAT/OSE, CDR, anulaciones |
| `l10n_pe_edi_stock` | Enterprise | Guía de remisión electrónica |
| `l10n_pe_pos` / `l10n_pe_edi_pos` | — | Punto de venta con comprobantes peruanos |
| `l10n_pe_reports` | Enterprise | Reportes locales |
| `l10n_pe_reports_stock` | Enterprise | Reportes de existencias (kardex) |

**Verifica siempre en tu versión** qué módulos existen y cuáles son Enterprise: cambia entre versiones.

## 2. Orden de configuración

```
1. Crear base NUEVA con país Perú
2. Instalar l10n_pe (+ l10n_pe_edi si hay Enterprise)   ← ANTES de cualquier asiento
3. Datos de la compañía: RUC, dirección con distrito, tipo de contribuyente
4. Certificado digital y credenciales del proveedor de envío
5. Modo de PRUEBA activado (l10n_pe_edi_test_env)
6. Diarios por tipo de comprobante, con serie y correlativo
7. Clientes con tipo de documento y número validado
8. Productos con su configuración tributaria
9. Recién entonces: emitir
```

## 3. Datos de la compañía

| Campo | Valor para ANDINA GOURMET |
|---|---|
| Nombre | ANDINA GOURMET S.A.C. |
| Tipo de identificación | **RUC** |
| RUC | 20510211015 |
| Dirección | Av. Los Frutales 1250, **distrito** Ate, Lima, Perú |
| Código de establecimiento | `0000` (el que SUNAT tenga registrado) |
| Proveedor de envío | IAP / OSE / SUNAT directo |
| Entorno | **Prueba** mientras se implementa |

> El **distrito** (`l10n_pe_district`) no es un campo decorativo: forma parte del ubigeo que se
> reporta a SUNAT. Cargar solo "Lima" sin distrito genera rechazos.

## 4. Clientes: tipo de documento

El archivo `01-clientes-pe.csv` trae 8 empresas con **RUC** y 4 personas con **DNI**, usando los
ID externos reales de la localización:

| Tipo | ID externo |
|---|---|
| RUC | `l10n_pe.it_RUC` |
| DNI | `l10n_pe.it_DNI` |

**Ejercicio de ruptura:** intenta emitir una factura a un cliente con DNI y una boleta a uno con RUC.
Anota qué permite Odoo, qué avisa y qué diría SUNAT. Esa distinción —**factura para RUC, boleta para
DNI**— es la primera que hay que explicar al usuario.

## 5. Diarios y series

| Diario | Tipo | Serie | Uso |
|---|---|---|---|
| Facturas de venta | Venta | F001 | Clientes con RUC |
| Boletas de venta | Venta | B001 | Consumidores finales |
| Notas de crédito | Venta | FC01 / BC01 | Según el comprobante que corrigen |
| Notas de débito | Venta | FD01 / BD01 | Según el comprobante |
| Compras | Compra | — | Facturas de proveedor |

**Las series deben estar autorizadas ante SUNAT.** Emitir con una serie no autorizada es rechazo seguro.

## 6. Productos y tributos

Cada producto necesita su afectación correcta. En el archivo `02-productos-pe.csv` hay casos
deliberadamente distintos para que configures cada uno:

| Producto | Afectación esperada | Por qué |
|---|---|---|
| Conserva, snack, harina, néctar | Gravado 18 % | Operación normal |
| Servicio de flete | Gravado 18 % | Servicio afecto |
| Muestra comercial | **Gratuito** | Transferencia gratuita: tributo distinto y leyenda obligatoria |
| Libro recetario | **Exonerado** | Los libros tienen exoneración |
| Bolsa plástica | Gravado + **ICBPER** | Impuesto al consumo de bolsas plásticas |

**Ejercicio:** configura los cinco casos y emite una factura con todos en la misma boleta.
Revisa cómo se agrupan los tributos en el PDF y en el XML.

## 7. Checklist antes de emitir el primer comprobante

- [ ] Localización instalada **antes** de cualquier asiento.
- [ ] RUC de la compañía correcto y con distrito.
- [ ] Certificado digital cargado y vigente.
- [ ] Credenciales del proveedor probadas.
- [ ] **Entorno de prueba activado** (`l10n_pe_edi_test_env`).
- [ ] Series creadas y autorizadas.
- [ ] Clientes con tipo y número de documento válidos.
- [ ] Productos con afectación tributaria revisada uno por uno.
- [ ] Impuestos con sus líneas de repartición y cuentas (Fase 4).
- [ ] Un comprobante de cada tipo emitido y **aceptado** en prueba.

## 8. Errores frecuentes de configuración

| Error | Consecuencia |
|---|---|
| Instalar la localización tarde | Hay que recrear la base entera |
| No cargar el distrito | Rechazos por ubigeo |
| Series no autorizadas | Rechazo en el primer envío |
| Cliente con RUC en boleta (o al revés) | Comprobante rechazado o inválido |
| Olvidar el entorno de prueba | **Se emiten comprobantes reales** durante las pruebas |
| Muestras gratuitas sin la leyenda | Comprobante rechazado |
| Copiar la configuración de otro cliente | Cada empresa tiene su régimen y sus series |
