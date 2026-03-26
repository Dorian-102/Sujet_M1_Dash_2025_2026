from dash import Input, Output, callback
import plotly.express as px
import pandas as pd

# Chargement et agrégation des données
df = pd.read_csv("datas/avocado.csv")
df["Date"] = pd.to_datetime(df["Date"])
df_agg = df.groupby(["Date", "region"], as_index=False)["Total Volume"].sum()

@callback(
    Output("graph-region-selectionnee", "figure"),
    Input("select-region", "value")
)
def update_graph(region_selectionnee):
    df_region = df_agg[df_agg["region"] == region_selectionnee]
    
    fig = px.line(
        df_region,
        x="Date",
        y="Total Volume",
        title=f"Quantités vendues - {region_selectionnee}",
        labels={"Total Volume": "Volume total", "Date": "Date"}
    )
    
    return fig