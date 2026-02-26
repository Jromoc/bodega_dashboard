# 🚀 Smart Grain Storage: 3D Monitoring & Autonomous Logistics

Este proyecto es un **Sistema de Gestión de Almacenamiento Inteligente** diseñado para bodegas de harina a gran escala (100m x 100m). El software integra visión 3D por **LiDAR**, monitoreo térmico y un motor de **estrategia de extracción** que optimiza el movimiento robótico hacia las zonas de despacho.

---

## 📐 Especificaciones del Espacio (Digital Twin)

La bodega física se ha digitalizado bajo un modelo de capas para permitir precisión en el relieve y eficiencia en la gestión:

* **Grid de Gestión (10x10):** El área de 100m x 100m se divide en 100 sectores de 10m cada uno. Cada celda es una unidad logística donde se clasifica la harina por "Montículo" (ID: M1, M2...).
* **Densidad de Datos LiDAR (50x50):** Los datos de elevación tienen una resolución de 2 metros por punto, permitiendo una reconstrucción fiel del relieve de la harina.
* **Zona de Extracción (Tolvas):** El canal central, ubicado entre los **metros 50 y 60** (eje X), está reservado para los ductos de extracción. El algoritmo identifica esta zona como el "Sumidero" o destino final de todo movimiento de producto.

---

## 🔬 Fundamentos Matemáticos y Algorítmicos

### 1. Interpolación de Grilla Regular
Para visualizar la temperatura sobre la superficie irregular del grano, utilizamos `RegularGridInterpolator` (SciPy). 
* **El Desafío:** Los sensores térmicos están en una malla de 10x10, pero el relieve LiDAR es de 50x50.
* **La Solución:** Mediante una interpolación bilineal, proyectamos los valores térmicos sobre la densa malla de elevación:
    $$f(x, y) \approx \sum_{i,j} z_{i,j} \cdot L_i(x) \cdot L_j(y)$$



### 2. Estrategia de Movimiento (Pathfinding & Rearrangement)
El sistema genera una hoja de ruta para desplazar el producto hacia el canal de tolvas central.

* **Priorización:** Se analizan variables de Calidad ($T > 25°C$) y Humedad ($H > 50\%$).
* **Lógica de Despeje:** Si un montículo prioritario está bloqueado, el algoritmo aplica **Rearrangement Planning**. Calcula el "costo de empuje" basado en la altura $Z$ y busca la celda vacía más cercana para desplazar el obstáculo temporalmente.
* **Optimización de Ruta:** Basado en el algoritmo **A***, donde la función de decisión es:
    $$f(n) = g(n) + h(n)$$
    *(Donde $g$ es el costo de energía del robot y $h$ la distancia a la tolva central).*



---

## 🤖 Estructura del Código

* `app.py`: Interfaz principal en **Streamlit** con dashboards interactivos.
* `logic.py`: Motor de reglas de negocio y clasificación de montículos por riesgo.
* `visuals.py`: Renderizado 3D con **Plotly** y mapas de calor de estrategia.
* `robotics.py`: Generador de secuencias lógicas para robots terrestres (ej. *"Mover M4 de sector 4D a 4C para liberar vía"*).

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Visualización:** Plotly (3D Surface & Heatmaps)
* **Procesamiento:** NumPy, Pandas, SciPy.
* **UI:** Streamlit.

---

## 🚀 Instalación y Uso

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/smart-grain-storage.git](https://github.com/tu-usuario/smart-grain-storage.git)
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install streamlit plotly scipy pandas numpy
    ```
3.  **Ejecutar la aplicación:**
    ```bash
    streamlit run app.py
    ```

---

> **Nota del Desarrollador:** Este proyecto demuestra la viabilidad de integrar Ciencia de Datos con Operaciones Logísticas Reales, transformando sensores pasivos en sistemas de decisión autónomos.
