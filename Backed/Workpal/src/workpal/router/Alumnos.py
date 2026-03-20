from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from fastapi import Query
from typing import TYPE_CHECKING, Optional
from Backed.Workpal.Database.conexion import SessionLocal
from Backed.Workpal.Database.Models import Alumno, Proyecto, ProyectoAlumno 

from Backed.Workpal.Database.Models.Alumnos import (
    AlumnoCreate,
    AlumnoResponse
)

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/alumnos",
    tags=["alumnos"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=AlumnoResponse)
def create_alumno(alumno: AlumnoCreate,query = Query(default=None,description="Creacion de un alumno")):
    db = SessionLocal()
    db_alumno = Alumno(name=alumno.name, last_name=alumno.last_name, carrera=alumno.carrera)
    db.add(db_alumno)
    db.commit()
    db.refresh(db_alumno)
    return AlumnoResponse.from_orm(db_alumno)
