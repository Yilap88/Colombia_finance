import streamlit as st
from pathlib import Path

#Cargar Librerías
import pandas as pd
from pathlib import Path
import os
import re
import openpyxl
from market_col.dir_set import project_root_nb
from market_col.figures import static_plot
from market_col.figures import html_2_plot
from market_col.plotly import plotly_oneplot
from market_col.company_table import company_table

PROJECT_DIR = Path(project_root_nb())
data = pd.read_csv(f"{PROJECT_DIR}/Data/Colombia_Stocks/Acciones_colab.csv")
data['Fecha'] = pd.to_datetime(data['Fecha'])

Cemargos = data[data["Nemotécnico"] == "CEMARGOS"]
PFCemargos = data[data["Nemotécnico"] == "PFCEMARGOS"]
Grupoargos = data[data["Nemotécnico"] == "GRUPOARGOS"]
Cibest = data[data["Nemotécnico"] == "CIBEST"]
Ecopetrol = data[data["Nemotécnico"] == "ECOPETROL"]
GrupoAval = data[data["Nemotécnico"] == "GRUPOAVAL"]
Isa = data[data["Nemotécnico"] == "ISA"]
PFaval = data[data["Nemotécnico"] == "PFAVAL"]
PFDavigroup = data[data["Nemotécnico"] == "PFDAVIGRP"]
COLCAP = data[data["Nemotécnico"] == "ICOLCAP"]

datainput = pd.read_excel(f"{PROJECT_DIR}/Data/colombia_company_data/table_Input.xlsx", index_col= 0)


st.set_page_config(
    page_title="My app",
    layout="wide"
)

company_list = ["COLCAP", "Cemargos"]

st.write("""
# Financial Markers and evaluation
This is a independent project - no for investment purposes - be aware!
""")

fig = plotly_oneplot(COLCAP, x_col="Fecha", y_col="Precios (último /cierre)", plot_title=f"COLCAP - Last Price {COLCAP['Precios (último /cierre)'].iloc[-1]:,.2f}",
                color_in="black", date_marker = pd.to_datetime("2026-07-14"))
st.plotly_chart(fig, use_container_width=True)


fig2 = plotly_oneplot(Cemargos, x_col="Fecha", y_col="Precios (último /cierre)", plot_title=f"Cemargos - Last Price {Cemargos['Precios (último /cierre)'].iloc[-1]:,.2f}",
                color_in="green", date_marker = pd.to_datetime("2026-07-14"))
st.plotly_chart(fig2, use_container_width=True)


fig3 = plotly_oneplot(PFCemargos, x_col="Fecha", y_col="Precios (último /cierre)", plot_title=f"PF Cemargos - Last Price {PFCemargos['Precios (último /cierre)'].iloc[-1]:,.2f}",
                color_in="green", date_marker = pd.to_datetime("2026-07-14"))
st.plotly_chart(fig3, use_container_width=True)


fig4 = plotly_oneplot(Grupoargos, x_col="Fecha", y_col="Precios (último /cierre)", plot_title=f"Grupo Cemargos - Last Price {Grupoargos['Precios (último /cierre)'].iloc[-1]:,.2f}",
                color_in="green", date_marker = pd.to_datetime("2026-07-14"))
st.plotly_chart(fig4, use_container_width=True)


fig5 = plotly_oneplot(Cibest, x_col="Fecha", y_col="Precios (último /cierre)", plot_title=f"CIBEST - Last Price {Cibest['Precios (último /cierre)'].iloc[-1]:,.2f}",
                color_in="blue", date_marker = pd.to_datetime("2026-07-14"))
st.plotly_chart(fig5, use_container_width=True)


fig6 = plotly_oneplot(Ecopetrol, x_col="Fecha", y_col="Precios (último /cierre)", plot_title=f"Ecopetrol - Last Price {Ecopetrol['Precios (último /cierre)'].iloc[-1]:,.2f}",
                color_in="green", date_marker = pd.to_datetime("2026-07-14"))
st.plotly_chart(fig6, use_container_width=True)

