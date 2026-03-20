import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from .Models.base import Base

# Cargar variables de entorno
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./.blog.db")
print("conectado a :", DATABASE_URL)

engine_kwargs = {}
if DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, echo=True, future=True, **engine_kwargs)
SessionLocal = sessionmaker(
    bind=engine, autoflush=False, autocommit=False, class_=Session
)

Base.metadata.create_all(bind=engine)  # dev