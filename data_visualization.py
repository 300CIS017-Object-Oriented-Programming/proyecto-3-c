# data_visualization.py
import plotly.express as px
import streamlit as st


def graficar_datos(resultados):
    if resultados.empty:
        st.write("No hay datos para mostrar")
        return

    # Gráfico de barras para admitidos
    fig = px.bar(resultados, x="Año", y="Admitidos", color="Programa", barmode="group")
    st.plotly_chart(fig)

    # Gráfico de líneas para inscritos
    fig = px.line(resultados, x="Año", y="Inscritos", color="Programa")
    st.plotly_chart(fig)