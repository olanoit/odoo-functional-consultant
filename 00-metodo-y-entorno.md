# 00 — Método de estudio y entorno de práctica

> Este documento define **cómo** se estudia. Las fases definen **qué**.
> Si el método no se respeta, el plan se convierte en lectura pasiva y no produce un consultor.

---

## 1. El ciclo de aprendizaje: LEER → CONFIGURAR → ROMPER → EXPLICAR

Cada tema del plan se recorre en cuatro pasos. Ninguno es opcional.

| Paso | Qué se hace | Tiempo relativo | Señal de que está hecho |
|---|---|---|---|
| **1. LEER** | Leer la página de documentación indicada, completa, tomando notas de *conceptos* (no de clics). | 20 % | Puedes listar los objetos/modelos que intervienen y sus relaciones. |
| **2. CONFIGURAR** | Reproducir la configuración en tu base de datos de práctica, **con datos propios inventados**, nunca con los datos demo. | 40 % | El flujo corre de punta a punta sin errores. |
| **3. ROMPER** | Provocar el error a propósito: quitar la configuración, saltar un paso, poner una fecha imposible, cancelar a mitad. Anotar el mensaje de Odoo y su causa. | 25 % | Puedes predecir el mensaje de error antes de provocarlo. |
| **4. EXPLICAR** | Escribir en tu bitácora una explicación de 5–10 líneas dirigida a **un cliente no técnico**: qué resuelve, qué se configura, qué límites tiene. | 15 % | Un tercero entiende el tema sin abrir Odoo. |

**Por qué "ROMPER"**: el 80 % del trabajo real de un consultor es diagnosticar por qué
el estándar no hace lo que el cliente espera. Eso solo se aprende viendo fallar el sistema
de forma controlada.

## 2. Regla de las tres fuentes

Para cada tema, se consultan en este orden:

1. **Documentación oficial ES** (fuente de verdad de *qué configura cada opción*).
2. **eLearning oficial de Odoo** (`odoo.com/slides`) o video (fuente de *cómo se ve el flujo real*).
3. **La base de datos** (fuente de *qué pasa de verdad en esta versión*).

Cuando 1 y 3 se contradicen, **gana 3** (la doc puede ir por detrás de la versión) — y eso se anota
en la bitácora como hallazgo. Cuando 2 contradice a 1 y 3, el video probablemente es de otra versión: descartarlo.

## 3. Entorno de práctica

Se necesitan **tres** bases de datos con propósitos distintos. No mezclarlas.

### 3.1 `SANDBOX` — la de romper cosas
- **Dónde:** <https://www.odoo.com/trial> (prueba gratuita, 15 días renovables creando una nueva)
  o Odoo Online. Alternativa sin límite de tiempo: instancia local.
- **Con datos demo activados.** Sirve para explorar rápido y ver flujos ya poblados.
- Se destruye y recrea sin culpa.

### 3.2 `LAB` — la de construir bien
- **Sin datos demo.** Es la base donde se ejecutan los laboratorios de cada fase.
- Se configura desde cero con una empresa ficticia (ver §4) y crece fase tras fase:
  la Fase 4 (Contabilidad) debe encontrar las ventas y compras que creaste en las Fases 2 y 3.
- **Se respalda al terminar cada fase** (Odoo Online: Ajustes → descargar copia de seguridad;
  local: `pg_dump` + carpeta `filestore`). Los respaldos se nombran `LAB_faseNN_YYYYMMDD.zip`.

### 3.3 `PE` — la de localización peruana
- Base independiente, creada en la Fase 10, con el paquete de localización de Perú instalado
  **antes** de registrar cualquier asiento (el plan contable define el resto de la configuración).

### 3.4 Instalación local (opcional pero recomendada desde la Fase 9)

Ventajas: modo desarrollador sin restricciones, acceso a logs, pruebas de importación masiva,
posibilidad de instalar módulos de terceros (`apps.odoo.com`) para el análisis GAP.

- Fuentes y paquetes: <https://nightly.odoo.com/>
- Guía oficial de instalación: <https://www.odoo.com/documentation/saas-19.4/es/administration/on_premise.html>
- Para ver una versión ya montada sin instalar nada: <https://runbot.odoo.com/> (bases efímeras de todas las ramas).

> **Nota sobre ediciones:** algunas apps son **Odoo Enterprise** (Studio, Contabilidad completa,
> Suscripciones, Nómina, Firma, Documentos, PLM, Calidad, Servicio de campo, IoT).
> Si trabajas en Community, esas fases requieren una prueba Enterprise o Odoo Online.
> El consultor funcional **debe** conocerlas: son argumento de venta y de alcance.

## 4. La empresa ficticia: hilo conductor del plan

Todos los laboratorios usan la misma empresa imaginaria, para que las fases se acumulen
en un caso coherente en vez de en ejercicios sueltos.

