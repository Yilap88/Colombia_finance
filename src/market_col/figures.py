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
  

from IPython.display import display, HTML

def html_2_plot (hmtl1, html2):
  html = f"""
  <div style="
  display: flex;
  align-items: flex-start;
  gap: 30px;
  ">

  <div style="flex: 1;">
      {hmtl1}
  </div>

  <div style="
    width: 300px;
    overflow-x: auto;
  ">
      {html2}
  </div>

  </div>
  """

  return display(HTML(html))