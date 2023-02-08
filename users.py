from fastapi import FastAPI
from pydantic import BaseModel

# Iniciar el server: uvicorn users:app --reload

app = FastAPI()

# Entidad usuario

# Opcion 1 con clases
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

# OBJETO
user_list = [User(id= 1, name="Nahuel",surname="Galeano",age=23),
            User(id=2, name="Mateo",surname="Risso",age=20)
            ]

# # Opcion 1
@app.get("/user/{id}") # url
async def User(id: int):
    return search_user(id)

# # Ejemplo 2
@app.get("/user_query/{id}") # url
async def User(id: int):
    return search_user(id)


#  FUNCION GENERAL
def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return "No se a encontrado el usuario."



# # Opcion 2 mas "manual"
# @app.get("/users") # url
# async def users():
#     return [{"id":"1","name":"Nahuel","surname": "Galeano","age":"23",},
#             {"id":"1","name":"Mateo","surname": "Risso","age":"20",},
#             ]


# Seguiremos actualizando proximamente.