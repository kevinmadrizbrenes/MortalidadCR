<<<<<<< HEAD
import pandas as pd
from sqlalchemy import create_engine, text

# Configuración de PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "MortalidadCR"

# Crear conexión con PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def cargar_datos():
    """Carga los datos limpios a la tabla 'defunciones' en PostgreSQL."""
    input_filename = "datos_cosevi_limpio.csv"

    # Cargar el CSV
    df = pd.read_csv(input_filename)

    # Iniciar la transacción
    with engine.begin() as conn:
        # Vaciar la tabla antes de insertar nuevos datos
        conn.execute(text('TRUNCATE TABLE "MortalidadCR" RESTART IDENTITY;'))

        # Insertar los datos nuevos
        df.to_sql("MortalidadCR", conn, if_exists="append", index=False)

    print("Datos cargados en PostgreSQL exitosamente.")

if __name__ == "__main__":
    cargar_datos()



=======
import pandas as pd
from sqlalchemy import create_engine, text

# Configuración de PostgreSQL
DB_USER = "postgres"
DB_PASSWORD = "12345"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "MortalidadCR"

# Crear conexión con PostgreSQL
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def cargar_datos():
    """Carga los datos limpios a la tabla 'defunciones' en PostgreSQL."""
    input_filename = "datos_cosevi_limpio.csv"

    # Cargar el CSV
    df = pd.read_csv(input_filename)

    # Iniciar la transacción
    with engine.begin() as conn:
        # Vaciar la tabla antes de insertar nuevos datos
        conn.execute(text('TRUNCATE TABLE "MortalidadCR" RESTART IDENTITY;'))

        # Insertar los datos nuevos
        df.to_sql("MortalidadCR", conn, if_exists="append", index=False)

    print("Datos cargados en PostgreSQL exitosamente.")

if __name__ == "__main__":
    cargar_datos()



>>>>>>> 96da0f649046087ad96650cc5231b514d6467301
