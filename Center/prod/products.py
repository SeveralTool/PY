
from fastapi import APIRouter

app = APIRouter()

@app.get("/products") # url
async def prod():
    return ["Producto 1","Producto 2","Producto 3","Producto 4",]


