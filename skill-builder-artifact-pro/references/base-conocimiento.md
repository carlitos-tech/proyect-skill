# BASE DE CONOCIMIENTO: ARTIFACTS DE CLAUDE
## Guía completa y auditada — Versión 1.0 | Fecha de corte: Abril 2026
> Elaborada con fuentes oficiales de Anthropic: Help Center, documentación técnica, release notes, catálogo oficial y anuncios de producto.
> Nivel de confianza indicado por íconos: ✅ Verificado oficial | 🔍 Inferido con alta confianza | ⚠️ Especulativo

---

## ÍNDICE

1. [Definición oficial de Artifact](#1-definición-oficial-de-artifact)
2. [Qué NO es un Artifact](#2-qué-no-es-un-artifact)
3. [Tipos de Artifact que Claude puede crear](#3-tipos-de-artifact-que-claude-puede-crear)
4. [Funcionalidades avanzadas](#4-funcionalidades-avanzadas)
5. [Ecosistema y capas del sistema](#5-ecosistema-y-capas-del-sistema)
6. [Catálogo oficial y descubrimiento](#6-catálogo-oficial-y-descubrimiento)
7. [Publicación, compartir y embeber](#7-publicación-compartir-y-embeber)
8. [Personalización y remix](#8-personalización-y-remix)
9. [Disponibilidad por plan](#9-disponibilidad-por-plan)
10. [Restricciones técnicas conocidas](#10-restricciones-técnicas-conocidas)
11. [Librerías disponibles en artifacts React](#11-librerías-disponibles-en-artifacts-react)
12. [Casos de uso por perfil de usuario](#12-casos-de-uso-por-perfil-de-usuario)
13. [Inventario maestro de tipos y funcionalidades](#13-inventario-maestro-de-tipos-y-funcionalidades)
14. [Rankings de adopción y utilidad](#14-rankings-de-adopción-y-utilidad)
15. [Historial de lanzamientos relevantes](#15-historial-de-lanzamientos-relevantes)
16. [Guía de uso para conferencias y formación](#16-guía-de-uso-para-conferencias-y-formación)
17. [Prompts de referencia por tipo de artifact](#17-prompts-de-referencia-por-tipo-de-artifact)
18. [Recursos y referencias oficiales](#18-recursos-y-referencias-oficiales)

---

## 1. Definición oficial de Artifact

✅ **Fuente:** Help Center oficial de Claude (`support.claude.com`)

Un **Artifact** es cualquier pieza de contenido sustancial generada por Claude que aparece en una ventana dedicada separada del chat principal. Permite ver, editar, iterar y reutilizar el contenido sin perder el hilo de la conversación.

### Criterios para que Claude genere un Artifact automáticamente:
- El contenido es **significativo y autocontenido**, típicamente más de 15 líneas
- Es algo que probablemente quieras **editar, iterar o reutilizar** fuera de la conversación
- Representa contenido complejo que **se sostiene por sí solo** sin requerir contexto adicional
- Es contenido que probablemente quieras **volver a consultar o usar más tarde**

### Definición ampliada (2026):
Los artifacts han evolucionado de ser un simple panel de previsualización a un **entorno completo de desarrollo de micro-aplicaciones**. Hoy soportan llamadas directas a la API de Claude (apps con IA embebida), integraciones con servicios externos vía MCP, y almacenamiento persistente de datos entre sesiones.

---

## 2. Qué NO es un Artifact

✅ Es importante no confundir artifacts con otros elementos del ecosistema Claude:

| Concepto | Qué es | Diferencia con Artifact |
|---|---|---|
| **Skill** | Instrucción reutilizable que define cómo Claude se comporta o qué flujo sigue | Un artifact es un *output* (contenido generado); un skill es una *instrucción de proceso* |
| **Connector / MCP Server** | Integración con servicio externo (Gmail, Asana, Slack) | Un artifact puede *usar* un connector, pero el connector en sí no es un artifact |
| **Project** | Espacio de trabajo con memoria persistente y contexto compartido | Un project *puede contener* artifacts, pero no es un artifact |
| **Archivo simple** | Texto plano generado por Claude sin renderizado especial | Un artifact tiene previsualización activa, iteración integrada y puede publicarse |
| **Respuesta de chat** | Texto en el hilo principal de la conversación | Los artifacts aparecen en panel lateral dedicado |

### Terminología correcta — ✅ Verificado:
| ❌ Incorrecto | ✅ Correcto |
|---|---|
| "Instalar un artifact" | Descubrir, abrir, customizar, remixear |
| "App store de artifacts" | Catálogo / Inspiration tab |
| "Descargar un artifact" | Publicar, compartir link, exportar código |
| "El artifact me recuerda" | El artifact puede tener storage persistente (con publicación previa) |

---

## 3. Tipos de Artifact que Claude puede crear

✅ **Fuente:** Documentación oficial + Help Center

Claude soporta los siguientes tipos de artifact de forma nativa:

### 3.1 Código (Code Snippet)
- **MIME type:** `application/vnd.ant.code`
- **Descripción:** Fragmento de código en cualquier lenguaje de programación
- **Lenguajes soportados:** Python, JavaScript, TypeScript, Java, C++, C#, Ruby, Go, Rust, PHP, SQL, Shell, YAML, JSON, y más
- **Cuándo usarlo:** Scripts, funciones, algoritmos, configuraciones, consultas de base de datos
- **Restricciones:** No se renderiza visualmente, solo se muestra el código con syntax highlighting
- **Caso de uso típico:** "Escribe una función Python que procese este CSV"

### 3.2 Documento Markdown
- **MIME type:** `text/markdown`
- **Descripción:** Documentos de texto con formato enriquecido
- **Soporta:** Headers, listas, links, tablas, código inline, negritas, cursivas, blockquotes
- **Cuándo usarlo:** Reportes, propuestas, artículos, guías, documentación técnica
- **Caso de uso típico:** "Escribe una propuesta comercial para [cliente]"

### 3.3 Página HTML
- **MIME type:** `text/html`
- **Descripción:** Página web completa con HTML, CSS y JavaScript en un solo archivo
- **Se renderiza:** Sí, como página web real en el panel de artifact
- **Restricciones:**
  - Scripts externos solo desde CDN de Cloudflare (`cdnjs.cloudflare.com`)
  - No puede usar imágenes externas (usar `/api/placeholder/width/height`)
  - Un solo archivo (no múltiples archivos vinculados)
- **Cuándo usarlo:** Landing pages, formularios, dashboards, herramientas interactivas, calculadoras
- **Caso de uso típico:** "Crea un dashboard con estos KPIs de negocio"

### 3.4 Imagen SVG
- **MIME type:** `image/svg+xml`
- **Descripción:** Gráficos vectoriales escalables, 100% editables por código
- **Se renderiza:** Sí, como imagen vectorial
- **Ventajas:** Escalable sin perder calidad, editable, exportable
- **Cuándo usarlo:** Logos, iconos, ilustraciones técnicas, infografías, diagramas simples
- **Caso de uso típico:** "Crea un diagrama de flujo del proceso de onboarding"

### 3.5 Diagrama Mermaid
- **MIME type:** `application/vnd.ant.mermaid`
- **Descripción:** Diagramas generados mediante sintaxis de texto Mermaid
- **Tipos de diagrama soportados:**
  - Flowcharts (diagramas de flujo)
  - Sequence diagrams (diagramas de secuencia)
  - Gantt charts (cronogramas)
  - Entity Relationship Diagrams — ERD (bases de datos)
  - User Journey Diagrams
  - Class diagrams
  - State diagrams
  - Mind maps
  - Pie charts
- **Cuándo usarlo:** Documentación técnica, visualización de procesos, arquitecturas de sistema, timelines
- **Caso de uso típico:** "Diagrama la arquitectura de microservicios de nuestra app"

### 3.6 Componente React
- **MIME type:** `application/vnd.ant.react`
- **Descripción:** Componente React interactivo con estado, hooks y lógica compleja
- **Se renderiza:** Sí, directamente en el browser del panel de artifact
- **Características:**
  - Soporte completo de React Hooks (`useState`, `useEffect`, `useRef`, etc.)
  - Styling con Tailwind CSS
  - Librerías de visualización y UI (ver sección 11)
  - Interactividad completa (clicks, formularios, sliders, animaciones)
- **Restricciones:** Sin localStorage/sessionStorage, un solo archivo
- **Cuándo usarlo:** Prototipos de UI, simuladores interactivos, dashboards complejos, juegos, herramientas
- **Caso de uso típico:** "Crea un simulador de ROI con sliders para ajustar variables"

### 3.7 PDF *(disponible en Cowork)*
- **Extensión:** `.pdf`
- **Descripción:** Documentos PDF generados directamente desde Claude
- **Disponibilidad:** Confirmado para Claude Cowork (entorno de escritorio)
- **Caso de uso típico:** Reportes formales, propuestas exportables

---

## 4. Funcionalidades avanzadas

### 4.1 AI-Powered Artifacts (Artifacts con IA embebida)
✅ **Fuente:** Help Center oficial

Los artifacts pueden **llamar directamente a la API de Claude**, convirtiéndose en micro-aplicaciones con inteligencia artificial integrada.

**Cómo funciona:**
1. El usuario describe lo que quiere
2. Claude escribe el código del artifact (HTML/React)
3. El artifact incluye llamadas a la API de Claude internamente
4. Otros usuarios pueden usar el artifact con su propia cuenta — sin costo para el creador
5. El uso cuenta contra los límites de cada usuario, no del creador

**Casos de uso:**
- Tutores personalizados por materia
- Coaches de productividad interactivos
- Generadores de contenido personalizados
- Juegos adaptativos con IA
- Asistentes especializados en un dominio
- Analizadores de documentos con IA
- Simuladores con respuestas inteligentes

**Ventajas clave:**
- No requiere API keys propias del usuario
- No requiere servidor propio
- Escala gratis para el creador (10 usuarios o 10,000)
- Corre en la infraestructura de Anthropic

### 4.2 MCP Integration (Model Context Protocol)
✅ **Fuente:** Help Center oficial

Los artifacts pueden **conectarse a servicios externos** a través del Model Context Protocol.

**Servicios oficiales disponibles:**
- Google Calendar
- Gmail
- Slack
- Asana
- Y cualquier MCP server personalizado configurado por el usuario

**Cómo funciona:**
- El artifact solicita acceso al servicio la primera vez
- El usuario aprueba el acceso (persiste para usos posteriores)
- Cada usuario debe autenticarse de forma independiente en el MCP server
- Los administradores de organización pueden habilitar/deshabilitar acceso a MCP a nivel de org

**Planes requeridos:** Pro, Max, Team y Enterprise (en Claude web y desktop)

**Importante:** Los admins de organización pueden habilitar o deshabilitar el acceso MCP de artifacts a nivel de organización, pero NO pueden gestionar qué MCP servers específicos pueden usar los artifacts.

### 4.3 Persistent Storage (Almacenamiento persistente)
✅ **Fuente:** Help Center oficial

Los artifacts pueden **guardar y recuperar datos entre sesiones** usando una API de clave-valor.

**Dos modos de storage:**
| Modo | Quién ve los datos | Caso de uso |
|---|---|---|
| **Personal** (por defecto) | Solo el usuario actual | Journals, trackers personales, historial privado |
| **Shared** (compartido) | Todos los usuarios del artifact | Leaderboards, wikis colaborativas, datos compartidos de equipo |

**Especificaciones técnicas:**
- Límite de 20 MB por artifact
- Solo texto (no imágenes, archivos binarios ni multimedia)
- Storage personal y compartido completamente aislados
- Al despublicar un artifact, se eliminan PERMANENTEMENTE todos los datos de storage

**Importante:** El storage persistente SOLO funciona en artifacts publicados. Durante desarrollo/pruebas, las operaciones de storage fallan.

**Planes requeridos:** Pro, Max, Team y Enterprise (Claude web y desktop)

**API de Storage (para desarrollo):**
```javascript
// Guardar dato
await window.storage.set('key', value, shared?);

// Obtener dato
const result = await window.storage.get('key', shared?);

// Eliminar dato
await window.storage.delete('key', shared?);

// Listar claves
const keys = await window.storage.list(prefix?, shared?);
```

### 4.4 Edición inline (Diff Editor)
🔍 **Fuente:** Comunidad + alineado con release notes (Oct 2025)

Claude puede hacer **ediciones quirúrgicas** en artifacts sin reescribir todo el código desde cero.

- Cambios pequeños → reemplazo inline de strings exactos
- Cambios grandes → reescritura completa
- Los cambios aparecen en tiempo real mientras se aplican
- Disponible en todos los tipos: React, Markdown, SVG, Mermaid, HTML

---

## 5. Ecosistema y capas del sistema

El ecosistema de Artifacts de Claude tiene las siguientes capas:

```
CAPA 1 — CREACIÓN
├── Generado por Claude en conversación
└── Tipos: HTML, SVG, Mermaid, React, Markdown, Código, PDF

CAPA 2 — FUNCIONALIDAD AVANZADA
├── AI-powered (API de Claude embebida)
├── MCP integration (servicios externos)
└── Persistent storage (datos entre sesiones)

CAPA 3 — GESTIÓN
├── Sidebar de Artifacts (historial de todos los artifacts)
├── Versiones (selector de versiones por artifact)
└── Multi-artifact (múltiples artifacts en una conversación)

CAPA 4 — DESCUBRIMIENTO
├── Inspiration Tab (curado por Anthropic)
└── Catálogo público (claude.ai/catalog/artifacts)

CAPA 5 — DISTRIBUCIÓN
├── Publicar con link (Free, Pro, Max)
├── Sharing interno de org (Team, Enterprise)
└── Embed en sitios externos (código iframe)
```

---

## 6. Catálogo oficial y descubrimiento

### 6.1 Inspiration Tab
✅ **Fuente:** Help Center oficial + Support documentación

- **URL:** `claude.ai/artifacts` (dentro de la app, sidebar)
- **Acceso:** Menú lateral → Artifacts → Inspiration (o banner "Get inspired" en móvil)
- **Curado por:** Anthropic
- **Contenido:** Artifacts de alta calidad seleccionados por el equipo de Anthropic

**Categorías oficiales del Inspiration Tab:**
| Categoría | Tipo de contenido |
|---|---|
| **Learn something** | Tutores, simuladores educativos, quizzes |
| **Life hacks** | Utilidades, productividad, herramientas cotidianas |
| **Play a game** | Juegos interactivos, puzzles, entretenimiento |
| **Be creative** | Generadores, arte, proyectos creativos |
| **Touch grass** | Experiencias relajantes, mindfulness, naturaleza |

**Nota importante para usuarios Team/Enterprise:** No tienen acceso al Inspiration Tab público. En su lugar, ven artifacts compartidos internamente por sus colegas.

### 6.2 Catálogo público
✅ **Fuente:** URLs indexadas del catálogo oficial

- **URL base:** `claude.ai/catalog/artifacts`
- **Estructura de URL:** `claude.ai/catalog/artifacts/{idioma}/{categoría}`
- **Contenido:** Miles de artifacts publicados por usuarios de todo el mundo
- **Idiomas indexados:** Español, inglés, japonés, francés, portugués, alemán, otros

**Categorías del catálogo público:**
| Categoría | URL slug | Contenido |
|---|---|---|
| **Be Creative** | `be-creative` | Arte, diseño, generadores de contenido |
| **Learn** | `learn` | Educación, tutoriales, cursos interactivos |
| **Life Hacks** | `life-hacks` | Productividad, utilidades, calculadoras |
| **Data Analysis** | `data-analysis` | Dashboards, gráficos, análisis de datos |
| **Play a Game** | `play-a-game` | Juegos, puzzles, entretenimiento |
| **Code & Tech** | `code-tech` | Herramientas para desarrolladores |
| **Touch Grass** | `touch-grass` | Relajación, mindfulness |

**Ejemplo de URLs por idioma y categoría:**
- `claude.ai/catalog/artifacts/es/be-creative` → Artifacts creativos en español
- `claude.ai/catalog/artifacts/es/learn` → Artifacts educativos en español
- `claude.ai/catalog/artifacts/es/life-hacks` → Utilidades en español

### 6.3 Made with Claude (comunidad no oficial)
🔍 **Fuente:** Comunidad

- **URL:** `madewithclaude.com`
- **Estado:** No es recurso oficial de Anthropic, pero es el directorio comunitario más usado
- **Categorías:** Tools, Design, Data, Graphics, Education, Programming, Creative, Web Design, Games, Applications, Entertainment
- **Utilidad:** Buena fuente de inspiración y ejemplos

---

## 7. Publicación, compartir y embeber

### 7.1 Publicación pública (Free, Pro, Max)
✅ **Fuente:** Help Center — Publishing and sharing artifacts

**Proceso:**
1. Navega al artifact que quieres publicar
2. Verifica que estás en la versión correcta
3. Haz clic en el botón "Publish"
4. Copia el link público para compartir

**Quién puede acceder a un artifact publicado:**

| Tipo de usuario | Qué puede hacer |
|---|---|
| No usuarios (sin cuenta) | Ver e interactuar con funciones básicas |
| Usuarios Free/Pro/Max | Acceso completo: ver, interactuar, customizar |
| Usuarios que usan AI features | Requiere cuenta Claude (se pide registro) |

### 7.2 Embeber en sitios web
✅ **Fuente:** Help Center oficial

Después de publicar, aparece el botón "Get embed code" que genera un iframe listo para usar.

- Debes especificar los dominios permitidos en el campo "Allowed domains"
- El artifact se renderiza completo dentro de tu sitio web
- Actualiza automáticamente si re-publicas

### 7.3 Sharing interno (Team y Enterprise)
✅ **Fuente:** Help Center oficial

- Solo para miembros de la organización
- Los viewers deben autenticarse con su cuenta Team/Enterprise
- Si compartes desde un Project, cualquier miembro de la org puede verlo (no solo los que tienen acceso al Project)
- Al compartir el artifact, también se comparten los archivos adjuntos de esa conversación

### 7.4 Despublicar — ⚠️ Acción irreversible
✅ **Fuente:** Help Center oficial — **IMPORTANTE**

- Una vez despublicado, **NO puedes volver a publicar el mismo artifact**
- Tendrás que crear uno nuevo
- La despublicación **elimina permanentemente** todos los datos de storage (personal y compartido)

---

## 8. Personalización y remix

✅ **Fuente:** Help Center oficial

### Proceso de Customize:
1. Al ver cualquier artifact publicado, busca el botón "Customize"
2. Claude abre una nueva conversación con el contenido del artifact
3. Puedes modificarlo, expandirlo o usarlo como inspiración
4. Tus cambios son completamente independientes del original

**Disponible en todos los planes:** Free, Pro, Max, Team, Enterprise

**Nota:** Si haces clic en Customize sin haber usado artifacts antes, la funcionalidad se activa automáticamente para tu cuenta.

---

## 9. Disponibilidad por plan

✅ **Fuente:** Help Center oficial + Release Notes

| Funcionalidad | Free | Pro | Max | Team | Enterprise |
|---|---|---|---|---|---|
| Crear artifacts | ✅ | ✅ | ✅ | ✅ | ✅ |
| Sidebar de artifacts | ✅ | ✅ | ✅ | ✅ | ✅ |
| Inspiration Tab | ✅ | ✅ | ✅ | ❌* | ❌* |
| Catálogo público | ✅ | ✅ | ✅ | ✅ | ✅ |
| Publicar artifact | ✅ | ✅ | ✅ | ❌** | ❌** |
| AI-powered artifacts | ✅ | ✅ | ✅ | ✅ | ✅ |
| MCP integration | ❌ | ✅ | ✅ | ✅ | ✅ |
| Persistent storage | ❌ | ✅ | ✅ | ✅ | ✅ |
| Sharing interno de org | ❌ | ❌ | ❌ | ✅ | ✅ |
| Embed en sitios web | ✅ | ✅ | ✅ | n/a | n/a |
| Apps móviles (iOS/Android) | ✅ | ✅ | ✅ | ✅ | ✅ |

*Team y Enterprise tienen artifacts compartidos internamente, no la galería pública de Inspiration
**Team y Enterprise solo pueden compartir internamente, no publicar públicamente

---

## 10. Restricciones técnicas conocidas

✅/🔍 **Fuentes:** Documentación oficial + comunidad verificada

### Restricciones universales:
- **Un archivo por artifact** — no pueden vincularse múltiples archivos entre sí
- **Sin imágenes externas** — usar `/api/placeholder/width/height` para placeholders
- **Scripts externos** — solo desde CDN permitidos: `cdnjs.cloudflare.com`, `esm.sh`, `cdn.jsdelivr.net`, `unpkg.com`
- **Sin generación de imágenes raster** — Claude no genera JPEGs ni PNGs de forma nativa
- **Sin acceso al sistema de archivos** — no puede leer/escribir en el filesystem del usuario

### Restricciones específicas de React:
- **Sin localStorage o sessionStorage** — usar `useState` o `useReducer` para estado temporal
- **Sin imports locales** — todo debe estar en un único archivo autocontenido
- **Sin código server-side** — solo frontend en entorno sandboxed de browser
- **Sin conexiones a bases de datos** — excepto vía MCP (requiere plan Pro+)
- **Sin llamadas a APIs externas arbitrarias** — excepto las explícitamente soportadas
- **Export default obligatorio** — el componente principal debe usar `export default`
- **Sin props requeridos** — todos los props deben tener valores por defecto

### Restricciones de storage persistente:
- Solo texto (no binarios, imágenes ni archivos)
- Límite de 20 MB por artifact
- Solo disponible en artifacts publicados (no en desarrollo/pruebas)
- Al despublicar → todos los datos se eliminan permanentemente

---

## 11. Librerías disponibles en artifacts React

✅/🔍 **Fuente:** Documentación técnica oficial + comunidad

### Librerías de UI e iconos:
```javascript
import { Camera, Settings } from "lucide-react"  // v0.383.0
import { Alert, AlertDescription } from '@/components/ui/alert'  // shadcn/ui
```

### Librerías de datos y visualización:
```javascript
import { LineChart, XAxis, YAxis } from "recharts"  // Charts
import * as d3 from "d3"  // D3.js — visualizaciones avanzadas
import * as Plotly from "plotly"  // Plotly charts
```

### Librerías de física y 3D:
```javascript
import * as THREE from "three"  // Three.js r128 — 3D
```

### Librerías de datos y procesamiento:
```javascript
import * as math from 'mathjs'  // Cálculos matemáticos
import _ from 'lodash'  // Utilidades JS
import * as Papa from 'papaparse'  // Procesamiento de CSV
import * as XLSX from 'xlsx'  // Procesamiento de Excel
import * as mammoth from 'mammoth'  // Procesamiento de Word
```

### Librerías de audio:
```javascript
import * as Tone from 'tone'  // Síntesis de audio
```

### Librerías de IA y ML:
```javascript
import * as tf from 'tensorflow'  // TensorFlow.js
```

### Librerías de gráficos adicionales:
```javascript
import * as Chart from 'chart.js'  // Chart.js
```

### Restricciones de librerías en React:
- No pueden usarse librerías fuera de esta lista o de CDNs permitidos
- Three.js solo en versión r128 — `CapsuleGeometry` no está disponible (introducida en r142)
- No usar `THREE.OrbitControls` — no está disponible en el CDN de Cloudflare

---

## 12. Casos de uso por perfil de usuario

### 👔 Directivos y C-Suite
| Caso de uso | Tipo de artifact | Impacto |
|---|---|---|
| Dashboard de KPIs en tiempo real | HTML / React | Alto |
| Reportes ejecutivos interactivos | HTML + Charts | Alto |
| Simuladores de escenarios de negocio | React con sliders | Alto |
| Presentaciones de datos | HTML / SVG | Medio |

### 📊 Analistas y equipos de datos
| Caso de uso | Tipo de artifact | Impacto |
|---|---|---|
| Analizador de CSV en lenguaje natural | HTML AI-powered | Muy alto |
| Dashboards con datos propios | React + Recharts/D3 | Alto |
| Visualizaciones de reportes | SVG + React | Alto |
| Herramientas de exploración de datos | React + Papa/XLSX | Alto |

### 💻 Desarrolladores
| Caso de uso | Tipo de artifact | Impacto |
|---|---|---|
| Prototipos de UI funcionales | React | Muy alto |
| Diagramas de arquitectura | Mermaid / SVG | Alto |
| Snippets y funciones | Código | Alto |
| ERDs y esquemas de BD | Mermaid (erDiagram) | Alto |
| Depuración visual de algoritmos | React interactivo | Medio |

### 🎓 Educadores y formadores
| Caso de uso | Tipo de artifact | Impacto |
|---|---|---|
| Tutores AI-powered por materia | React + API Claude | Muy alto |
| Quizzes interactivos | React | Alto |
| Simuladores de conceptos complejos | React interactivo | Muy alto |
| Material educativo interactivo | HTML / React | Alto |
| Cursos gamificados | React AI-powered | Alto |

### 🚀 Founders y emprendedores
| Caso de uso | Tipo de artifact | Impacto |
|---|---|---|
| MVP visual en minutos | HTML / React | Muy alto |
| Calculadoras de ROI/pricing | React con sliders | Alto |
| Landing pages para validación | HTML | Alto |
| Demos para inversores | React interactivo | Muy alto |

### 📢 Marketers y creadores de contenido
| Caso de uso | Tipo de artifact | Impacto |
|---|---|---|
| Infografías vectoriales | SVG | Medio |
| Calculadoras interactivas para leads | React AI-powered | Alto |
| Herramientas gratuitas para audiencia | HTML/React + storage | Alto |
| Visualizaciones de campañas | React + Charts | Medio |

---

## 13. Inventario maestro de tipos y funcionalidades

| # | Nombre | Tipo | Categoría | Renderizado | AI-powered posible | Plan mínimo | Verificación |
|---|---|---|---|---|---|---|---|
| 1 | Código (snippet) | Tipo base | Desarrollo | No | No | Free | ✅ |
| 2 | Markdown / Documento | Tipo base | Escritura | Sí (Markdown) | No | Free | ✅ |
| 3 | HTML + CSS + JS | Tipo base | Web / Apps | Sí (página web) | Sí | Free | ✅ |
| 4 | SVG | Tipo base | Visual | Sí (vector) | No | Free | ✅ |
| 5 | Mermaid Diagram | Tipo base | Diagramas | Sí (diagrama) | No | Free | ✅ |
| 6 | React Component | Tipo base | UI interactiva | Sí (app) | Sí | Free | ✅ |
| 7 | PDF | Tipo base | Documentos | Sí | No | Cowork | ✅ |
| 8 | AI-powered Artifact | Funcionalidad | Micro-app IA | Sí | Sí (nativamente) | Free | ✅ |
| 9 | MCP Artifact | Funcionalidad | Integración | Sí | Opcional | Pro | ✅ |
| 10 | Persistent Storage Artifact | Funcionalidad | Stateful app | Sí | Opcional | Pro | ✅ |
| 11 | Inspiration Tab | Galería curada | Descubrimiento | — | — | Free | ✅ |
| 12 | Catálogo público | Galería comunitaria | Descubrimiento | — | — | Free | ✅ |
| 13 | Artifact embebido | Distribución | Publicación | Sí (iframe) | Opcional | Free | ✅ |
| 14 | Artifact compartido (org) | Distribución | Colaboración | Sí | Opcional | Team | ✅ |

---

## 14. Rankings de adopción y utilidad

### Ranking 1 — Por frecuencia de caso de uso (🔍 Inferido)

| # | Tipo | Razón | Confianza |
|---|---|---|---|
| 1 | HTML interactivo | Caso de uso más amplio, sin barreras técnicas para el usuario final | Alta |
| 2 | Código (snippet) | Primer uso histórico, masivo entre devs y técnicos | Alta |
| 3 | Markdown/Documento | Uso diario universal: reportes, propuestas, artículos | Alta |
| 4 | React Component | Mayor complejidad pero mayor impacto visual | Media-alta |
| 5 | Mermaid/SVG | Alto valor para comunicación técnica | Media-alta |
| 6 | AI-powered artifact | Más reciente, crecimiento acelerado | Media |
| 7 | MCP artifact | Potencial enorme, requiere configuración previa | Media |

### Ranking 2 — Por valor de impacto para el usuario (🔍 Inferido)

| # | Tipo/Funcionalidad | Valor | Por qué |
|---|---|---|---|
| 1 | AI-powered artifact | ★★★★★ | Transforma a cualquier usuario en desarrollador de micro-apps con IA |
| 2 | Analizador CSV (HTML/React) | ★★★★★ | Democratiza el análisis de datos para no técnicos |
| 3 | Dashboard HTML | ★★★★☆ | Convierte datos en narrativa visual ejecutiva |
| 4 | Prototipo React | ★★★★☆ | MVP visual funcional en minutos sin código propio |
| 5 | MCP artifact | ★★★★☆ | Claude actúa en herramientas reales del trabajo |
| 6 | Persistent storage | ★★★★☆ | Convierte artifact en app real con memoria |
| 7 | Mermaid / ERD | ★★★☆☆ | Documenta sistemas técnicos al instante |

---

## 15. Historial de lanzamientos relevantes

✅ **Fuente:** Release Notes oficiales + anuncios de Anthropic

| Fecha | Hito | Impacto |
|---|---|---|
| **Jun 2024** | Lanzamiento de Artifacts como feature preview con Claude 3.5 Sonnet | Primer artifact: panel lateral básico |
| **Ago 2024** | Artifacts generalmente disponibles para Free, Pro y Team. Apps iOS/Android | Masificación del uso |
| **Sep-Oct 2024** | AI-powered artifacts: API de Claude embebida directamente | Artifacts se convierten en micro-apps |
| **Oct 2024** | Catálogo público de artifacts lanzado (`claude.ai/catalog/artifacts`) | Ecosistema de descubrimiento |
| **Oct 2025** | Diff editor inline — edición quirúrgica sin reescribir todo el código (3-4x más rápido) | Mejora masiva de UX en iteración |
| **Oct 2025** | MCP integration para artifacts (Pro+) — conexión a Gmail, Calendar, Slack, Asana | Artifacts conectados a servicios reales |
| **Oct 2025** | Persistent storage para artifacts (Pro+) — datos entre sesiones | Artifacts como apps reales |
| **Oct 2025** | Embed de artifacts en sitios web externos | Distribución fuera de Claude |
| **Dic 2025** | Skills para organizaciones con directorio de partners | Ecosistema de skills maduro |
| **Ene 2026** | Interactive apps en Claude para iOS y Android | Artifacts en móvil con experiencia completa |
| **Mar 2026** | Claude crea charts, diagramas y visualizaciones inline en chat (no solo en artifacts) | Visualización sin artifact obligatorio |
| **Abr 2026** | Estado actual: ecosistema maduro con AI-powered, MCP, storage y catálogo global | — |

---

## 16. Guía de uso para conferencias y formación

> Esta sección es especial para formadores, trainers y speakers que usan Claude como herramienta demo en vivo.

### Los 5 artifacts más impactantes para demostrar en tarima

#### Demo #1 — Analizador de CSV en vivo ⭐⭐⭐⭐⭐
**Prompt recomendado:**
```
Crea una herramienta interactiva en HTML que permita al usuario
subir un archivo CSV, lo analice automáticamente y genere:
- Resumen estadístico de cada columna
- 3 gráficas relevantes según el tipo de datos
- Un resumen en lenguaje natural de los hallazgos principales
- Opción para hacer preguntas sobre los datos en lenguaje natural

Diseño limpio, profesional, en español.
```
**Momento wow:** Cuando alguien del público sube su propio reporte de ventas
**Duración de demo:** 3–5 minutos
**Audiencia ideal:** Directivos, gerentes, equipos de ventas

#### Demo #2 — Micro-app con IA en 60 segundos ⭐⭐⭐⭐⭐
**Prompt recomendado:**
```
Crea una app React de simulador de ROI para implementar IA en una empresa.
Incluye:
- Slider para número de empleados (10-500)
- Slider para horas semanales dedicadas a tareas repetitivas (1-40)
- Slider para costo por hora promedio (USD $5-100)
- Slider para % de automatización posible con IA (10-80%)
- Cálculo del ROI anual, ahorro mensual y tiempo de recuperación de inversión
- Visualización con gráfica de barras de comparación antes/después
- Botón para generar reporte en texto

Diseño ejecutivo, colores profesionales, en español.
```
**Momento wow:** "Acabo de crear una app funcional sin escribir código"
**Duración de demo:** 4–6 minutos
**Audiencia ideal:** Empresarios, consultores, founders

#### Demo #3 — Dashboard ejecutivo en tiempo real ⭐⭐⭐⭐
**Prompt recomendado:**
```
Crea un dashboard ejecutivo HTML con los siguientes KPIs ficticios
de una empresa de manufactura:
- Ventas del mes: $2.4M (meta: $2.2M) → Verde
- Producción: 8,450 unidades (meta: 9,000) → Amarillo
- Clientes activos: 342 (mes anterior: 318) → Verde
- NPS: 72 (meta: 70) → Verde
- Costo operativo: $1.8M (presupuesto: $1.7M) → Rojo

Incluye gráfica de tendencia de los últimos 6 meses,
alertas visuales por color, y resumen narrativo automático.
Diseño tipo Fortune 500, en español.
```
**Momento wow:** Comparar con el tiempo que tarda hacer esto en PowerPoint
**Duración de demo:** 2–3 minutos
**Audiencia ideal:** CFOs, directores, boards

#### Demo #4 — Prototipo de app en minutos ⭐⭐⭐⭐
**Prompt recomendado:**
```
Crea el prototipo funcional de una app móvil (en HTML,
simulando vista mobile 375px) para gestión de turnos
de una clínica médica:
- Pantalla de login
- Dashboard del médico con próximas citas
- Vista para agendar nueva cita
- Panel de historial de paciente
- Navegación entre secciones

UI moderna, colores médicos (azul/blanco), totalmente interactiva.
```
**Momento wow:** "Esto antes costaba $5,000 y 3 semanas con un desarrollador"
**Duración de demo:** 3–4 minutos
**Audiencia ideal:** Fundadores, PMs, emprendedores digitales

#### Demo #5 — Tutor AI-powered personalizado ⭐⭐⭐⭐
**Prompt recomendado:**
```
Crea una app React de tutor de inteligencia artificial para
empresarios latinoamericanos. El tutor debe:
- Recibir preguntas del usuario en un chat
- Responder usando la API de Claude con conocimiento especializado en:
  * Automatización de procesos con IA
  * Prompts para marketing y ventas
  * ROI de implementar IA
- Dar ejemplos siempre con casos de LATAM
- Mantener historial de la conversación
- Tener personalidad amigable y directa

UI tipo chat moderno, en español, con nombre "Aria - Tu consultora IA"
```
**Momento wow:** El asistente responde con inteligencia real y personalización
**Duración de demo:** 5–7 minutos
**Audiencia ideal:** Audiencias de cursos, comunidades de aprendizaje

### Consejos de producción para demos en vivo

1. **Prepara el CSV con anticipación** — Usa datos de negocio ficticios pero realistas, o pide permiso a alguien para usar sus datos reales en escena
2. **Practica los prompts 3 veces** — La fluidez importa más que la perfección del resultado
3. **Muestra el proceso, no solo el output** — El público debe ver cómo escribes el prompt (ese es el aprendizaje)
4. **Siempre termina con el link publicado** — "Esto lo pueden usar hoy mismo con su cuenta de Claude"
5. **Prepara un fallback** — Si el artifact falla en vivo, ten una screenshot del resultado esperado
6. **Usa proyector en modo oscuro** — Los artifacts se ven mejor en dark mode con fondo oscuro
7. **El Demo #2 (ROI calculator) es el mejor cierre** — El público siente que ya aprendió algo antes de comprar
8. **Invita al público a participar** — "¿Alguien quiere subir sus propios datos?"

---

## 17. Prompts de referencia por tipo de artifact

### Prompts base para cada tipo:

**HTML Interactivo:**
```
Crea una [herramienta/calculadora/dashboard] en HTML con:
- [funcionalidad principal]
- [elementos interactivos: sliders, botones, inputs]
- [visualización: gráficas, tablas, colores]
Diseño profesional, en español, responsive.
```

**React Component:**
```
Crea un componente React interactivo que [objetivo].
Debe incluir:
- Estado con useState para [variables]
- [Librería de visualización] para los gráficos
- Diseño con Tailwind CSS
- Texto en español
```

**Diagrama Mermaid:**
```
Crea un diagrama de [flujo/secuencia/arquitectura/ERD]
que represente [proceso/sistema].
Incluye: [componentes principales]
Dirección: [TB (top-bottom) / LR (left-right)]
```

**AI-Powered App:**
```
Crea una aplicación React que incluya un chat con IA
donde el modelo actúe como [rol/especialidad].
El asistente debe:
- [comportamiento 1]
- [comportamiento 2]
- Responder siempre en español
- Mantener el contexto de la conversación
```

**Dashboard con datos reales (CSV):**
```
Crea una aplicación HTML que:
1. Permita subir un archivo CSV
2. Lo procese con PapaParse
3. Detecte automáticamente el tipo de datos en cada columna
4. Genere visualizaciones apropiadas usando Chart.js
5. Presente un resumen estadístico en lenguaje natural
```

---

## 18. Recursos y referencias oficiales

✅ Todos verificados como URLs oficiales de Anthropic/Claude

| Recurso | URL | Tipo |
|---|---|---|
| Help Center — Qué son los Artifacts | `https://support.claude.com/en/articles/9487310` | Documentación oficial |
| Help Center — Publicar y compartir | `https://support.claude.com/en/articles/9547008` | Documentación oficial |
| Catálogo público de Artifacts | `https://claude.ai/catalog/artifacts` | Catálogo oficial |
| Inspiration Tab | `https://claude.ai/artifacts` | Galería curada por Anthropic |
| Anuncio GA de Artifacts | `https://www.anthropic.com/news/artifacts` | Blog oficial Anthropic |
| Release Notes oficiales | `https://support.claude.com/en/articles/12138966-release-notes` | Documentación oficial |
| Configuración de Artifacts | `https://claude.ai/settings/capabilities` | Configuración en app |
| Made with Claude (comunidad) | `https://madewithclaude.com` | Comunidad (no oficial) |

---

## GLOSARIO

| Término | Definición |
|---|---|
| **Artifact** | Contenido sustancial generado por Claude que aparece en panel lateral dedicado |
| **AI-powered artifact** | Artifact con la API de Claude embebida — funciona como micro-app con IA |
| **MCP** | Model Context Protocol — protocolo para conectar artifacts a servicios externos |
| **Persistent storage** | Capacidad de guardar datos entre sesiones en un artifact publicado |
| **Remix / Customize** | Proceso de tomar un artifact existente como base para crear uno nuevo |
| **Publish** | Hacer un artifact públicamente accesible via link (Free/Pro/Max) |
| **Share** | Compartir un artifact dentro de una organización (Team/Enterprise) |
| **Embed** | Insertar un artifact publicado en otro sitio web via iframe |
| **Inspiration Tab** | Galería curada por Anthropic con artifacts de alta calidad |
| **Catálogo** | Directorio público de artifacts publicados por usuarios |
| **Diff editor** | Sistema de edición inline que modifica solo las partes necesarias del artifact |
| **Cowork** | Producto de Anthropic para agentes de escritorio — soporta artifacts con PDF |
| **Skills** | Instrucciones reutilizables para Claude (diferente a artifacts) |
| **Connector** | Integración con servicio externo via MCP (diferente a artifact) |
| **Project** | Espacio de trabajo con memoria persistente en Claude (puede contener artifacts) |

---

*Base de conocimiento elaborada con fuentes oficiales de Anthropic. Fecha de corte: Abril 2026.*
Para actualizaciones, revisar: `https://support.claude.com/en/articles/12138966-release-notes`
