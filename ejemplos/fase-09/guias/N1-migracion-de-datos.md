# N1 — Migración de datos: el caso de los 512 clientes

> El archivo `datos/01-clientes-legado.csv` es una exportación **realista** del sistema anterior de
> ANDINA GOURMET: 512 filas con los problemas que **siempre** trae un cliente real.
> Tu trabajo es dejarlo listo para importar y **demostrar** que la carga es correcta.
>
> Soluciones y sumas de control en
> [`../soluciones/respuestas-migracion.md`](../soluciones/respuestas-migracion.md).

---

## 1. Antes de tocar el archivo: el perfilado

Nunca se importa un archivo que no se ha perfilado. Con una hoja de cálculo (o `python`/`awk`),
responde **estas preguntas y anota los números**:

| # | Pregunta | Tu respuesta |
|---|---|---|
| 1 | ¿Cuántas filas tiene el archivo? | |
| 2 | ¿Cuántos clientes están ACTIVOS y cuántos INACTIVOS? | |
| 3 | ¿Hay **nombres duplicados**? ¿Cuántas filas afecta? | |
| 4 | ¿Cuántos **RUC son inválidos** (dígito verificador o formato)? | |
| 5 | ¿Cuántos registros no tienen ciudad? | |
| 6 | ¿Cuántos no tienen correo? | |
| 7 | ¿Todos los límites de crédito son numéricos? | |
| 8 | ¿Cuál es la **suma total de los límites de crédito**? | |

> La pregunta 8 no es curiosidad: es tu **suma de control**. Si después de importar no da el mismo
> número, algo se perdió o se truncó. Es la diferencia entre "creo que se importó bien" y "puedo
> demostrar que se importó bien".

## 2. Las decisiones que hay que tomar (y consultar al cliente)

| Problema encontrado | Opciones | ¿Quién decide? |
|---|---|---|
| Clientes INACTIVOS | No migrar / migrar archivados | El cliente |
| Nombres duplicados | Fusionar / migrar ambos / revisar uno a uno | El cliente, con tu recomendación |
| RUC inválidos | Corregir con consulta a SUNAT / migrar sin RUC / no migrar | El cliente |
| Sin ciudad | Migrar igual / completar / marcar para revisión | Tú, si es menor |
| Sin correo | Migrar igual (no es obligatorio) | Tú |
| Límite de crédito con formato roto | Limpiar en tránsito | Tú |

**Regla profesional:** los problemas de **datos del negocio** los decide el cliente por escrito;
los problemas de **formato** los resuelves tú sin molestarlo. Confundir ambos hace que el cliente
sienta que le estás pasando tu trabajo, o que tú tomes decisiones que no te corresponden.

## 3. El mapeo campo a campo

Completa esta tabla antes de transformar nada:

| Campo origen | Campo Odoo | Transformación | ¿Obligatorio? |
|---|---|---|---|
| `codigo_cliente` | `id` (ID externo) | prefijo `mig.cli_` + código | Sí |
| `razon_social` | `name` | recortar espacios, normalizar mayúsculas | Sí |
| `ruc` | `vat` | validar dígito verificador; limpiar guiones | No |
| `ciudad` | `city` | tal cual | No |
| `telefono` | `phone` | normalizar prefijo +51 | No |
| `email` | `email` | validar formato | No |
| `limite_credito` | *(campo a crear con Studio)* | quitar `S/` y separadores | No |
| `estado` | `active` | ACTIVO → True, INACTIVO → False | Sí |
| — | `customer_rank` | fijo `1` | Sí |
| — | *(ninguna)* | `is_company` es **calculado** en v19: sale de `vat`. No se mapea | — |
| — | `country_id/id` | fijo `base.pe` | No |

> Fíjate en el último bloque: hay campos que **no vienen del origen** y que hay que añadir con un
> valor fijo. Olvidarlos es la causa de que los clientes migrados no aparezcan en Ventas
> (`customer_rank`) o queden como personas en vez de empresas (`is_company`, que Odoo deduce del `vat`).

## 4. El campo que no existe: `limite_credito`

El sistema viejo maneja un límite de crédito que Odoo no tiene de fábrica.
**Esta es la decisión de personalización de la fase** (ver `N2`):

1. ¿Se necesita de verdad, o basta con la condición de pago?
2. Si se necesita: ¿solo informativo o debe **bloquear** ventas al superarlo?
3. Informativo → un campo con Studio. Bloqueante → automatización o desarrollo.

Para el ejercicio: crea el campo con Studio, migra el dato y añade una **regla de aprobación**
cuando un pedido haga que el cliente supere su límite.

## 5. El proceso de carga

```
1. Perfilar (§1)                          → números anotados
2. Decidir con el cliente (§2)            → por escrito
3. Mapear (§3)                            → tabla completa
4. Transformar el archivo                 → archivo limpio + archivo de descartes
5. Crear el campo faltante con Studio     → antes de importar
6. Probar importación con 20 filas        → corregir
7. Importar completo                      → anotar cuántos registros creó
8. Validar con sumas de control (§6)      → demostrar
9. Documentar y archivar los descartes    → trazabilidad
```

**El archivo de descartes es obligatorio.** Todo registro que decidiste no migrar debe quedar en un
archivo con el motivo. Cuando dentro de seis meses el cliente pregunte "¿y el cliente X?",
la respuesta está ahí, no en tu memoria.

## 6. Validación post-carga

| Control | Origen | En Odoo | ✔ |
|---|---|---|---|
| Nº de registros creados | | | |
| Nº de clientes activos | | | |
| Nº de archivados | | | |
| Suma de límites de crédito | | | |
| Muestreo de 10 registros al azar, campo por campo | | | |
| Ningún cliente sin `customer_rank` | | | |
| Ningún RUC duplicado | | | |

## 7. Reimportar: la prueba definitiva

Modifica 5 registros en tu archivo limpio y **vuelve a importar**. Si el ID externo está bien puesto,
el número total de contactos **no cambia** y los 5 se actualizan. Si crece, tu migración no es
reproducible — y una migración que no se puede repetir no sirve, porque **siempre** hay que repetirla.

## 8. Plan de reversión

Antes de la carga definitiva en producción:

- [ ] Respaldo de la base **antes** de importar (y probado).
- [ ] Los registros importados llevan un ID externo con prefijo identificable (`mig.`), de modo que
      se puedan localizar y archivar en bloque si hay que deshacer.
- [ ] Criterio escrito de "cuándo se aborta la carga y se restaura".
- [ ] Ventana de tiempo acordada con el cliente y responsable de la decisión.
