# Actualización de robotics.py
import config

def encontrar_espacio_libre_adyacente(r, c, grid_data):
    """Busca una celda cercana con poca harina para mover un obstáculo."""
    # Direcciones posibles: arriba o abajo (para no interferir con el eje X hacia la tolva)
    posibles = [(r-1, c), (r+1, c)]
    for pr, pc in posibles:
        if 0 <= pr < config.RESOLUCION_GRID:
            if grid_data[pr, pc] < 1.0: # Si hay menos de 1m de harina
                return (pr, pc)
    return None

def planificar_empuje(pos_objetivo, grid_data):
    """
    Si el camino a la tolva está bloqueado, genera la orden 
    de mover el obstáculo antes de proceder.
    """
    r, c = pos_objetivo
    instrucciones_limpieza = []
    
    # Si la celda en el camino tiene mucha harina (obstáculo)
    if grid_data[r, c] > 2.0:
        espacio_libre = encontrar_espacio_libre_adyacente(r, c, grid_data)
        if espacio_libre:
            instrucciones_limpieza.append({
                "accion": "DESPEJAR",
                "de": (r, c),
                "a": espacio_libre,
                "motivo": "Liberar acceso a tolva central"
            })
    return instrucciones_limpieza
