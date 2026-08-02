# 05 — EJEMPLO REAL: Spec completo de un artifact
## Dashboard KPI Bancario para taller de Bancolombia

Este es un ejemplo completo del Artifact Spec Template (12 campos) aplicado
a un caso real. Sirve como referencia para que el Artifact Architect produzca
specs con este nivel de detalle.

---

# ARTIFACT SPEC: Dashboard KPI Bancario

## 1. CLASIFICACIÓN
- **Nivel de complejidad:** ALTO
- **Tipo de artifact:** HTML (con Chart.js via CDN y Tailwind via CDN)
- **AI-powered:** No
- **MCP integration:** No
- **Persistent storage:** No
- **Modelo para construir:** Sonnet 4.6

## 2. OBJETIVO
Dashboard interactivo que muestra 6 KPIs bancarios clave con gráficos
profesionales, diseñado para proyectarse en un taller ejecutivo de
Bancolombia sobre adopción de IA en banca.

## 3. CONTEXTO DE USO
- **Dónde se usa:** Proyectado en pantalla durante un taller presencial
- **Audiencia:** 15-25 ejecutivos de Bancolombia (VPs, directores, gerentes)
- **Dispositivo principal:** Desktop (proyector 1920x1080)

## 4. TIPO Y JUSTIFICACIÓN
- **Tipo elegido:** HTML (no React)
- **Por qué HTML:** Acceso a Chart.js via CDN (mejor para gráficos financieros
  que Recharts), control total de CSS para paleta corporativa, más ligero para
  proyección. Un solo archivo HTML que se abre en cualquier navegador.
- **Alternativa descartada:** React — innecesario para datos estáticos sin
  interactividad compleja. Recharts no soporta gauges nativos.

## 5. LIBRERÍAS A USAR
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.js"></script>
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
```

## 6. ESTRUCTURA DE COMPONENTES
```
┌─────────────────────────────────────────────────────────┐
│ HEADER: "Dashboard de KPIs Bancarios" + logo placeholder│
│ Subtítulo: "Taller IA Aplicada — Abril 2026"           │
├─────────────────────────────────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ │
│ │Cartera│ │Mora  │ │ROE   │ │Efi-  │ │Satis-│ │Trans-│ │
│ │Total │ │>90d  │ │      │ │cien- │ │fac-  │ │accio-│ │
│ │$45.2T│ │4.2%  │ │15.8% │ │cia   │ │ción  │ │nes   │ │
│ │  ↑3% │ │ ↓0.5%│ │ ↑1.2%│ │52.3% │ │ 8.4  │ │Digital│
│ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ │
├──────────────────────┬──────────────────────────────────┤
│ GRÁFICO 1:           │ GRÁFICO 2:                      │
│ Evolución Cartera    │ Composición por Segmento         │
│ (Line chart 12 meses)│ (Doughnut chart)                 │
├──────────────────────┼──────────────────────────────────┤
│ GRÁFICO 3:           │ GRÁFICO 4:                      │
│ Mora por Segmento    │ Canales Digitales vs Presencial  │
│ (Bar chart horizontal)│ (Stacked bar mensual)           │
└──────────────────────┴──────────────────────────────────┘
```

## 7. DATOS DE EJEMPLO
```javascript
// KPIs principales
const kpis = [
  { label: "Cartera Total", value: "$45.2T", change: "+3.1%", trend: "up", icon: "fa-wallet" },
  { label: "Mora >90 días", value: "4.2%", change: "-0.5pp", trend: "down", icon: "fa-exclamation-triangle" },
  { label: "ROE", value: "15.8%", change: "+1.2pp", trend: "up", icon: "fa-chart-line" },
  { label: "Eficiencia", value: "52.3%", change: "-2.1pp", trend: "down", icon: "fa-cogs" },
  { label: "Satisfacción", value: "8.4/10", change: "+0.3", trend: "up", icon: "fa-smile" },
  { label: "Digital", value: "67%", change: "+8pp", trend: "up", icon: "fa-mobile-alt" }
];

// Evolución cartera (12 meses)
const carteraData = {
  labels: ["May","Jun","Jul","Ago","Sep","Oct","Nov","Dic","Ene","Feb","Mar","Abr"],
  values: [41.2, 41.8, 42.1, 42.5, 43.0, 43.4, 43.9, 44.2, 44.5, 44.8, 45.0, 45.2]
};

// Composición por segmento
const segmentos = {
  labels: ["Corporativo","Pyme","Personas","Microcrédito"],
  values: [35, 25, 30, 10],
  colors: ["#1e40af","#3b82f6","#60a5fa","#93c5fd"]
};

// Mora por segmento
const moraData = {
  labels: ["Corporativo","Pyme","Personas","Microcrédito"],
  values: [1.8, 6.5, 3.9, 8.2]
};

// Canales digitales vs presencial
const canalesData = {
  labels: ["Ene","Feb","Mar","Abr"],
  digital: [58, 61, 64, 67],
  presencial: [42, 39, 36, 33]
};
```

## 8. INTERACTIVIDAD
- **Inputs del usuario:** Ninguno (datos estáticos para demo)
- **Acciones:** Hover en gráficos muestra tooltips con valores
- **Estados:** Solo estado renderizado (no hay loading/error)
- **Animaciones:** Gráficos animan al cargar (Chart.js default)

## 9. DISEÑO VISUAL
- **Paleta:** Azul Bancolombia (#1e40af, #3b82f6, #60a5fa) + blanco + gris claro
- **Estilo:** Corporativo limpio, bordes sutiles, sombras suaves
- **Tipografía:** System fonts (Tailwind default)
- **Responsive:** No (optimizado para proyección 1920x1080)
- **Modo oscuro:** No
- **Fondo:** Blanco (#ffffff) con cards en blanco con sombra sutil

## 10. RESTRICCIONES TÉCNICAS
- Sin localStorage (no necesario para datos estáticos)
- Sin imágenes externas (logo = placeholder o texto)
- Un solo archivo HTML autocontenido
- Chart.js via CDN (no npm import)
- Tailwind via CDN (no build step)
- Font Awesome para iconos (via CDN)

## 11. CRITERIOS DE ÉXITO
- [ ] Se renderiza sin errores en Chrome
- [ ] Los 6 KPI cards muestran valores con indicadores de tendencia
- [ ] Los 4 gráficos se renderizan correctamente con Chart.js
- [ ] Los tooltips funcionan al hacer hover
- [ ] La paleta de colores es consistente (azules Bancolombia)
- [ ] Se ve profesional proyectado en pantalla grande
- [ ] Los datos son realistas para el sector bancario colombiano

## 12. PROMPT PARA SONNET
```
Construye un artifact HTML con este spec exacto. Es un dashboard de KPIs
bancarios para proyectar en un taller ejecutivo de Bancolombia.

Usa Chart.js 4.4.0 via CDN de Cloudflare y Tailwind CSS via CDN.
Usa Font Awesome 6.5.0 para iconos.

Incluye:
- Header con título "Dashboard de KPIs Bancarios — Taller IA Aplicada"
- 6 cards de KPI en una fila (grid responsive)
- 4 gráficos en grid 2x2:
  1. Line chart: Evolución Cartera 12 meses
  2. Doughnut chart: Composición por Segmento
  3. Bar chart horizontal: Mora por Segmento
  4. Stacked bar: Digital vs Presencial

Paleta: azules #1e40af, #3b82f6, #60a5fa sobre fondo blanco.
Estilo corporativo limpio. Datos hardcoded (ver datos de ejemplo).
No uses localStorage. No uses imágenes externas.



