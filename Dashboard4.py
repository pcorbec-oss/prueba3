import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# -----------------------------------------------------
# CARGA DE DATOS
# -----------------------------------------------------
st.title("Dashboard de Ventas")

st.write("Cargando datos desde el archivo Excel...")

# Asegúrate de que este archivo exista
df = pd.read_excel("D:/Power BI + AI/Informe_Ventas.xlsx", engine='openpyxl')

st.success("Datos cargados correctamente.")

# Convertir fecha
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# Filtrar datos
df = df[(df['UnitPrice'] > 0) & (df['Quantity'] > 0)]

# Crear columna con el mes
df['Mes'] = df['InvoiceDate'].dt.to_period('M')

# -----------------------------------------------------
# ANÁLISIS
# -----------------------------------------------------
# 1️⃣ Evolución de ventas por mes
ventas_mensuales = df.groupby('Mes').apply(lambda x: (x['Quantity'] * x['UnitPrice']).sum())
ventas_mensuales.index = ventas_mensuales.index.to_timestamp()

# 2️⃣ Top 10 productos más vendidos
top_productos = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

# 3️⃣ Distribución de precios unitarios
precios = df['UnitPrice']

# -----------------------------------------------------
# VISUALIZACIÓN
# -----------------------------------------------------
st.header("Evolución de Ventas por Mes")
fig1, ax1 = plt.subplots()
ventas_mensuales.plot(kind='line', marker='o', ax=ax1)
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
st.pyplot(fig1)

st.header("Top 10 Productos Más Vendidos")
fig2, ax2 = plt.subplots()
top_productos.plot(kind='barh', color='skyblue', ax=ax2)
ax2.invert_yaxis()
plt.xlabel('Cantidad Vendida')
st.pyplot(fig2)

st.header("Distribución de Precios Unitarios")
fig3, ax3 = plt.subplots()
sns.histplot(precios, bins=50, kde=True, color='salmon', ax=ax3)
plt.xlabel('Precio Unitario')
plt.ylabel('Frecuencia')
st.pyplot(fig3)


