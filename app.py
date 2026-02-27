import streamlit as st
import simulation
import visuals
import logic

# 1. Configuración de página
st.set_page_config(layout="wide")
st.title("🌾 Smart Grain Storage - Dashboard")

# 2. INICIALIZACIÓN SEGURA (ELIMINA ERRORES DE ATRIBUTO)
if 'data' not in st.session_state:
    st.session_state['data'] = simulation.obtener_datos_sensores()

# 3. LAYOUT
col1, col2 = st.columns([2, 1])

with col1:
    # Pasamos el diccionario completo, no el atributo
    fig = visuals.crear_mapa_calor(st.session_state['data'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    if st.button("Generar Estrategia"):
        # Usamos ['data'] para acceder a los datos
        instrucciones = logic.generar_estrategia(st.session_state['data'])
        for inst in instrucciones:
            st.success(inst)
            
    if st.button("Actualizar Sensores"):
        st.session_state['data'] = simulation.obtener_datos_sensores()
        st.rerun()
