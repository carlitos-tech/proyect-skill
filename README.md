# Proyect Skill - Entradas y Salidas de los Skills

Documentación de los inputs y outputs de los skills disponibles en este repositorio después de importarlos en Claude.

---

## Índice

1. [skill-builder-artifact-pro](#skill-builder-artifact-pro)
2. [skill-builder-pro](#skill-builder-pro)

---

## skill-builder-artifact-pro

**Descripción:** Diseña, clasifica y construye artifacts de Claude (React, HTML, SVG, Mermaid, Markdown) con base de conocimiento propia sobre tipos, librerías permitidas, restricciones de producción, patrones probados y 50 casos por industria.

### Entradas (Inputs)

El skill se activa cuando mencionas:

- **Diseño de artifacts**: "no sé qué construir", "dame ideas", "tengo una presentación"
- **Specs de artifacts**: Describes una idea concreta para un artifact visual
- **Código de artifact**: Pegas un bloque de spec o código existente
- **Problemas con artifacts**: "no carga", "pantalla en blanco", "quedó feo", "mejora este artifact"
- **Palabras clave**: artifact, dashboard interactivo, calculadora, simulador, quiz, comparador, demo visual, herramienta interactiva, "algo visual para mostrar"

**Tipos de entrada esperados:**
- Descripción textual de lo que necesitas visualizar
- Especificación JSON/YAML del artifact (spec)
- Código React/HTML/SVG/Mermaid existente con problemas
- Imágenes o referencias a diseños deseados
- Datos de ejemplo que incluir en el artifact

### Salidas (Outputs)

Según el tipo de entrada, produce:

1. **CASO 0 - Orientación**
   - 4 ideas en tabla: `Nombre | Qué hace | Nivel | Impacto visual`
   - Ideas sacadas de casos de uso reales por industria

2. **CASO 1 - Diseño (Spec)**
   - Bloque único markdown con 12 campos:
     1. Clasificación (nivel BÁSICO/MEDIO/ALTO/EXPERTO, tipo, AI-powered, MCP, storage)
     2. Objetivo
     3. Contexto de uso
     4. Tipo y justificación
     5. Librerías (imports exactos)
     6. Estructura de componentes (ASCII diagram)
     7. Datos de ejemplo (JavaScript listo para usar)
     8. Interactividad (inputs, estados, eventos)
     9. Diseño visual (paleta, tipografía, responsive)
     10. Restricciones técnicas
     11. Criterios de éxito
     12. Notas adicionales
   - Sección "QUÉ VAS A VER" (descripción visual sin jerga técnica)
   - Sección "CÓMO SEGUIR" (pasos literales para construir)

3. **CASO 2 - Construcción**
   - Artifact funcional completo en React/HTML/SVG/Mermaid
   - Código compilado y validado
   - Instrucciones de 30 segundos para probar

4. **CASO 3 - Arreglo/Mejora**
   - Diagnóstico de errores (etiquetados CRÍTICO/MEJORA/SUGERENCIA)
   - Código corregido
   - Explicación de la causa raíz
   - Recomendaciones para evitar en el futuro

### Formatos de salida

- **Markdown** para specs y documentación
- **React (JSX)** para artifacts interactivos
- **HTML5** para artifacts sin dependencias
- **SVG** para gráficos y diagramas
- **Mermaid** para diagramas automáticos
- **Tablas de comparación** de alternativas

### Restricciones técnicas que maneja

- Set seguro: React + Recharts + lucide-react
- Prohibido: xlsx, papaparse, localStorage, sessionStorage (excepto en published artifacts con plan Pro)
- Máximo 4 ResponsiveContainer de Recharts
- Sin imágenes externas (solo `/api/placeholder/` o cloudflare CDN)
- lucide-react v0.383.0 (íconos clásicos solamente)
- Sin breakpoints de Tailwind para elementos críticos
- Componentes auxiliares FUERA del componente principal

---

## skill-builder-pro

**Descripción:** Fábrica de skills. Convierte una idea vaga en un Spec de 12 secciones, el Spec en un SKILL.md válido, y ese archivo en un paquete instalable listo para usar en chat, Cowork o CLI.

### Entradas (Inputs)

El skill se activa cuando mencionas:

- **Crear skills**: "quiero crear un skill", "hazme un skill para", "necesito automatizar esta tarea repetitiva"
- **Convertir tareas en skills**: "convierte esto en un skill", "construye este spec", "diseña el flujo de un skill"
- **Diagnosticar skills**: "mi skill no se activa", "revisa este SKILL.md", "mejora la descripción"
- **Tareas repetitivas**: Describes algo que repites cada semana y quieres dejar automatizado
- **Empaquetado**: "cómo empaqueto mi skill", "ayuda con la instalación"

**Tipos de entrada esperados:**
- Descripción de una tarea que repites regularmente
- Idea vaga de lo que quieres automatizar
- Spec ya escrito para revisar o mejorar
- Archivo SKILL.md con problemas
- Requisitos técnicos y conectores disponibles

### Salidas (Outputs)

Según el tipo de entrada, produce a través de 5 modos:

1. **MODO 0 - Orientación**
   - Explicación simple de qué es un skill (con analogía)
   - Las 3 fases: diseño → construcción → instalación
   - 3 ejemplos de primer skill (simples, sin conectores complejos)
   - Pregunta de arranque para empezar

2. **MODO 1 - Diseño del Spec**
   - Spec de 12 secciones completo:
     1. Identidad (nombre, versión, propósito)
     2. Disparadores (frases-clave, cuándo se activa)
     3. Entradas (qué datos recibe)
     4. Flujo (fases con pasos numerados)
     5. Salidas (qué produce)
     6. Conectores (servicios externos necesarios)
     7. Reglas de oro (lo que no se puede romper)
     8. Casos borde (situaciones especiales)
     9. Archivos de referencia (documentación adicional)
     10. Ejemplos (entrada → salida, mínimo 3 incluyendo caso borde)
     11. Métricas de éxito (checklist verificable)
     12. Notas para quien construye
   - Bloque listo para copiar en un hilo nuevo
   - Supuestos marcados con `[SUPUESTO]` si aplica

3. **MODO 2 - Construcción**
   - Archivo `SKILL.md` completo y válido con:
     - Frontmatter YAML (name, description, version)
     - Cuerpo en imperativo con reglas críticas primero
     - Fases numeradas con fallbacks
     - Mínimo 3 ejemplos documentados
     - Archivos auxiliares (references/, scripts/, assets/)
   - Validación contra 7 reglas hard
   - Archivo listo para empaquetar

4. **MODO 3 - Diagnóstico**
   - Análisis de 15 puntos de checklist
   - Hallazgos clasificados: CRÍTICO / MEJORA / SUGERENCIA
   - Explicación de consecuencias reales (no solo reglas abstractas)
   - Tabla "actual vs propuesta"
   - Spec mejorado de 12 secciones
   - Listo para llevar a Modo 2

5. **MODO 4 - Empaque e Instalación**
   - Comandos de validación y empaque:
     ```bash
     python scripts/validar_skill.py <ruta>
     python scripts/empaquetar_skill.py <ruta>
     ```
   - Archivo `.skill` (zip) instalable
   - Pasos numerados de instalación según superficie:
     - Claude.ai (chat)
     - Cowork
     - CLI de código
   - Instrucciones de verificación y prueba

### Formatos de salida

- **Spec Markdown** (12 secciones estructuradas)
- **SKILL.md** (archivo ejecutable con frontmatter YAML)
- **Archivos auxiliares**:
  - `references/*.md` - Datos y documentación
  - `scripts/*.py` - Trabajo determinista y automatizado
  - `assets/*.md` - Plantillas y formatos
- **Paquete .skill** (ZIP instalable)
- **Tabla de validación** (puntos checklist vs cumplimiento)
- **Tabla comparativa** (actual vs propuesta para diagnósticos)

### Patrones que reconoce y maneja

- **Flujo secuencial**: Pasos en orden estricto, cada uno depende del anterior
- **Coordinación multi-conector**: Toca 2+ servicios externos
- **Refinamiento iterativo**: Resultado mejora con vueltas (borradores, reportes)
- **Selección según contexto**: La herramienta a usar depende de lo que entre
- **Dominio embebido**: Reglas de negocio o cumplimiento en la lógica

### Reglas que valida

1. `name` en kebab-case (minúsculas, guiones, sin espacios)
2. `name` no contiene palabras del asistente ni su empresa
3. Frontmatter sin `<` ni `>`
4. `description` ≤ 1024 caracteres, con QUÉ + CUÁNDO
5. Cuerpo ≤ 500 líneas (lo largo va a `references/`)
6. Archivo se llama `SKILL.md` exactamente
7. Estructura correcta (SKILL.md obligatorio, subdirectorios opcionales)

### Fallbacks y seguridad

- Fallback por cada conector
- Pausa de aprobación humana antes de flujos que escriben/envían/borran
- Casos borde documentados
- Ejemplos con entrada y salida reales
- Cero supuestos pendientes en versión final

---

## Estructura del repositorio

```
proyect-skill/
├── skill-builder-artifact-pro/   # Skill para diseñar y construir artifacts
│   ├── SKILL.md
│   ├── assets/                   # Plantillas de specs
│   ├── references/               # Base de conocimiento
│   └── scripts/                  # Validadores
├── skill-builder-pro/            # Skill para crear y validar skills
│   ├── SKILL.md
│   ├── assets/                   # Plantillas
│   ├── references/               # Documentación y patrones
│   └── scripts/                  # Scripts de validación
├── README.md                      # Este archivo
├── .gitignore                     # Configuración de Git
```

## Cómo usar este repositorio

1. **Para crear un artifact**: Importa `skill-builder-artifact-pro` en tu instancia de Claude
2. **Para crear un skill**: Importa `skill-builder-pro` en tu instancia de Claude
3. Sigue los modos/casos del skill activado
4. Los skills guiarán el flujo completo de diseño → construcción → instalación

## Instalación rápida

```bash
# Clonar el repositorio
git clone https://github.com/carlitos-tech/proyect-skill.git

# Navegar al directorio
cd proyect-skill

# Los skills están listos para importar en Claude
```

## Referencia rápida

| Skill | Entrada típica | Salida típica | Tiempo |
|-------|---|---|---|
| skill-builder-artifact-pro | "Quiero un dashboard" | Spec de 12 campos o artifact funcional | 10-15 min |
| skill-builder-pro | "Automatizar esta tarea" | SKILL.md validado + paquete .skill | 20-30 min |

## Soporte

- Para problemas con artifacts: Consulta `skill-builder-artifact-pro/references/`
- Para problemas con skills: Consulta `skill-builder-pro/references/diagnostico.md`
- Para validar: Usa los scripts en `scripts/validar_*.py`
