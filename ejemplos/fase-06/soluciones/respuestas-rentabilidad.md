# Soluciones — K1: rentabilidad de servicios

---

## Proyecto Sol de Oro (precio fijo S/ 18 000)

| # | Concepto | Resultado |
|---|---|---|
| 1 | Horas registradas | **108 h** |
| 2 | Costo de mano de obra | **S/ 4 320.00** |
| 3 | Costo total (con S/ 1 850 de gastos) | **S/ 6 170.00** |
| 4 | Margen | **S/ 11 830.00 → 65.7 %** |
| 5 | Desvío | **−12 h** (se usaron menos horas de las presupuestadas) |

Detalle del costo de mano de obra:

| Persona | Horas | Costo/hora | Costo |
|---|---|---|---|
| Lucía Ferrer | 52 | 45.00 | 2 340.00 |
| Pedro Quiroz | 26 | 24.00 | 624.00 |
| Ana Vílchez | 18 | 32.00 | 576.00 |
| Sofía Reátegui | 12 | 65.00 | 780.00 |
| **Total** | **108** | | **4 320.00** |

**6. ¿Quién consumió más costo?** Lucía, que además puso más horas (52). Pero el dato interesante es
otro: **Sofía puso 12 horas y costó S/ 780, más que Ana con 18 horas (S/ 576)**. Las horas del
gerente cuestan el doble que las de la jefa de ventas y el triple que las del técnico.

Conclusión de negocio: en proyectos a precio fijo, cada hora de dirección que se puede delegar
mejora el margen. Y si el gerente participa en todos los proyectos "para asegurar la calidad", la
empresa tiene un problema de escalabilidad que el reporte de rentabilidad hace visible por primera vez.

## Bolsa de 20 horas (S/ 2 200)

| # | Concepto | Resultado |
|---|---|---|
| 7 | Consumidas **22 h** de 20 vendidas → **saldo −2 h** | |
| 8 | Costo real: 6 × 45 + 9 × 32 + 7 × 24 | **S/ 726.00** |
| 9 | Margen | **S/ 1 474.00 → 67.0 %** |

**10. ¿Qué debe hacer el sistema al superar las 20 horas?**
Odoo muestra el consumo por encima de lo vendido en la tarea y en el reporte, pero **no bloquea**
el registro de horas: eso sería contraproducente (el trabajo ya se hizo y hay que registrarlo).

Lo correcto es un **procedimiento de negocio** apoyado en el sistema:
- Alerta cuando se consume el 80 % de la bolsa → se contacta al cliente para renovarla.
- Al superarla, las horas se siguen registrando pero quedan visibles como no facturables.
- La renovación se vende como un pedido nuevo que repone el saldo.

Sin ese procedimiento, la empresa regala horas de forma sistemática y solo lo descubre cuando
compara la facturación anual con el costo del equipo.

## La lección transversal

Ambos casos tienen margen alto (65–67 %) porque **el costo/hora está bien cargado**. El error más
común en implementaciones reales es no cargarlo: entonces el costo de horas es cero, todos los
proyectos muestran 100 % de margen y el reporte de rentabilidad —la razón por la que el cliente
compró el módulo— queda inservible.

**Regla para tu checklist de go-live de servicios:** ningún empleado que registre horas puede quedar
sin `hourly_cost`. Es una verificación de una línea que evita que el proyecto entero pierda sentido.
