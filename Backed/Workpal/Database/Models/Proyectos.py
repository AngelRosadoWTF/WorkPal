from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Integer, String, Text, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Proyecto(Base):
    __tablename__ = "Proyectos"
    __table_args__ = (UniqueConstraint('id', name='uq_proyectos_id'),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    skill: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    start: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    end: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    image: Mapped[str] = mapped_column(String(255), nullable=True)

    lista_alumnos: Mapped[list] = relationship(
        "Alumno",
        secondary="ProyectoAlumno",
        back_populates="lista_proyectos"
    )

class ProyectoCreate(BaseModel):
    name: str
    skill: str
    description: str
    start: datetime | None = None
    end: datetime | None = None
    image: str | None = None


class ProyectoResponse(BaseModel):
    id: int
    name: str
    skill: str
    description: str
    start: datetime
    end: datetime
    image: str | None = None

    class Config:
        from_attributes = True