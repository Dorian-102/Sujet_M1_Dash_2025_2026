from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pages import page1, page1_cb
from pages import page2, page2_cb
from pages import page3

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout principal avec navigation
app.layout = html.Div([
    # Barre de navigation
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dcc.Link("Comparaison entre régions", href="/page1", className="nav-link text-white")),
            dbc.NavItem(dcc.Link("Affichage des données", href="/page2", className="nav-link text-white")),
            dbc.NavItem(dcc.Link("Aide en ligne", href="/page3", className="nav-link text-white")),
        ],
        brand="Application des M1 MECEN",
        brand_style={"color": "white"},
        color="#1a6fc4",
        dark=True,
    ),

    # Contenu de la page
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

@callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/page2":
        return page2.layout
    elif pathname == "/page3":
        return page3.layout
    else:
        return page1.layout

if __name__ == '__main__':
    app.run(debug=True)