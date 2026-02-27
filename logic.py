# logic.py
import robotics

def generar_estrategia(grid_data):
    instrucciones = []
    # Buscamos puntos calientes (temperatura > 30)
    indices_criticos = [(r,c) for r in range(10) for c in range(10) if grid_data[r,c] > 30]
    
    for r, c in indices_criticos:
        if c == robotics.TOLVA_COLUMN:
            instrucciones.append(f"✅ Montículo en {r},{c} en zona de descarga.")
        else:
            # Llamamos al motor de robótica
            ruta = robotics.calcular_ruta_paso_a_paso((r, c), grid_data)
            instrucciones.append(f"🤖 Mover M{r}{c} desde ({r},{c}). Ruta: {ruta}")
            
    return instrucciones
