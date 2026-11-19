# Este script llama datos desde el datos.gov y actualiza la base de datos local de TRM en Colombia, 
# combinando los datos antiguos con los nuevos datos obtenidos de un archivo CSV más reciente (diarios) .


#Cargar Librerías
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re
import openpyxl
from market_col.dir_set import project_root_py

PROJECT_DIR = project_root_py()

url = "https://www.datos.gov.co/resource/32sa-8pi3.json"
newTRM = pd.read_json(url)

newTRM["vigenciadesde"] = pd.to_datetime(newTRM["vigenciadesde"])
newTRM["vigenciahasta"] = pd.to_datetime(newTRM["vigenciahasta"])
newTRM = newTRM[["vigenciadesde", "vigenciahasta", "valor"]]


# Crear una lista de fechas para cada fila
newTRM["fecha"] = newTRM.apply(
    lambda x: pd.date_range(x["vigenciadesde"], x["vigenciahasta"], freq="D"),
    axis=1
)

# Expandir las listas
newTRM = newTRM.explode("fecha")

# Conservar únicamente lo necesario
newTRM = (
    newTRM[["fecha", "valor"]]
    .reset_index(drop=True)
)

print(newTRM.head())


newTRM = newTRM.sort_values(by='fecha', ascending=True).reset_index(drop=True)

oldTRM = pd.read_csv(f"{PROJECT_DIR}/Data/TRM/TRM.csv", parse_dates=["fecha"])

fullTRM = pd.concat([oldTRM, newTRM]).drop_duplicates(subset='fecha', keep='last').reset_index(drop=True)

fullTRM.to_csv(f"{PROJECT_DIR}/Data/TRM/newTRM.csv", index=False)
fullTRM['fecha'] = pd.to_datetime(fullTRM['fecha'])