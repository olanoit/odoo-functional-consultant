# O3 — Matriz de hosting, actualizaciones y multiempresa

> **Entregable C2 de la Fase 10.** La decisión de hosting condiciona todo el proyecto: qué se puede
> personalizar, quién controla los datos, cuánto cuesta y cómo se actualiza.

---

## 1. La matriz de decisión

| Criterio | Odoo Online | Odoo.sh | On-premise |
|---|---|---|---|
| Módulos de terceros / OCA | ❌ No | ✅ Sí | ✅ Sí |
| Studio | ✅ Sí | ✅ Sí | ✅ (Enterprise) |
| Desarrollo a medida | ❌ No | ✅ Sí | ✅ Sí |
| Acceso a la base de datos | ❌ No | ✅ Sí | ✅ Total |
| Entornos de prueba (staging) | Limitado | ✅ Sí | Según tu infraestructura |
| Acceso a logs | ❌ No | ✅ Sí | ✅ Sí |
| Actualizaciones | Automáticas | Controladas | A tu cargo |
| Respaldos | Gestionados | Gestionados | **Tu responsabilidad** |
| Equipo técnico necesario | Ninguno | Bajo-medio | Alto |
| Costo de infraestructura | Incluido | Incluido | Servidor + administración |
| Control de datos / cumplimiento | Odoo | Odoo | Total |

## 2. Recomendación por perfil de cliente

**Perfil A — Comercializadora de 15 usuarios, sin desarrollos, quiere empezar rápido**
→ **Odoo Online.** Cero infraestructura, actualizaciones incluidas. Si más adelante necesita un
módulo de terceros, se migra a Odoo.sh.

**Perfil B — ANDINA GOURMET: 25 usuarios, localización peruana, 2 módulos de terceros, integración con balanza**
→ **Odoo.sh.** Necesita módulos de terceros y entornos de prueba, pero no quiere administrar servidores.
Es la opción por defecto para la mayoría de las empresas medianas en Perú.

**Perfil C — Empresa con área de TI, requisitos de datos en sus servidores, integraciones internas**
→ **On-premise**, siempre que exista un responsable real del mantenimiento y los respaldos.
Sin ese responsable, es la peor opción: nadie actualiza, nadie prueba los respaldos.

## 3. Respaldos: lo que hay que dejar por escrito

| Pregunta | Respuesta acordada |
|---|---|
| ¿Cada cuánto se respalda? | |
| ¿Cuánto tiempo se conservan? | |
| ¿Dónde se guardan (fuera del servidor)? | |
| ¿Quién es responsable? | |
| **¿Cuándo se probó la última restauración?** | |

> **Un respaldo que nunca se restauró no existe.** Restaurar en otra base es parte del laboratorio
> de esta fase, no un opcional.

## 4. Actualización de versión

| Paso | Qué implica |
|---|---|
| 1. Leer las notas de la versión destino | Qué cambia funcionalmente |
| 2. Inventariar personalizaciones | Studio, módulos de terceros, desarrollos |
| 3. Solicitar base de prueba actualizada | Odoo ofrece el servicio de actualización |
| 4. Probar **con casos escritos** | Los mismos de la UAT (Fase 11) |
| 5. Corregir lo que rompió | Aquí se paga el costo de las personalizaciones |
| 6. Capacitar en los cambios de interfaz | Los usuarios notan cada cambio |
| 7. Ventana de corte y actualización real | Fuera de horario, con plan de reversión |

**Lo que suele romper:** módulos de terceros sin versión nueva, desarrollos a medida, reportes
personalizados, integraciones por API y automatizaciones que dependen de campos renombrados.

> Los cambios de v19 que este plan documenta —`hr.contract` → `hr.version`, `uom_po_id` eliminado,
> `account.fiscal.position.tax` eliminado, `qty_multiple` eliminado— son exactamente el tipo de cosa
> que rompe una actualización. Por eso cada cuaderno de este plan tiene su chuleta de campos.

## 5. Multiempresa

**Ejercicio:** crea una segunda compañía (ANDINA GOURMET Chile) y responde con pruebas:

| Pregunta | Tu respuesta verificada |
|---|---|
| ¿Los contactos se comparten o son por compañía? | |
| ¿Y los productos? ¿Y las listas de precios? | |
| ¿Un usuario puede ver ambas a la vez? | |
| ¿Las secuencias de facturas son independientes? | |
| ¿Cómo se registra una venta de una compañía a la otra? | |
| ¿Se pueden consolidar reportes? ¿Con qué límites? | |

**Riesgos típicos:** registros creados en la compañía equivocada (el error #1), diarios cruzados,
reglas de acceso mal definidas y reportes que suman lo que no debe sumarse.

**Criterio:** multiempresa **solo** si hay dos entidades legales reales. Para sucursales o líneas de
negocio, se usan **almacenes** (Fase 3) y **analítica** (Fase 4), que es mucho más simple.

## 6. Costos y licencias

Preguntas que el cliente hará y debes saber responder sin improvisar:

1. ¿Cómo se cuentan los usuarios? ¿Y los usuarios de **portal**?
2. ¿Qué pasa si un usuario solo entra una vez al mes?
3. ¿Qué son los créditos **IAP** y qué consume (SMS, correos, digitalización, consultas)?
4. ¿Qué diferencia hay entre Community y Enterprise en costo total, contando implementación?
5. ¿Qué pasa con el precio al renovar y al crecer en usuarios?

**No improvises cifras.** Consulta la información vigente y responde por escrito.
