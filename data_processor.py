import pandas as pd


def procesar_datos(archivos, programa_academico, anio_inicio, anio_fin):
    """
    Procesa los datos para contar estudiantes por estado y metodología.

    Parameters:
    archivos : list
        Lista de archivos a procesar.
    programa_academico : str
        Nombre del programa académico a filtrar.
    anio_inicio : int
        Año de inicio del filtro.
    anio_fin : int
        Año de fin del filtro.

    Returns:
    pd.DataFrame
        DataFrame con los resultados del procesamiento.
    """
    resultados = []

    for archivo in archivos:
        df = pd.read_excel(archivo)

        # Filtrar por año
        df = df[df['AÑO'].between(anio_inicio, anio_fin)]

        # Filtrar por programa académico
        df_programa = df[df['PROGRAMA ACADÉMICO'].str.contains(programa_academico, case=False, na=False)]

        for index, row in df_programa.iterrows():
            universidad = row['UNIVERSIDAD']
            año = row['AÑO']
            metodologia = row['METODOLOGÍA']
            estado = row['ESTADO']

            resultados.append({
                'Universidad': universidad,
                'Año': año,
                'Metodología': metodologia,
                'Estado': estado,
                'Cantidad': 1
            })

    # Crear DataFrame desde la lista de resultados
    df_resultados = pd.DataFrame(resultados)

    # Agrupar y contar por Universidad, Año, Metodología y Estado
    df_agrupado = df_resultados.groupby(['Universidad', 'Año', 'Metodología', 'Estado']).sum().reset_index()

    return df_agrupado