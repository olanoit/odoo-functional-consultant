# Soluciones — J1: laboratorio de costeo

> Cálculo con los costos de la Fase 1 y los centros de trabajo del archivo `02-centros-trabajo.csv`.
> **La mano de obra incluye el tiempo de preparación y de limpieza**, no solo el tiempo de ciclo:
> ese es el error más común al calcular a mano.

---

## Resultados

| # | Concepto | Resultado |
|---|---|---|
| 1 | Materiales de 100 kg de pulpa | **S/ 1 027.40** |
| 2 | Mano de obra de esa orden | **S/ 120.17** |
| 3 | **Costo por kg de pulpa** | **S/ 11.4757** |
| 4 | **Costo por litro de almíbar** | **S/ 2.2216** |
| 5 | Materiales de 1 000 conservas | **S/ 5 159.45** |
| 6 | Mano de obra de esa orden | **S/ 344.00** |
| 7 | **Costo unitario de la conserva** | **S/ 5.5034** |
| 8 | Margen sobre S/ 12.50 | **56.0 %** |
| 9 | Diferencia con el estándar de 6.80 | **−S/ 1.2966** (el estándar estaba **sobrevalorado**) |
| 10 | Con aguaymanto a S/ 12.00/kg | **S/ 6.4114** (+16.5 %) |

## Detalle

### Pulpa (LdM de 100 kg)
```
Materiales : 120 kg × 8.50  = 1 020.00
             0.4 kg × 18.50 =     7.40   →  1 027.40
Mano obra  : Recepción  (45 + 10 + 15) = 70 min = 1.1667 h × 18.00 =  21.00
             Pulpeado   (90 + 20 + 30) = 140 min = 2.3333 h × 42.50 =  99.17   →  120.17
Total 1 147.57 / 100 kg  →  11.4757 S//kg
```

### Almíbar (LdM de 200 L)
```
Materiales : 80 × 4.20 = 336.00 · 0.6 × 18.50 = 11.10 · 0.2 × 34.00 = 6.80  →  353.90
Mano obra  : Cocina (120 + 15 + 20) = 155 min = 2.5833 h × 35.00       →   90.42
Total 444.32 / 200 L  →  2.2216 S//L
```

### Conserva 400 g (LdM de 1 000 unidades)
```
Pulpa      : 240 kg × 11.4757 = 2 754.16   ← 53 % del costo total
Almíbar    : 180 L  ×  2.2216 =   399.89
Frascos    : 1 000  ×  1.35   = 1 350.00   ← 26 %
Tapas      : 1 000  ×  0.28   =   280.00
Etiquetas  : 1 000  × (0.12 + 0.10) = 220.00
Cajas      :    84  ×  1.85   =   155.40
                              Materiales  5 159.45
Mano obra  : Envasado  (240 + 25 + 25) = 290 min = 4.8333 h × 56.00 = 270.67
             Etiquetado (180 + 10 + 10) = 200 min = 3.3333 h × 22.00 =  73.33
                              Mano de obra  344.00
Total 5 503.45 / 1 000 u  →  5.5034 S//unidad
```

## Lo que enseña el resultado

**El componente que más pesa es la pulpa (53 %)**, es decir, el **aguaymanto**. No los envases, que
es lo que casi todos adivinan. Conclusión de negocio: el margen de ANDINA GOURMET depende del precio
de la materia prima agrícola, no de negociar mejor los frascos.

**La mano de obra es solo el 6.3 %** del costo total. Consecuencia práctica de consultoría: montar
órdenes de trabajo detalladas con registro de tiempos por operario añade trabajo diario en planta
para afinar el 6 % del costo. **Se justifica si hay cuellos de botella o capacidad que planificar;
no se justifica solo "para tener el costo exacto".** Saber decir esto es lo que distingue a un
consultor de un vendedor de funcionalidades.

**El costo estándar estaba mal**: la empresa venía usando S/ 6.80 cuando el costo real es S/ 5.50.
Estaba **subestimando su margen en 1.30 por unidad** — y probablemente rechazando negocios rentables
o fijando precios demasiado altos. Con 50 000 unidades al año, son S/ 65 000 de margen mal medido.
Ese número, dicho en una reunión, vende el proyecto entero.

**Sensibilidad:** si el aguaymanto sube de 8.50 a 12.00 (algo normal entre campañas), el costo pasa
de 5.50 a 6.41 (+16.5 %) y el margen cae del 56 % al 48.7 %. El cliente necesita ver ese cálculo
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
2 conservas (2 × 5.5034) + 1 mermelada (4.60) + 3 snacks (3 × 2.10) = **S/ 21.91**.
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
