# O2 — Manual de errores de facturación electrónica

> **Entregable C1 de la Fase 10** y la herramienta de soporte que más veces vas a usar en tu carrera.
> Se construye provocando los errores a propósito, no esperando a que aparezcan en producción.
>
> Formato: **síntoma → causa → solución → cómo evitarlo**. Amplíalo con cada caso real que encuentres.

---

## Cómo usar esta guía

1. Provoca cada error en tu base `PE` en **modo de prueba**.
2. Anota el **mensaje literal** que devuelve Odoo o el proveedor (varía según el proveedor: IAP,
   OSE o SUNAT directo).
3. Completa la columna de tu experiencia.
4. Al terminar tendrás un documento que se entrega al usuario final y que evita el 80 % de las
   llamadas de soporte del primer mes.

---

## 1. Documento de identidad no válido para el tipo de comprobante

| | |
|---|---|
| **Síntoma** | El comprobante es rechazado; el mensaje menciona el tipo de documento del receptor |
| **Causa** | Factura emitida a un cliente con DNI, o boleta a un cliente con RUC por encima del monto permitido |
| **Solución** | Corregir el tipo de documento del cliente o emitir el comprobante correcto |
| **Prevención** | Validar los tipos de documento en la migración; capacitar al facturador en la regla RUC→factura / DNI→boleta |

## 2. RUC inexistente o no habilitado

| | |
|---|---|
| **Síntoma** | Rechazo indicando que el número de documento del receptor no existe |
| **Causa** | RUC mal tecleado, con dígito verificador incorrecto, o de un contribuyente dado de baja |
| **Solución** | Verificar el RUC en el portal de SUNAT y corregirlo en la ficha del cliente |
| **Prevención** | Validación de RUC en la carga de datos (Fase 9) y consulta en línea al crear el cliente |

## 3. Serie no autorizada

| | |
|---|---|
| **Síntoma** | Rechazo por serie o correlativo |
| **Causa** | La serie del diario no está registrada ante SUNAT, o no corresponde al tipo de comprobante |
| **Solución** | Registrar la serie ante SUNAT o usar una autorizada |
| **Prevención** | Confirmar por escrito con el contador las series autorizadas **antes** de configurar los diarios |

## 4. Certificado vencido o inválido

| | |
|---|---|
| **Síntoma** | Error de firma; ningún comprobante sale |
| **Causa** | Certificado digital caducado, con contraseña incorrecta o mal cargado |
| **Solución** | Renovar y volver a cargar el certificado |
| **Prevención** | Anotar la fecha de vencimiento en el calendario del cliente y avisar 60 días antes. **Este aviso es parte del servicio de soporte y casi nadie lo da.** |

## 5. Importe declarado no cuadra con el detalle

| | |
|---|---|
| **Síntoma** | Rechazo por diferencia entre el total y la suma de las líneas o los tributos |
| **Causa** | Redondeos, descuentos mal aplicados, o un impuesto con líneas de repartición mal configuradas |
| **Solución** | Revisar la configuración del impuesto y el redondeo de la lista de precios |
| **Prevención** | Emitir un comprobante de prueba por cada combinación de impuestos **antes** del go-live |

## 6. Tipo de afectación incorrecto (gratuito, exonerado, inafecto)

| | |
|---|---|
| **Síntoma** | Rechazo relacionado con el tipo de operación o falta de leyenda |
| **Causa** | Muestra gratuita facturada como venta normal, o producto exonerado con IGV |
| **Solución** | Corregir la afectación del producto y la leyenda del comprobante |
| **Prevención** | Revisar producto por producto la afectación en la carga de datos |

## 7. Comprobante enviado fuera de plazo

| | |
|---|---|
| **Síntoma** | Aceptado con observación, o rechazado según el tipo y la antigüedad |
| **Causa** | Se emitió con fecha anterior y se envió días después |
| **Solución** | Emitir con la fecha correcta y enviar el mismo día |
| **Prevención** | Acción planificada de envío automático + revisión diaria de comprobantes no enviados |

## 8. SUNAT no responde / servicio caído

| | |
|---|---|
| **Síntoma** | Timeout, sin CDR, comprobante en estado *enviado* sin respuesta |
| **Causa** | Indisponibilidad del servicio (ocurre, y más en fin de mes) |
| **Solución** | Reintentar; consultar el estado antes de reenviar para **no duplicar** |
| **Prevención** | Procedimiento de contingencia escrito: qué hace el usuario, cuánto espera, a quién avisa |

## 9. Anulación fuera de plazo o de un comprobante ya usado

| | |
|---|---|
| **Síntoma** | La comunicación de baja es rechazada |
| **Causa** | Se intenta anular fuera del plazo permitido o un comprobante ya declarado |
| **Solución** | Emitir **nota de crédito** en lugar de anular |
| **Prevención** | Capacitar: anular ≠ nota de crédito, y cada una tiene su plazo y su uso |

## 10. Cliente sin dirección completa o sin distrito

| | |
|---|---|
| **Síntoma** | Rechazo por datos del receptor incompletos |
| **Causa** | Falta el ubigeo (departamento / provincia / distrito) |
| **Solución** | Completar la dirección con el distrito de la localización |
| **Prevención** | Incluir el distrito como campo obligatorio en la carga de clientes |

---

## Procedimiento de soporte (para el usuario final)

```
1. ¿El comprobante salió? → revisar el estado en la factura
2. ¿Hay mensaje de error? → buscarlo en este manual
3. ¿Está en la lista? → aplicar la solución y reenviar
4. ¿No está? → capturar el mensaje COMPLETO y escalar
5. NUNCA: volver a emitir el mismo comprobante sin consultar el estado
   (se generan duplicados imposibles de anular)
```

## Registro de casos nuevos

| Fecha | Síntoma | Causa | Solución | Cliente |
|---|---|---|---|---|
| | | | | |
