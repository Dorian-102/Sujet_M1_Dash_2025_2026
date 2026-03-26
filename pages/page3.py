from dash import html, dcc
import dash_bootstrap_components as dbc

# Lecture des fichiers markdown
with open("expli1.md", "r", encoding="utf-8") as f:
    expli1 = f.read()

with open("expli2.md", "r", encoding="utf-8") as f:
    expli2 = f.read()

with open("expli3.md", "r", encoding="utf-8") as f:
    expli3 = f.read()

# Layout
layout = dbc.Container([
    dbc.Card([
        dbc.CardHeader(
            html.H4("Présentation de Dash", className="text-white mb-0"),
            style={"backgroundColor": "#1a6fc4"}
        ),
        dbc.CardBody([
            dbc.Tabs([
                dbc.Tab(
                    dcc.Markdown(expli1, style={"color": "white", "padding": "20px"}),
                    label="Accueil",
                    tab_id="tab-1",
                    label_style={"color": "white"},
                    active_label_style={"color": "white", "backgroundColor": "#1a6fc4"}
                ),
                dbc.Tab(
                    dcc.Markdown(expli2, style={"color": "white", "padding": "20px"}),
                    label="Layout",
                    tab_id="tab-2",
                    label_style={"color": "white"},
                    active_label_style={"color": "white", "backgroundColor": "#1a6fc4"}
                ),
                dbc.Tab(
                    dcc.Markdown(expli3, style={"color": "white", "padding": "20px"}),
                    label="CallBack",
                    tab_id="tab-3",
                    label_style={"color": "white"},
                    active_label_style={"color": "white", "backgroundColor": "#1a6fc4"}
                ),
            ], active_tab="tab-1")
        ], style={"backgroundColor": "#1a1a2e"})
    ], className="mt-3")
], fluid=True, style={"backgroundColor": "#1a1a2e", "minHeight": "100vh"})