# app.py
import streamlit as st
import logic
import visuals
import simulation

st.set_page_config(layout="wide")
st.title("🌾 Smart Grain Storage - Dashboard de Control")

# --- CÓDIGO CORREGIDO ---

# Verifica si 'data' ya existe en la memoria de la sesión
if 'data' not in st.session_state:
    # Si no existe, entonces (y solo entonces) ejecuta la simulación
    st.session_state['data'] = simulation.obtener_datos_sensores()

# A partir de aquí, el resto de tu código usa st.session_state.data sin problemas

col1, col2 = st.columns([2, 1])

with col1:
    fig = visuals.crear_mapa_calor(st.session_state.data)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Control de Robots")
    if st.button("Calcular Rutas"):
        # Esto ahora llama a la lógica que usa robotics.py
        instrucciones = logic.generar_estrategia(st.session_state.data)
        for instr in instrucciones:
            st.code(instr) # Mostramos la ruta como código
            
    if st.button("Actualizar Sensores"):
        st.session_state.data = simulation.obtener_datos_sensores()
        st.rerun()
