from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Chargement des données
df = pd.read_csv("datas/avocado.csv")

# Agrégation par région et par date
df["Date"] = pd.to_datetime(df["Date"])
df_agg = df.groupby(["Date", "region"], as_index=False)["Total Volume"].sum()

# Régions fixes du graphique 1 - noms exacts du CSV
REGIONS_PRINCIPALES = ["Midsouth", "Northeast", "SouthCentral", "Southeast", "TotalUS", "West"]

# Couleurs de la légende - noms exacts du CSV
COLOR_MAP = {
    "Midsouth": "#636efa",
    "Northeast": "#ef553b",
    "SouthCentral": "#00cc96",
    "Southeast": "#ab63fa",
    "TotalUS": "#ffa15a",
    "West": "#19d3f3"
}

# Graphique 1 - fixe
df_principales = df_agg[df_agg["region"].isin(REGIONS_PRINCIPALES)]
fig1 = px.line(
    df_principales,
    x="Date",
    y="Total Volume",
    color="region",
    color_discrete_map=COLOR_MAP,
    title="Quantités vendues - Régions principales",
    labels={"Total Volume": "Volume total", "Date": "Date", "region": "Région"}
)

# Liste des régions pour le select (sans doublon, triées)
regions = sorted(df["region"].unique())

# Layout
layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(
            html.H4("Quantités vendues (Total Volume)", className="text-white mb-0"),
            style={"backgroundColor": "#1a6fc4"}
        ),
        dbc.CardBody([
            dbc.Row([
                # Colonne 1 - Graphique fixe
                dbc.Col([
                    dcc.Graph(id="graph-regions-principales", figure=fig1)
                ], width=6),

                # Colonne 2 - Badge + Select + Graphique dynamique
                dbc.Col([
                    dbc.Badge(
                        "Sélectionnez une région:",
                        className="w-100 text-center mb-2",
                        style={
                            "fontSize": "1rem",
                            "padding": "10px",
                            "backgroundColor": "#9b59b6",
                            "color": "white",
                            "borderRadius": "25px"
                        }
                    ),
                    dbc.Select(
                        id="select-region",
                        options=[{"label": r, "value": r} for r in regions],
                        value=regions[0],
                        className="mb-3"
                    ),
                    dcc.Graph(id="graph-region-selectionnee")
                ], width=6),
            ])
        ], style={"backgroundColor": "#000000"}),
    ], className="mt-3")
], fluid=True)