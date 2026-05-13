from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Backed.Workpal.Database.conexion import get_db
from Backed.Workpal.Database.Models import Proyecto
from Backed.Workpal.Database.Models.Proyectos import ProyectoCreate, ProyectoResponse

router = APIRouter(
    prefix="/proyectos",
    tags=["proyectos"],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/",
    response_model=ProyectoResponse,
    description="Crea un nuevo proyecto"
)
def create_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_db)):
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

    return ProyectoResponse.model_validate(db_proyecto)

@router.get(
    "/",
    response_model=list[ProyectoResponse],
    description="Obtiene todos los proyectos"
)
def get_proyectos(db: Session = Depends(get_db)):
    return db.query(Proyecto).all()

@router.get(
    "/{proyecto_id}",
    response_model=ProyectoResponse,
    description="Obtiene un proyecto por ID"
)
def get_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto not found")

    return ProyectoResponse.model_validate(proyecto)

@router.put(
    "/{proyecto_id}",
    response_model=ProyectoResponse,
    description="Actualiza un proyecto existente"
)
def update_proyecto(proyecto_id: int, updated: ProyectoCreate, db: Session = Depends(get_db)):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto not found")

    proyecto.name = updated.name
    proyecto.skill = updated.skill
    proyecto.description = updated.description
    proyecto.start = updated.start
    proyecto.end = updated.end
    proyecto.image = updated.image

    db.commit()
    db.refresh(proyecto)

    return ProyectoResponse.model_validate(proyecto)


@router.delete(
    "/{proyecto_id}",
    description="Elimina un proyecto por su ID"
)
def delete_proyecto(proyecto_id: int, db: Session = Depends(get_db)):
    proyecto = db.query(Proyecto).filter(Proyecto.id == proyecto_id).first()

    if not proyecto:
        raise HTTPException(status_code=404, detail="Proyecto not found")

    db.delete(proyecto)
    db.commit()

    return {"message": "Proyecto deleted"}