# Diagnóstico de 15 puntos

Contenido: la lista completa de verificación del Modo 3, con la consecuencia
observable de cada falla. Léelo cuando alguien traiga un skill que no funciona.

Explica cada hallazgo por su **consecuencia**, no por la regla que incumple.
"Tu descripción no tiene disparadores" no le dice nada a nadie; "por eso no se
activa cuando escribes 'hazme la factura'" sí, y además le da a la persona una
forma de verificar si el arreglo sirvió.

Clasifica cada hallazgo:

- **CRÍTICO** — el skill no instala, o no se activa, o produce resultados malos.
- **MEJORA** — funciona, pero desperdicia contexto, tiempo o dinero.
- **SUGERENCIA** — vale la pena, no urge.

---

## Frontmatter (5 puntos)

**1. Nombre en kebab-case**
Falla: mayúsculas, espacios o guión bajo.
Consecuencia: el validador lo rechaza al instalar. CRÍTICO.

**2. Nombre sin las palabras del asistente ni de su empresa**
Consecuencia: rechazo en la instalación. CRÍTICO.

**3. Sin los símbolos menor-que ni mayor-que en el frontmatter**
Consecuencia: el frontmatter no se parsea y el skill no carga. CRÍTICO.

**4. Descripción con qué + cuándo + disparadores, bajo 1024 caracteres**
Falla frecuente: dice qué hace pero no cuándo usarla.
Consecuencia: el skill queda instalado pero invisible — nunca se activa solo, la
persona tiene que nombrarlo cada vez, que es justo lo que quería evitar. CRÍTICO.
Si se pasa de 1024, se corta o se rechaza: recorta ejemplos, no los disparadores.

**5. Frases-NO presentes**
Consecuencia: choca con otros skills de vocabulario parecido y se activa el
equivocado. CRÍTICO si la persona tiene skills adyacentes; MEJORA si no.

---

## Cuerpo (5 puntos)

**6. Reglas críticas al inicio**
Consecuencia: si van al final, el modelo ya tomó decisiones antes de leerlas.
MEJORA.

**7. Fases numeradas con condición de salida**
Consecuencia: sin condición de salida, el skill avanza con datos incompletos y
el error solo se ve al final. MEJORA, o CRÍTICO si el flujo escribe o envía algo.

**8. Un fallback por cada conector**
Consecuencia: cuando el servicio no responde, el skill se cuelga a mitad de
camino sin explicar por qué, y la persona deja de usarlo. CRÍTICO.

**9. Pausas de aprobación humana antes de escribir, enviar, cobrar o borrar**
Consecuencia: acciones irreversibles sin revisión. CRÍTICO.

**10. Mínimo 3 ejemplos, uno de ellos borde**
Consecuencia: sin ejemplos el modelo improvisa el formato de salida y cambia
entre usos. Sin ejemplo borde, falla justo donde más importa. MEJORA.

---

## Calidad (5 puntos)

**11. Patrón canónico reconocible**
Falla: el cuerpo mezcla estructuras sin forma clara.
Consecuencia: difícil de mantener y de diagnosticar. SUGERENCIA.

**12. Menos de 500 líneas**
Consecuencia: consume contexto en cada activación y diluye lo importante.
MEJORA — muévelo a `references/`.

**13. Datos en `references/`, no en el cuerpo**
Falla: tarifas, catálogos y listas largas metidas entre las instrucciones.
Consecuencia: hay que reescribir el skill cada vez que cambia un dato, y
mientras tanto trabaja con información vieja sin avisar. MEJORA.

**14. Versión declarada en la descripción**
Consecuencia: nadie sabe cuál copia está instalada cuando hay varias dando
vueltas. SUGERENCIA.

**15. Casos borde cubiertos**
Pregunta de control: ¿qué hace si el dato no existe, si el archivo está vacío,
si el conector devuelve cero resultados?
Consecuencia: inventa datos o se detiene sin explicar. CRÍTICO si inventa.

---

## Entrega del diagnóstico

1. Los 15 puntos revisados, clasificados.
2. Cada CRÍTICO con su consecuencia observable.
3. Tabla "versión actual vs versión propuesta".
4. Spec mejorado de 12 secciones.
5. Bloque listo para llevar a Modo 2.

## Atajo: síntomas frecuentes

| Síntoma | Mira primero |
|---|---|
| "No se activa nunca" | Puntos 4 y 5 |
| "Se activa cuando no debe" | Punto 5 |
| "Se activa pero hace otra cosa" | Puntos 6, 7 y 10 |
| "Funciona a veces sí y a veces no" | Puntos 8 y 15 |
| "Va lentísimo o cuesta mucho" | Puntos 12 y 13 |
| "El validador lo rechaza" | Puntos 1, 2 y 3 |
