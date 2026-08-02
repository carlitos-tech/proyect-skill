#!/usr/bin/env python3
"""Revisa un archivo de artifact (.jsx o .html) contra las restricciones duras.

Uso:
    python validar_artifact.py <ruta-del-archivo.jsx|.html>

Sale con codigo 1 si hay errores bloqueantes, 0 si solo hay advertencias.
Sin dependencias externas: es un lint de texto, a proposito. La idea no es
sustituir a esbuild sino atrapar antes las fallas que esbuild NO ve, porque
compilan perfecto y aun asi el artifact sale en blanco en el panel.
"""

import os
import re
import sys

# Iconos de lucide-react que existen con seguridad en v0.383.0. La lista no es
# exhaustiva; por eso un icono fuera de ella es AVISO y no ERROR.
ICONOS_SEGUROS = {
    "Users", "User", "Star", "Award", "TrendingUp", "TrendingDown", "DollarSign",
    "BarChart3", "BarChart2", "PieChart", "LineChart", "Activity", "Clock",
    "Calendar", "Check", "CheckCircle", "X", "XCircle", "AlertTriangle",
    "AlertCircle", "Info", "Settings", "Search", "Filter", "Download", "Upload",
    "ChevronDown", "ChevronUp", "ChevronLeft", "ChevronRight", "ArrowUp",
    "ArrowDown", "ArrowRight", "ArrowLeft", "Plus", "Minus", "Trash2", "Edit",
    "Eye", "EyeOff", "Mail", "Phone", "MapPin", "Home", "Briefcase", "Target",
    "Zap", "Shield", "Lock", "Unlock", "FileText", "Folder", "Camera", "Image",
    "Play", "Pause", "RefreshCw", "RotateCw", "Send", "Share2", "Heart",
    "ThumbsUp", "MessageSquare", "Bell", "Menu", "MoreVertical", "Loader2",
    "Package", "ShoppingCart", "CreditCard", "Percent", "Hash", "Layers",
    "Grid", "List", "Database", "Server", "Cpu", "Wifi", "Globe", "Building2",
}

LIBRERIAS_PROHIBIDAS = {
    "xlsx": "rompe el montaje del componente. Para Excel, pide exportar a CSV y parsea con FileReader.readAsText.",
    "papaparse": "lo bloquea la seguridad del navegador. Parsea el CSV a mano con FileReader.readAsText.",
    "react-router": "no existe en el sandbox. Usa renderizado condicional con useState.",
    "styled-components": "no existe en el sandbox. Usa clases de Tailwind.",
    "axios": "no existe en el sandbox. Usa fetch nativo.",
    "moment": "no existe en el sandbox. Usa Date o Intl.DateTimeFormat.",
}

SET_SEGURO = {"react", "recharts", "lucide-react"}


def leer(ruta):
    with open(ruta, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def sin_comentarios(src):
    """Quita comentarios para no reportar codigo que ya esta desactivado."""
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.S)
    src = re.sub(r"^\s*//.*$", "", src, flags=re.M)
    return src


