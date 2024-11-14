# file_handler.py
import os


def cargar_archivo(uploaded_file):
    """Carga el archivo subido en el directorio especificado."""
    try:
        # Crear el directorio si no existe
        save_path = os.path.join("docs", "inputs")
        os.makedirs(save_path, exist_ok=True)

        # Ruta del archivo a guardar
        file_path = os.path.join(save_path, uploaded_file.name)

        # Guardar el archivo en el sistema
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        print(f"Archivo guardado en: {file_path}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def listar_archivos():
    """Lista todos los archivos disponibles en el directorio de inputs."""
    try:
        # Definir el path de la carpeta
        input_dir = os.path.join("docs", "inputs")

        # Verificar si el directorio existe
        if not os.path.exists(input_dir):
            return []

        # Listar archivos
        archivos = os.listdir(input_dir)
        return [archivo for archivo in archivos if archivo.endswith('.xlsx')]
    except Exception as e:
        print(f"Error al listar archivos: {e}")
        return []