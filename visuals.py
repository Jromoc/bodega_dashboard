# visuals.py
import plotly.graph_objects as go
import config

def crear_mapa_calor(data):
    fig = go.Figure(data=go.Heatmap(z=data['temperatura'], colorscale='Viridis'))
    fig.add_shape(type="rect", x0=config.TOLVA_EJE_X - 0.5, y0=-0.5, 
                  x1=config.TOLVA_EJE_X + 0.5, y1=9.5, line=dict(color="red", width=3))
    return fig
