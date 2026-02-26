from fastapi import FastAPI

app = FastAPI(title="Workpal")

@app.get("/")
def home():
    print("Canto sueltame")
    return{"Mensaje": "Bienvendios"}