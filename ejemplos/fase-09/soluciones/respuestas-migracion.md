# Soluciones — N1: perfilado y validación de los 512 clientes

> Números exactos del archivo `datos/01-clientes-legado.csv`.
> Si tu perfilado no coincide, revisa cómo estás contando (espacios, mayúsculas, formatos).

---

## 1. Perfilado del archivo

| # | Control | Valor |
|---|---|---|
| 1 | Filas totales | **512** |
| 2 | Clientes ACTIVO / INACTIVO | **434 / 78** |
| 3 | Nombres duplicados | **13 nombres**, que afectan a **27 filas** |
| 4 | RUC inválidos o con formato roto | **14** (8 con dígito verificador incorrecto + 6 con guiones) |
| 5 | Sin ciudad | **10** |
| 6 | Sin correo | **55** |
| 7 | Límites con formato no numérico | **7** (traen `S/` y separador de miles) |
| 8 | **Suma de límites de crédito** | **S/ 3 776 000** |

**Cómo se cuentan los duplicados correctamente:** normalizando antes de comparar
(`strip()` + mayúsculas). Hay 5 registros con espacios al inicio y el nombre en mayúsculas: si
comparas el texto tal cual, esos duplicados **no aparecen** y se migran repetidos.
Ese detalle —normalizar antes de comparar— es lo que separa un perfilado real de uno aparente.

## 2. Qué hacer con cada problema

| Problema | Decisión recomendada | Quién decide |
|---|---|---|
| 78 INACTIVOS | Migrar **archivados** (`active = False`): conservan historial y no estorban | Cliente |
| 27 filas duplicadas | **Revisar una a una**: pueden ser sucursales reales del mismo grupo | Cliente |
| 14 RUC malos | Migrar **sin RUC** y entregar la lista para que el cliente los complete | Cliente |
| 10 sin ciudad | Migrar igual; no es obligatorio | Consultor |
| 55 sin correo | Migrar igual; se completan al operar | Consultor |
| 7 límites con formato | Limpiar en tránsito: quitar `S/`, puntos y espacios | Consultor |
| 5 nombres con espacios/mayúsculas | Normalizar: `strip()` y capitalización | Consultor |

> **Ojo con los duplicados:** la tentación es fusionarlos automáticamente. No lo hagas.
> *"Distribuidora Sol de Oro S.A.C."* puede ser la matriz y la sucursal, con RUC distinto y
> condiciones distintas. Fusionar dos clientes reales es un error que se descubre facturando.

## 3. Validación post-carga esperada

Si migras **todos** los registros (activos + archivados), sin fusionar duplicados:

| Control | Valor esperado |
|---|---|
| Contactos creados con prefijo `mig.` | 512 |
| Activos | 434 |
| Archivados | 78 |
| Suma de límites de crédito | 3 776 000 |
| Con `customer_rank = 1` | 512 |
| Con `is_company = True` | 512 *(calculado por Odoo a partir del `vat`; no se importa)* |
| Con RUC cargado | 498 |

Si el cliente decide **no migrar los inactivos**, los números cambian a 434 creados y la suma de
límites baja: **recalcula la suma de control sobre el archivo filtrado**, no sobre el original.
Este es el error más común al validar: comparar contra el número equivocado y concluir que faltan datos.

## 4. El error que más veces se comete

Importar el archivo **sin la columna `id`** (ID externo). Todo parece salir bien: 512 contactos
creados. Pero al detectar un error de mapeo y volver a importar, quedan **1 024 contactos**.
Y en ese punto ya no hay forma limpia de saber cuál es cuál, salvo restaurar el respaldo.

Por eso el ID externo es la primera columna del mapeo, y por eso el paso 7 de la guía —modificar
5 registros y reimportar— es obligatorio **antes** de la carga en producción.

## 5. Los tres números que se entregan al cliente

Al terminar una migración, el entregable no es "ya está cargado". Son tres números y un archivo:

1. **Cuántos registros se migraron** y cuántos se descartaron.
2. **Qué sumas de control cuadran** (importes, conteos) y con qué valores exactos.
3. **Cuántos registros requieren acción del cliente** (los 14 RUC, los 27 duplicados).
4. El **archivo de descartes** con el motivo de cada uno.

Con eso, la migración es auditable. Sin eso, es un acto de fe.
