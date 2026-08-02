# 02 — ARTIFACT SPEC TEMPLATE
## Template obligatorio de 12 campos para diseñar artifacts

Usa este template para CADA artifact que diseñes. Los 12 campos son obligatorios.
Produce el spec en un bloque de código markdown para fácil copy-paste.

---

## TEMPLATE

```markdown
# ARTIFACT SPEC: [Nombre descriptivo]

## 1. CLASIFICACIÓN
- **Nivel de complejidad:** BÁSICO | MEDIO | ALTO | EXPERTO
- **Tipo de artifact:** HTML | React | SVG | Mermaid | Markdown | Código
- **AI-powered:** Sí / No (¿usa API de Claude embebida?)
- **MCP integration:** Sí / No (¿se conecta a servicios externos?)
- **Persistent storage:** Sí / No (¿guarda datos entre sesiones?)
- **Modelo para construir:** Haiku | Sonnet | Opus

## 2. OBJETIVO
[Una oración: qué hace el artifact y para quién]

## 3. CONTEXTO DE USO
- **Dónde se usa:** Taller / Demo / Curso / Herramienta interna / Publicado
- **Audiencia:** [Quién lo va a ver/usar]
- **Dispositivo principal:** Desktop / Mobile / Ambos

## 4. TIPO Y JUSTIFICACIÓN
- **Tipo elegido:** [HTML | React | etc.]
- **Por qué este tipo:** [Razón técnica concreta]
- **Alternativa descartada:** [Y por qué se descartó]

## 5. LIBRERÍAS A USAR
[Solo de la lista permitida. Incluir import exacto]
```javascript
// Ejemplo:
import { useState, useEffect } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { TrendingUp, DollarSign, Clock, Users } from "lucide-react";
```

## 6. ESTRUCTURA DE COMPONENTES
[Descripción jerárquica de la UI]
```
┌─────────────────────────────────────┐
│ HEADER: Título + logo/icono        │
├─────────────────────────────────────┤
│ PANEL IZQUIERDO   │ PANEL DERECHO   │
│ - Input 1         │ - Resultado 1   │
│ - Input 2         │ - Resultado 2   │
│ - Input 3         │ - Gráfico       │
├─────────────────────────────────────┤
│ FOOTER: CTA o resumen              │
└─────────────────────────────────────┘
```

## 7. DATOS DE EJEMPLO
[Datos reales o realistas listos para usar en el artifact]
```javascript
const data = [
  { category: "Ejemplo 1", before: 100, after: 60 },
  { category: "Ejemplo 2", before: 200, after: 80 },
];
```

## 8. INTERACTIVIDAD
- **Inputs del usuario:** [Sliders, dropdowns, text inputs, botones, etc.]
- **Acciones:** [Qué pasa cuando el usuario interactúa]
- **Estados:** [Estados visuales: loading, error, success, empty]

## 9. DISEÑO VISUAL
- **Paleta de colores:** [Hex codes o descripción]
- **Estilo:** [Minimalista, corporativo, moderno, colorido]
- **Tipografía:** [Tailwind defaults o especificaciones]
- **Responsive:** Sí / No
- **Modo oscuro:** Sí / No

## 10. RESTRICCIONES TÉCNICAS
[Restricciones específicas que Sonnet debe conocer]
- Sin localStorage (usar useState)
- Sin imágenes externas (usar /api/placeholder/w/h)
- Un solo archivo autocontenido
- Export default obligatorio (React)
- [Otras restricciones específicas del artifact]

## 11. CRITERIOS DE ÉXITO
[Checklist binario: cómo saber si el artifact quedó bien]
- [ ] Se renderiza sin errores en el panel de Claude
- [ ] Los inputs funcionan y actualizan la UI en tiempo real
- [ ] Los datos se muestran correctamente en gráficos/tablas
- [ ] Es visualmente profesional (no genérico)
- [ ] [Criterio específico del artifact]

## 12. PROMPT PARA SONNET
[Prompt listo para pegar en un hilo nuevo con Sonnet 4.6]
```
Construye este artifact React/HTML siguiendo este spec exacto.
No modifiques la estructura, librerías ni datos.
Si algo no es claro, pregúntame antes de construir.

[Pegar secciones 1-11 del spec aquí]
```
```

---

## GUÍA DE NIVELES DE COMPLEJIDAD

### BÁSICO (Haiku diseña → Sonnet construye)
- Un solo componente, sin estado complejo
- Datos estáticos hardcoded
- Visualización simple (tabla, lista, texto formateado)
- Ejemplos: infografía SVG, documento markdown, diagrama Mermaid, tabla HTML
- Tiempo estimado: 5-10 min diseño + 2-5 min construcción

### MEDIO (Haiku diseña → Sonnet construye)
- 2-4 componentes con estado (useState)
- Interactividad con sliders, dropdowns o formularios
- 1-2 gráficos con Recharts o Chart.js
- Datos calculados dinámicamente
- Ejemplos: calculadora ROI, dashboard KPI, quiz interactivo
- Tiempo estimado: 10-15 min diseño + 5-10 min construcción

### ALTO (Sonnet diseña → Sonnet construye)
- 5+ componentes con estado compartido
- Múltiples vistas o tabs
- Animaciones y transiciones
- Lógica de negocio compleja
- D3.js o Three.js para visualizaciones avanzadas
- Ejemplos: simulador multi-variable, dashboard con filtros, juego
- Tiempo estimado: 15-25 min diseño + 10-20 min construcción

### EXPERTO (Opus diseña → Sonnet/Opus construye)
- AI-powered (llamadas a API de Claude embebidas)
- MCP integration (conexión a servicios externos)
- Persistent storage (datos entre sesiones)
- Múltiples flujos de usuario
- Manejo de errores robusto
- Ejemplos: tutor IA personalizado, app de productividad con memoria, analizador de documentos con IA
- Tiempo estimado: 20-30 min diseño + 15-30 min construcción

---

## CHECKLIST PRE-ENTREGA DEL SPEC

Antes de entregar un spec al usuario, verifica:

- [ ] Los 12 campos están completos (ninguno vacío o con placeholder)
- [ ] El tipo de artifact es el óptimo para el caso de uso
- [ ] Las librerías son SOLO de la lista permitida
- [ ] Los datos de ejemplo son realistas y suficientes
- [ ] La estructura de componentes es clara y dibujada en ASCII
- [ ] Las restricciones técnicas relevantes están listadas
- [ ] El prompt para Sonnet es autocontenido (no requiere contexto adicional)
- [ ] El nivel de complejidad está correctamente clasificado
