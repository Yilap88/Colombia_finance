## JUPITER ROOT DIRECTORY SET
### This module is used to set the root directory of the project based on the presence 
### of a marker file (default is ".git"). 
### It traverses up the directory tree until it finds the marker file, indicating the root of the project.

# Configuramos la ruta del proyecto
from pathlib import Path
def project_root_py(marker=".git"):
    ruta = Path(__file__).resolve().parent

    while ruta != ruta.parent:
        if (ruta / marker).exists():
            return ruta
        ruta = ruta.parent

    raise FileNotFoundError(f"No se encontró '{marker}'")


def project_root_nb(marker=".git"):
    ruta = Path.cwd().resolve()
    while ruta != ruta.parent:
        if (ruta / marker).exists():
            return ruta
        ruta = ruta.parent
    raise FileNotFoundError(f"No se encontró '{marker}'")

PROJECT_DIR = project_root_nb()