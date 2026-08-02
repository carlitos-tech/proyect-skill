# 01 — REFERENCIA TÉCNICA DE ARTIFACTS
## Tipos, librerías permitidas, restricciones y capacidades


> **AVISO — jerarquía de reglas.** Este documento describe lo que el runtime de artifacts
> admite en teoría. Las "Restricciones técnicas duras" del SKILL.md describen lo que revienta
> en producción y **tienen prioridad** donde haya contradicción. En concreto: aquí aparecen
> `xlsx`, `papaparse`, `d3`, `three`, `plotly`, `tone`, `tensorflow` y varios CDNs; el set
> seguro real es **React + Recharts + lucide-react** sobre `cdnjs.cloudflare.com`, y `xlsx`
> y `papaparse` están prohibidos. Usa lo de más abajo solo cuando el SKILL.md no lo contradiga.

---

## TIPOS DE ARTIFACT RENDERIZABLES

| Tipo | Extensión | Renderiza en vivo | Interactivo | Mejor para |
|------|-----------|-------------------|-------------|------------|
| HTML | .html | Sí | Sí | Dashboards, landing pages, formularios |
| React | .jsx | Sí | Sí | Apps complejas, simuladores, juegos |
| SVG | .svg | Sí | Limitado | Diagramas, iconos, infografías |
| Mermaid | .mermaid | Sí | No | Diagramas de flujo, ERDs, timelines |
| Markdown | .md | Sí | No | Reportes, guías, documentación |
| PDF | .pdf | Sí | No | Documentos formales (Cowork) |
| Código | cualquiera | No (syntax highlight) | No | Scripts, funciones |

---

## CUÁNDO USAR HTML vs REACT

### Usa HTML cuando:
- No necesitas estado reactivo complejo
- Quieres acceso a CDNs externos (Chart.js, D3 via script tags)
- El artifact es principalmente visual (dashboards estáticos, landing pages)
- Necesitas control total de CSS sin Tailwind

### Usa React cuando:
- Necesitas estado reactivo (useState, useEffect, useReducer)
- Hay múltiples componentes que interactúan entre sí
- Quieres usar Recharts, shadcn/ui, lucide-react
- Necesitas Tailwind CSS
- El artifact es una "mini-app" con lógica de negocio
- Vas a hacer un artifact AI-powered (API de Claude embebida)

### Regla general:
- Dashboard simple con datos fijos → HTML + Chart.js
- Calculadora con sliders interactivos → React + Recharts
- Diagrama de proceso → Mermaid o SVG
- Documento formateado → Markdown
- App con IA embebida → React + fetch API Claude

---

## LIBRERÍAS PERMITIDAS EN REACT

### UI e iconos
```javascript
import { Camera, Settings, TrendingUp } from "lucide-react"  // v0.383.0
import { Alert, AlertDescription } from '@/components/ui/alert'  // shadcn/ui
```

### Visualización de datos
```javascript
import { LineChart, BarChart, PieChart, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts"
import * as d3 from "d3"
import * as Plotly from "plotly"
import * as Chart from "chart.js"
```

### 3D
```javascript
import * as THREE from "three"  // r128 ONLY
// NO usar CapsuleGeometry (r142+)
// NO usar THREE.OrbitControls (no en CDN)
```

### Datos y procesamiento
```javascript
import * as math from 'mathjs'
import _ from 'lodash'
import * as Papa from 'papaparse'   // CSV
import * as XLSX from 'xlsx'        // Excel (SheetJS)
import * as mammoth from 'mammoth'  // Word docs
```

### Audio y ML
```javascript
import * as Tone from 'tone'
import * as tf from 'tensorflow'
```

---

## CDNs PERMITIDOS

- https://cdnjs.cloudflare.com
- https://esm.sh
- https://cdn.jsdelivr.net
- https://unpkg.com

---

## RESTRICCIONES TÉCNICAS

### Prohibido en TODOS los artifacts:
- localStorage / sessionStorage / indexedDB
- Imágenes externas (usar /api/placeholder/width/height)
- Múltiples archivos (todo en uno solo)
- Imports locales
- Código server-side
- Conexiones directas a bases de datos (excepto MCP)
- APIs externas arbitrarias (excepto las soportadas)

### Obligatorio en React:
- export default en el componente principal
- Todos los props con valores por defecto
- Solo Tailwind core utility classes
- Importar hooks explícitamente

### Placeholders de imágenes:
```
/api/placeholder/400/300
```

---

## FUNCIONALIDADES AVANZADAS

### AI-Powered (API de Claude embebida)
```javascript
const response = await fetch("https://api.anthropic.com/v1/messages", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    model: "claude-sonnet-4-20250514",
    max_tokens: 1000,
    messages: [{ role: "user", content: prompt }],
  })
});
const data = await response.json();
const text = data.content[0].text;
```
- No requiere API key (la maneja Claude)
- Uso cuenta contra límites del USUARIO, no del creador
- Escala gratis para el creador

### MCP Integration
- Conecta a Google Calendar, Gmail, Slack, etc.
- Requiere plan Pro+
- Usuario aprueba acceso la primera vez

### Persistent Storage
```javascript
await window.storage.set('key', JSON.stringify(data));
const result = await window.storage.get('key');
const parsed = result ? JSON.parse(result.value) : null;
await window.storage.list('prefix:');
await window.storage.delete('key');
```
- Max 20 MB por artifact
- Solo texto/JSON
- SOLO funciona en artifacts PUBLICADOS
- Dos modos: personal (default) y shared
- Despublicar = datos eliminados PERMANENTEMENTE

---

## PUBLICACIÓN

| Acción | Plan mínimo |
|--------|-------------|
| Crear artifacts | Free |
| Publicar con link | Free |
| AI-powered | Free |
| MCP integration | Pro |
| Persistent storage | Pro |
| Compartir en org | Team |
| Embeber en sitio externo | Free |
