import numpy as np

def calculate_inventory(Z, hum_int):
    pixel_area = (100 * 100) / Z.size
    volumen_total = np.sum(Z) * pixel_area
    # La harina es higroscópica: absorbe humedad ambiente
    densidad_base = 550 
    ajuste_humedad = (hum_int - 45) * 0.5 # Aumenta peso si hay más humedad
    peso_toneladas = (volumen_total * (densidad_base + ajuste_humedad)) / 1000
    return volumen_total, peso_toneladas
