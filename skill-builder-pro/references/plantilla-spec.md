# Plantilla del Spec — 12 secciones

Contenido: el formato exacto de cada sección del Spec que produce el Modo 1.
Léelo cuando vayas a escribir o revisar un Spec. No omitas ni reordenes
secciones: el Modo 2 las lee en este orden para construir.

Si falta información, escribe `[SUPUESTO]` con tu mejor default y sigue. Un Spec
con supuestos marcados se corrige en 30 segundos; un Spec incompleto obliga a
empezar de nuevo.

---

## 1. IDENTIDAD

```
Nombre técnico (kebab-case): generador-de-cobros
Nombre legible: Generador de Cobros
Propósito en una línea: Convierte las horas registradas de la semana en una
  factura lista para enviar al cliente.
Para quién: dueños de agencias pequeñas que facturan por horas.
Cuándo se usa: cada viernes al cerrar la semana, o al terminar un proyecto.
Superficie: chat / Cowork / CLI de código
Patrón dominante: flujo secuencial — porque no puedes calcular el total antes
  de haber consolidado las horas.
Patrones secundarios: dominio embebido (tus tarifas y reglas de descuento).
```

## 2. DISPARADORES

De 10 a 20 frases reales que la persona diría. Escríbelas como habla la gente,
no como habla un manual: minúsculas, jerga de su industria, abreviaciones.

```
Frases que SÍ activan:
- "hazme la factura de esta semana"
- "cuánto le cobro a [cliente] por lo de este mes"
- "arma el cobro del proyecto que acabamos de cerrar"
- ...

Frases que NO deben activarlo:
- "cuánto llevo gastado este mes"   (eso es control de gastos)
- "revisa si [cliente] ya me pagó"  (eso es cartera)
```

Las frases-NO no son opcionales. Sin ellas, dos skills con vocabulario parecido
se pisan y se activa el equivocado.

## 3. ENTRADAS

| Dato | ¿Obligatorio? | Cómo se obtiene | Ejemplo |
|---|---|---|---|
| Nombre del cliente | Sí | Lo dice la persona | "Ferretería Rojas" |
| Horas trabajadas | Sí | Hoja de cálculo conectada | 18.5 |
| Tarifa por hora | No | `references/tarifas.md` | 120000 |

**Máximo de preguntas que el skill puede hacer:** 3. Ponle un techo explícito.
Un skill que interroga se abandona.

## 4. FLUJO

Fases numeradas. Cada paso con sus cuatro campos, y cada fase con su condición
de salida.

```
FASE 1 — Consolidar horas
  Paso 1.1
    Entrada: nombre del cliente y rango de fechas
    Salida: lista de registros de horas
    Herramienta: hoja de cálculo conectada
    Fallback: si no hay conexión, pedir que peguen las horas en el chat
  Condición para pasar a la Fase 2: hay al menos un registro y la persona
  confirmó que el total de horas es correcto.  [PAUSA HUMANA]

FASE 2 — Calcular y redactar
  ...
```

Marca las **pausas de aprobación humana** con `[PAUSA HUMANA]`. Todo paso que
escriba, envíe, cobre o borre algo lleva una antes.

## 5. SALIDAS

| Salida | Formato | Destino | Ejemplo |
|---|---|---|---|
| Factura | .docx | carpeta del proyecto | `factura-rojas-2026-08.docx` |
| Resumen | texto | el chat | "18.5 h · 2.220.000 · vence 15/09" |

## 6. CONECTORES

| Conector | En qué paso | Para qué | Fallback |
|---|---|---|---|
| Hoja de cálculo | 1.1 | leer horas | pedir pegado manual en el chat |
| Correo | 3.2 | dejar borrador | entregar el texto para copiar |

Nunca listes un conector sin verificar que existe en la superficie elegida, y
nunca sin fallback. Un conector caído sin fallback deja el skill muerto a mitad
de camino.

## 7. REGLAS DE ORO

Lo que el skill no puede romper nunca, con la razón al lado:

```
- Nunca envía la factura, solo la deja en borrador — el envío es una decisión
  comercial que no le corresponde al skill.
- Si faltan horas de algún día, avisa antes de calcular en vez de asumir cero.
```

## 8. CASOS BORDE

Mínimo 3. Cada uno con situación, comportamiento esperado y justificación.

```
Caso 1
  Situación: el cliente tiene tarifas distintas por tipo de trabajo.
  Comportamiento: separar por tipo y mostrar subtotales antes de sumar.
  Por qué: cobrar todo a una tarifa única es el error más caro y el más difícil
  de detectar en la revisión.
```

## 9. ARCHIVOS DE REFERENCIA

```
references/tarifas.md    — tabla de tarifas por cliente y tipo de trabajo
assets/plantilla.docx    — machote de factura con el logo
scripts/calcular.py      — cálculo de subtotales, impuestos y descuentos
```

Regla de decisión: si el contenido **cambia sin que cambie el flujo**, va a
`references/`. Si es **cálculo determinista**, va a `scripts/`. Si es **un
archivo que aparece en la salida**, va a `assets/`.

## 10. EJEMPLOS

Mínimo 3 pares entrada-salida, e incluye al menos uno borde.

```
Ejemplo 1 (normal)
  Entrada: "hazme la factura de Rojas de esta semana"
  Salida: [factura .docx + resumen en el chat]

Ejemplo 3 (borde)
  Entrada: "hazme la factura de Rojas" — pero no hay horas registradas
  Salida: "No encontré horas registradas para Rojas entre el 27/07 y el 01/08.
  ¿Quieres que use otro rango de fechas, o prefieres pegarme las horas aquí?"
```

## 11. MÉTRICAS DE ÉXITO

Medibles, no opiniones. "Que quede bonita" no es métrica.

```
- La factura sale sin corrección manual en 8 de cada 10 usos.
- El proceso baja de 25 minutos a menos de 5.
- El skill se activa con la frase natural de la persona sin tener que nombrarlo.
```

## 12. NOTAS PARA QUIEN CONSTRUYE

Advertencias para el Modo 2:

```
- El nombre del cliente llega con mayúsculas inconsistentes; normalizar antes
  de buscar en la hoja.
- La descripción necesita frases-NO fuertes: la persona ya tiene instalado un
  skill de control de gastos con vocabulario muy parecido.
```
