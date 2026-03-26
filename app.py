from dash import Dash
import dash_bootstrap_components as dbc
import sys
import os

# Ajout de la racine au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

#from pages import page1
#from pages import page1_cb
# from pages import page2_cb
# from pages import page2
from pages import page3
#from pages import page3_cb

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = page3.layout

if __name__ == '__main__':
    app.run(debug=True)