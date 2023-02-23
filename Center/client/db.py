# Instalar MongoDB
# pip install pymongo
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from pymongo import MongoClient
from client import users
from client.users import User
from client.schemes.users import users_schemas, all_users
from bson import ObjectId


router = APIRouter()

db_client = MongoClient()

# Insertar clientes
@router.post("/addUser")
async def createUser(user: User):
    if type(search_user(user.email)) == User:
        return "Ya existe"
    
    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = users_schemas(db_client.local.users.find_one({"_id":id}))
    
    return User(**new_user)

# Buscar clientes
@router.get("/find_users")
async def find_all():
    return all_users(db_client.local.users.find())        


# Delete clientes
@router.delete("/del_users/{id}")
async def del_user(id: str):
    found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})
    if not found:
        return "error: No se elimino el usuario"

    return "Eliminado correctamente."


# Buscar el usuario antes de agregarlo a la db
def search_user(email: str):
    try:
        return User(**users_schemas(db_client.local.users.find_one({"email":email})))
    except:
        return "No se a encontrado el usuario."
    
    
    