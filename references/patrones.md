# Los 5 patrones canónicos

Contenido: cómo reconocer cada patrón, cómo se ve su flujo, y en qué falla
típicamente. Léelo en el Paso 3 del Modo 1, cuando tengas que justificar la
elección del patrón.

Casi ningún skill real es de un solo patrón. Elige **uno dominante** (el que
define la forma del flujo) y **uno o dos secundarios** (los que aparecen dentro
de alguna fase). Nombrar el patrón no es burocracia: es lo que decide si el
cuerpo del skill se escribe como una lista de fases, como un árbol de decisión,
o como un ciclo.

---

## 1. Flujo secuencial

**Señal:** los pasos van en orden estricto y cada uno necesita el resultado del
anterior. Si intentas saltarte el paso 2, el 3 no tiene con qué trabajar.

**Analogía:** una receta. No puedes hornear antes de mezclar.

**Forma del cuerpo:** fases numeradas, con condición de salida explícita en cada
una.

**Falla típica:** no declarar la condición de salida, así que el skill avanza a
la fase siguiente con datos incompletos y el error solo aparece al final, cuando
ya es caro corregirlo. Arréglalo poniendo una condición verificable al cierre de
cada fase.

**Ejemplos:** facturación, onboarding de un cliente, cierre de mes.

---

## 2. Coordinación multi-conector

**Señal:** el skill toca dos o más servicios externos, y el valor está justo en
que alguien mueva datos entre ellos.

**Analogía:** un coordinador que llama a tres oficinas distintas y arma una sola
respuesta.

**Forma del cuerpo:** una tabla de conectores arriba, y en cada paso el conector
que usa más su fallback en la línea de al lado.

**Falla típica:** asumir que todos los conectores están activos y responden. En
la práctica uno se cae, o la persona nunca lo conectó, y el skill se queda
colgado sin decir por qué. Cada conector necesita su fallback escrito *junto al
paso*, no en una sección aparte que el modelo lee tarde.

**Segunda falla:** encadenar servicios sin pausa humana. Si el skill lee de un
sitio y escribe en otro, la escritura necesita aprobación.

**Ejemplos:** preparar reuniones, digest semanal, sincronizar tareas.

---

## 3. Refinamiento iterativo

**Señal:** el resultado mejora con vueltas. La primera versión nunca es la
buena, y eso es esperado, no un error.

**Analogía:** un borrador que pasa por edición dos o tres veces.

**Forma del cuerpo:** un ciclo con criterio de parada explícito y un techo de
iteraciones. Sin techo, el skill puede quedarse puliendo indefinidamente.

**Falla típica:** no definir qué es "suficientemente bueno", así que el skill
itera de más (quema tokens y paciencia) o de menos (entrega el primer borrador
como si fuera final). Escribe el criterio de parada en términos verificables y
pon una pausa humana en la primera vuelta.

**Ejemplos:** redacción de propuestas, reportes ejecutivos, guiones.

---

## 4. Selección según contexto

**Señal:** la herramienta o la ruta a seguir depende de lo que entre. Un PDF se
trata distinto de una hoja de cálculo; un cliente nuevo distinto de uno
recurrente.

**Analogía:** un triage. Primero clasificas, después tratas.

**Forma del cuerpo:** una tabla de decisión al inicio y luego una sección por
rama. Si las ramas son largas, cada una va a su propio archivo en `references/`
y el cuerpo solo se queda con la tabla — así el modelo carga solo la rama que
necesita.

**Falla típica:** no cubrir el caso "no encaja en ninguna rama". Siempre define
la rama por defecto y qué hace el skill cuando no logra clasificar: preguntar
suele ser mejor que adivinar.

**Ejemplos:** procesar archivos de formato variable, clasificar correos entrantes.

---

## 5. Dominio embebido

**Señal:** hay reglas de negocio, tarifas, políticas o requisitos de cumplimiento
metidos dentro de la lógica. El skill no solo ejecuta pasos: aplica criterios
propios de esa organización.

**Analogía:** un empleado que ya se sabe las políticas de la casa.

**Forma del cuerpo:** las reglas de negocio arriba del todo, y los datos que las
alimentan en `references/`. Las reglas son instrucciones y se quedan; los datos
cambian y se van.

**Falla típica:** escribir los datos dentro del cuerpo. Cuando cambia una tarifa
hay que reescribir el skill entero, y mientras tanto el skill sigue cotizando
con precios viejos sin que nadie lo note. Separa siempre.

**Segunda falla:** reglas sin justificación. Si el modelo no entiende por qué
una regla existe, no sabe aplicarla en el caso que no previste.

**Ejemplos:** cotizador con reglas de descuento, revisión de contratos, control
de cumplimiento.

---

## Cómo combinar

| Dominante | Secundario frecuente | Por qué se juntan |
|---|---|---|
| Secuencial | Multi-conector | las fases van en orden y cada una consulta un servicio distinto |
| Secuencial | Dominio embebido | el orden es fijo pero las reglas de la casa mandan en el cálculo |
| Multi-conector | Selección por contexto | según lo que devuelva el primer servicio, cambia el segundo |
| Iterativo | Dominio embebido | cada vuelta se evalúa contra los criterios de la organización |
| Selección | Secuencial | clasificas primero, y cada rama es un flujo ordenado |
