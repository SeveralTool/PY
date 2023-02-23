# Instalar MongoDB
# pip install pymongo
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from pymongo import MongoClient
from client import users
from client.users import User
from client.schemes.users import users_schemas

router = APIRouter()

db_client = MongoClient()


@router.post("/addUser")
async def createUser(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    id = db_client.local.users.insert_one(user_dict).inserted_id
    new_user = users_schemas(db_client.local.users.find_one({"_id":id}))
    
    return User(**new_user)

