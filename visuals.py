import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def plot_3d_lidar(X, Y, Z):
    fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y, colorscale='YlOrBr')])
    fig.update_layout(
        scene=dict(
            zaxis=dict(range=[0, 15], title="Altura (m)"),
            aspectratio=dict(x=1, y=1, z=0.4)
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    return fig

def plot_comparative_trends(df_dia):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Temperaturas (Eje Principal)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Temp_Ext'], name="Temp Ext (MTY)"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Temp_Int'], name="Temp Int (Bodega)"), secondary_y=False)
    
    # Humedad (Eje Secundario)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Hum_Int'], name="Hum Int (%)", line=dict(dash='dash', color='green')), secondary_y=True)
    
    fig.update_layout(title="Análisis Térmico e Higrométrico (24h)", hovermode="x unified")
    fig.update_yaxes(title_text="Temperatura °C", secondary_y=False)
    fig.update_yaxes(title_text="Humedad %", secondary_y=True)
    return fig
