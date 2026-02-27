# logic.py
import robotics

def generar_estrategia(data):
    instrucciones = []
    temp_grid = data['temperatura']
    # Buscar puntos calientes
    indices = [(r,c) for r in range(10) for c in range(10) if temp_grid[r,c] > 30]
    for r, c in indices:
        instrucciones.append(f"⚠️ Punto caliente en {r},{c}: {robotics.calcular_ruta(r, c)}")
    return instrucciones
