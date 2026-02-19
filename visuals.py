import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def plot_3d_thermal_lidar(X, Y, Z, temp_grid):
    """
    Crea una superficie 3D donde la altura es el LiDAR (Z) 
    pero el color representa la temperatura.
    """
    # CORRECCIÓN: Es 'scipy', no 'spicy'
    from scipy.interpolate import interp2d 
    
    # Creamos una función para suavizar la temperatura del grid 10x10 al mapa 50x50
    f = interp2d(np.linspace(0, 100, 10), np.linspace(0, 100, 10), temp_grid, kind='linear')
    temp_resampled = f(np.linspace(0, 100, 50), np.linspace(0, 100, 50))

    fig = go.Figure(data=[go.Surface(
        z=Z, x=X, y=Y, 
        surfacecolor=temp_resampled,
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
