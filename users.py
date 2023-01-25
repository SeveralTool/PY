from fastapi import FastAPI
from pydantic import BaseModel

# Iniciar el server: uvicorn users:app --reload

app = FastAPI()

# Entidad usuario

# Opcion 1 con clases
class User(BaseModel):
    name: str
    surname: str
    age: int

user_list = [User(name="Nahuel",surname="Galeano",age=23),
            User(name="Mateo",surname="Risso",age=20)
            ]

@app.get("/usersclass") # url
async def usersclass():
    return user_list

# Opcion 2
@app.get("/users") # url
async def users():
    return [{"name":"Nahuel","surname": "Galeano","age":"23",},
            {"name":"Mateo","surname": "Risso","age":"20",},
            ]


