# Este script actualiza el archivo de datos de acciones en Colombia, combinando los datos antiguos con los nuevos datos obtenidos de un archivo CSV más reciente (diarios) . 

#Cargar Librerías
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re
import openpyxl
from market_col.dir_set import project_root_py

PROJECT_DIR = project_root_py()

# Leemos datos viejos
oldata = pd.read_csv(f"{PROJECT_DIR}/Data/Colombia_Stocks/Acciones_colab.csv", sep=",", decimal=".")


# Transformación de los nuevos datos (archivo mas reciente)
carpeta = Path("Data/Colombia_Stocks/Input")
archivo_csv = max(carpeta.glob("*.csv"), key=lambda f: f.stat().st_mtime)
nombre_sin_extension = archivo_csv.stem


# Lectura de los nuevos datos, asignamos nombres de columnas y definimos el tipo de datos del csv
columnas = [
    "Nemotécnico",
    "Precios (último /cierre)",
    "Variación porcentual",
    "Volúmenes",
    "Cantidad",
    "Variación absoluta",
    "Precio apertura",
    "Precio máximo",
    "Precio mínimo",
    "Precio promedio",
    "Emisor / nombre",
    "Tipo  Activo"          # <- nombre de la columna faltante
]

newdata = pd.read_csv(
    archivo_csv,
    sep=";",
    decimal=",",
    names=columnas,
    header=0,
)

# Extraemos nombre del nuevo archivo para tomar fecha
fecha = re.search(r"\d{8}", archivo_csv.stem).group()
fecha = pd.to_datetime(fecha, format="%Y%m%d").strftime("%Y-%m-%d")
newdata["Fecha"] = fecha


# Concatenamos los datos viejos y nuevos
data = (
    pd.concat([oldata, newdata], ignore_index=True)
      .drop_duplicates(subset=["Fecha", "Nemotécnico"], keep="last")
)

data["Fecha"] = pd.to_datetime(data["Fecha"]).dt.strftime("%Y-%m-%d")


# Guardamos el archivo actualizado
data.to_csv(f"{PROJECT_DIR}/Data/Colombia_Stocks/Acciones_colab.csv", index=False)

# avisamos al usuario que el archivo ha sido actualizado
print(f"Archivo de datos de acciones actualizado correctamente. Ha sido guardado en {PROJECT_DIR}/Data/Colombia_Stocks/Acciones_colab.csv")