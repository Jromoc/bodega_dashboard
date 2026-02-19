import numpy as np
import streamlit as st

@st.cache_data
def generate_lidar_data(resolution=50):
    x = np.linspace(0, 100, resolution)
    y = np.linspace(0, 100, resolution)
    X, Y = np.meshgrid(x, y)
    Z = (np.exp(-((X-30)**2 + (Y-30)**2)/400) * 12 + 
         np.exp(-((X-70)**2 + (Y-80)**2)/500) * 8 +
         np.random.normal(0, 0.1, X.shape)) 
    Z = np.clip(Z, 0, 15)
    return X, Y, Z

def get_spatial_grid(base_value, variation=2):
    """Convierte un valor único del CSV en una malla de 10x10 con variaciones locales."""
    return base_value + np.random.uniform(-variation, variation, (10, 10))
