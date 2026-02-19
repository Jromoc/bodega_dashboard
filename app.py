import streamlit as st
from simulation import generate_lidar_data, get_sensor_grid
from logic import calculate_inventory
from visuals import plot_2d_heatmap, plot_3d_lidar

st.set_page_config(layout="wide", page_title="Bodega 4.0")

# --- LÓGICA DE INTERFAZ ---
st.title("🏗️ Dashboard de Bodega Plana (MVP)")

# Sidebar
t_step = st.sidebar.slider("Línea de Tiempo (min)", 0, 60, 0)
sensor_type = st.sidebar.selectbox("Capa de Sensor", ["Temperatura", "Humedad", "CO2"])

# Procesamiento
X, Y, Z = generate_lidar_data()
temp, hum, co2 = get_sensor_grid(t_step)
vol, peso, dens = calculate_inventory(Z, hum)

# KPIs
c1, c2, c3 = st.columns(3)
c1.metric("Volumen", f"{vol:,.1f} m³")
c2.metric("Masa Est.", f"{peso:,.1f} Ton")
c3.metric("Densidad Prom.", f"{dens:.1f} kg/m³")

# Tabs de Visualización
tab1, tab2 = st.tabs(["📍 Mapa de Sensores", "☁️ Nube LiDAR 3D"])

with tab1:
    data_map = {"Temperatura": temp, "Humedad": hum, "CO2": co2}[sensor_type]
    st.plotly_chart(plot_2d_heatmap(data_map, f"Distribución de {sensor_type}"), use_container_width=True)

with tab2:
    st.plotly_chart(plot_3d_lidar(X, Y, Z), use_container_width=True)

# Sección de IA (Placeholder)
st.divider()
st.subheader("🤖 Consultas Inteligentes")
if st.text_input("Pregunta al asistente sobre el estado de la bodega:"):
    st.write("**Respuesta simulada:** Basado en la humedad y CO2, el riesgo de fermentación es bajo en el sector norte.")
