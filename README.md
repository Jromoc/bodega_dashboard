# 🚀 Smart Grain Storage: 3D Monitoring & Autonomous Logistics (MVP)

Este proyecto representa una solución de **Bodega 4.0** diseñada para la gestión automatizada de almacenamiento de granos y harinas en instalaciones de gran escala (**100m x 100m**). El sistema integra monitoreo térmico, humedad y relieve **LiDAR** para ejecutar estrategias de extracción inteligente mediante robots terrestres.

---
## 🎯 Resumen Ejecutivo

Este proyecto soluciona uno de los retos más críticos en la industria de almacenamiento de granos: la **gestión de riesgos y la eficiencia operativa en bodegas de gran escala**.

### Propósito
El objetivo principal es transformar una bodega convencional en un **Centro Logístico Autónomo**. A través de la digitalización, buscamos maximizar la rentabilidad mediante dos pilares:
* **Preservación de Activos:** Mitigar mermas por deterioro térmico o humedad mediante monitoreo en tiempo real.
* **Excelencia Operativa:** Automatizar el flujo de inventario, reduciendo la intervención humana y optimizando los tiempos de despacho hacia el canal de extracción central.

### Funcionamiento
El sistema opera bajo un ciclo cerrado de **Inteligencia Industrial (IoT + AI)**:
1. **Percepción:** Sensores LiDAR y térmicos capturan el estado físico del inventario (Gemelo Digital).
2. **Razonamiento:** El motor lógico analiza el riesgo de degradación y calcula la ruta de extracción óptima.
3. **Acción:** Robots terrestres ejecutan comandos de reconfiguración (Rearrangement Planning), asegurando que el producto prioritario siempre tenga vía libre hacia las tolvas de salida.
---

## 🏗️ Arquitectura del Sistema (Modular)

El software sigue un patrón de diseño profesional, separando las responsabilidades en módulos específicos:

* **`config.py`**: Centraliza parámetros críticos (dimensiones de la bodega, umbrales de temperatura, ubicación de tolvas).
* **`simulation.py`**: Generador de datos sintéticos que emula sensores IoT (Térmicos, Humedad y Nubes de puntos LiDAR).
* **`logic.py`**: Cerebro de negocio que prioriza qué producto debe salir basado en riesgos de degradación.
* **`robotics.py`**: Motor de navegación que calcula rutas hacia la tolva central y gestiona el **Rearrangement Planning** (despeje de obstáculos).
* **`visuals.py`**: Renderizado de gemelos digitales en 3D y mapas de calor interactivos.
* **`app.py`**: Interfaz de usuario construida en Streamlit.

---

## 📐 Especificaciones de la Bodega

* **Dimensiones:** 100m x 100m.
* **Grid de Gestión:** 10x10 sectores (cada sector representa 10m²).
* **Zona de Extracción (Tolvas):** Canal central ubicado entre los **metros 50 y 60**. El sistema lo identifica como el "Sumidero Logístico" donde el producto es extraído.
* **Resolución LiDAR:** Datos procesados en una malla de 50x50 para una reconstrucción precisa del relieve.

---

## 🔬 Fundamentos Matemáticos y Estrategia

### 1. Planificación de Movimiento (Sokoban Logic)
Cuando un montículo crítico está bloqueado, el robot aplica una lógica de **reconfiguración**. No solo evita obstáculos, sino que planea cómo mover el producto bloqueador a una celda adyacente para liberar la ruta hacia la tolva.



### 2. Algoritmo de Aplanado (Flattening)
Para optimizar el espacio y facilitar el tránsito robótico, el sistema propone un suavizado de la superficie mediante **Suavizado Laplaciano**, calculando la altura ideal como el promedio de los sectores vecinos:
$$Z_{nuevo} = \frac{1}{n} \sum_{i=1}^{n} Z_{vecino, i}$$

### 3. Interpolación Térmica
Mapeo de datos dispersos (sensores cada 10m) a una malla densa (LiDAR cada 2m) utilizando `RegularGridInterpolator` para predecir puntos calientes internos.

---

## 🛠️ Tecnologías

* **Python 3.10+**
* **Streamlit** (Dashboard UI)
* **Plotly** (Visualización 3D Interactiva)
* **NumPy & SciPy** (Cálculo matricial y espacial)
* **Pandas** (Estructura de datos)

---

## 🚀 Instalación y Ejecución

1.  **Clonar repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/smart-grain-storage.git](https://github.com/tu-usuario/smart-grain-storage.git)
    cd smart-grain-storage
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install streamlit plotly scipy pandas numpy
    ```
3.  **Correr aplicación:**
    ```bash
    streamlit run app.py
    ```

---

> **Visión Estratégica:** Este MVP demuestra cómo la integración de hardware (sensores) y software (algoritmos de optimización) puede reducir pérdidas post-cosecha y maximizar la eficiencia operativa en la cadena de suministro agroindustrial.
