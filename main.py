<<<<<<< HEAD
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Importa CORSMiddleware
from dotenv import load_dotenv
import os
from supabase import create_client, Client
import uvicorn

# Cargar variables de entorno
load_dotenv()

# Conectar con Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Iniciar FastAPI
app = FastAPI()

# Configuración CORS
origins = [
    "http://localhost:5173",  # Frontend de Vite (ajustar según tu URL)
    "https://mortalidad-cr-react.vercel.app", # Frontend de Vercel
    "https://mortalidadcr.onrender.com",  # La URL de producción de tu API
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite solicitudes de estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# 📌 Obtener todos los registros
@app.get("/mortalidad/")
async def obtener_mortalidad():
    try:
        response = supabase.table("MortalidadCR").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Configuración del puerto dinámico
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Utiliza la variable de entorno "PORT"
    uvicorn.run(app, host="0.0.0.0", port=port)  # Escucha en el puerto asignado
=======
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Importa CORSMiddleware
from dotenv import load_dotenv
import os
from supabase import create_client, Client
import uvicorn

# Cargar variables de entorno
load_dotenv()

# Conectar con Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Iniciar FastAPI
app = FastAPI()

# Configuración CORS
origins = [
    "http://localhost:5173",  # Frontend de Vite (ajustar según tu URL)
    "https://mortalidad-cr-react.vercel.app", # Frontend de Vercel
    "https://mortalidadcr.onrender.com",  # La URL de producción de tu API
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permite solicitudes de estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos HTTP
    allow_headers=["*"],  # Permite todos los encabezados
)

# 📌 Obtener todos los registros
@app.get("/mortalidad/")
async def obtener_mortalidad():
    try:
        response = supabase.table("MortalidadCR").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Configuración del puerto dinámico
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Utiliza la variable de entorno "PORT"
    uvicorn.run(app, host="0.0.0.0", port=port)  # Escucha en el puerto asignado
>>>>>>> 96da0f649046087ad96650cc5231b514d6467301
