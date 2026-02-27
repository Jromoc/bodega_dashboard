# simulation.py
import numpy as np
import config

def obtener_datos_completos():
    """
    Simula una lectura integral de sensores: Temperatura, Humedad y Elevación (LiDAR).
    """
    size = config.RESOLUCION_GRID
    
    # 1. Simulación de Temperatura (20°C a 35°C)
    temp_data = np.random.uniform(20, 35, (size, size))
    
    # 2. Simulación de Humedad (30% a 65%)
    hum_data = np.random.uniform(30, 65, (size, size))
    
    # 3. Simulación de Elevación LiDAR (Z)
    # Creamos "montañas" de harina usando una función senoidal + ruido
    x = np.linspace(0, 5, size)
    y = np.linspace(0, 5, size)
    X, Y = np.meshgrid(x, y)
    # Altura base entre 0 y 5 metros con variaciones
    z_data = (np.sin(X) + np.cos(Y) + 2) + np.random.normal(0, 0.1, (size, size))
    
    # --- REGLA DE ORO: La Zona de Tolvas (Metros 50-60) ---
    # En el canal central no puede haber producto acumulado (es un ducto)
    canal = config.TOLVA_EJE_X
    temp_data[:, canal] = 0
    hum_data[:, canal] = 0
    z_data[:, canal] = 0  # El sensor LiDAR ve el fondo del ducto
    
    return {
        "temperatura": temp_data,
        "humedad": hum_data,
        "elevacion": z_data
    }

def simular_paso_tiempo(datos_actuales):
    """
    Simula que pasa el tiempo: los puntos calientes tienden a subir de temperatura.
    """
    # Aumentamos ligeramente la temperatura en zonas que ya están sobre el umbral
    datos_actuales["temperatura"] += (datos_actuales["temperatura"] > config.UMBRAL_TEMP_CRITICA) * 0.5
    return datos_actuales
