import numpy as np

def calculate_inventory(Z, hum_grid):
    # Área total 100x100m dividido entre el número de puntos
    pixel_area = (100 * 100) / Z.size
    volumen_total = np.sum(Z) * pixel_area
    
    # Densidad base harina ~550 kg/m3. 
    # Ajuste: +0.8% de peso por cada 1% de humedad arriba de 40%
    hum_avg = hum_grid.mean()
    densidad_ajustada = 550 * (1 + (max(0, hum_avg - 40) * 0.008))
    
    peso_toneladas = (volumen_total * densidad_ajustada) / 1000
    return volumen_total, peso_toneladas, densidad_ajustada
