# C3 — Ocho conversaciones difíciles

> Escribe tu respuesta a cada situación en 5–8 líneas, **como si la dijeras en voz alta**.
> Después compárala con la respuesta modelo. No hay una única correcta; se evalúan tres cosas:
> **transparencia temprana**, **no prometer lo que no has probado** y **que el cliente decida
> informado**.

---

## 1. La funcionalidad prometida al directorio

El gerente comercial ya le presentó al directorio que el sistema "va a calcular las comisiones
automáticamente según margen y cobranza". Nunca lo mencionó en el levantamiento y no está en el alcance.

**Tu respuesta:**

> *Modelo:* "Entiendo la situación y quiero ayudarte a salir bien de esta. Eso no está en el alcance
> que firmamos, y hacerlo bien requiere definir las reglas de comisión, que hoy no están escritas en
> ningún lado. Te propongo dos cosas: primero, en el arranque el cálculo lo seguimos haciendo en
> Excel con los datos que ya te va a dar el sistema —que es más de lo que tienes hoy—; y segundo, lo
> cotizamos aparte con las reglas por escrito. Si necesitas presentarlo al directorio, puedo darte el
> alcance y el plazo esta semana para que lo lleves como fase dos."

**Por qué funciona:** no lo humilla, no dice "no", ofrece algo hoy y convierte el problema en una
decisión con precio y fecha.

---

## 2. El usuario clave que sabotea

El jefe de almacén no asiste a las reuniones, no entrega los datos y en la capacitación dice que
"antes era más rápido". Su forma de trabajar quedará auditada por primera vez.

**Tu respuesta:**

> *Modelo:* Con él, en privado y sin acusarlo: "Marco, necesito tu ayuda con algo. Tú eres el que más
> sabe cómo se mueve el almacén y si el sistema no refleja cómo trabajas de verdad, va a salir mal y
> el que va a sufrir eres tú. ¿Qué es lo que más te preocupa de esto?" — y escuchar.
> Con el patrocinador, después y por escrito: "El proyecto necesita que el almacén participe. Sin los
> datos de X y la validación de Y, la fecha de enero está en riesgo. Necesito que definas con Marco
> cuánto tiempo puede dedicar."

**La regla:** la resistencia se trabaja en privado; el impacto en el proyecto se comunica al
patrocinador por escrito, sin adjetivos sobre las personas.

---

## 3. "Son tres módulos rapiditos"

A mitad de proyecto piden agregar Mantenimiento, Calidad y Flota "que ya vienen incluidos".

**Tu respuesta:**

> *Modelo:* "Vienen incluidos en la licencia, sí, pero no en el trabajo. Cada módulo necesita
> definir su proceso, configurarlo, cargar sus datos, probarlo y capacitar. Calidad, por ejemplo,
> exige definir qué se controla y quién decide si algo se rechaza, y eso es una decisión de ustedes,
> no una configuración. Te propongo terminar lo que está en marcha para llegar a enero, y en febrero
> evaluamos estos tres con su propio alcance. Si alguno es urgente, dime cuál y vemos qué sale del
> alcance actual para hacerle sitio."

**La clave:** *"¿qué sale para que esto entre?"* convierte una petición gratis en una decisión real.

---

## 4. Los datos del cliente están podridos

La migración revela que el maestro de productos tiene duplicados, precios en cero y códigos repetidos
desde hace años. Nadie lo sabía.

**Tu respuesta:**

> *Modelo:* "Encontramos algo que necesitan saber: en su maestro hay 340 productos duplicados y 80
> sin precio. No es culpa de nadie, pasa en todos lados, pero tenemos que decidir qué hacemos. Migrar
> tal cual es rápido pero arrastra el problema; limpiarlo toma unas 30 horas y necesito a alguien de
> ustedes que decida qué producto queda cuando hay duplicados. Mi recomendación es limpiarlo ahora:
> es la única oportunidad de empezar con datos sanos, y el costo es menor que convivir con esto otro año."

---

## 5. Reportes imposibles

El gerente quiere un reporte de rentabilidad por cliente incluyendo el costo de las visitas
comerciales, pero nadie registra las visitas ni el tiempo del vendedor.

**Tu respuesta:**

> *Modelo:* "Ese reporte se puede construir, pero necesita un dato que hoy no existe: cuánto tiempo
> le dedica cada vendedor a cada cliente. El sistema no puede inventarlo. Hay dos caminos: que los
> vendedores registren sus visitas —lo que cambia su rutina y hay que acordarlo con ellos—, o
> empezamos con la rentabilidad por venta, que sí sale desde el día uno, y agregamos el costo
> comercial cuando el registro de visitas esté funcionando. Yo empezaría por lo segundo."

**El principio:** *ningún reporte puede salir de un dato que nadie captura.* Decirlo temprano evita
la frustración de la UAT.

---

## 6. Tu propio error

En la UAT se descubre que configuraste mal la política de facturación de 40 productos. Corregirlo y
reprocesar toma 3 días y hay pruebas hechas sobre esos datos.

**Tu respuesta:**

> *Modelo:* "Encontré un error mío: configuré 40 productos para facturar contra pedido cuando debían
> ser contra entrega. Lo detectamos ahora, que es el momento correcto para detectarlo. Corregirlo me
> toma un día y hay que repetir 6 casos de prueba, que son otros dos. Ya ajusté el cronograma y no
> afecta la fecha de salida. Y para que no vuelva a pasar, agregué al checklist una verificación de
> política por categoría de producto."

**Las tres partes:** lo digo yo antes de que lo descubran, digo el impacto real, y digo qué cambio
para que no se repita. Sin excusas y sin dramatizar.

---

## 7. El cambio de alcance a cinco días del go-live

El cliente pide agregar un campo obligatorio y un reporte nuevo "antes de salir".

**Tu respuesta:**

> *Modelo:* "A cinco días de salir, cualquier cambio nos obliga a repetir pruebas, y ese es el riesgo
> real: no el cambio, sino lo que puede romper sin que lo veamos. Te propongo salir como está —que ya
> pasó UAT— y lo entregamos en la primera semana de estabilización, que además es cuando vas a saber
> si de verdad lo necesitas así. Si consideras que es imprescindible para operar, lo hacemos y
> movemos la fecha; esa decisión sí es tuya, pero necesito que sea explícita."

---

## 8. "El sistema anterior sí lo hacía"

Un usuario compara constantemente con el sistema viejo y bloquea la adopción.

**Tu respuesta:**

> *Modelo:* "Cuéntame exactamente cómo lo hacías allá, paso a paso." Y escuchar de verdad.
> Habrá tres casos: (a) Odoo lo hace de otra forma → se le enseña; (b) Odoo no lo hace y es
> importante → se registra como requerimiento y se decide; (c) Odoo no lo hace porque era una mala
> práctica → se explica por qué, con el beneficio para él, no para la empresa.
> Lo que nunca funciona es responder "así es Odoo".

---

## Autoevaluación

| Criterio | ¿Tus 8 respuestas lo cumplen? |
|---|---|
| ¿Comuniqué el problema antes de que lo descubrieran? | |
| ¿Ofrecí una alternativa concreta, no solo un "no"? | |
| ¿Dejé la decisión en manos del cliente, informada? | |
| ¿Evité prometer algo que no he probado? | |
| ¿Hablé de impacto y fechas, no de culpas? | |
| ¿Lo dejé por escrito después? | |
