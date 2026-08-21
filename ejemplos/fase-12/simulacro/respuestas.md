# Simulacro de certificación — respuestas y explicaciones

> Corrige con la penalización real: **+1** por acierto, **−0.5** por error, **0** por no responder.
> Puntaje máximo: 60. **Aprobado: 42 (70 %).**

---

## Clave rápida

| 1-10 | 11-20 | 21-30 | 31-40 | 41-50 | 51-60 |
|---|---|---|---|---|---|
| 1. **b** | 11. **a** | 21. **b** | 31. **b** | 41. **b** | 51. **b** |
| 2. **b** | 12. **b** | 22. **b** | 32. **a** | 42. **a** | 52. **b** |
| 3. **b** | 13. **b** | 23. **b** | 33. **b** | 43. **b** | 53. **b** |
| 4. **b** | 14. **b** | 24. **b** | 34. **b** | 44. **b** | 54. **b** |
| 5. **b** | 15. **b** | 25. **b** | 35. **b** | 45. **b** | 55. **b** |
| 6. **b** | 16. **b** | 26. **b** | 36. **b** | 46. **b** | 56. **b** |
| 7. **b** | 17. **b** | 27. **b** | 37. **b** | 47. **b** | 57. **b** |
| 8. **b** | 18. **b** | 28. **b** | 38. **d** | 48. **b** | 58. **b** |
| 9. **b** | 19. **b** | 29. **c** | 39. **a** | 49. **b** | 59. **b** |
| 10. **b** | 20. **b** | 30. **b** | 40. **b** | 50. **b** | 60. **b** |

---

## Explicaciones de las que más se fallan

**3 · v19: `type = consu` + `is_storable`.** El valor `product` desapareció en v18/v19. Es el error
número uno al reutilizar plantillas de importación antiguas.

**10 · Especificidad sobre importe.** La regla de **producto** gana a la global aunque el precio
resultante sea mayor. Odoo ordena por `applied_on, min_quantity desc` y toma la primera aplicable.
De aquí sale la mayoría de los "Odoo me pone mal los precios".

**12 y 16 · Cambios de v19.** Los opcionales son líneas con `is_optional`; las etapas de CRM se
relacionan con equipos por `team_ids` (Many2many). Cualquier material anterior a v19 falla aquí.

**19 · Ubicación virtual de inventario.** Todo movimiento tiene origen y destino: un ajuste positivo
"viene" de la ubicación de pérdidas/ganancias de inventario. Es la partida doble del stock.

**22 · Se usa el stock previsto, no el físico.** 1 500 − 3 000 = −1 500. Para llegar al máximo de
10 000 hay que comprar **11 500**. Quien responde 8 500 está mirando solo lo que hay en el estante.

**24 y 30 · Renombres de v19.** `stock.production.lot` → `stock.lot`; valoración `manual_periodic`
→ `periodic`.

**34 · El cambio más disruptivo de v19 en contabilidad.** El modelo `account.fiscal.position.tax`
desapareció: ahora el impuesto **destino** declara a quién reemplaza (`original_tax_ids`) y en qué
posiciones aplica (`fiscal_position_ids`).

**38 · La respuesta correcta es la (d).** Tener varias ubicaciones no descuadra nada: el valor es el
mismo esté donde esté la mercancía dentro de la empresa. Las otras tres sí son causas reales de
descuadre. Ojo: es la única pregunta del simulacro donde se pide la opción **falsa**; en el examen
real también aparecen preguntas invertidas y hay que leer con cuidado.

**43 · Kit.** No genera orden de fabricación ni stock del producto padre: al entregar, se reemplaza
por sus componentes. Si el cliente arma y almacena el producto, **necesita una LdM normal**.

**49 · Costo por hora.** Sin `hourly_cost` cargado, todos los proyectos muestran 100 % de margen y el
reporte que justificó comprar el módulo queda inservible.

**53 · v19: `hr.version`.** El modelo `hr.contract` desapareció. Los datos laborales viven en
versiones fechadas del empleado.

**56 · El carrito no reserva.** La reserva ocurre al confirmar el pedido, según el método de reserva
configurado. Por eso hay que decidir la política de venta sin stock **antes** de la primera campaña.

**58 · El criterio antes que la herramienta.** Antes de Studio, de un módulo o de un desarrollo, la
pregunta es si el requerimiento es real o es una costumbre heredada del sistema anterior. Es la
diferencia entre un consultor y un configurador.

---

## Cómo interpretar tu resultado

| Puntaje | Lectura | Qué hacer |
|---|---|---|
| 50–60 | Listo para el examen oficial | Repasa solo los fallados y agenda |
| 42–49 | Aprobarías, con margen justo | Refuerza las áreas falladas antes de agendar |
| 30–41 | Todavía no | Vuelve a los cuadernos de las áreas débiles |
| < 30 | Faltan fases por consolidar | Repite los gates de las fases correspondientes |

## Mapa de preguntas por fase

| Preguntas | Fase a repasar si fallaste |
|---|---|
| 1–8 | Fase 1 — Fundamentos |
| 9–18 | Fase 2 — Ventas y CRM |
| 19–30 | Fase 3 — Compras e Inventario |
| 31–42 | Fase 4 — Contabilidad |
| 43–48 | Fase 5 — Manufactura |
| 49–54 | Fases 6 y 7 — Servicios y RR. HH. |
| 55–60 | Fases 8 y 9 — Web, Studio y datos |

> **Advertencia sobre este simulacro:** las respuestas correctas están casi siempre en la opción (b)
> porque el objetivo es que estudies el contenido, no que entrenes a adivinar patrones. El examen
> oficial distribuye las respuestas al azar y usa formatos que aquí no están (selección múltiple,
> verdadero/falso, preguntas invertidas). **Haz también el examen de muestra oficial**:
> <https://www.odoo.com/slides/odoo-functional-certification-sample-test-50>
