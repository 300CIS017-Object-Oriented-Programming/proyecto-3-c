# data_filter.py
import pandas as pd
import os


def buscar_programas(keyword, archivos):
    """
    Busca programas que contengan la palabra clave en los archivos proporcionados.
    Args:
    - keyword (str): Palabra clave a buscar.
    - archivos (list): Lista de rutas de archivos a analizar.

    Returns:
    - list: Lista de programas que coinciden con la palabra clave.
    """
    programas_encontrados = []

    for archivo in archivos:
        try:
            df = pd.read_excel(archivo)
            # Asegurémonos de que el DataFrame tiene la columna "PROGRAMA ACADÉMICO"
            if "PROGRAMA ACADÉMICO" in df.columns:
                # Filtrar los programas que contengan la palabra clave
                resultados = df[df["PROGRAMA ACADÉMICO"].str.contains(keyword, case=False, na=False)]
                programas_encontrados.extend(resultados.to_dict('records'))
            else:
                print(f"No se encontró la columna 'PROGRAMA ACADÉMICO' en el archivo {archivo}")
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")

    return programas_encontrados