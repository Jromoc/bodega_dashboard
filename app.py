import streamlit as st
import pandas as pd
from simulation import generate_lidar_data
from logic import calculate_inventory
from visuals import plot_comparative_trends, plot_3d_lidar

st.set_page_config(layout="wide", page_title="Bodega Monterrey Feb")

# Cargar Datos del CSV
@st.cache_data
def load_data():
    df = pd.read_csv("inventario_semana.csv")
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'])
    return df

df = load_data()

st.title("🌡️ Control de Bodega - Monterrey (Febrero)")

# Selector de Día
fecha_seleccionada = st.sidebar.date_input("Selecciona el día de análisis", df['Fecha_Hora'].min())
df_dia = df[df['Fecha_Hora'].dt.date == fecha_seleccionada]

if not df_dia.empty:
    # Simulación de Lidar para el momento actual (usamos la última hora del día seleccionado)
    X, Y, Z = generate_lidar_data()
    ultimo_registro = df_dia.iloc[-1]
    
    # KPIs
    vol, peso = calculate_inventory(Z, ultimo_registro['Hum_Int'])
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Masa Harina", f"{peso:,.1f} Ton")
    c2.metric("Temp Ext", f"{ultimo_registro['Temp_Ext']} °C")
    c3.metric("Hum Int", f"{ultimo_registro['Hum_Int']} %")
    c4.metric("CO2", f"{ultimo_registro['CO2']} ppm")

    # Visualizaciones
    t1, t2 = st.tabs(["📈 Histórico del Día", "🏔️ Vista LiDAR 3D"])
    with t1:
        st.plotly_chart(plot_comparative_trends(df_dia), use_container_width=True)
    with t2:
        st.plotly_chart(plot_3d_lidar(X, Y, Z), use_container_width=True)
else:
    st.error("No hay datos para la fecha seleccionada.")
