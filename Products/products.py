
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/products") # url
async def prod():
    return ["Producto 1","Producto 2","Producto 3","Producto 4",]