import streamlit as st
import pandas as pd
import numpy as np

from simulation import generate_lidar_data, get_spatial_grid
from logic import calculate_inventory, get_dispatch_strategy
from visuals import plot_3d_thermal_lidar, plot_2d_grid, plot_comparative_trends, plot_strategy_grid


# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

st.set_page_config(layout="wide", page_title="Bodega Monterrey MVP")

SENSOR_MAP = {
    "Temperatura": "temp",
    "Humedad": "hum",
    "CO2": "co2"
}

GRID_PARAMS = {
    "Temperatura": 3,
    "Humedad": 5,
    "CO2": 20
}

DISPATCH_CRITERIA = {
    "temperature_threshold": 25,
    "humidity_threshold": 50,
    "height_threshold": 10
}


# ============================================================================
# DATA LOADING
# ============================================================================

@st.cache_data
def load_data():
    """Load and prepare inventory data from CSV."""
    df = pd.read_csv("inventario_semana.csv")
    df['Fecha_Hora'] = pd.to_datetime(df['Fecha_Hora'])
    return df


# ============================================================================
# DATA PROCESSING
# ============================================================================

def prepare_spatial_grids(ultimo):
    """Generate spatial grids for temperature, humidity, and CO2."""
    grid_temp = get_spatial_grid(ultimo['Temp_Int'], GRID_PARAMS["Temperatura"])
    grid_hum = get_spatial_grid(ultimo['Hum_Int'], GRID_PARAMS["Humedad"])
    grid_co2 = get_spatial_grid(ultimo['CO2'], GRID_PARAMS["CO2"])
    
    return grid_temp, grid_hum, grid_co2


def prepare_lidar_grids(Z, grid_temp):
    """Convert LiDAR data to spatial grid format."""
    # Reshape from 50x50 to 10x10 by averaging
    Z_grid = Z.reshape(10, 5, 10, 5).mean(axis=(1, 3))
    return Z_grid


# ============================================================================
# UI RENDERING
# ============================================================================

def render_grid_tab(sensor_map, grid_temp, grid_hum, grid_co2):
    """Render the 2D Grid sector view tab."""
    with st.container():
        data_sel = {
            "Temperatura": grid_temp,
            "Humedad": grid_hum,
            "CO2": grid_co2
        }[sensor_map]
        
        st.plotly_chart(
            plot_2d_grid(data_sel, f"Distribución Espacial: {sensor_map}"),
            use_container_width=True
        )


def render_3d_thermal_tab(X, Y, Z, grid_temp):
    """Render the 3D Thermal LiDAR analysis tab."""
    with st.container():
        st.plotly_chart(
            plot_3d_thermal_lidar(X, Y, Z, grid_temp),
            use_container_width=True
        )
        st.info(
            "La altura representa el volumen (LiDAR) y el color la temperatura "
            "(Verde: Frío, Rojo: Calor)."
        )


def render_trends_tab(df_dia):
    """Render the comparative trends tab."""
    with st.container():
        st.plotly_chart(
            plot_comparative_trends(df_dia),
            use_container_width=True
        )


def render_dispatch_strategy_tab(estrategia):
    """Render the dispatch strategy tab."""
    with st.container():
        st.subheader("Planificación de Despacho Sugerida")
        
        col_a, col_b = st.columns([2, 1])
        
        with col_a:
            st.plotly_chart(
                plot_strategy_grid(estrategia),
                use_container_width=True
            )
        
        with col_b:
            st.write("📋 **Sectores con Criterio de Salida:**")
            render_dispatch_sectors(estrategia)
        
        st.info(
            """
            **Criterios de Salida:**
            1. **Temperatura > 25°C:** Riesgo de degradación de harina.
            2. **Humedad > 50%:** Riesgo de apelmazamiento.
            3. **Altura > 10m:** Rotación de inventario por volumen acumulado.
            """
        )


def render_dispatch_sectors(estrategia):
    """Display sectors that meet dispatch criteria."""
    for r in range(10):
        for c in range(10):
            if estrategia[r, c] != "ALMACENAR":
                st.warning(f"Sector [{r+1}, {c+1}]: {estrategia[r, c]}")


# ============================================================================
# SIDEBAR CONFIGURATION
# ============================================================================

def render_sidebar(df):
    """Render sidebar configuration controls."""
    st.sidebar.header("Configuración de Vista")
    
    fecha_sel = st.sidebar.date_input(
        "Día de análisis",
        df['Fecha_Hora'].min()
    )
    
    sensor_map = st.sidebar.selectbox(
        "Variable en Grid",
        ["Temperatura", "Humedad", "CO2"]
    )
    
    return fecha_sel, sensor_map


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point."""
    try:
        # Load data
        df = load_data()
        
        # Render sidebar
        fecha_sel, sensor_map = render_sidebar(df)
        
        # Filter data by selected date
        df_dia = df[df['Fecha_Hora'].dt.date == fecha_sel]
        
        if df_dia.empty:
            st.warning("No hay datos disponibles para la fecha seleccionada.")
            return
        
        # Get latest record
        ultimo = df_dia.iloc[-1]
        
        # Generate LiDAR and spatial grids
        X, Y, Z = generate_lidar_data()
        grid_temp, grid_hum, grid_co2 = prepare_spatial_grids(ultimo)
        Z_grid = prepare_lidar_grids(Z, grid_temp)
        
        # Calculate dispatch strategy
        estrategia = get_dispatch_strategy(grid_temp, grid_hum, Z_grid)
        
        # Create tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            ["🗺️ Vista de Sectores (Grid)", "🏔️ Análisis 3D Térmico", "📈 Tendencias", "🚛 Estrategia de Salida"]
        )
        
        # Render tab content
        with tab1:
            render_grid_tab(sensor_map, grid_temp, grid_hum, grid_co2)
        
        with tab2:
            render_3d_thermal_tab(X, Y, Z, grid_temp)
        
        with tab3:
            render_trends_tab(df_dia)
        
        with tab4:
            render_dispatch_strategy_tab(estrategia)
    
    except Exception as e:
        st.error(f"Error: {e}")
        st.exception(e)


if __name__ == "__main__":
    main()