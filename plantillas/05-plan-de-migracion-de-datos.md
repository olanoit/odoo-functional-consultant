# Plantilla — Plan de migración de datos

**Cliente:** ____________ · **Fecha de corte prevista:** ____________ · **Responsable:** ____________

---

## 1. Inventario de fuentes

| Fuente | Sistema/archivo | Responsable del dato | Calidad estimada | Volumen | ¿Se migra? |
|---|---|---|---|---|---|
| Clientes | | | Alta/Media/Baja | | Sí/No |
| Proveedores | | | | | |
| Productos | | | | | |
| Stock inicial | | | | | |
| Plan de cuentas | | | | | |
| Saldos iniciales | | | | | |
| Cuentas por cobrar abiertas | | | | | |
| Cuentas por pagar abiertas | | | | | |
| Pedidos/órdenes pendientes | | | | | |
| Histórico de ventas | | | | | |

**Criterio de decisión:** se migra lo que se **usa operativamente**. El histórico se conserva en el
sistema anterior o en archivos, salvo justificación explícita (y presupuesto).

## 2. Orden de carga (respetar dependencias)

1. Compañías y configuración base
2. Contactos (clientes, proveedores) — con ID externo
3. Categorías de producto, unidades de medida, atributos
4. Productos y variantes
5. Listas de precios y precios de proveedor
6. Plan de cuentas, diarios, impuestos, posiciones fiscales
7. Saldos iniciales contables (asiento de apertura)
8. Stock inicial por almacén/ubicación/lote
9. Documentos abiertos (facturas por cobrar/pagar pendientes)
10. Pedidos de venta y órdenes de compra pendientes
11. Datos complementarios (empleados, proyectos, activos)

## 3. Mapeo campo a campo (una tabla por entidad)

**Entidad:** ____________

| Campo origen | Campo Odoo (técnico) | Transformación / regla | Obligatorio | Valor por defecto |
|---|---|---|---|---|
| | | | Sí/No | |

**Convención de ID externo:** `<prefijo>.<entidad>_<código origen>` — ejemplo: `mig.cli_10023`.

## 4. Reglas de limpieza

| Problema detectado | Regla de corrección | Responsable | ¿Se corrige en origen o en tránsito? |
|---|---|---|---|
| Duplicados de cliente | | | |
| RUC/DNI inválidos | | | |
| Productos sin categoría/UdM | | | |
| Precios en cero | | | |
| Saldos descuadrados | | | |

## 5. Ensayos

| Ensayo | Fecha | Alcance | Resultado | Errores encontrados | Tiempo de carga |
|---|---|---|---|---|---|
| Ensayo 1 (muestra 10 %) | | | | | |
| Ensayo 2 (completo) | | | | | |
| Ensayo 3 (final, cronometrado) | | | | | |

## 6. Validación post-carga (sumas de control)

| Control | Valor en origen | Valor en Odoo | Diferencia | ✔ |
|---|---|---|---|---|
| Nº de clientes activos | | | | |
| Nº de productos activos | | | | |
| Valor total del inventario | | | | |
| Total cuentas por cobrar | | | | |
| Total cuentas por pagar | | | | |
| Suma del debe = suma del haber (apertura) | | | | |
| Muestreo manual de 10 registros | | | | |

**Criterio de aceptación:** diferencia 0 en importes; discrepancias de conteo explicadas por escrito.

## 7. Fecha de corte y congelamiento

- Último día de operación en el sistema anterior: ____________
- Ventana de carga final: ____________
- Qué se hace con las operaciones ocurridas durante la ventana: ____________
- Comunicación a los usuarios (quién, cuándo, por qué medio): ____________

## 8. Plan de reversión

| Escenario | Señal de alarma | Acción | Responsable | Tiempo máximo de decisión |
|---|---|---|---|---|
| Carga con errores masivos | | Restaurar respaldo previo y reprogramar | | |
| Descuadre contable | | Corregir por asiento de ajuste documentado | | |
| Datos faltantes no críticos | | Cargar en post go-live con plan fechado | | |
