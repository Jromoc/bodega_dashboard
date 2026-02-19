import streamlit as st
import pandas as pd
from simulation import generate_lidar_data, get_spatial_grid
from logic import calculate_inventory
from visuals import plot_3d_thermal_lidar, plot_2d_grid, plot_comparative_trends

st.set_page_config(layout="wide", page_title="Bodega Monterrey MVP")

@st.cache_data
def load_data():
    df = pd.read_csv("inventario_semana.csv")
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'])
    return df

try:
    df = load_data()
    st.sidebar.header("Configuración de Vista")
    fecha_sel = st.sidebar.date_input("Día de análisis", df['Fecha_Hora'].min())
    sensor_map = st.sidebar.selectbox("Variable en Grid", ["Temperatura", "Humedad", "CO2"])

    df_dia = df[df['Fecha_Hora'].dt.date == fecha_sel]

    if not df_dia.empty:
        ultimo = df_dia.iloc[-1]
        X, Y, Z = generate_lidar_data()
        
        # Generar Grids espaciales basados en el valor promedio del historial
        grid_temp = get_spatial_grid(ultimo['Temp_Int'], 3)
        grid_hum = get_spatial_grid(ultimo['Hum_Int'], 5)
        grid_co2 = get_spatial_grid(ultimo['CO2'], 20)

        # Tabs
        tab1, tab2, tab3 = st.tabs(["🗺️ Vista de Sectores (Grid)", "🏔️ Análisis 3D Térmico", "📈 Tendencias"])

        with tab1:
            data_sel = {"Temperatura": grid_temp, "Humedad": grid_hum, "CO2": grid_co2}[sensor_map]
            st.plotly_chart(plot_2d_grid(data_sel, f"Distribución Espacial: {sensor_map}"), use_container_width=True)

        with tab2:
            st.plotly_chart(plot_3d_thermal_lidar(X, Y, Z, grid_temp), use_container_width=True)
            st.info("La altura representa el volumen (LiDAR) y el color la temperatura (Verde: Frío, Rojo: Calor).")

        with tab3:
            st.plotly_chart(plot_comparative_trends(df_dia), use_container_width=True)

except Exception as e:
    st.error(f"Error: {e}")
    
# ... (imports anteriores)
from logic import get_dispatch_strategy
from visuals import plot_strategy_grid

# ... (dentro del bloque principal de app.py)

# 1. Calculamos la estrategia primero
# Nota: Para Z_grid necesitamos promediar el Z del LiDAR (50x50) a 10x10
Z_grid = Z.reshape(10, 5, 10, 5).mean(axis=(1, 3)) 
estrategia = get_dispatch_strategy(grid_temp, grid_hum, Z_grid)

# 2. Agregamos la pestaña
tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Sectores", "🏔️ 3D Térmico", "📈 Tendencias", "🚛 Estrategia de Salida"])

with tab4:
    st.subheader("Planificación de Despacho Sugerida")
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.plotly_chart(plot_strategy_grid(estrategia), use_container_width=True)
    
    with col_b:
        st.write("📋 **Sectores con Criterio de Salida:**")
        # Listamos los sectores que cumplen el criterio para el usuario
        for r in range(10):
            for c in range(10):
                if estrategia[r, c] != "ALMACENAR":
                    st.warning(f"Sector [{r+1}, {c+1}]: {estrategia[r, c]}")

    st.info("""
    **Criterios de Salida:**
    1. **Temperatura > 25°C:** Riesgo de degradación de harina.
    2. **Humedad > 50%:** Riesgo de apelmazamiento.
    3. **Altura > 10m:** Rotación de inventario por volumen acumulado.
    """)

