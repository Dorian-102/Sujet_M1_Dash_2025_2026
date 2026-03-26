
import pandas as pd
import plotly.express as px

# Chargement des données
df = pd.read_csv("datas/avocado.csv")

# Vérification des noms exacts des régions (à retirer après vérification)
print(sorted(df["region"].unique()))

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