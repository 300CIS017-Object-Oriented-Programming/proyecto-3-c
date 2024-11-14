[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/9bKkctvo)
# snies_proyecto_3
Proyecto_3

# Sistema de Visualización y Consolidación de Datos SNIES

## Descripción General
Este proyecto permite analizar información del Sistema Nacional de Información de la Educación Superior (SNIES) en Colombia.

## Instrucciones de Instalación

1. Clona este repositorio.
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta la aplicación:
    ```bash
    streamlit run main.py
    ```

## Diagrama UML

```mermaid
classDiagram
    class FileHandler {
        +listar_archivos()
        +cargar_archivo(uploaded_file)
    }

    class DataFilter {
        +buscar_programas(palabra_clave)
    }

    class DataProcessor {
        +procesar_datos(archivos, programas, anio_inicio, anio_fin)
    }

    class DataVisualization {
        +graficar_datos(resultados)
    }

    (por ahora solo por ejemplificar)
```

# snies_proyecto_3
Proyecto_3