def validar(ruta):
    errores, avisos, oks = [], [], []

    if not os.path.isfile(ruta):
        return [f"La ruta no existe o no es un archivo: {ruta}"], [], []

    ext = os.path.splitext(ruta)[1].lower()
    if ext not in (".jsx", ".js", ".html", ".htm"):
        avisos.append(f"Extension '{ext}' inesperada. Esperaba .jsx o .html.")
    es_react = ext in (".jsx", ".js")

    bruto = leer(ruta)
    src = sin_comentarios(bruto)

    # --- almacenamiento del navegador ---
    for api in ("localStorage", "sessionStorage", "indexedDB"):
        if re.search(rf"\b{api}\b", src):
            errores.append(
                f"Usa {api}. Esta bloqueado en artifacts y falla en silencio: el "
                "componente no monta y no veras ningun error en pantalla. Usa useState "
                "para datos temporales, o window.storage si el artifact va publicado."
            )
    if not any(re.search(rf"\b{a}\b", src) for a in ("localStorage", "sessionStorage", "indexedDB")):
        oks.append("Sin localStorage / sessionStorage / indexedDB")

    # --- librerias ---
    imports = re.findall(r"""(?:import\s[^'"]*from\s*|require\(\s*)['"]([^'"]+)['"]""", src)
    hay_prohibida = False
    for imp in imports:
        raiz = imp.split("/")[0].lower()
        for prohibida, razon in LIBRERIAS_PROHIBIDAS.items():
            if raiz == prohibida or raiz.startswith(prohibida):
                errores.append(f"Importa '{imp}': {razon}")
                hay_prohibida = True
    externos = {
        i.split("/")[0] for i in imports
        if not i.startswith((".", "/", "@/"))
        and i.split("/")[0].lower() not in SET_SEGURO
        and i.split("/")[0].lower() not in LIBRERIAS_PROHIBIDAS
    }
    if externos:
        avisos.append(
            f"Importa fuera del set seguro (React + Recharts + lucide-react): {', '.join(sorted(externos))}. "
            "Puede funcionar, pero es la primera sospecha si el artifact no monta."
        )
    elif imports and not hay_prohibida:
        oks.append("Todos los imports dentro del set seguro")

    # --- iconos de lucide-react ---
    m = re.search(r"import\s*\{([^}]*)\}\s*from\s*['\"]lucide-react['\"]", src)
    if m:
        usados = {x.strip().split(" as ")[0].strip() for x in m.group(1).split(",") if x.strip()}
        raros = sorted(usados - ICONOS_SEGUROS)
        if raros:
            avisos.append(
                f"Iconos de lucide-react que no estan en la lista conocida de v0.383.0: {', '.join(raros)}. "
                "Un icono que no existe en esa version rompe el render entero. Verificalo o cambialo por uno clasico."
            )
        else:
            oks.append(f"{len(usados)} icono(s) de lucide-react, todos clasicos")

    # --- red e imagenes externas ---
    urls = re.findall(r"https?://([\w.-]+)", src)
    externas = sorted({d for d in urls if d != "cdnjs.cloudflare.com" and "api.anthropic.com" not in d})
    if externas:
        errores.append(
            f"Apunta a dominios externos: {', '.join(externas)}. El sandbox solo permite "
            "cdnjs.cloudflare.com. Para imagenes usa /api/placeholder/ancho/alto; para datos, "
            "embebelos ya procesados en el archivo."
        )
    else:
        oks.append("Sin dominios externos fuera de cdnjs.cloudflare.com")

    if re.search(r"<img[^>]+src\s*=\s*['\"]https?://", src):
        errores.append("Tiene una etiqueta img con URL externa. La CSP la bloquea. Usa /api/placeholder/ancho/alto.")

    # --- Recharts ---
    n_rc = len(re.findall(r"<ResponsiveContainer", src))
    if n_rc > 4:
        avisos.append(
            f"Monta {n_rc} ResponsiveContainer. Por encima de 4 al tiempo el navegador se congela. "
            "Si hay pestanas, renderiza solo la activa en vez de montarlas todas y ocultarlas."
        )
    elif n_rc:
        oks.append(f"{n_rc} ResponsiveContainer, dentro del limite de 4")

    # --- React ---
    if es_react:
        if not re.search(r"export\s+default\b", src):
            errores.append(
                "Falta 'export default'. Sin el, el artifact no renderiza y la pantalla queda en blanco."
            )
        else:
            oks.append("export default presente")

        # componentes auxiliares definidos dentro del principal
        anidados = []
        for mm in re.finditer(r"^(\s+)(?:const|function)\s+([A-Z]\w*)\s*[=(]", src, flags=re.M):
            if len(mm.group(1)) >= 2:
                anidados.append(mm.group(2))
        if anidados:
            avisos.append(
                f"Componente(s) con mayuscula definidos dentro de otra funcion: {', '.join(sorted(set(anidados)))}. "
                "React los vuelve a crear en cada render, asi que se desmontan y pierden su estado (un input se "
                "vacia al escribir). Sacalos al nivel superior del archivo."
            )
        else:
            oks.append("Sin componentes auxiliares anidados")

        if re.search(r"\b(hidden|block|flex|grid)\s+(sm|md|lg|xl):", src):
            avisos.append(
                "Usa breakpoints de Tailwind para mostrar u ocultar elementos. El viewport del panel de "
                "artifacts no los dispara de forma confiable; si algo es critico para el layout, no lo "
                "condiciones a un breakpoint."
            )

    # --- tamano ---
    n_lineas = len(src.strip().splitlines())
    if n_lineas > 500:
        avisos.append(
            f"{n_lineas} lineas. Por encima de 500 sin estructura interna clara aparecen fallos de "
            "renderizado. Separa datos, helpers y subcomponentes."
        )
    else:
        oks.append(f"{n_lineas} lineas, tamano manejable")

    return errores, avisos, oks


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    ruta = os.path.abspath(sys.argv[1])
    errores, avisos, oks = validar(ruta)

    print(f"\nValidando artifact: {ruta}\n" + "=" * 68)
    for o in oks:
        print(f"  OK       {o}")
    for a in avisos:
        print(f"  AVISO    {a}")
    for e in errores:
        print(f"  ERROR    {e}")
    print("=" * 68)
    if errores:
        print(f"RECHAZADO: {len(errores)} error(es) bloqueante(s), {len(avisos)} aviso(s).")
        sys.exit(1)
    print(f"APROBADO: 0 errores bloqueantes, {len(avisos)} aviso(s).")
    print("Si tienes terminal, confirma tambien que compila:")
    print("  npx esbuild ARCHIVO.jsx --bundle --external:react --external:recharts "
          "--external:lucide-react --loader:.jsx=jsx --outfile=/dev/null")
    sys.exit(0)


if __name__ == "__main__":
    main()
