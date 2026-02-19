import plotly.graph_objects as go
import numpy as np

def plot_2d_heatmap(data, title):
    fig = go.Figure(data=go.Heatmap(
        z=data,
        x=np.linspace(0, 100, 10),
        y=np.linspace(0, 100, 10),
        colorscale='Viridis'
    ))
    fig.update_layout(title=title, xaxis_title="Metros", yaxis_title="Metros")
    return fig

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
