# 03 — PATRONES DE DISEÑO Y ANTI-PATRONES
## Guía de buenas prácticas para artifacts de alta calidad

---

## PATRONES QUE FUNCIONAN

### 1. Patrón "Estado Central" (React)
Un solo useState con objeto que contiene todas las variables.
Ideal para calculadoras y simuladores.
```javascript
const [state, setState] = useState({
  employees: 50,
  hourlyRate: 25,
  hoursPerWeek: 40,
  automationPercent: 30
});
const updateField = (field, value) => setState(prev => ({...prev, [field]: value}));
```

### 2. Patrón "Tabs/Vistas" (React)
Múltiples vistas en un solo componente con tab navigation.
Ideal para dashboards complejos.
```javascript
const [activeTab, setActiveTab] = useState('overview');
const tabs = ['overview', 'details', 'settings'];
// Renderizar condicionalmente según activeTab
```

### 3. Patrón "Datos Derivados" (React)
Calcular resultados en tiempo real con useMemo.
Ideal para visualizaciones que dependen de inputs.
```javascript
const results = useMemo(() => {
  const savings = state.employees * state.hourlyRate * state.hoursPerWeek * (state.automationPercent / 100);
  const roi = (savings * 12) / investment;
  return { savings, roi, paybackMonths: 12 / roi };
}, [state]);
```

### 4. Patrón "Cards Grid" (HTML/React)
Grid de tarjetas con KPIs. El layout más usado en dashboards.
```
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ KPI1 │ │ KPI2 │ │ KPI3 │ │ KPI4 │
│ $50K │ │ 85%  │ │ 2.3x │ │ 120  │
└──────┘ └──────┘ └──────┘ └──────┘
┌────────────────┐ ┌────────────────┐
│   GRÁFICO 1    │ │   GRÁFICO 2    │
│   (barras)     │ │   (líneas)     │
└────────────────┘ └────────────────┘
```

### 5. Patrón "Slider → Resultado" (React)
Input range que actualiza visualización en tiempo real.
El patrón más impactante en demos para ejecutivos.
```javascript
<input type="range" min={0} max={100} value={state.value}
  onChange={(e) => updateField('value', parseInt(e.target.value))} />
```

### 6. Patrón "Before/After" (React)
Dos columnas comparando escenario actual vs con IA.
Ideal para pitch comercial.
```
┌─────────────────┐ ┌─────────────────┐
│    SIN IA        │ │    CON IA        │
│ ⏱ 40 hrs/sem    │ │ ⏱ 16 hrs/sem    │
│ 💰 $8,000/mes   │ │ 💰 $3,200/mes   │
│ ❌ 15% errores  │ │ ✅ 2% errores   │
│ 📊 Manual       │ │ 📊 Automatizado │
└─────────────────┘ └─────────────────┘
```

### 7. Patrón "AI Chat" (React AI-powered)
Interface de chat que llama a la API de Claude.
Base para tutores, coaches y asistentes especializados.
```javascript
const [messages, setMessages] = useState([]);
const [input, setInput] = useState('');
const [loading, setLoading] = useState(false);

const sendMessage = async () => {
  setLoading(true);
  const response = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      model: "claude-sonnet-4-20250514",
      max_tokens: 1000,
      system: "Eres un tutor experto en [tema]. Responde en español.",
      messages: [...messages, { role: "user", content: input }],
    })
  });
  const data = await response.json();
  // Agregar respuesta a messages
  setLoading(false);
};
```

### 8. Patrón "Responsive Grid" (Tailwind)
Layout que funciona en desktop y mobile.
```jsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
  {/* Cards */}
</div>
```

---

## ANTI-PATRONES (errores frecuentes)

### 1. Usar localStorage
NUNCA funciona en artifacts. Siempre da error silencioso.
Solución: useState para datos temporales, window.storage para persistencia.

### 2. Importar librerías no permitidas
react-router, styled-components, axios, moment.js — ninguna está disponible.
Solución: condicionales para navegación, Tailwind para estilos, fetch nativo.

### 3. Código demasiado largo sin separar
Artifacts de 500+ líneas sin estructura = errores de renderizado.
Solución: funciones helper, componentes internos, datos separados.

### 4. Datos hardcoded sin contexto
Poner datos genéricos "Company A, Company B" es inútil para demos.
Solución: usar datos realistas del sector del cliente.

### 5. Olvidar export default (React)
Sin export default, el artifact no renderiza.
```javascript
// MAL
function MyComponent() { return <div>Hello</div>; }
// BIEN
export default function MyComponent() { return <div>Hello</div>; }
```

### 6. Usar imágenes externas
URLs de imágenes externas se bloquean por CSP.
Solución: /api/placeholder/400/300 o iconos de lucide-react.

### 7. No manejar estados de carga (AI-powered)
Llamar a la API de Claude sin indicador de loading = UX terrible.
Solución: siempre useState loading + spinner visual.

### 8. Diseño "AI slop"
Cards grises, botones azules genéricos, Inter font, sin personalidad.
Solución: paleta de colores específica, bordes redondeados variados,
espaciado generoso, gradientes sutiles.

---

## TIPS DE DISEÑO VISUAL

### Paletas profesionales probadas:
- **Corporativo:** #1e293b (oscuro), #3b82f6 (azul), #f8fafc (fondo)
- **Fintech:** #0f172a (navy), #10b981 (verde), #f59e0b (dorado)
- **Educativo:** #7c3aed (violeta), #06b6d4 (cyan), #fafafa (fondo)
- **Startup:** #ec4899 (rosa), #8b5cf6 (violeta), #111827 (oscuro)
- **Smart4AI:** #2563eb (azul), #f97316 (naranja), #ffffff (fondo)

### Técnicas que elevan la calidad:
- Sombras sutiles: shadow-sm en cards, shadow-lg en modales
- Bordes redondeados: rounded-xl para cards, rounded-full para avatares
- Gradientes en headers: bg-gradient-to-r from-blue-600 to-blue-800
- Iconos de lucide-react en vez de emojis
- Spacing generoso: p-6 en cards, gap-6 en grids
- Transiciones: transition-all duration-200 en hovers
