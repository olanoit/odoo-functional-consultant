# Plantilla — Casos de prueba de aceptación (UAT)

**Cliente:** ____________ · **Ciclo de pruebas:** ____ · **Fechas:** ____ a ____
**Regla:** los casos los ejecuta **el usuario**, no el consultor. El consultor acompaña y registra.

---

## 1. Cobertura planificada

| Área | Casos felices | Casos de excepción | Casos de permisos | Casos de reporte | Total |
|---|---|---|---|---|---|
| Ventas | | | | | |
| Compras | | | | | |
| Inventario | | | | | |
| Producción | | | | | |
| Contabilidad | | | | | |
| RR. HH. | | | | | |
| **Total** | | | | | |

## 2. Ficha de caso de prueba

| Campo | Valor |
|---|---|
| **ID** | UAT-VEN-001 |
| **Proceso** | Venta a distribuidor con entrega parcial |
| **Objetivo** | Verificar que se factura solo lo entregado |
| **Rol ejecutante** | Vendedor / Almacenero / Facturador |
| **Precondiciones** | Cliente X existe, producto Y con 100 unidades en Lima, lista de precios mayorista activa |
| **Datos de prueba** | Pedido de 50 unidades, entrega de 30 |
| **Pasos** | 1. … 2. … 3. … |
| **Resultado esperado** | Factura por 30 unidades al precio mayorista, saldo pendiente de 20 |
| **Resultado obtenido** | |
| **Estado** | ☐ Aprobado ☐ Fallido ☐ Bloqueado |
| **Evidencia** | Captura / nº de documento |
| **Ejecutado por / fecha** | |

## 3. Registro de ejecución

| ID | Caso | Rol | Ejecutado por | Fecha | Estado | Defecto asociado |
|---|---|---|---|---|---|---|
| UAT-001 | | | | | | |

## 4. Gestión de defectos

| ID | Descripción | Caso | Severidad | Prioridad | Causa | Responsable | Estado | Fecha cierre |
|---|---|---|---|---|---|---|---|---|
| DEF-001 | | UAT-001 | Crítica/Alta/Media/Baja | | Configuración / Dato / Desarrollo / Expectativa | | Abierto/En curso/Reprueba/Cerrado | |

**Severidades:**
- **Crítica:** impide operar; bloquea el go-live.
- **Alta:** hay solución temporal, pero debe resolverse antes del go-live.
- **Media:** se resuelve en las 2 semanas posteriores al go-live.
- **Baja:** mejora; entra en backlog.

**Un defecto se cierra solo cuando el usuario que lo reportó re-ejecuta el caso y lo aprueba.**

## 5. Criterio de salida de UAT

- [ ] 100 % de casos críticos aprobados.
- [ ] 0 defectos críticos abiertos; ≤ ____ defectos altos con plan y fecha.
- [ ] Reportes clave validados por el usuario que los consume.
- [ ] Permisos probados por cada rol con su propio usuario.
- [ ] Cierre contable de prueba ejecutado sobre datos de UAT.

## 6. Acta de aceptación

Por medio de la presente, ____________ (cliente) declara que las pruebas de aceptación del alcance
descrito en ____________ fueron ejecutadas y aprobadas con los resultados registrados en este
documento, dando inicio a la etapa de ____________ (puesta en marcha / garantía).

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Líder de proyecto (cliente) | | | |
| Usuario clave por área | | | |
| Consultor responsable | | | |
