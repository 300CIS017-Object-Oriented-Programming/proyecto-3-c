# data_processor.py
import pandas as pd
import re


def procesar_datos(uploaded_files, programa_academico):
    resultados = []

    for uploaded_file in uploaded_files:
        # Leer el archivo Excel
        df = pd.read_excel(uploaded_file)

        # Filtrar por el programa académico seleccionado
        df_programa = df[df['PROGRAMA ACADÉMICO'].str.contains(programa_academico, case=False, na=False)]

        # Extraer el año del nombre del archivo
        year_match = re.search(r'\d{4}', uploaded_file.name)
        if year_match:
            year = year_match.group(0)
        else:
            year = 'Unknown'

        # Agregar la columna del año
        df_programa['AÑO'] = year

        # Contar el número de estudiantes por universidad, metodología y año
        conteo = df_programa.groupby(
            ['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)', 'METODOLOGÍA', 'AÑO']).size().reset_index(name='Cantidad')
        if uploaded_file.name == f"admitidos{year}.xlsx":
            conteo['Archivo'] = f"Admitido"
            resultados.append(conteo)
        elif uploaded_file.name == f"matriculadosPrimerCurso{year}.xlsx":
            conteo['Archivo'] = f"Neos"
            resultados.append(conteo)
        elif uploaded_file.name == f"graduados{year}.xlsx":
            conteo['Archivo'] = f"Graduado"
            resultados.append(conteo)
        elif uploaded_file.name == f"matriculados{year}.xlsx":
            conteo['Archivo'] = f"Matriculado"
            resultados.append(conteo)
        elif uploaded_file.name == f"inscritos{year}.xlsx":
            conteo['Archivo'] = f"Inscrito"
            resultados.append(conteo)
        resultados.append(conteo)

    # Concatenar los resultados de todos los archivos
    df_resultados = pd.concat(resultados, ignore_index=True)

    # Crear una lista para almacenar los DataFrames separados por modalidad
    modalidades = df_resultados['METODOLOGÍA'].unique()
    tablas_modalidades = []

    for modalidad in modalidades:
        df_modalidad = df_resultados[df_resultados['METODOLOGÍA'] == modalidad]
        df_pivot = df_modalidad.pivot_table(index=['INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)'],
                                            columns=['AÑO', 'Archivo'], values='Cantidad', fill_value=0)

        # Crear una fila con el nombre de la modalidad
        fila_modalidad = pd.DataFrame({col: [modalidad] for col in df_pivot.columns}, index=[f'{modalidad}'])

        # Concatenar la fila de la modalidad con el DataFrame pivotado
        df_pivot = pd.concat([fila_modalidad, df_pivot])

        tablas_modalidades.append(df_pivot)

    # Concatenar todas las tablas de modalidades en una sola
    df_final = pd.concat(tablas_modalidades)

    return df_final