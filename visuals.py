import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy.interpolate import interp2d # <-- Corregido de 'spicy' a 'scipy'

def plot_3d_thermal_lidar(X, Y, Z, temp_grid):
    """Superficie 3D con color basado en temperatura."""
    # Suavizamos el grid de 10x10 para que coincida con el mapa de 50x50
    f = interp2d(np.linspace(0, 100, 10), np.linspace(0, 100, 10), temp_grid, kind='linear')
    temp_resampled = f(np.linspace(0, 100, 50), np.linspace(0, 100, 50))

    fig = go.Figure(data=[go.Surface(
        z=Z, x=X, y=Y, 
        surfacecolor=temp_resampled,
        colorscale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']],
        colorbar=dict(title="Temp °C")
    )])
    
    fig.update_layout(
        scene=dict(
            zaxis=dict(range=[0, 15], title="Altura (m)"),
            aspectratio=dict(x=1, y=1, z=0.4)
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    return fig

def plot_2d_grid(data, title, label="Valor"):
    """Vista aérea de sectores (Grid 10x10)."""
    fig = go.Figure(data=go.Heatmap(
        z=data,
        x=np.linspace(5, 95, 10),
        y=np.linspace(5, 95, 10),
        colorscale='RdYlGn_r', 
        colorbar=dict(title=label)
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Metros (Ancho)",
        yaxis_title="Metros (Largo)",
        width=700, height=500
    )
    return fig

def plot_comparative_trends(df_dia):
    """Gráfico de líneas histórico."""
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Temp_Ext'], name="Temp Ext (MTY)"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Temp_Int'], name="Temp Int (Bodega)"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Hum_Int'], name="Hum Int (%)", line=dict(dash='dash')), secondary_y=True)
    
    fig.update_layout(title="Tendencias de las últimas 24h", hovermode="x unified")
    fig.update_yaxes(title_text="Temperatura °C", secondary_y=False)
    fig.update_yaxes(title_text="Humedad %", secondary_y=True)
    return fig
