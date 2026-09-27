# E1 — Los 4 usuarios de ANDINA GOURMET y su matriz de permisos

**Objetivo:** ver con tus propios ojos la diferencia entre **grupo de acceso** (qué menús ve un usuario)
y **regla de registro** (qué filas ve dentro de esos menús). Es la base de toda la seguridad de Odoo.

**Dónde:** *Ajustes → Usuarios y compañías → Usuarios*. Con **modo desarrollador activo** verás
todas las secciones de permisos.

---

## 1. Los usuarios a crear

| # | Nombre | Correo de acceso | Puesto real en la empresa |
|---|---|---|---|
| U1 | Ana Vílchez | ana.vilchez@andinagourmet.com.pe | Vendedora de canal retail |
| U2 | Diego Castro | diego.castro@andinagourmet.com.pe | Comprador / abastecimiento |
| U3 | Marco Huamán | marco.huaman@andinagourmet.com.pe | Almacenero de Lima |
| U4 | Sofía Reátegui | sofia.reategui@andinagourmet.com.pe | Gerente general |

> Créalos como **usuarios internos** con rol **Usuario**. En v20 el formulario de usuario muestra un
> selector de rol con tres opciones: *ligero* (Light), *usuario* y *administrador*. El rol ligero solo
> admite permisos "ligeros" (pedir ausencias, marcar asistencia…) y oculta apps como Contactos o
> Ventas; si eliges *ligero*, Odoo recorta los grupos de la matriz de abajo.
>
> Si tu base es una prueba en línea con límite de usuarios,
> crea U1 y U4 como usuarios reales y prueba U2/U3 reasignando grupos a U1 (anota que lo hiciste así).

## 2. Matriz de grupos

| Área | U1 Ana (Ventas) | U2 Diego (Compras) | U3 Marco (Almacén) | U4 Sofía (Gerencia) |
|---|---|---|---|---|
| **Ventas** | Usuario: **solo mostrar documentos propios** | — | — | Administrador |
| **Compras** | — | Usuario | — | Administrador |
| **Inventario** | — | Usuario | Usuario | Administrador |
| **Contabilidad** | — | — | — | Facturación (o Contable) |
| **Contactos** | Usuario | Usuario | — | Administrador |
| **Ajustes / Administración** | — | — | — | Ajustes |

Además, en la sección **Otros** / **Técnico** (visible con modo desarrollador), observa —sin activarlos
todavía— grupos como *Gestión de múltiples monedas*, *Gestión de precios de venta*,
*Unidades de medida*: son los que aparecen y desaparecen al activar opciones en Ajustes.

## 3. Las 12 pruebas de acceso

Entra con **cada usuario en una ventana de navegación privada** (para no perder tu sesión de administrador)
y marca el resultado observado. Si algo no coincide con lo esperado, corrige los grupos y repite.

| # | Usuario | Prueba | Resultado esperado | ✔ |
|---|---|---|---|---|
| 1 | Ana | Abrir el menú principal | Ve Ventas y Contactos; **no** ve Compras, Inventario ni Ajustes | ☐ |
| 2 | Ana | Crear un presupuesto para *Bodega Doña Rosa* | Lo puede crear y confirmar | ☐ |
| 3 | Ana | Ver la lista de presupuestos | Solo ve los suyos (regla de registro) | ☐ |
| 4 | Ana | Intentar entrar a Ajustes por URL directa (`/odoo/settings`) | Acceso denegado | ☐ |
| 5 | Diego | Menú principal | Ve Compras, Inventario y Contactos; **no** ve Ventas | ☐ |
| 6 | Diego | Crear una solicitud de presupuesto de *Quinua perlada* | Puede; el proveedor y el precio salen del CSV importado | ☐ |
| 7 | Diego | Abrir un producto y ver el precio de venta | Lo ve, pero no puede modificar campos de Ventas | ☐ |
| 8 | Marco | Menú principal | Ve Inventario y Contactos (en v20 el menú Contactos lo ve todo usuario con rol *Usuario*); **no** ve Ventas, Compras ni Ajustes | ☐ |
| 9 | Marco | Hacer un ajuste de inventario | Puede (y en la Fase 3 decidiremos si **debe** poder) | ☐ |
| 10 | Marco | Ver el costo de un producto | **No** debería ver información de compra/coste | ☐ |
| 11 | Sofía | Menú principal | Ve todo, incluidos Ajustes | ☐ |
| 12 | Sofía | Ver los presupuestos de Ana | Los ve todos (sin regla de registro restrictiva) | ☐ |

## 4. El experimento clave: grupo vs. regla de registro

1. Con Ana creados 3 presupuestos, entra como **administrador** y crea 2 presupuestos más
   asignando otro vendedor.
2. Entra como Ana: ve **3**.
3. Vuelve como administrador y cambia el grupo de Ventas de Ana de
   *Usuario: solo mostrar documentos propios* a *Usuario: todos los documentos*.
4. Entra como Ana: ahora ve **5**. **Los menús no cambiaron** — cambió qué filas puede leer.

**Escribe en tu bitácora, con tus palabras:**
> El grupo define **qué puede hacer y qué menús ve**; la regla de registro define **sobre qué registros**.
> Ejemplo de negocio de cada uno: ____________

## 5. Cómo inspeccionar las reglas (modo desarrollador)

En v20 (igual que desde saas-19.x) ya no hay dos menús separados de *Listas de control de acceso* y
*Reglas de registro*: ambos se fusionaron en un solo modelo, `ir.access`.

- *Ajustes → Técnico → Seguridad → Permisos de acceso*: filtra por modelo `sale.order`. Cada fila dice
  **qué grupo** puede hacer **qué operaciones** (`r` leer, `u` modificar, `c` crear, `d` eliminar) y,
  opcionalmente, **sobre qué registros** (el *dominio*).
- Busca la fila *Personal Orders* del grupo *Usuario: solo mostrar documentos propios*: su dominio es
  `['|', ('user_id', '=', user.id), ('user_id', '=', False)]` —sus pedidos **y** los que no tienen
  vendedor—. Ahí está, literalmente, la restricción. La fila *All Orders* del grupo *Usuario: todos los
  documentos* no tiene dominio: por eso ve todo.
- Una fila **sin grupo** es una *restricción* global (lo que antes era una regla de registro global);
  una con grupo es un *permiso*.

No modifiques nada aquí todavía: en la Fase 9 aprenderás cuándo tocar esto y cuándo no.

## 6. Errores frecuentes en este ejercicio

| Error | Síntoma | Corrección |
|---|---|---|
| Probar permisos con el mismo navegador | "Sigo viendo todo" | Usar ventana privada o cerrar sesión |
| Ana ve los presupuestos de otros aunque tenga *solo propios* | Con *Punto de venta* instalado, v20 da a cada usuario nuevo el grupo *Punto de venta / Usuario*, y ese grupo lee todos los pedidos (permiso *POS Sales Orders*) | Quita a Ana el grupo de Punto de venta y revisa los grupos que Odoo añadió por defecto al crear el usuario |
| Dar *Ajustes* a un usuario "para que pueda trabajar" | Ve y modifica toda la configuración | Nunca es la solución; buscar el grupo correcto |
| Confundir usuario interno con usuario de portal | El de portal no consume licencia y ve muy poco | El portal se usa para clientes (Fase 2) |
| Asignar grupos y no probarlos | En UAT el usuario no puede trabajar | Cada rol se prueba **entrando con él** |
