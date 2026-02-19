import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_monterrey_february_data():
    start_date = datetime(2026, 2, 1)
    rows = []
    
    for i in range(168): # 7 días x 24 horas
        current_time = start_date + timedelta(hours=i)
        hour = current_time.hour
        
        # Simulación Clima Monterrey (Febrero)
        # Ciclo circadiano: más frío a las 6 AM, más calor a las 4 PM
        temp_ext = 15 + 8 * np.sin((hour - 10) * np.pi / 12) + np.random.normal(0, 1)
        hum_ext = 40 - 10 * np.sin((hour - 10) * np.pi / 12) + np.random.normal(0, 2)
        
        # Interior de la Bodega (Inercia térmica: varía menos que el exterior)
        temp_int = temp_ext * 0.7 + 5 + np.random.normal(0, 0.3)
        hum_int = hum_ext * 0.8 + 10 + np.random.normal(0, 0.5)
        co2_int = 400 + (np.sin(i/5) * 20) + np.random.normal(10, 2)
        
        rows.append({
            "Fecha_Hora": current_time,
            "Temp_Ext": round(temp_ext, 2),
            "Hum_Ext": round(hum_ext, 2),
            "Temp_Int": round(temp_int, 2),
            "Hum_Int": round(hum_int, 2),
            "CO2": round(co2_int, 2)
        })
    
    df = pd.DataFrame(rows)
    df.to_csv("inventario_semana.csv", index=False)
    print("✅ Archivo 'inventario_semana.csv' generado con éxito.")

if __name__ == "__main__":
    generate_monterrey_february_data()
