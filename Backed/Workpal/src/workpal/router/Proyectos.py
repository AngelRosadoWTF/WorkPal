from fastapi import APIRouter, Query
from Backed.Workpal.Database.conexion import SessionLocal
from Backed.Workpal.Database.Models import Proyecto
from Backed.Workpal.Database.Models.Proyectos import (
    ProyectoCreate,
    ProyectoResponse
)

router = APIRouter(
    prefix="/proyectos",
    tags=["proyectos"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ProyectoResponse)
def create_proyecto(proyecto: ProyectoCreate, query=Query(default=None, description="Creacion de un proyecto")):
    db = SessionLocal()

    db_proyecto = Proyecto(
        name=proyecto.name,
        skill=proyecto.skill,
        description=proyecto.description,
        start=proyecto.start,
        end=proyecto.end,
        image=proyecto.image
    )

    db.add(db_proyecto)
    db.commit()
    db.refresh(db_proyecto)

    return ProyectoResponse.from_orm(db_proyecto)