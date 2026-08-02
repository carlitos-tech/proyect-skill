# Biblioteca de frases disparadoras

Contenido: cómo escribir la parte de la descripción que decide si el skill se
activa. Léelo en el Paso 3 del Modo 2, y siempre que el diagnóstico apunte a
"no se activa".

La descripción es lo único que Claude lee **antes** de decidir si abre el skill.
Todo lo demás llega tarde. Por eso vale la pena tratarla como el producto
principal, no como un campo administrativo.

---

## La fórmula

```
[QUÉ hace, en una o dos frases]
[CUÁNDO usarla: el contexto, el momento, el tipo de tarea]
Actívate con frases como "...", "...", "..." (de 10 a 20).
Actívate también cuando [situación donde la persona no usa el vocabulario técnico].
NO usar para [de 2 a 4 casos adyacentes que pertenecen a otro skill].
```

---

## Cómo escribir las frases que SÍ activan

Escríbelas como **habla la persona antes de saber que el skill existe**. Ese es
el punto entero: si tuviera que aprender la frase mágica, el skill no le ahorra
nada.

Reglas prácticas:

- **Minúsculas y desorden.** La gente escribe "necesito la factura de rojas ya",
  no "Genere una factura para el cliente Rojas".
- **Jerga de su industria.** Si son contadores, "conciliación" y "cartera". Si
  son diseñadores, "mockup" y "entregable".
- **Variar la formalidad.** Tres o cuatro frases formales, el resto casuales.
- **Incluir el caso implícito.** La persona describe el problema sin nombrar la
  solución: "no sé cuánto llevo cobrado este mes" debería activar el skill de
  facturación aunque no diga "factura".
- **Incluir los sinónimos reales.** Cobro, factura, cuenta de cobro, remisión —
  en distintos países la misma cosa se llama distinto.
- **Incluir el verbo de arranque.** "hazme", "arma", "genera", "necesito",
  "cómo hago para".

Prueba de calidad: lee las frases y pregúntate si alguien las escribiría un
martes a las 4 de la tarde con prisa. Si suenan a documentación, reescríbelas.

---

## Cómo escribir las frases-NO

Las buenas frases-NO son las **casi-aciertos**: comparten vocabulario con el
skill pero pertenecen a otro sitio. Una frase-NO obviamente irrelevante no
protege de nada.

Malas (no prueban nada):

```
NO usar para: escribir poemas, hacer cálculos matemáticos
```

Buenas (protegen de la confusión real):

```
NO usar para: revisar si un cliente ya pagó (eso es cartera), proyectar
ingresos futuros (eso es presupuesto), ni registrar horas conforme se trabajan
(eso es control de tiempo). Este skill solo convierte horas ya registradas en
un cobro.
```

Fuente para encontrarlas: pregunta qué otros skills tiene instalados y qué hace
cada uno. Las fronteras entre skills vecinos son donde ocurren los choques.

---

## El límite de 1024 caracteres

Cuando no quepa, recorta en este orden:

1. Adjetivos y frases de relleno ("de manera profesional", "de alta calidad").
2. Frases disparadoras redundantes — quédate con las que usan vocabulario
   distinto, no con las que repiten la misma palabra clave.
3. La explicación larga del qué; una frase basta.

Nunca recortes: las frases-NO, ni el "cuándo". Son lo que más rinde por carácter.

---

## Ejemplos comparados

**Descripción que no se activa nunca:**

```
description: Genera facturas.
```

Problema: dice el qué, nada del cuándo, cero disparadores. Claude no tiene
ninguna señal para saber en qué momento abrirla.

**Descripción que se activa cuando debe:**

```
description: Convierte las horas ya registradas de un cliente en una cuenta de
cobro lista para revisar, aplicando las tarifas y descuentos de la casa.
Actívate con frases como "hazme la factura de esta semana", "cuánto le cobro a
[cliente]", "arma el cobro del proyecto", "necesito la cuenta de cobro de
agosto", "pásame las horas de [cliente] a factura", "cuánto llevo cobrado este
mes", "genera la remisión", "hay que facturarle a [cliente]". Actívate también
cuando alguien cierre un proyecto o una semana de trabajo y pregunte cuánto
corresponde cobrar, aunque no diga la palabra factura. NO usar para revisar si
ya pagaron (eso es cartera), proyectar ingresos (eso es presupuesto), ni
registrar horas trabajadas (eso es control de tiempo). v1.0
```

---

## Cómo probar el disparo

Pide a la persona 5 frases con las que **ella** pediría la tarea, sin haber
visto la descripción. Compáralas con tu lista. Las que no cubriste son
exactamente las que faltaban — y suelen ser mejores que las que inventaste tú,
porque salen del vocabulario real de su trabajo.
