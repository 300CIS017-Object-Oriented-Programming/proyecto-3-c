import streamlit as st
import pandas as pd
import plotly.express as px


def graficar_tendencias_historicas(data):
    st.write("### Tendencias Históricas")
    programas = st.multiselect("Seleccionar Programas", options=data['Archivo'].unique(),
                               default=data['Archivo'].unique())

    if programas:
        df_filtrado = data[data['Archivo'].isin(programas)]

        # Gráficos de líneas
        fig_line = px.line(df_filtrado, x='Año',
                           y=['Inscripción', 'Admisión', 'Nuevos Matriculados', 'Matrícula Total', 'Graduación'],
                           color='Programa', title="Tendencias Históricas por Año")
        fig_line.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
        st.plotly_chart(fig_line)

        # Gráficos de barras
        fig_bar = px.bar(df_filtrado, x='Año',
                         y=['Inscripción', 'Admisión', 'Nuevos Matriculados', 'Matrícula Total', 'Graduación'],
                         color='Programa', barmode='group', title="Distribución por Año")
        fig_bar.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
        st.plotly_chart(fig_bar)
    else:
        st.write("Por favor, selecciona al menos un programa.")


def graficar_comparativos(data):
    st.write("### Gráficos Comparativos Entre Programas")

    # Comparativo Virtual y Presencial
    fig_vp = px.bar(data, x='Programa',
                    y=['Inscritos', 'Admitidos', 'Nuevos Matriculados', 'Matriculados', 'Graduados'], color='Categoría',
                    barmode='group', title="Comparativo Virtual/Presencial")
    st.plotly_chart(fig_vp)

    # Comparativo por Género
    fig_genero = px.bar(data, x='Programa',
                        y=['Inscritos', 'Admitidos', 'Nuevos Matriculados', 'Matriculados', 'Graduados'],
                        color='Género', barmode='group', title="Comparativo por Género")
    st.plotly_chart(fig_genero)

    # Comparativo por Nivel de Formación
    fig_nivel = px.bar(data, x='Programa',
                       y=['Inscritos', 'Admitidos', 'Nuevos Matriculados', 'Matriculados', 'Graduados'],
                       color='Nivel de formación', barmode='group', title="Comparativo por Nivel de Formación")
    st.plotly_chart(fig_nivel)
