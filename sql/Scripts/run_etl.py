<<<<<<< HEAD
import extraer_datos
import limpiar_datos
import cargar_datos

if __name__ == "__main__":
    print("🔄 Iniciando proceso ETL...")

    print("\n📥 Extrayendo datos...")
    extraer_datos.extraer_datos()

    print("\n🧹 Limpiando datos...")
    limpiar_datos.limpiar_datos()

    print("\n📤 Cargando datos a PostgreSQL...")
    cargar_datos.cargar_datos()

    print("\n✅ ETL completado exitosamente 🚀")
=======
import extraer_datos
import limpiar_datos
import cargar_datos

if __name__ == "__main__":
    print("🔄 Iniciando proceso ETL...")

    print("\n📥 Extrayendo datos...")
    extraer_datos.extraer_datos()

    print("\n🧹 Limpiando datos...")
    limpiar_datos.limpiar_datos()

    print("\n📤 Cargando datos a PostgreSQL...")
    cargar_datos.cargar_datos()

    print("\n✅ ETL completado exitosamente 🚀")
>>>>>>> 96da0f649046087ad96650cc5231b514d6467301
