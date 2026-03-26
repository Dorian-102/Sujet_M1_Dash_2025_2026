from dash import Input, Output, callback
import pandas as pd
from dash import html

# Chargement des données
df = pd.read_csv("datas/avocado.csv")

# Colonnes à afficher
COLONNES_CACHEES = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
colonnes_affichees = [col for col in df.columns if col not in COLONNES_CACHEES]

@callback(
    Output("tbody-p2", "children"),
    Output("badge-lignes-p2", "children"),
    Input("select-region-p2", "value"),
    Input("radio-type-p2", "value")
)
def update_table(region, type_avocat):
    # Filtrage par région
    df_filtre = df[df["region"] == region]
    
    # Filtrage par type
    if type_avocat != "Tous":
        df_filtre = df_filtre[df_filtre["type"] == type_avocat]
    
    # Génération des lignes du tableau
    rows = [
        html.Tr([html.Td(df_filtre.iloc[i][col]) for col in colonnes_affichees])
        for i in range(len(df_filtre))
    ]
    
    # Badge avec le nombre de lignes
    badge = f"Lignes: {len(df_filtre)}"
    
    return rows, badge