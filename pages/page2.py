from dash import html
import dash_bootstrap_components as dbc
import pandas as pd

# Chargement des données
df = pd.read_csv("datas/avocado.csv")

# Liste des régions sans doublon, triées
regions = sorted(df["region"].unique())

# Colonnes à afficher
COLONNES_CACHEES = ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
colonnes_affichees = [col for col in df.columns if col not in COLONNES_CACHEES]

# Layout
layout = dbc.Container([
    # Barre noire du haut
    dbc.Row([
        # Colonne menu déroulant région
        dbc.Col([
            html.Label("Sélectionner une région:", style={"color": "white"}),
            dbc.Select(
                id="select-region-p2",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0],
            ),
        ], xs=12, md=6),

        # Colonne type d'avocat
        dbc.Col([
            html.Label("Sélectionner un type:", style={"color": "white"}),
            dbc.RadioItems(
                id="radio-type-p2",
                options=[
                    {"label": "Tous", "value": "Tous"},
                    {"label": "conventional", "value": "conventional"},
                    {"label": "organic", "value": "organic"},
                ],
                value="Tous",
                inline=True,
                style={"color": "white"}
            ),
        ], xs=12, md=4),

        # Badge nombre de lignes
        dbc.Col([
            dbc.Badge(
                "Lignes: 0",
                id="badge-lignes-p2",
                className="w-100 text-center",
                style={
                    "fontSize": "1rem",
                    "padding": "10px",
                    "backgroundColor": "#9b59b6",
                    "color": "white",
                    "borderRadius": "25px"
                }
            ),
        ], xs=12, md=2, className="d-flex align-items-end"),
    ], className="mb-3 mt-3 p-3",
       style={"backgroundColor": "#1a1a2e", "borderRadius": "10px"}),  # Barre noire uniquement

    # Tableau
    dbc.Table(
        id="table-p2",
        children=[
            html.Thead(html.Tr([html.Th(col) for col in colonnes_affichees])),
            html.Tbody(id="tbody-p2")
        ],
        bordered=True,
        hover=True,
        striped=True,
        responsive=True,
        style={"fontSize": "0.85rem"}
    )
], fluid=True)