> **ANDINA GOURMET S.A.C.** — Lima, Perú.
> Produce y comercializa conservas y snacks andinos (quinua, kiwicha, aguaymanto).
> - **Canales:** venta mayorista B2B (distribuidores), tienda propia (punto de venta) y tienda en línea.
> - **Operación:** 1 planta de producción, 2 almacenes (Lima y Arequipa), 18 empleados.
> - **Dolores actuales:** control de lotes y vencimientos en Excel, costos de producción estimados
>   "a ojo", facturación electrónica en un portal externo, sin visibilidad de rentabilidad por producto.
> - **Moneda:** PEN, con compras de insumos en USD.

Cada fase agrega una capa a esta empresa. La Fase 12 la implementa completa como si fuera un cliente real.

## 5. Bitácora obligatoria

Copia [`plantillas/07-bitacora-de-estudio.md`](plantillas/07-bitacora-de-estudio.md) a `bitacora.md` en la raíz.
Por cada sesión de estudio se registra:

- Fecha, fase, bloque, horas.
- **Conceptos nuevos** (lista corta).
- **Qué rompí y qué mensaje dio Odoo.**
- **Dudas abiertas** (se resuelven antes del gate de la fase).
- **Explicación para el cliente** (el paso 4 del ciclo).

La bitácora *es* el material de repaso para la certificación. Sin ella, la Fase 12 cuesta el triple.

## 6. Cómo se valida cada fase (el "gate")

Cada fase cierra con tres pruebas. Las tres deben pasarse **el mismo día**:

| Prueba | Formato | Criterio de aprobación |
|---|---|---|
| **A. Configuración a ciegas** | Reconstruir la configuración clave de la fase en una base nueva, **sin abrir la documentación**, contra reloj. | Se completa en el tiempo indicado por la fase y el flujo corre. |
| **B. Preguntas de comprensión** | Responder por escrito el cuestionario de la fase. | ≥ 80 % correctas, sin consultar. |
| **C. Entregable** | El documento/artefacto que pide la fase (usando una plantilla). | Un tercero podría ejecutar el proceso leyéndolo. |

Si falla A → faltó práctica: repetir laboratorios.
Si falla B → faltó lectura: releer y rehacer el paso EXPLICAR.
Si falla C → faltó consultoría: es el síntoma más común y el más importante de corregir.

## 7. Repaso espaciado

Odoo se olvida rápido porque son cientos de casillas de configuración. Calendario mínimo:

- **+7 días** de cerrada una fase: rehacer la prueba A de esa fase (30 min).
- **+30 días**: responder el cuestionario B otra vez (20 min).
- **Antes de la Fase 12**: repasar todos los cuestionarios en una sola sesión.

Registrar cada repaso en `seguimiento.md`.

## 8. Errores de estudio que arruinan el plan

| Error | Consecuencia | Antídoto |
|---|---|---|
| Estudiar con datos demo | Nunca ves los errores de configuración inicial, que es el 90 % del trabajo real | Base `LAB` sin demo |
| Ver videos sin tocar Odoo | Sensación de dominio, cero capacidad de ejecución | Ratio máximo 1 h de video por cada 3 h de configuración |
| Saltar Contabilidad "porque no soy contador" | Techo permanente: sin contabilidad no hay consultor funcional senior | Fase 4 completa, sin excepciones |
| Aprender clics en lugar de modelo de datos | Cada versión nueva te deja obsoleto | Anotar siempre *qué objeto* se crea y *qué campo* cambia |
| Personalizar antes de dominar el estándar | Se cotizan desarrollos innecesarios; se pierde credibilidad | Studio recién en la Fase 9, tras 8 fases de estándar |
| No documentar | No se puede vender ni transferir el conocimiento | Bitácora + entregable por fase |

## 9. Modo desarrollador (herramienta funcional, no técnica)

Actívalo desde el primer día: *Ajustes → Herramientas para desarrolladores → Activar el modo de desarrollador*
(<https://www.odoo.com/documentation/saas-19.4/es/applications/general/developer_mode.html>).

Un consultor funcional lo usa para:
- Ver el **nombre técnico** de campos y modelos (indispensable para hablar con desarrolladores e importar datos).
- Inspeccionar **acciones automatizadas**, **secuencias**, **campos calculados** y **reglas de registro**.
- Revisar los **datos de módulo** (XML IDs) al importar/exportar.
- Ver el **historial de cambios** de un registro y sus mensajes de log.

No se usa para editar vistas a mano: eso es desarrollo, y va en la Fase 9 con Studio.

## 10. Glosario mínimo que debes dominar desde la Fase 1

`modelo` · `registro` · `campo` (monetario, relacional, calculado, relacionado) ·
`Many2one / One2many / Many2many` · `vista` (lista, formulario, kanban, calendario, pivote, gráfico) ·
`acción de ventana` · `menú` · `grupo de seguridad` · `regla de registro` · `secuencia` ·
`chatter` · `actividad` · `flujo de trabajo (estados)` · `producto vs. variante` ·
`compañía` · `diario` · `apunte contable` · `movimiento de existencias` · `ruta / regla de abastecimiento`.

Definir cada uno con tus palabras en la bitácora **antes** de cerrar la Fase 1.
