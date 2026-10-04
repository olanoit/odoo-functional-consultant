# Página web del plan de estudios

Genera **una sola página HTML** con todo el contenido del repositorio: los documentos Markdown
(fases, cuadernos, guías, casos, soluciones, simulacro, plantillas y recursos) y los CSV de
`ejemplos/*/datos/`, mostrados como tablas. Incluye índice lateral por fase, búsqueda de texto
completo, navegación anterior/siguiente y una portada con el mapa de fases.

## Uso

```bash
python3 -m pip install -r herramientas/web/requirements.txt
python3 herramientas/web/build.py
```

La página queda en `herramientas/web/build/consultor-odoo-20.html` (carpeta ignorada por git).
Se puede abrir directamente en el navegador o publicar como página estática.

Argumentos opcionales: `build.py [ruta-del-repo] [archivo-de-salida]`.

## Qué hace

- Lee los archivos versionados (`git ls-files`), así que solo incluye lo que está en el repositorio.
- Convierte el Markdown con `markdown-it-py` (CommonMark + tablas), igual que lo muestra GitHub.
- Reescribe los enlaces relativos entre archivos para que funcionen dentro de la página, incluidos
  los que apuntan a secciones (`archivo.md#seccion`) y a carpetas. Si un enlace no tiene destino,
  lo avisa por la salida de error.
- Cada documento enlaza a su archivo en GitHub (rama `20.0`).

## Qué hay que actualizar a mano

La portada se construye en `build.py`. Lee del repositorio la tabla de fases del `README.md`
(nombres, horas y entregables) y los últimos commits. Estos textos están escritos en el propio
generador y hay que revisarlos cuando cambien:

- la lista `V20` (lo que cambia en Odoo 20);
- el bloque «Cómo se verificó este material» (número de comprobaciones, enlaces y fecha);
- el diccionario `FASES` (nombres cortos del índice).

El diseño (colores, tipografías, tema claro/oscuro, adaptación a móvil) y el JavaScript de
navegación y búsqueda están en `template.html`.
