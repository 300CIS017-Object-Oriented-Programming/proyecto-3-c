# main.py

import streamlit as st
import pandas as pd
import os
import re
from io import BytesIO
from login import login, logout, register  # Supongamos que estas funciones existen
from file_handler import cargar_archivo, listar_archivos  # Supongamos que estas funciones existen
from data_filter import buscar_programas
from data_processor import procesar_datos  # Supongamos que esta función existe
from data_visualization import graficar_datos  # Supongamos que esta función existe
from utils import aplicar_estilos

aplicar_estilos()

# Título de la Aplicación
st.title("Sistema de Visualización y Consolidación de Datos SNIES")


def to_excel(df):
    #Convierte un DataFrame a un archivo Excel en memoria.
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    processed_data = output.getvalue()
    return processed_data


def listar_archivos_por_anio(anio_inicio, anio_fin):
    #Lista archivos en el rango de años especificado.
    input_dir = "docs/inputs"
    archivos = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
    archivos_relevantes = []

    st.write(f"Archivos encontrados en {input_dir}: {archivos}")

    pattern = re.compile(r'(\d{4})')  # Buscar patrones de 4 dígitos que representan el año
    for archivo in archivos:
        match = pattern.search(archivo)
        if match:
            year = int(match.group(0))
            if anio_inicio <= year <= anio_fin:
                archivos_relevantes.append(os.path.join(input_dir, archivo))

    st.write(f"Archivos relevantes entre {anio_inicio} y {anio_fin}: {archivos_relevantes}")
    return archivos_relevantes


if 'user' not in st.session_state:
    # Botones para iniciar sesión o registrarse
    option = st.sidebar.selectbox("Seleccione una opción", ["Iniciar Sesión", "Registrarse"])
    if option == "Iniciar Sesión":
        user = login()
    else:
        user = register()

    if user:
        st.session_state['user'] = user
else:
    st.write(f"Bienvenido, {st.session_state['user']['email']}")
    logout()

    # Apartado de Carga de Información
    st.subheader("Carga de Información")
    input_files = listar_archivos()

    st.write(f"Archivos disponibles ({len(input_files)} archivos):")
    st.write(input_files)

    uploaded_file = st.file_uploader("Cargar nuevo archivo", type="xlsx")
    if uploaded_file:
        try:
            cargar_archivo(uploaded_file)
            st.success(f"Archivo {uploaded_file.name} cargado exitosamente")
        except PermissionError as e:
            st.error(f"Error de permisos al cargar el archivo: {e}")
        except Exception as e:
            st.error(f"Error al cargar el archivo: {e}")

    # Pestañas para manejar los pasos de selección y filtrado
    tab1, tab2 = st.tabs(["Filtrar por Años y Programas", "Procesar y Visualizar Datos"])

    with tab1:
        st.header("Paso I: Filtrar por Años y Programas")

        # Entradas para especificar el rango de años
        anio_inicio = st.number_input("Ingrese año inicio", min_value=2000, max_value=2025, value=2021)
        anio_fin = st.number_input("Ingrese año fin", min_value=2000, max_value=2025, value=2023)

        # Botón para buscar y filtrar los archivos por año
        if st.button("Buscar Archivos por Año"):
            try:
                archivos_filtrados = listar_archivos_por_anio(anio_inicio, anio_fin)
                st.write(f"Archivos filtrados para el rango de años {anio_inicio} - {anio_fin}:")
                st.write(archivos_filtrados)
                if not archivos_filtrados:
                    st.warning("No se encontraron archivos en el rango de años especificado.")
                else:
                    st.session_state[
                        'archivos_filtrados'] = archivos_filtrados  # Guardar archivos filtrados en session_state
            except Exception as e:
                st.error(f"Error al listar archivos: {e}")

        # Entrada para palabra clave del programa académico
        if 'archivos_filtrados' in st.session_state:
            keyword = st.text_input("Ingrese palabra(s) clave para buscar programas académicos")
            # Botón para buscar programas
            if st.button("Buscar Programas"):
                if keyword:
                    try:
                        programas = buscar_programas(keyword, st.session_state['archivos_filtrados'])
                        if programas:
                            st.write(f"Programas encontrados ({len(programas)}):")
                            st.session_state['programas'] = programas
                            st.dataframe(pd.DataFrame(programas))
                        else:
                            st.write("No se encontraron programas con el término buscado.")
                    except Exception as e:
                        st.error(f"Error al buscar programas: {e}")
                else:
                    st.warning("Por favor, ingrese una palabra clave para buscar programas.")
        else:
            st.warning("Primero filtre los archivos por año.")

    with tab2:
        st.header("Procesar y Visualizar Datos")
        if 'programas' in st.session_state:
            programas_df = pd.DataFrame(st.session_state['programas'])
            selected_programs = st.multiselect("Seleccione programas para el análisis", programas_df.to_dict('records'),
                                               format_func=lambda x: f"{x['PROGRAMA ACADÉMICO']} - {x['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)']}")
            st.session_state['selected_programs'] = selected_programs

            if st.button("Procesar Datos"):
                try:
                    if 'archivos_filtrados' in st.session_state and st.session_state['selected_programs']:
                        programas_seleccionados = [p['PROGRAMA ACADÉMICO'] for p in
                                                   st.session_state['selected_programs']]
                        resultados = procesar_datos(st.session_state['archivos_filtrados'], programas_seleccionados,
                                                    anio_inicio, anio_fin)

                        df_resultados = pd.DataFrame(resultados)
                        st.write("Resultados del análisis:")
                        st.dataframe(df_resultados)

                        st.subheader("Descargar resultados")
                        st.download_button(
                            label="Descargar Excel",
                            data=to_excel(df_resultados),
                            file_name='resultados.xlsx'
                        )

                        st.download_button(
                            label="Descargar JSON",
                            data=df_resultados.to_json(orient='records'),
                            file_name='resultados.json',
                            mime='application/json'
                        )

                        st.download_button(
                            label="Descargar CSV",
                            data=df_resultados.to_csv(index=False).encode('utf-8'),
                            file_name='resultados.csv'
                        )

                        st.subheader("Visualización de Información")
                        graficar_datos(resultados)
                    else:
                        st.warning("No hay programas seleccionados o archivos filtrados para el análisis.")
                except Exception as e:
                    st.error(f"Error al procesar los datos: {e}")
        else:
            st.warning("No hay programas cargados. Por favor, busque programas en el Paso I.")