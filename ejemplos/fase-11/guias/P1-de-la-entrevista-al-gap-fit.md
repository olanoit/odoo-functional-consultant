# P1 — De la entrevista al GAP-FIT

> Ejercicio sobre [`../casos/C1-entrevista-transcrita.md`](../casos/C1-entrevista-transcrita.md).
> Es el ejercicio más importante de todo el plan: convierte lo que un cliente dice en lo que hay que
> hacer.
>
> Soluciones en [`../soluciones/respuestas-entrevista.md`](../soluciones/respuestas-entrevista.md).

---

## Parte 1 — Extraer los requerimientos (45 min)

Lee la transcripción y completa esta tabla. Usa la plantilla
[`../../../plantillas/01-levantamiento-de-requerimientos.md`](../../../plantillas/01-levantamiento-de-requerimientos.md).

| ID | Requerimiento (en palabras del cliente) | Quién lo pidió | Área | Prioridad |
|---|---|---|---|---|
| R-001 | | | | |

**Meta: al menos 20 requerimientos.** Si sacas menos de 15, estás leyendo la entrevista como un
usuario, no como un consultor.

## Parte 2 — Separar síntomas de causas (30 min)

El cliente describe **síntomas**. Tu trabajo es identificar la **causa**. Completa:

| Síntoma que mencionó | Causa probable | ¿Qué lo resuelve? |
|---|---|---|
| "14 notas de crédito en un mes" | | |
| "El Excel de stock se actualiza lunes y jueves" | | |
| "Tres días para saber a quién le fue un lote" | | |
| "Ajuste de inventario de S/ 15 000" | | |
| "El costo lo sacamos hace dos años" | | |
| "Si Ana no está, la empresa se para" | | |
| "Hay que teclear todo tres veces" | | |

## Parte 3 — Los datos que faltan (20 min)

Un buen levantamiento se mide por lo que **no** quedó claro. Enumera al menos **10 preguntas** que
debiste hacer y no se hicieron en esta entrevista. Ejemplos del tipo de hueco que hay que ver:

- No se preguntó cuántos **SKU** manejan.
- No se preguntó cuántos usuarios usarían el sistema.
- No se preguntó el **presupuesto** ni quién firma.
- …

## Parte 4 — Volúmenes y viabilidad (15 min)

De la entrevista se puede deducir algún volumen (facturas al mes, notas de crédito) y falta casi
todo lo demás. Arma la tabla de volúmenes que necesitas para estimar y marca qué falta pedir.

| Métrica | Dato de la entrevista | ¿Falta? |
|---|---|---|
| Facturas de venta al mes | ~120–130 | No |
| Notas de crédito al mes | 14 | No |
| SKU activos | | **Sí** |
| Clientes activos | | **Sí** |
| … | | |

## Parte 5 — La matriz GAP-FIT (60 min)

Clasifica tus requerimientos con
[`../../../plantillas/03-matriz-gap-fit.md`](../../../plantillas/03-matriz-gap-fit.md):
**FIT · CONFIG · STUDIO · TERCEROS · DEV · PROCESO · OUT**.

Presta atención a los que son **PROCESO**: la entrevista tiene varios requerimientos que no se
resuelven con software sino cambiando cómo trabajan. Identificarlos y decirlo es lo que distingue a
un consultor de un configurador.

## Parte 6 — El alcance y la conversación difícil (30 min)

1. Redacta el **objetivo del proyecto** en tres líneas, en el lenguaje de Sofía (no en el tuyo).
2. Define qué entra en la **primera fase** y qué queda para después. Justifica el corte con la fecha
   límite de enero.
3. Escribe las **exclusiones explícitas**.
4. Prepara cómo le dirías a Sofía las dos malas noticias que aparecen en la entrevista:
   - el ajuste de inventario de S/ 15 000 que su contador venía haciendo sin contárselo,
   - que "facturar electrónico" implica configuración fiscal, certificados y series autorizadas,
     y que eso no es un botón.

## Parte 7 — Estimación (30 min)

Estima el proyecto por bloques, con supuestos escritos:

| Bloque | Horas | Supuesto |
|---|---|---|
| Configuración base y datos maestros | | |
| Comercial (CRM, ventas, precios) | | |
| Compras e inventario con lotes | | |
| Producción y costeo | | |
| Contabilidad y localización PE | | |
| Migración de datos | | |
| Pruebas (UAT) | | |
| Capacitación | | |
| Acompañamiento go-live y primer cierre | | |
| Gestión de proyecto (%) | | |
| **Reserva de riesgo (%)** | | |

**Regla:** si tu estimación no tiene reserva de riesgo, no es una estimación: es un deseo.
