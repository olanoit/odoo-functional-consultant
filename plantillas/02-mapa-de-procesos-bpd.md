# Plantilla — Mapa de procesos (AS-IS / TO-BE)

**Proceso:** ____________ · **Cliente:** ____________ · **Versión:** ____ · **Fecha:** ____

---

## 1. Ficha del proceso

| Campo | Valor |
|---|---|
| Nombre del proceso | |
| Objetivo de negocio | |
| Disparador (¿qué lo inicia?) | |
| Resultado final | |
| Dueño del proceso | |
| Frecuencia / volumen | |
| Indicadores actuales | |

## 2. Diagrama AS-IS

> Usa notación simple de carriles (un carril por rol). Se puede dibujar en texto:

```
CLIENTE      │ (1) Envía pedido por WhatsApp
             ▼
VENDEDOR     │ (2) Copia a Excel  → (3) Consulta stock por teléfono
             ▼
ALMACÉN      │ (4) Verifica físicamente → (5) Separa mercancía
             ▼
FACTURACIÓN  │ (6) Emite factura en portal externo → (7) Re-teclea en contabilidad
```

**Puntos de dolor identificados:**

| # | Dolor | Consecuencia medible | Paso afectado |
|---|---|---|---|
| D1 | | | |

## 3. Diagrama TO-BE (en Odoo)

```
CLIENTE      │ (1) Portal / correo / formulario web
             ▼  [crm.lead]
VENDEDOR     │ (2) Cotización [sale.order] con stock en línea
             ▼
ALMACÉN      │ (3) Entrega [stock.picking] con reserva automática
             ▼
FACTURACIÓN  │ (4) Factura [account.move] + envío electrónico
             ▼
CONTABILIDAD │ (5) Asiento y conciliación automáticos
```

## 4. Detalle de pasos TO-BE

| # | Paso | Rol | App de Odoo | Objeto / documento | Estado resultante | Control / validación |
|---|---|---|---|---|---|---|
| 1 | | | | | | |

## 5. Reglas de negocio aplicadas

| ID | Regla | Cómo se implementa en Odoo |
|---|---|---|
| RN-1 | | Configuración / Studio / Aprobación / Desarrollo |

## 6. Cambios que implica para el cliente

| Cambio respecto al AS-IS | Impacto en el usuario | Acción de gestión del cambio |
|---|---|---|
| | | Capacitación / comunicación / rediseño de puesto |

## 7. Indicadores del proceso TO-BE

| Indicador | Fuente en Odoo | Frecuencia | Responsable |
|---|---|---|---|
| | | | |
