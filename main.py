from fastapi import FastAPI
from database.db import Base, engine
from routers import productos

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(productos.router, tags=["Productos"])

@app.get("/", tags=["Main"])
def main():
    return {"message": "Hello World"}