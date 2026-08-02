# This module contains functions to create interactive plots using Plotly for the market_col package. 

import plotly.graph_objects as go
import nbformat as nbf

# This function creates an interactive plot using Plotly. Just for 1 series.
# It takes a DataFrame, the names of the x and y columns, and titles for the plot and axes as input parameters.
#  The function returns a Plotly Figure object that can be displayed in a Jupyter notebook or saved as an HTML file.
def plotly_oneplot(data, x_col, y_col, plot_title):
    """
    Create an interactive plot using Plotly.

    Parameters:
    data (pd.DataFrame): The data to plot.
    x_col (str): The column name for the x-axis.
    y_col (str): The column name for the y-axis.
    title (str): The title of the plot.
    x_title (str): The title of the x-axis.
    y_title (str): The title of the y-axis.

    Returns:
    plotly.graph_objects.Figure: The interactive plot.
    """
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data[x_col], y=data[y_col], mode='lines', name=y_col))

    fig.update_layout(
        title= plot_title,
        xaxis_title = "Fecha",
        yaxis_title = "Valor",
        template="plotly_white",
        hovermode="x unified"
    )

    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(
                visible=True
            )
        )
    )

    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=[
                    dict(count=1, label="1M", step="month", stepmode="backward"),
                    dict(count=6, label="6M", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1A", step="year", stepmode="backward"),
                    dict(step="all", label="Todo")
                ]
            ),
            rangeslider=dict(visible=True),
            type="date"
        )
    )

    return fig 