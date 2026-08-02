# Superficies: dónde corre el skill

Contenido: qué cambia entre las tres superficies donde vive un skill. Léelo en
el Paso 1 del Modo 1 (para saber qué conectores son posibles) y en el Modo 4
(para dar los pasos de instalación correctos).

El mismo `SKILL.md` funciona en las tres. Lo que cambia es **dónde se instala**
y **qué puede hacer**. Por eso hay que preguntar la superficie antes de diseñar:
un flujo que depende de ejecutar scripts sobre archivos locales no se puede
diseñar igual para un chat que para un entorno con terminal.

---

## Chat (la app y el sitio web)

**Instalación:** ajustes → personalización → skills → subir el archivo `.skill`.

**Conectores:** se activan por cuenta (almacenamiento, correo, notas,
calendario, entre otros). Verifica cuáles tiene activos la persona en vez de
asumir.

**Límite importante:** el conector de correo **crea borradores, no envía**.
Diseña el flujo contando con eso — y de hecho es sano: el envío es exactamente
el paso donde quieres una revisión humana.

**Archivos:** puede generar archivos si la persona tiene habilitada la creación
de archivos y la ejecución de código en su cuenta.

**Cómo se prueba:** abrir un hilo nuevo y escribir una de las frases
disparadoras, sin nombrar el skill. Si hay que nombrarlo para que se active, la
descripción tiene un problema.

---

## Cowork

**Instalación:** usa las mismas skills habilitadas en la cuenta; se gestionan
desde personalización en la barra lateral o desde la web.

**Fortaleza:** trabaja sobre carpetas locales y sostiene tareas largas en
segundo plano. Es la superficie natural para skills que producen entregables
(documentos, hojas de cálculo, presentaciones) a partir de archivos reales.

**Trampa que cuesta horas:** Cowork **no lee la carpeta de skills local del CLI
de código**. Si el skill solo existe como carpeta en el computador, en Cowork no
aparece. Hay que subirlo como cualquier otro skill de la cuenta.

**Cómo se prueba:** conectar la carpeta donde están los archivos de entrada,
abrir un hilo nuevo y escribir una frase disparadora.

---

## CLI de código

**Instalación:** se copia la **carpeta** del skill (no un zip) a la carpeta de
skills personal — sirve para todos sus proyectos — o a la del repositorio, que
la comparte con su equipo. Después se reinicia la sesión.

**Servicios externos:** se conectan como servidores MCP configurados localmente,
no como conectores de cuenta. Son configuración por máquina o por proyecto, así
que un skill que dependa de ellos hay que documentarlo con su requisito.

**Fortaleza:** ejecuta comandos y scripts sobre archivos reales. Es la
superficie donde `scripts/` rinde más.

**Cómo se prueba:** reiniciar y pedir algo que active el skill de forma natural.

---

## Regla de decisión rápida

| Lo que necesita el skill | Superficie |
|---|---|
| Solo conversación y texto | Chat |
| Producir documentos a partir de archivos del computador | Cowork |
| Ejecutar scripts o tocar un repositorio | CLI de código |
| No se sabe | Chat (es el default y el más fácil de instalar) |

Si dudas de la ruta exacta de instalación en la versión que usa la persona, pide
que la verifique en la configuración de esa superficie. Inventar una ruta que no
existe cuesta más confianza de la que ahorra tiempo.
