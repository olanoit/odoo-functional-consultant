# N2 — Studio: la app propia y el árbol de decisión

> Studio es la herramienta que más rápido impresiona a un cliente y la que más deuda técnica genera
> si se usa sin criterio. Este ejercicio entrena las dos cosas: **construirlo** y **decidir si debe
> construirse**.
>
> Studio es **Enterprise**.

---

## Parte 1 — El árbol de decisión (escríbelo antes de tocar Studio)

```
¿El estándar ya lo hace?
 ├── Sí → configurar. Documentar la configuración.
 └── No → ¿el requerimiento es real o es costumbre del proceso viejo?
      ├── Costumbre → proponer cambio de proceso
      │               (la opción más barata y la que casi nadie ofrece)
      └── Real → ¿se resuelve con campos, vistas o automatizaciones simples?
           ├── Sí → Studio. Riesgo: mantenimiento en cada actualización.
           └── No → ¿existe un módulo de terceros confiable?
                ├── Sí → evaluar: versión, mantenedor, código, soporte, costo
                └── No → desarrollo a medida: especificar, estimar y advertir
                         el costo de por vida
```

**Aplícalo a estos 6 casos reales** (respuesta + argumento en 3 líneas cada uno):

| # | Requerimiento del cliente | Tu decisión |
|---|---|---|
| 1 | "Quiero un campo de límite de crédito en el cliente" | |
| 2 | "Que no se pueda confirmar un pedido si el cliente supera su límite" | |
| 3 | "Necesito que la factura salga con nuestro diseño y el logo grande" | |
| 4 | "Quiero registrar las visitas de los vendedores a los distribuidores" | |
| 5 | "Que el sistema calcule automáticamente la comisión del vendedor" | |
| 6 | "Necesito que al confirmar una venta se avise por WhatsApp al almacén" | |

## Parte 2 — Construir la app *Visitas a distribuidores*

**El encargo:** *"Nuestros vendedores visitan distribuidores y no queda registro de nada: ni de qué
se habló, ni de qué exhibición tiene el cliente, ni de qué se acordó."*

### Modelo

| Campo | Tipo | Notas |
|---|---|---|
| Distribuidor | Many2one → Contacto | Obligatorio |
| Vendedor | Many2one → Usuario | Por defecto: usuario actual |
| Fecha de visita | Fecha y hora | Obligatorio |
| Tipo de visita | Selección | Comercial · Cobranza · Reclamo · Exhibición |
| Estado | Selección | Planificada · Realizada · Cancelada |
| Duración (horas) | Decimal | |
| Productos exhibidos | Many2many → Producto | |
| Rotación observada | Selección | Alta · Media · Baja · Sin stock |
| Requiere seguimiento | Booleano | |
| Fecha de seguimiento | Fecha | **Obligatoria solo si** requiere seguimiento |
| Observaciones | Texto | |
| Oportunidad generada | Many2one → Oportunidad | Enlace con el CRM de la Fase 2 |

### Vistas a construir

- **Kanban** agrupado por estado, con color según la rotación observada.
- **Lista** con distribuidor, fecha, vendedor y estado.
- **Formulario** con dos pestañas: *Datos de la visita* y *Resultado*.
- **Calendario** por fecha de visita.
- **Mapa** por dirección del distribuidor.
- **Pivote y gráfico**: visitas por vendedor y por mes.

### Reglas y automatizaciones

1. `Fecha de seguimiento` **obligatoria condicionalmente** cuando *Requiere seguimiento* está marcado.
   *(Nota: "obligatorio si" ≠ "obligatorio". Prueba las dos y anota la diferencia.)*
2. Al marcar la visita como **Realizada** con seguimiento requerido → **crear una actividad**
   para el vendedor en la fecha indicada.
3. Si la rotación observada es **Sin stock** → notificar al jefe de ventas.
4. Menú propio con permisos: los vendedores ven **solo sus visitas**; el jefe, todas.

### Verificación

- [ ] Un vendedor puede registrar una visita en menos de 1 minuto desde el móvil.
- [ ] El jefe ve el mapa de visitas de la semana.
- [ ] El reporte responde: ¿cuántas visitas hizo cada vendedor y cuántas generaron oportunidad?

## Parte 3 — Reportes y aprobaciones

1. **Factura personalizada**: logo, datos fiscales de ANDINA GOURMET, términos y pie legal.
2. **Etiqueta de producto** con código de barras y lote (enlace con la Fase 3).
3. **Regla de aprobación**: descuento superior al 20 % en un pedido de venta (Fase 2).
4. **Regla de aprobación**: orden de compra por encima de S/ 20 000 (Fase 3).

## Parte 4 — El costo oculto

Documenta, para cada personalización que hiciste:

| Personalización | ¿Por qué era necesaria? | ¿Qué pasa al actualizar de versión? | ¿Quién la mantiene? |
|---|---|---|---|
| | | | |

> **La frase que debes poder decirle al cliente:** *"esto lo puedo hacer hoy en dos horas, y le va a
> costar revisarlo cada vez que actualicemos de versión. ¿Le compensa frente a ajustar el proceso?"*
> Un consultor que solo dice "sí, se puede" no está haciendo su trabajo.

## Parte 5 — Rompe a propósito

| Prueba | Qué observar |
|---|---|
| Añadir un campo obligatorio a un modelo con 500 registros | Qué pasa con los existentes |
| Hacerlo obligatorio **condicionalmente** | La diferencia real |
| Crear una automatización que se dispare a sí misma | Bucles y cómo evitarlos |
| Cambiar el tipo de un campo con datos | Qué permite y qué no |
| Borrar un campo usado en una vista y en una automatización | Qué se rompe y dónde aparece el error |
