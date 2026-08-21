# Soluciones — Cuestionario de la Fase 1

> **Respóndelo primero tú.** Estas respuestas son el criterio de corrección, no material de lectura.
> Se aprueba con **8 de 10**. Si fallas más de dos, el problema no es memoria: es que faltó configurar.

---

**1. Diferencia entre grupo de acceso y regla de registro. Ejemplo de negocio de cada uno.**

El **grupo** define *qué puede hacer* un usuario y *qué menús y acciones ve*: es un permiso sobre el
**modelo** (leer/escribir/crear/eliminar) y sobre la interfaz.
La **regla de registro** define *sobre qué filas* se aplica ese permiso: es un filtro (dominio) sobre
los **registros**.

- Grupo: *el almacenero ve Inventario pero no ve Compras ni los costes*.
- Regla de registro: *la vendedora Ana ve solo los presupuestos donde ella es la responsable*.

Un usuario sin el grupo no ve el menú; con el grupo pero con regla restrictiva, ve el menú **vacío**
o parcialmente lleno. Diagnóstico rápido: si no ve el menú → grupo; si ve el menú sin datos → regla.

**2. ¿Qué es un ID externo y por qué es imprescindible en una migración?**

Es un identificador de texto (`andina.cli_001`) que Odoo asocia a la clave interna del registro.
Permite que una importación sea **idempotente**: si el ID ya existe, Odoo **actualiza** el registro
en vez de crear otro.
Sin ID externo, cada corrección del archivo genera duplicados, y en una migración real se corrige
el archivo cinco o seis veces. También hace inequívocas las relaciones (`categ_id/id`), sin depender
del nombre ni del idioma de la base.

**3. "Que el vendedor solo vea sus propios clientes": ¿configuración, Studio o desarrollo?**

**Configuración.** Es un grupo estándar de Ventas (*Usuario: solo documentos propios*) apoyado en una
regla de registro que ya existe. No se toca código ni Studio.
Lo importante es el razonamiento: **antes de personalizar, se busca si el estándar ya lo resuelve**.
La variante que sí requeriría más análisis: "que vea los suyos **y** los de su equipo" — también es
estándar vía equipos de ventas; "que vea los de su región" ya empieza a necesitar más diseño.

**4. Archivar vs. eliminar. ¿Qué recomiendas?**

**Archivar** desactiva el registro (`active = False`): desaparece de las búsquedas normales pero
conserva su historial y las referencias de documentos pasados.
**Eliminar** lo borra, y Odoo lo impedirá si tiene documentos asociados.
Se recomienda **archivar siempre**: mantiene la trazabilidad y la integridad contable. Eliminar se
reserva para errores de carga recién cometidos, sin documentos asociados.

**5. ¿Por qué al instalar Contabilidad cambian campos en el formulario de Producto?**

Porque en Odoo los módulos **heredan y extienden** modelos existentes. `account` añade a
`product.template` campos como cuentas contables e impuestos por defecto, y añade pestañas en la vista.
El producto no es de "Inventario" ni de "Contabilidad": es un modelo compartido que cada módulo enriquece.
Consecuencia práctica: **el orden de instalación de las apps cambia lo que ves**, y por eso la
localización debe instalarse antes de operar (Fase 10).

**6. ¿Qué se pierde y qué se conserva al desinstalar un módulo?**

Se eliminan los modelos, campos, menús, vistas y **datos** propios de ese módulo (con sus columnas en
la base de datos). Se conservan los datos de modelos que no le pertenecen, aunque pierdan la información
que ese módulo añadía.
Regla profesional: **desinstalar es destructivo e irreversible sin respaldo**. Nunca se hace en
producción para "probar"; se prueba en una copia neutralizada.

**7. Explica el chatter a un gerente que hoy usa cadenas de correo (máx. 6 líneas).**

> Cada documento —un pedido, una factura, un cliente— lleva su propia conversación pegada.
> Lo que se habló sobre ese pedido está en ese pedido, no en el correo de alguien.
> Cuando entra una persona nueva o alguien sale de vacaciones, la historia completa está ahí:
> quién dijo qué, cuándo y qué se decidió. Las tareas pendientes se registran como actividades con
> responsable y fecha, así nada queda en "yo pensé que lo hacías tú". Y todo queda auditable
> sin depender de que alguien reenvíe un correo.

**8. ¿Cuándo Odoo.sh en lugar de Odoo Online? Dos criterios.**

1. **Necesitas módulos de terceros o desarrollo a medida** (Odoo Online solo admite apps estándar y Studio).
2. **Necesitas entornos separados** de producción/preproducción/desarrollo, control de versiones y
   acceso a logs y a la base de datos para depurar.
Criterio adicional válido: requisitos de integración o de procesamiento que exigen control del servidor.

**9. ¿Qué es una secuencia? ¿Y si el cliente exige numeración que reinicia cada año?**

Una secuencia es el generador de numeración de documentos (pedidos, facturas, transferencias), con
prefijo, sufijo, relleno y siguiente número.
Reiniciar por año es estándar: se configura el prefijo con la máscara de año y la periodicidad de
reinicio. En documentos contables, además, la numeración depende del **diario** y Odoo controla la
continuidad — no permite dejar huecos arbitrarios en facturas publicadas, y eso es una **característica**,
no una limitación: es lo que exige la normativa fiscal.

**10. Diferencia entre unidad de medida y unidad de compra. Ejemplo con un insumo.**

**Atención — pregunta con trampa en Odoo 19:** el campo de *unidad de medida de compra* (`uom_po_id`)
**ya no existe** en esta versión. Antes permitía comprar en una unidad (sacos) y almacenar en otra (kg),
con conversión automática.
En v19 el producto tiene una **única** unidad (`uom_id`) y, para los múltiplos, se usa `uom_ids`
(empaques adicionales, que reemplazan al antiguo modelo de *packaging*).
Ejemplo con *Quinua perlada*: la unidad es **kg**; si el proveedor vende en sacos de 25 kg, eso se
modela como un empaque, no como una segunda unidad de compra.

**Respuesta esperada del consultor:** además de explicar el concepto, decir explícitamente
*"esto cambió en la versión 19"*. Un consultor que repite lo que aprendió en la v16 sin verificar
configura mal y cotiza mal. Verificar la versión **antes** de afirmar es parte del trabajo.

---

## Calificación

| Aciertos | Lectura |
|---|---|
| 9–10 | Listo para la Fase 2 |
| 8 | Aprobado; repasa los temas fallados antes de avanzar |
| 6–7 | Repite los bloques 1.4 y 1.6 (permisos e importación) |
| < 6 | Faltó configurar, no faltó leer. Rehaz los Ejemplos 2 a 7 |
