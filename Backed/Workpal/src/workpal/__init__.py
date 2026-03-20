#todos los router
from .router.Alumnos import router as alumnos_router
from .router.Proyectos import router as proyectos_router

__all__=(
    "alumnos_router",
    "proyectos_router"
)