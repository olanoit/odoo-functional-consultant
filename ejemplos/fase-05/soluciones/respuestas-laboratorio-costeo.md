# Soluciones — J1: laboratorio de costeo

> Cálculo con los costos de la Fase 1 y los centros de trabajo del archivo `02-centros-trabajo.csv`,
> con la misma fórmula que usa Odoo 20 (`mrp.routing.workcenter`, `time_total` y `cost`):
> **duración = preparación + limpieza + ciclos × tiempo de ciclo × 100 / eficiencia**, y el costo de
> cada operación redondeado a céntimos. Los dos errores más comunes al calcular a mano son olvidar la
> preparación y la limpieza, y olvidar la **eficiencia** del centro (que alarga el tiempo de ciclo).

---

> **Verificado en Odoo 20** con los CSV de la fase cargados: *Calcular el costo desde la LdM* da
> 11.5536 (pulpa), 2.2520 (almíbar) y 5.5616 (conserva); el *Resumen de la LdM* de la conserva,
> 5 562.24; con el aguaymanto a 12.00, 15.7536 y 6.5696. Requisito: la LdM de la pulpa debe estar en
> **kg** y la del almíbar en **L** (la unidad de la LdM, no solo la del producto). Si la LdM queda en
> *Unidades*, Odoo convierte unidades a kg y el costo por kg sale multiplicado por 1 000.

## Resultados

| # | Concepto | Resultado |
|---|---|---|
| 1 | Materiales de 100 kg de pulpa | **S/ 1 027.40** |
| 2 | Mano de obra de esa orden | **S/ 127.96** |
| 3 | **Costo por kg de pulpa** | **S/ 11.5536** |
| 4 | **Costo por litro de almíbar** | **S/ 2.2520** |
| 5 | Materiales de 1 000 conservas | **S/ 5 183.62** |
| 6 | Mano de obra de esa orden | **S/ 378.02** |
| 7 | **Costo unitario de la conserva** | **S/ 5.5616** |
| 8 | Margen sobre S/ 12.50 | **55.5 %** |
| 9 | Diferencia con el estándar de 6.80 | **−S/ 1.2384** (el estándar estaba **sobrevalorado**) |
| 10 | Con aguaymanto a S/ 12.00/kg | **S/ 6.5696** (+18.1 %) |

## Detalle

### Pulpa (LdM de 100 kg · 1 ciclo)
```
Materiales : 120 kg × 8.50  = 1 020.00
             0.4 kg × 18.50 =     7.40   →  1 027.40
Mano obra  : Recepción  10 + 15 + 45 × 100/95 =  72.37 min = 1.2061 h × 18.00 =  21.71
             Pulpeado   20 + 30 + 90 × 100/90 = 150.00 min = 2.5000 h × 42.50 = 106.25   →  127.96
Total 1 155.36 / 100 kg  →  11.5536 S//kg
```

### Almíbar (LdM de 200 L · 1 ciclo)
```
Materiales : 80 × 4.20 = 336.00 · 0.6 × 18.50 = 11.10 · 0.2 × 34.00 = 6.80  →  353.90
Mano obra  : Cocina 15 + 20 + 120 × 100/92 = 165.43 min = 2.7572 h × 35.00  →   96.50
Total 450.40 / 200 L  →  2.2520 S//L
```

### Conserva 400 g (LdM de 1 000 unidades · 1 ciclo)
```
Pulpa      : 240 kg × 11.5536 = 2 772.86   ← 50 % del costo total
Almíbar    : 180 L  ×  2.2520 =   405.36
Frascos    : 1 000  ×  1.35   = 1 350.00   ← 24 %
Tapas      : 1 000  ×  0.28   =   280.00
Etiquetas  : 1 000  × (0.12 + 0.10) = 220.00
Cajas      :    84  ×  1.85   =   155.40
                              Materiales  5 183.62
Mano obra  : Envasado   25 + 25 + 240 × 100/88 = 322.73 min = 5.3788 h × 56.00 = 301.21
             Etiquetado 10 + 10 + 180 × 100/95 = 209.47 min = 3.4912 h × 22.00 =  76.81
                              Mano de obra  378.02
Total 5 561.64 / 1 000 u  →  5.5616 S//unidad
```

### Escenario 10: aguaymanto a S/ 12.00/kg
```
Pulpa      : materiales 120 × 12.00 = 1 440.00 + 0.4 × 18.50 = 7.40  →  1 447.40
             mano de obra sin cambio                                 →    127.96
             1 575.36 / 100 kg                                       →  15.7536 S//kg
Conserva   : 240 kg × 15.7536 = 3 780.86   (antes 2 772.86, +1 008.00)
             el resto de componentes y la mano de obra no cambian
             6 191.62 materiales + 378.02 mano de obra = 6 569.64 / 1 000 u
                                                        →  6.5696 S//unidad
```
Solo cambia **una** línea de la lista de materiales de la pulpa y el costo unitario sube 18.1 %.
Ese apalancamiento —un insumo que pesa la mitad del costo— es el argumento para contratar la
cosecha por campaña en lugar de comprar al precio de mercado.

