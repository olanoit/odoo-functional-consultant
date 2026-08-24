# Cuaderno de ejemplos — Fase 10: Localización peruana y administración

Casos prácticos para [`../../fases/fase-10-localizacion-pe-administracion.md`](../../fases/fase-10-localizacion-pe-administracion.md).

> ⚠️ **Base nueva.** Esta fase **no** se hace sobre `LAB`. Se crea la base `PE` desde cero, porque la
> localización debe instalarse **antes de cualquier asiento contable**. Es la regla que más veces se
> incumple y la que más caro se paga.

*(Si tu mercado no es Perú, sustituye por la localización de tu país desde el
[índice de localizaciones fiscales](https://www.odoo.com/documentation/saas-19.4/es/applications/finance/fiscal_localizations.html);
la estructura del cuaderno es la misma.)*

---

## Contenido

| Archivo | Qué es |
|---|---|
| `datos/01-clientes-pe.csv` | 12 clientes: 8 empresas con **RUC** y 4 personas con **DNI**, con los ID externos reales de la localización. En v19 es `l10n_latam_identification_type_id` quien determina si el contacto es empresa o persona (`is_company` es calculado) |
| `datos/02-productos-pe.csv` | 8 productos con casos tributarios deliberadamente distintos (gravado, exonerado, gratuito, con ICBPER) |
| `guias/O1` | Instalación y configuración de la localización, paso a paso |
| `guias/O2` | **Manual de errores de facturación electrónica** (10 casos) — entregable |
| `guias/O3` | **Matriz de hosting**, actualizaciones y multiempresa — entregable |

## Módulos de la localización (verificados en v19)

| Módulo | Edición | Aporta |
|---|---|---|
| `l10n_pe` | Community | Plan contable, impuestos, tipos de identificación (`l10n_pe.it_RUC`, `l10n_pe.it_DNI`), ciudades y **distritos** |
| `l10n_pe_edi` | Enterprise | Envío a SUNAT/OSE, CDR, anulaciones |
| `l10n_pe_edi_stock` | Enterprise | Guía de remisión electrónica |
| `l10n_pe_pos`, `l10n_pe_edi_pos` | — | Punto de venta con comprobantes peruanos |
| `l10n_pe_reports`, `l10n_pe_reports_stock` | Enterprise | Reportes locales y kardex |

---

## Ejemplo 1 — Estudiar la norma antes de tocar Odoo
*(Bloque 10.1 · 5 h · fuera del sistema)*

Resume en tu bitácora, con fuente en <https://www.sunat.gob.pe>:
tipos de comprobante y sus series · tipos de documento de identidad · IGV, exonerado, inafecto,
gratuito, ICBPER · detracciones, retenciones y percepciones · el circuito OSE/PSE y el CDR ·
libros electrónicos (PLE/SIRE) · tipo de cambio SUNAT compra/venta.

**No es teoría prescindible:** un cliente peruano detecta en cinco minutos si entiendes su realidad
tributaria, y de eso depende que te tome en serio.

## Ejemplo 2 — Instalar y configurar
*(Bloque 10.2 · 90 min)*

Sigue [`guias/O1-instalacion-localizacion-pe.md`](guias/O1-instalacion-localizacion-pe.md):
base nueva, localización, compañía con RUC y **distrito**, certificado, **modo de prueba**,
diarios con series.

Luego importa `01-clientes-pe.csv` y `02-productos-pe.csv`.

**Verificación:** abre un cliente y comprueba que su tipo de documento es RUC o DNI según
corresponda; abre un producto y revisa su afectación tributaria.

## Ejemplo 3 — Emitir en modo de prueba
*(Bloque 10.3 · 120 min)*

1. **Factura** a una empresa con RUC → enviar → verificar CDR.
2. **Boleta** a una persona con DNI → enviar → verificar.
3. **Nota de crédito** por anulación y otra por descuento.
4. **Nota de débito** por intereses.
5. Una factura que incluya los cinco casos tributarios del catálogo (gravado, exonerado, gratuito,
   servicio, bolsa con ICBPER) y revisa cómo se agrupan los tributos en el PDF.
6. Una factura en **USD** con tipo de cambio del día: comprueba qué tipo usa y cómo se muestra el
   equivalente en soles.

## Ejemplo 4 — Provocar y resolver 8 rechazos
*(Bloque 10.3 · 90 min)* ← **el entregable de la fase**

[`guias/O2-manual-de-errores-sunat.md`](guias/O2-manual-de-errores-sunat.md): 10 errores clásicos con
su síntoma, causa, solución y prevención. Provoca al menos 8 en modo de prueba y **anota el mensaje
literal** que devuelve tu proveedor.

El documento resultante es reutilizable en **todos** tus proyectos peruanos y evita la mayor parte
de las llamadas de soporte del primer mes.

## Ejemplo 5 — Detracciones, retenciones y percepciones
*(Bloque 10.4 · 60 min)*

1. Configura los impuestos y cuentas correspondientes.
2. Emite una factura afecta a **detracción** y registra su pago con depósito en la cuenta del Banco
   de la Nación.
3. Registra una **retención** de un cliente agente de retención y observa el efecto en el saldo por cobrar.
4. Documenta qué se declara, dónde se consulta y quién lo hace.

## Ejemplo 6 — Reportes, libros y el cierre local
*(Bloque 10.5 · 60 min)*

1. Recorre los reportes de la localización disponibles en tu edición.
2. **Evalúa la brecha de PLE/SIRE**: qué cubre Odoo, qué requiere módulo adicional y qué se hace fuera.
3. Escribe la **respuesta comercial honesta** a *"¿Odoo me genera mis libros electrónicos?"*.
   Esa respuesta, junto con la de nómina (Fase 7), es lo que evita proyectos fallidos.

## Ejemplo 7 — Multiempresa
*(Bloque 10.6 · 60 min)*

[`guias/O3-hosting-y-administracion.md`](guias/O3-hosting-y-administracion.md), sección 5:
segunda compañía, qué se comparte y qué no, operación interempresa y los riesgos típicos.

## Ejemplo 8 — Administración de la plataforma
*(Bloque 10.7 · 90 min)*

Guía O3, secciones 1 a 4 y 6:
1. Completa la **matriz de hosting** con recomendación argumentada para 3 perfiles de cliente.
2. **Haz un respaldo y restáuralo en otra base.** Un respaldo no probado no existe.
3. Estudia el proceso de actualización de versión y qué suele romperse.
4. Prepara las respuestas sobre usuarios, portal, IAP y licencias, sin improvisar cifras.

---

## Cierre: entregables de la Fase 10

- [ ] Base `PE` con localización, compañía, diarios y series configurados.
- [ ] Factura, boleta, nota de crédito y nota de débito **aceptadas** en modo de prueba.
- [ ] **Entregable 1:** manual de errores de facturación electrónica con mínimo 8 casos vividos.
- [ ] **Entregable 2:** matriz de decisión de hosting con recomendación para 3 perfiles.
- [ ] Respaldo **restaurado** en otra base, con evidencia.
- [ ] Respuesta escrita y honesta sobre PLE/SIRE.
- [ ] Segunda compañía con accesos diferenciados y una operación interempresa.
- [ ] Respaldos `PE_fase10` y `LAB_fase10`.
