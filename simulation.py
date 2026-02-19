import numpy as np
import streamlit as st

@st.cache_data
def generate_lidar_data(resolution=50):
    x = np.linspace(0, 100, resolution)
    y = np.linspace(0, 100, resolution)
    X, Y = np.meshgrid(x, y)
    
    # Simulación de cerros de harina
    Z = (np.exp(-((X-30)**2 + (Y-30)**2)/400) * 12 + 
         np.exp(-((X-70)**2 + (Y-80)**2)/500) * 8 +
         np.random.normal(0, 0.1, X.shape)) 
    Z = np.clip(Z, 0, 15)
    return X, Y, Z

def get_sensor_grid(t_step):
    np.random.seed(t_step)
    temp = 20 + np.random.normal(5, 2, (10, 10)) + np.sin(t_step/10) * 5
    hum = 40 + np.random.normal(5, 5, (10, 10))
    co2 = 400 + np.random.normal(100, 20, (10, 10))
    return temp, hum, co2