### Por qué el *Resumen de la LdM* de Odoo muestra S/ 5 562.24 y no 5 561.64
El informe no usa el costo por kg de una orden de 100 kg: despliega la pulpa **para los 240 kg que
pide la conserva**, es decir, 3 ciclos con **una sola** preparación y limpieza, y el almíbar para
180 L (1 ciclo, porque la capacidad es la LdM de 200 L):
```
Pulpa 240 kg : 288 × 8.50 = 2 448.00 · 0.96 × 18.50 = 17.76
               Recepción 25 + 3 × 47.37 = 167.11 min → 50.13
               Pulpeado  50 + 3 × 100.00 = 350.00 min → 247.92          →  2 763.81
Almíbar 180 L: 302.40 + 9.99 + 6.12 + cocina 165.43 min → 96.50         →    415.01
Envases, etiquetas y cajas                                              →  2 005.40
Operaciones de la conserva                                              →    378.02
                                                                   Total  5 562.24
```
Los dos cálculos son correctos; responden a preguntas distintas. El tuyo es el costo si la pulpa se
fabrica en órdenes de 100 kg (tres preparaciones); el del informe, si se fabrica de una vez la
cantidad exacta. **Esa diferencia es el argumento para dimensionar el lote de pulpa.** Y el costo que
de verdad entra en la valoración de la conserva es el de las órdenes de pulpa que se ejecutaron.

## Lo que enseña el resultado

**El componente que más pesa es la pulpa (50 %)**, es decir, el **aguaymanto**. No los envases, que
es lo que casi todos adivinan (el frasco es el 24 %). Conclusión de negocio: el margen de ANDINA
GOURMET depende del precio de la materia prima agrícola, no de negociar mejor los frascos.

**La mano de obra directa de la conserva es solo el 6.8 %** del costo total (13.9 % si se suma la
incluida en la pulpa y el almíbar). Consecuencia práctica de consultoría: montar órdenes de trabajo
detalladas con registro de tiempos por operario añade trabajo diario en planta para afinar menos del
15 % del costo. **Se justifica si hay cuellos de botella o capacidad que planificar; no se justifica
solo "para tener el costo exacto".** Saber decir esto es lo que distingue a un consultor de un
vendedor de funcionalidades.

**El costo estándar estaba mal**: la empresa venía usando S/ 6.80 cuando el costo real es S/ 5.56.
Estaba **subestimando su margen en 1.24 por unidad** — y probablemente rechazando negocios rentables
o fijando precios demasiado altos. Con 50 000 unidades al año, son S/ 61 920 de margen mal medido.
Ese número, dicho en una reunión, vende el proyecto entero.

**Sensibilidad:** si el aguaymanto sube de 8.50 a 12.00 (algo normal entre campañas), el costo pasa
de 5.5616 a 6.5696 (+18.1 %) y el margen cae del 55.5 % al 47.4 %. El cliente necesita ver ese cálculo
**antes** de comprometer una lista de precios anual con sus distribuidores.

## Respuestas de diseño

**A. ¿La pulpa como producto o como fase interna?**
Como **producto almacenable con su propia LdM**, por tres razones: (1) tiene vida útil y se almacena
entre etapas, (2) se necesita trazabilidad del lote de pulpa hacia varios lotes de conserva
—un lote de pulpa alimenta varias órdenes—, y (3) permite costear la etapa por separado y detectar
si la merma está en el pulpeado o en el envasado.
Sería una fase interna (una sola LdM con todas las operaciones) si la pulpa se consumiera de
inmediato, sin stock intermedio ni trazabilidad propia.

**B. El Kit Navideño.** Su costo es la suma de sus componentes:
2 conservas (2 × 5.5616) + 1 mermelada (4.60) + 3 snacks (3 × 2.10) = **S/ 22.02**.
Es lo que pone *Calcular el costo desde la LdM* en el kit (verificado en v20: 22.0233, con la conserva
ya a 5.5616). Ojo con el *Resumen de la LdM* del kit: despliega la LdM de la conserva para **2 unidades**
y le carga una preparación, una limpieza y un ciclo completo de cada operación (y lo mismo en la pulpa
y el almíbar), así que muestra **S/ 622.96**. No es el costo del kit: es el costo de fabricar 2
conservas sueltas, que nadie hace.
No genera orden de fabricación porque una LdM tipo **kit (phantom)** no crea un producto físico: al
vender el kit, Odoo **reemplaza** la línea por sus componentes en la entrega. El kit no existe en el
almacén, no tiene stock propio y no se puede trazar como producto. Por eso, si el cliente quiere
armar las canastas con anticipación y tenerlas en el estante, **necesita una LdM normal, no un kit**.

**C. Tercerizar el etiquetado.** La operación desaparece de la LdM de fabricación y se convierte en
una **LdM de subcontratación** con el proveedor: se le envían los componentes (o no, según el
acuerdo) y se recibe el producto etiquetado. El costo del servicio del subcontratista entra al costo
del producto en lugar del costo/hora del centro de trabajo.

**D. Método de costo.**
Semielaborados: **promedio (AVCO)** — su costo varía con cada campaña de materia prima y no tiene
sentido rastrear capas PEPS de pulpa.
Producto terminado: **PEPS**, coherente con la rotación física real (FEFO por caducidad) y con la
trazabilidad por lote que exige el negocio alimentario.
