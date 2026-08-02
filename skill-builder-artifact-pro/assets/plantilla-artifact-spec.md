# Plantilla de arranque — Artifact Spec

Copia el bloque de abajo, rellena cada marcador y entrégalo como **un solo
bloque de código markdown**. Fuera del bloque solo van las secciones
"QUÉ VAS A VER" y "CÓMO SEGUIR".

Un campo con marcador sin rellenar es peor que un campo ausente: quien construya
lo va a inventar, y va a inventar distinto cada vez. Si un campo no aplica,
escribe explícitamente "No aplica — [razón]" en vez de borrarlo.

---

```
CASO 2 — CONSTRUIR ARTIFACT
Modelo recomendado: [Sonnet / Opus] — [razón en una línea]
Instrucción: construye este artifact siguiendo el spec exacto. No modifiques
estructura, librerías ni datos. Si algo no es claro, pregunta antes de construir.
═══════════════════════════════════════════
ARTIFACT SPEC: [nombre descriptivo, no genérico]

1. CLASIFICACIÓN
   - Nivel: [BÁSICO / MEDIO / ALTO / EXPERTO]
   - Tipo: [React / HTML / SVG / Mermaid / Markdown]
   - AI-powered: [sí / no]   MCP: [sí / no]   Storage persistente: [sí / no]

2. OBJETIVO
   [Una oración: qué hace y para quién. Si necesitas dos, el artifact
   probablemente son dos artifacts.]

3. CONTEXTO DE USO
   - Dónde se usa: [taller / demo comercial / curso / herramienta interna / publicado]
   - Audiencia: [quién lo ve y qué sabe del tema]
   - Dispositivo: [desktop / móvil / proyector — con resolución si importa]

4. TIPO Y JUSTIFICACIÓN
   - Tipo elegido: [...]
   - Por qué: [razón técnica concreta, no "es más moderno"]
   - Alternativa descartada: [...] porque [...]

5. LIBRERÍAS
   [Imports exactos, solo del set seguro. Si no lleva ninguna, dilo.]
   import { useState, useMemo } from "react";
   import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
   import { TrendingUp, DollarSign, Users } from "lucide-react";

6. ESTRUCTURA DE COMPONENTES
   [Diagrama ASCII del layout real, no una lista de nombres.]
   ┌─────────────────────────────────────────┐
   │ HEADER: [título] + [subtítulo]          │
   ├──────────────────┬──────────────────────┤
   │ [panel izquierdo]│ [panel derecho]      │
   │ - [input 1]      │ - [resultado 1]      │
   │ - [input 2]      │ - [gráfico]          │
   ├──────────────────┴──────────────────────┤
   │ FOOTER: [CTA o resumen]                 │
   └─────────────────────────────────────────┘

7. DATOS DE EJEMPLO
   [JavaScript listo para pegar. Realista y del sector del usuario — nunca
   "Empresa A / Producto B". Suficiente para que el artifact se vea lleno:
   si un gráfico necesita 12 meses, pon los 12.]
   const datos = [
     { ... },
   ];

8. INTERACTIVIDAD
   - Inputs: [sliders / dropdowns / campos de texto / botones / carga de CSV]
   - Qué pasa al usarlos: [cálculo o cambio visual concreto]
   - Estados: carga [...] · error [...] · vacío [...]
   [Si no hay interactividad, escribe "Ninguna — datos estáticos" y explica
   por qué, para que nadie la agregue por su cuenta.]

9. DISEÑO VISUAL
   - Paleta: [#hex principal] / [#hex acento] / [#hex fondo]
   - Estilo: [minimalista / corporativo / editorial / colorido]
   - Tipografía: [Tailwind por defecto o especificación]
   - Responsive: [sí / no]   Modo oscuro: [sí / no]

10. RESTRICCIONES TÉCNICAS
    [Solo las que apliquen a ESTE artifact, copiadas textualmente del SKILL.md.
    Meterlas todas es ruido; omitir las que aplican es la causa #1 de artifacts
    que no renderizan.]
    - [...]
    - [...]

11. CRITERIOS DE ÉXITO
    [Checklist binario: cada línea se responde sí o no mirando la pantalla.
    "Se ve profesional" no sirve; "los 6 KPI muestran flecha de tendencia" sí.]
    - [ ] Se renderiza sin errores
    - [ ] [...]
    - [ ] [...]

12. NOTAS ADICIONALES
    [Cualquier detalle que evite una pregunta al construir: formato de números,
    idioma de las etiquetas, qué hacer si un dato viene en cero, textos exactos
    de botones.]
```

---

## Después del bloque

**QUÉ VAS A VER** — 3 a 5 líneas describiendo la pantalla final en lenguaje
cotidiano, sin una sola palabra técnica. Es lo que la persona aprueba o corrige,
y solo puede hacerlo si entiende cada palabra.

**CÓMO SEGUIR** — pasos literales: abre un chat nuevo, selecciona el modelo
indicado arriba, pega el bloque completo, espera.
