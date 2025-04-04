<<<<<<< HEAD
import pandas as pd

def limpiar_datos():
    """Limpia y normaliza los datos del CSV, convirtiendo todo a minúsculas."""
    input_filename = "datos_cosevi_corregido.csv"
    output_filename = "datos_cosevi_limpio.csv"

    # Cargar CSV
    df = pd.read_csv(input_filename)

    # 1. Convertir nombres de columnas a minúsculas
    df.columns = [col.lower().strip() for col in df.columns]

    # 2. Convertir todo el contenido de texto a minúsculas y eliminar espacios extra
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

    # 3. Guardar el CSV limpio
    df.to_csv(output_filename, index=False, encoding="utf-8-sig")

    print(f"✅ Datos limpios guardados como '{output_filename}'")

if __name__ == "__main__":
    limpiar_datos()
=======
import pandas as pd

def limpiar_datos():
    """Limpia y normaliza los datos del CSV, convirtiendo todo a minúsculas."""
    input_filename = "datos_cosevi_corregido.csv"
    output_filename = "datos_cosevi_limpio.csv"

    # Cargar CSV
    df = pd.read_csv(input_filename)

    # 1. Convertir nombres de columnas a minúsculas
    df.columns = [col.lower().strip() for col in df.columns]

    # 2. Convertir todo el contenido de texto a minúsculas y eliminar espacios extra
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.lower().str.strip()

    # 3. Guardar el CSV limpio
    df.to_csv(output_filename, index=False, encoding="utf-8-sig")

    print(f"✅ Datos limpios guardados como '{output_filename}'")

if __name__ == "__main__":
    limpiar_datos()
>>>>>>> 96da0f649046087ad96650cc5231b514d6467301
