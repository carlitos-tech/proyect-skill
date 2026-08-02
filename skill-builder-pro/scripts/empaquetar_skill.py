#!/usr/bin/env python3
"""Empaqueta una carpeta de skill en un archivo .skill instalable.

Uso:
    python empaquetar_skill.py <ruta-de-la-carpeta-del-skill> [carpeta-de-salida]

Un .skill es un zip con la carpeta del skill adentro. Se valida antes de
empaquetar para no entregar un paquete que el instalador va a rechazar.
Ignora archivos de sistema y temporales que solo estorban.
"""

import os
import sys
import zipfile

IGNORAR_ARCHIVOS = {".DS_Store", "Thumbs.db", "desktop.ini"}
IGNORAR_CARPETAS = {"__pycache__", ".git", ".ipynb_checkpoints", "node_modules"}
IGNORAR_SUFIJOS = (".pyc", ".pyo", ".tmp", ".swp")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from validar_skill import validar
except ImportError:
    validar = None


def empaquetar(ruta, salida):
    ruta = os.path.abspath(ruta.rstrip(os.sep))
    nombre = os.path.basename(ruta)
    os.makedirs(salida, exist_ok=True)
    destino = os.path.join(salida, f"{nombre}.skill")

    incluidos = 0
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for raiz, dirs, archivos in os.walk(ruta):
            dirs[:] = [d for d in dirs if d not in IGNORAR_CARPETAS and not d.startswith(".")]
            for archivo in archivos:
                if archivo in IGNORAR_ARCHIVOS or archivo.endswith(IGNORAR_SUFIJOS):
                    continue
                completo = os.path.join(raiz, archivo)
                relativo = os.path.relpath(completo, os.path.dirname(ruta))
                z.write(completo, relativo)
                incluidos += 1
    return destino, incluidos


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    ruta = sys.argv[1]
    salida = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(ruta))

    if validar is not None:
        errores, avisos, _ = validar(ruta)
        if errores:
            print("No empaqueto: el skill tiene errores bloqueantes.\n")
            for e in errores:
                print(f"  ERROR  {e}")
            print("\nCorrige y vuelve a intentar.")
            sys.exit(1)
        for a in avisos:
            print(f"  AVISO  {a}")

    destino, n = empaquetar(ruta, salida)
    tam = os.path.getsize(destino) / 1024
    print(f"\nPaquete creado: {destino}")
    print(f"{n} archivo(s), {tam:.1f} KB")
    print("\nSiguiente paso: subelo en la configuracion de skills de tu superficie, "
          "verifica que quede activado, abre un hilo nuevo y escribe una de las "
          "frases disparadoras sin nombrar el skill.")


if __name__ == "__main__":
    main()
