<<<<<<< HEAD
import requests
import pandas as pd
import chardet

# URL de la API
URL = "http://cosevi.cloudapi.junar.com/api/v2/datastreams/REGIS-DE-FALLE-EN-SITIO/data.csv/?auth_key=KgUCdTH23mHCAqaAhvG3OBOvu2hyv5dZ0RMJCWih"

def extraer_datos():
    """Descarga el CSV desde la API, detecta la codificación y lo guarda en UTF-8-SIG."""
    response = requests.get(URL)

    if response.status_code == 200:
        temp_filename = "datos_cosevi_temp.csv"

        # Guardar el archivo temporalmente en modo binario
        with open(temp_filename, "wb") as archivo:
            archivo.write(response.content)

        # Detectar la codificación del archivo
        with open(temp_filename, "rb") as archivo:
            resultado = chardet.detect(archivo.read())

        encoding_detectado = resultado["encoding"]
        print(f"Codificación detectada: {encoding_detectado}")

        # Cargar el CSV con la codificación detectada
        df = pd.read_csv(temp_filename, encoding=encoding_detectado)

        # Guardarlo en UTF-8-SIG para compatibilidad con PostgreSQL y Excel
        output_filename = "datos_cosevi_corregido.csv"
        df.to_csv(output_filename, index=False, encoding="utf-8-sig")

        print(f"Archivo corregido guardado como '{output_filename}'")
    else:
        print(f"Error al obtener los datos. Código de estado: {response.status_code}")

if __name__ == "__main__":
    extraer_datos()
=======
import requests
import pandas as pd
import chardet

# URL de la API
URL = "http://cosevi.cloudapi.junar.com/api/v2/datastreams/REGIS-DE-FALLE-EN-SITIO/data.csv/?auth_key=KgUCdTH23mHCAqaAhvG3OBOvu2hyv5dZ0RMJCWih"

def extraer_datos():
    """Descarga el CSV desde la API, detecta la codificación y lo guarda en UTF-8-SIG."""
    response = requests.get(URL)

    if response.status_code == 200:
        temp_filename = "datos_cosevi_temp.csv"

        # Guardar el archivo temporalmente en modo binario
        with open(temp_filename, "wb") as archivo:
            archivo.write(response.content)

        # Detectar la codificación del archivo
        with open(temp_filename, "rb") as archivo:
            resultado = chardet.detect(archivo.read())

        encoding_detectado = resultado["encoding"]
        print(f"Codificación detectada: {encoding_detectado}")

        # Cargar el CSV con la codificación detectada
        df = pd.read_csv(temp_filename, encoding=encoding_detectado)

        # Guardarlo en UTF-8-SIG para compatibilidad con PostgreSQL y Excel
        output_filename = "datos_cosevi_corregido.csv"
        df.to_csv(output_filename, index=False, encoding="utf-8-sig")

        print(f"Archivo corregido guardado como '{output_filename}'")
    else:
        print(f"Error al obtener los datos. Código de estado: {response.status_code}")

if __name__ == "__main__":
    extraer_datos()
>>>>>>> 96da0f649046087ad96650cc5231b514d6467301
