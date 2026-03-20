#conectar todo
from Backed.Workpal.Database.Models import Alumno, Proyecto, ProyectoAlumno
from Backed.Workpal.Database.conexion import engine, SessionLocal
from .router.Alumnos import router as alumnos_router
from fastapi import FastAPI
# Registrar todos los modelos antes de crear las tablas
from Backed.Workpal.Database.Models.Alumnos import Alumno
from Backed.Workpal.Database.Models.Proyectos import Proyecto
from Backed.Workpal.Database.Models.Alumnos import Base


app = FastAPI()


# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

app.include_router(alumnos_router)

