import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), 'Database/.env'))

app = FastAPI()

# conexion a la base de datos utilizando el .env
DB_URL = f"postgresql://{os.getenv('USUARIO')}:{os.getenv('CONTRASENA')}@{os.getenv('HOST')}:{os.getenv('PUERTO')}/{os.getenv('NOMBRE_BD')}"

# obtener la URL de la base de datos desde el .env
@app.get("/db_url")
def get_db_url():
    return {"db_url": DB_URL}

#Obtener el host de la base de datos desde el .env
@app.get("/db_host")
def get_db_host():
    return {"db_host": os.getenv('HOST')}


