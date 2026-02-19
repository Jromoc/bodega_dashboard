import numpy as np

def calculate_inventory(Z, hum_int):
    pixel_area = (100 * 100) / Z.size
    volumen_total = np.sum(Z) * pixel_area
    # La harina es higroscópica: absorbe humedad ambiente
    densidad_base = 550 
    ajuste_humedad = (hum_int - 45) * 0.5 # Aumenta peso si hay más humedad
    peso_toneladas = (volumen_total * (densidad_base + ajuste_humedad)) / 1000
    return volumen_total, peso_toneladas

def get_dispatch_strategy(grid_temp, grid_hum, Z_grid):
    """
    Analiza cada cuadrante y asigna una acción.
    Criterio: Si Temp > 25°C o Hum > 50% -> SALIDA PRIORITARIA
    """
    rows, cols = grid_temp.shape
    strategy_map = np.empty((rows, cols), dtype=object)
    
    for r in range(rows):
        for c in range(cols):
            # Prioridad por riesgo térmico o de humedad
            if grid_temp[r, c] > 25 or grid_hum[r, c] > 50:
                strategy_map[r, c] = "SALIDA (Riesgo)"
            elif Z_grid[r, c] > 10: # Montículos muy altos (antigüedad supuesta)
                strategy_map[r, c] = "DESPACHO (Stock)"
            else:
                strategy_map[r, c] = "ALMACENAR"
                
    return strategy_map
