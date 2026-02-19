import streamlit as st
import pandas as pd
from simulation import generate_lidar_data
from logic import calculate_inventory
from visuals import plot_comparative_trends, plot_3d_lidar # <-- Esto debe coincidir

st.set_page_config(layout="wide", page_title="Bodega Monterrey Feb")

@st.cache_data
def load_data():
    # Asegúrate de que este archivo también esté subido a GitHub
    df = pd.read_csv("inventario_semana.csv")
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'])
    return df

try:
    df = load_data()
    st.title("🌡️ Control de Bodega - Monterrey (Febrero)")

    fecha_seleccionada = st.sidebar.date_input("Selecciona el día", df['Fecha_Hora'].min())
    df_dia = df[df['Fecha_Hora'].dt.date == fecha_seleccionada]

    if not df_dia.empty:
        X, Y, Z = generate_lidar_data()
        ultimo = df_dia.iloc[-1]
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Temp Exterior", f"{ultimo['Temp_Ext']} °C")
        col2.metric("Hum Interior", f"{ultimo['Hum_Int']} %")
        col3.metric("CO2", f"{ultimo['CO2']} ppm")

        t1, t2 = st.tabs(["📈 Gráfico Comparativo", "🏔️ Mapa 3D LiDAR"])
        with t1:
            st.plotly_chart(plot_comparative_trends(df_dia), use_container_width=True)
        with t2:
            st.plotly_chart(plot_3d_lidar(X, Y, Z), use_container_width=True)
except Exception as e:
    st.error(f"Error al cargar datos: ¿Subiste el archivo inventario_semana.csv?")
