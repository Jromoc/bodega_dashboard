# simulation.py
import numpy as np
import config

def obtener_datos_sensores():
    size = config.RESOLUCION_GRID
    data = {
        "temperatura": np.random.uniform(20, 35, (size, size)),
        "elevacion": np.random.uniform(0, 5, (size, size))
    }
    # Canal de tolva limpio
    data["temperatura"][:, config.TOLVA_EJE_X] = 0
    data["elevacion"][:, config.TOLVA_EJE_X] = 0
    return data

def simular_paso_tiempo(data):
    """Aumenta la temperatura en zonas críticas para simular degradación."""
    # Incrementa temperatura en 0.5°C si supera el umbral
    mask = data["temperatura"] > config.UMBRAL_TEMP_CRITICA
    data["temperatura"] += mask * 0.5
    return data
