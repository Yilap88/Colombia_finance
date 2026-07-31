## FIGURES

# This module contains functions to generate figures for the Colombia finance project. 
# It includes functions to create various types of plots and visualizations based on financial data.
import matplotlib.pyplot as plt

### Non interactive historical plot
def static_plot(dfinput, colores):
  # Graficar
    titulo = dfinput["Nemotécnico"].iloc[0]
    plt.figure(figsize=(12,6))
    plt.plot(dfinput["Fecha"], dfinput["Precios (último /cierre)"], color = colores, linewidth=2)
    plt.title(titulo)
    plt.xlabel("Fecha")
    plt.ylabel("Precio Cierre")
    plt.grid(True)
    plt.show()
