from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from typing import TYPE_CHECKING, Optional
from .base import Base
# esta parte no se ha implementado toda via 
if TYPE_CHECKING:
    from Proyectos import Proyecto
    from Alumnos import Alumno

class ProyectoAlumno(Base):
    __tablename__ = "ProyectoAlumno"
    __table_args__ = (UniqueConstraint('id', name='uq_id'),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    proyecto_id: Mapped[int] = mapped_column(Integer, nullable=False)
    alumno_id: Mapped[int] = mapped_column(Integer, nullable=False)

    # Relaciones
    proyecto: Mapped["Proyecto"] = relationship("Proyecto", back_populates="lista_alumnos")
    alumno: Mapped["Alumno"] = relationship("Alumno", back_populates="lista_proyectos")