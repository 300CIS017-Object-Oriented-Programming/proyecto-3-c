# data_filter.py
import pandas as pd

def obtener_programas_academicos(archivos, anio_inicio, anio_fin):
    """
    Obtiene una lista de programas académicos disponibles en los archivos proporcionados dentro del rango de años especificado.
    Args:
    - archivos (list): Lista de rutas de archivos a analizar.
    - anio_inicio (int): Año de inicio del rango.
    - anio_fin (int): Año de fin del rango.

    Returns:
    - list: Lista de programas académicos disponibles.
    """
    programas_academicos = set()

    for archivo in archivos:
        try:
            df = pd.read_excel(archivo, usecols=["AÑO", "PROGRAMA ACADÉMICO"])
            df["AÑO"] = pd.to_numeric(df["AÑO"], errors='coerce')  # Convertir a numérico, NaN si falla
            df = df.dropna(subset=["AÑO"])  # Eliminar filas donde "AÑO" es NaN
            df["AÑO"] = df["AÑO"].astype(int)  # Convertir a enteros
            df = df[df['AÑO'].between(anio_inicio, anio_fin)]
            programas_academicos.update(df["PROGRAMA ACADÉMICO"].dropna().unique())
        except Exception as e:
            print(f"Error al procesar el archivo {archivo}: {e}")

    return programas_academicos