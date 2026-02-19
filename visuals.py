import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def plot_3d_thermal_lidar(X, Y, Z, temp_grid):
    """
    Crea una superficie 3D donde la altura es el LiDAR (Z) 
    pero el color representa la temperatura (Verde a Rojo).
    """
    # Reseamos la matriz de temperatura (10x10) para que coincida con la resolución del LiDAR (50x50)
    from scipy.interpolate import interp2d
    f = interp2d(np.linspace(0, 100, 10), np.linspace(0, 100, 10), temp_grid, kind='linear')
    temp_resampled = f(np.linspace(0, 100, 50), np.linspace(0, 100, 50))

    fig = go.Figure(data=[go.Surface(
        z=Z, x=X, y=Y, 
        surfacecolor=temp_resampled, # Aquí aplicamos el color térmico
        colorscale=[[0, 'green'], [0.5, 'yellow'], [1, 'red']],
        colorbar=dict(title="Temp °C")
    )])
    
    fig.update_layout(
        title="Visualización LiDAR 3D (Color por Temperatura)",
        scene=dict(
            zaxis=dict(range=[0, 15], title="Altura (m)"),
            aspectratio=dict(x=1, y=1, z=0.4)
        ),
        margin=dict(l=0, r=0, b=0, t=0)
    )
    return fig

def plot_2d_grid(data, title, label="Valor"):
    """Genera la vista aérea de sectores (Grid 10x10)."""
    fig = go.Figure(data=go.Heatmap(
        z=data,
        x=np.linspace(5, 95, 10), # Centrado en los cuadrantes
        y=np.linspace(5, 95, 10),
        colorscale='RdYlGn_r', # Rojo para alto, Verde para bajo (típico en calor)
        colorbar=dict(title=label)
    ))
    fig.update_layout(
        title=title,
        xaxis_title="Sectores (Ancho m)",
        yaxis_title="Sectores (Largo m)",
        width=600, height=500
    )
    return fig

def plot_comparative_trends(df_dia):
    # (Mantener la función anterior para el gráfico de líneas)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Temp_Ext'], name="Temp Ext"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Temp_Int'], name="Temp Int"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_dia['Fecha_Hora'], y=df_dia['Hum_Int'], name="Hum Int (%)", line=dict(dash='dash')), secondary_y=True)
    fig.update_layout(title="Tendencias del Día", hovermode="x unified")
    return fig
