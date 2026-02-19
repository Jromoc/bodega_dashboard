import plotly.graph_objects as go
from plotly.subplots import make_subplots

def plot_comparative_trends(df_filtrado):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Temperatura
    fig.add_trace(go.Scatter(x=df_filtrado['Fecha_Hora'], y=df_filtrado['Temp_Ext'], name="Temp Ext (MTY)"), secondary_y=False)
    fig.add_trace(go.Scatter(x=df_filtrado['Fecha_Hora'], y=df_filtrado['Temp_Int'], name="Temp Int (Bodega)"), secondary_y=False)
    
    # Humedad
    fig.add_trace(go.Scatter(x=df_filtrado['Fecha_Hora'], y=df_filtrado['Hum_Int'], name="Hum Int (%)", line=dict(dash='dash')), secondary_y=True)
    
    fig.update_layout(title="Análisis Térmico e Higrométrico", hovermode="x unified")
    fig.update_yaxes(title_text="Temperatura °C", secondary_y=False)
    fig.update_yaxes(title_text="Humedad %", secondary_y=True)
    return fig
