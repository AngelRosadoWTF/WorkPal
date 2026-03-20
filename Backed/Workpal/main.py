
# Ejecutor de todo el proyecto
import sys
import os
from Backed.Workpal.src.workpal.app import app



import uvicorn

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)