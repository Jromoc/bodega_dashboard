import streamlit as st
import simulation
import visuals
import logic # ¡Aquí está el ingrediente secreto que faltaba!
import robotics

st.set_page_config(layout="wide", page_title="Smart Grain Storage")
st.title("🌾 Smart Grain Storage - Dashboard de Control")

# --- 1. INICIALIZACIÓN SEGURA ---
if 'data' not in st.session_state:
    st.session_state['data'] = simulation.obtener_datos_sensores()

# --- 2. LAYOUT ---
col1, col2 = st.columns([2, 1])

with col1:
    # Usamos la sintaxis ['data'] para evitar errores
    fig = visuals.crear_mapa_calor(st.session_state['data'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Panel de Control")
    
    # BOTÓN 1: Estrategia Lógica
    if st.button("Generar Estrategia"):
        # Aquí es donde usamos el import logic que faltaba
        instrucciones = logic.generar_estrategia(st.session_state['data']['temperatura'])
        for instr in instrucciones:
            st.success(instr)
            
    # BOTÓN 2: Actualizar
    if st.button("Actualizar Sensores"):
        st.session_state['data'] = simulation.obtener_datos_sensores()
        st.rerun()

    st.info("Nota: El sistema utiliza lógica modular para reconfiguración de carga.")
