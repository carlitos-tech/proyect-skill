#!/usr/bin/env python3
"""Valida un skill contra las reglas que rechaza el instalador.

Uso:
    python validar_skill.py <ruta-de-la-carpeta-del-skill>

Sale con codigo 1 si hay errores bloqueantes, 0 si solo hay advertencias.
No requiere dependencias externas: parsea el frontmatter a mano para que
funcione en cualquier entorno sin instalar nada.
"""

import os
import re
import sys

LIMITE_DESCRIPCION = 1024
LIMITE_LINEAS = 500
PALABRAS_PROHIBIDAS = ("claude", "anthropic")


def leer_frontmatter(texto):
    """Devuelve (dict_campos, cuerpo, error). Solo soporta claves de primer nivel."""
    if not texto.startswith("---"):
        return {}, texto, "El archivo no empieza con el delimitador --- del frontmatter."
    partes = texto.split("---", 2)
    if len(partes) < 3:
        return {}, texto, "El frontmatter no esta cerrado con un segundo ---."
    bruto, cuerpo = partes[1], partes[2]
    campos, clave = {}, None
    for linea in bruto.splitlines():
        if not linea.strip():
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", linea)
        if m:
            clave = m.group(1)
            campos[clave] = m.group(2).strip()
        elif clave:
            campos[clave] = (campos[clave] + " " + linea.strip()).strip()
    return campos, cuerpo, None


def validar(ruta):
    errores, avisos, oks = [], [], []

    if not os.path.isdir(ruta):
        return [f"La ruta no existe o no es una carpeta: {ruta}"], [], []

    archivos = os.listdir(ruta)
    if "SKILL.md" not in archivos:
        parecidos = [a for a in archivos if a.lower() == "skill.md"]
        if parecidos:
            errores.append(
                f"El archivo se llama '{parecidos[0]}'. Debe llamarse SKILL.md exacto, "
                "respetando mayusculas."
            )
        else:
            errores.append("Falta SKILL.md en la raiz de la carpeta.")
        return errores, avisos, oks
    oks.append("SKILL.md presente con el nombre correcto")

    with open(os.path.join(ruta, "SKILL.md"), encoding="utf-8") as fh:
        texto = fh.read()

    campos, cuerpo, err = leer_frontmatter(texto)
    if err:
        errores.append(err)
        return errores, avisos, oks
    oks.append("Frontmatter delimitado correctamente")

    bruto_fm = texto.split("---", 2)[1]
    if "<" in bruto_fm or ">" in bruto_fm:
        errores.append(
            "El frontmatter contiene los simbolos menor-que o mayor-que. "
            "Quitalos: rompen el parseo y el skill no carga."
        )
    else:
        oks.append("Frontmatter sin simbolos prohibidos")

    # name
    nombre = campos.get("name", "")
    if not nombre:
        errores.append("Falta el campo name en el frontmatter.")
    else:
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", nombre):
            errores.append(
                f"name '{nombre}' no esta en kebab-case. Usa solo minusculas, "
                "numeros y guiones simples; sin espacios ni guion bajo."
            )
        else:
            oks.append(f"name en kebab-case: {nombre}")
        for palabra in PALABRAS_PROHIBIDAS:
            if palabra in nombre.lower():
                errores.append(
                    f"name contiene la palabra prohibida '{palabra}'. El instalador lo rechaza."
                )

    # description
    desc = campos.get("description", "")
    if not desc:
        errores.append("Falta el campo description. Sin el, el skill nunca se activa solo.")
    else:
        n = len(desc)
        if n > LIMITE_DESCRIPCION:
            errores.append(
                f"description tiene {n} caracteres y el maximo es {LIMITE_DESCRIPCION}. "
                f"Recorta {n - LIMITE_DESCRIPCION}: quita adjetivos y disparadores redundantes, "
                "nunca las frases-NO."
            )
        else:
            oks.append(f"description dentro del limite ({n}/{LIMITE_DESCRIPCION} caracteres)")

        comillas = desc.count('"') // 2 + len(re.findall(r"[«”']\s*,", desc))
        disparadores = desc.count('"') // 2
        if disparadores < 5:
            avisos.append(
                f"Solo detecte ~{disparadores} frases disparadoras entre comillas. "
                "Lo sano son de 10 a 20: es lo que decide si el skill se activa solo."
            )
        else:
            oks.append(f"~{disparadores} frases disparadoras detectadas")

        low = desc.lower()
        if not any(k in low for k in ("no usar", "no uses", "no aplica", "no activar")):
            avisos.append(
                "No encuentro frases-NO en la description. Sin ellas el skill choca "
                "con otros de vocabulario parecido y se activa el equivocado."
            )
        else:
            oks.append("Frases-NO presentes")

        if not any(k in low for k in ("cuando", "cuándo", "activate", "actívate", "usa este")):
            avisos.append(
                "La description parece decir QUE hace pero no CUANDO usarla. "
                "Sin el cuando, queda instalada pero invisible."
            )

    # cuerpo
    n_lineas = len(cuerpo.strip().splitlines())
    if n_lineas > LIMITE_LINEAS:
        avisos.append(
            f"El cuerpo tiene {n_lineas} lineas (recomendado bajo {LIMITE_LINEAS}). "
            "Mueve datos y tablas largas a references/."
        )
    else:
        oks.append(f"Cuerpo de {n_lineas} lineas, dentro de lo recomendado")

    low_cuerpo = cuerpo.lower()
    if low_cuerpo.count("ejemplo") < 3:
        avisos.append(
            "Menos de 3 ejemplos en el cuerpo. Sin ejemplos el formato de salida "
            "cambia entre usos; incluye siempre uno de caso borde."
        )
    else:
        oks.append("Al menos 3 ejemplos en el cuerpo")

    # carpetas auxiliares
    for carpeta in ("references", "scripts", "assets"):
        d = os.path.join(ruta, carpeta)
        if os.path.isdir(d):
            contenido = [x for x in os.listdir(d) if not x.startswith(".")]
            if not contenido:
                avisos.append(f"La carpeta {carpeta}/ existe pero esta vacia. Borrala o llenala.")
            else:
                oks.append(f"{carpeta}/ con {len(contenido)} archivo(s)")

    # referencias rotas
    for ref in set(re.findall(r"(references/[\w.-]+|scripts/[\w.-]+|assets/[\w.-]+)", cuerpo)):
        if not os.path.exists(os.path.join(ruta, ref)):
            errores.append(
                f"El SKILL.md menciona '{ref}' pero ese archivo no existe en la carpeta."
            )

    return errores, avisos, oks


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    ruta = os.path.abspath(sys.argv[1])
    errores, avisos, oks = validar(ruta)

    print(f"\nValidando: {ruta}\n" + "=" * 60)
    for o in oks:
        print(f"  OK       {o}")
    for a in avisos:
        print(f"  AVISO    {a}")
    for e in errores:
        print(f"  ERROR    {e}")
    print("=" * 60)
    if errores:
        print(f"RECHAZADO: {len(errores)} error(es) bloqueante(s), {len(avisos)} aviso(s).")
        sys.exit(1)
    print(f"APROBADO: 0 errores bloqueantes, {len(avisos)} aviso(s).")
    sys.exit(0)


if __name__ == "__main__":
    main()
