### Company Table
"""
This script is used to create a table of companies with their respective information.
It reads data to generate a financial data structured table.
"""

import pandas as pd

def company_table(df_table, company_name):
    """
    Create a table with an input company information.

    Parameters:
    df_table (pd.DataFrame): A DataFrame containing the company information.
    company_name (str): The name of the company to extract information for.

    Returns:
    pd.DataFrame: A DataFrame containing the company table.
    """

    input_table = pd.DataFrame(df_table.loc[:, company_name])

    input_table.style \
    .set_properties(**{
        "text-align": "left",
        "padding": "10px",
        "font-size": "14px"
    }) \
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#e6e3e3"),
                ("color", "black"),
                ("font-weight", "bold"),
                ("text-align", "left"),
                ("padding", "10px")
            ]
        },
        {
            "selector": "td",
            "props": [
                ("border-bottom", "1px solid #eeeeee")
            ]
        }
    ])

    return input_table