
import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la aplicación
st.set_page_config(
    page_title="Mi primera aplicación",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Mi primera aplicación con Streamlit")

st.write("Bienvenido a mi primera aplicación web.")

# Menú lateral
st.sidebar.header("Configuración")

cantidad = st.sidebar.slider(
    "Cantidad de datos",
    10, 100, 50
)

# Crear datos de ejemplo
np.random.seed(42)

df = pd.DataFrame({
    "Número": range(1, cantidad + 1),
    "Ventas": np.random.randint(100, 1000, cantidad)
})

# Mostrar indicadores
col1, col2, col3 = st.columns(3)

col1.metric("Total de registros", len(df))

col2.metric(
    "Promedio de ventas",
    round(df["Ventas"].mean(), 2)
)

col3.metric(
    "Venta máxima",
    df["Ventas"].max()
)

# Mostrar gráfico
st.subheader("Gráfico de ventas")

st.line_chart(
    df.set_index("Número")["Ventas"]
)

# Mostrar tabla
st.subheader("Datos registrados")

st.dataframe(df, use_container_width=True)
