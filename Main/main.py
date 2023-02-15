################# BACKEND ##################
############################################

#   Comandos basicos
#   pip install "fastapi[all]" # --user si no funciona al final 
#   pip install "uvicorn[standard]"
#   uvicorn main:app --reload | or | python -m uvicorn main:app --reload

#   url/docs # para ver al documentacion automatica del API

from fastapi import FastAPI
from pydantic import BaseModel
from Products import products

app = FastAPI()

# Router
app.include_router(products.router)


@app.get("/") # url
async def root():
    return "Hola FastAPI"

@app.get("/github") # url/github
async def root():
    return "https://github/severaltool"



# Iniciar el server: uvicorn users:app --reload
# python -m uvicorn main:app --reload : Este comando siempre funciona.




######################################

# Entidad usuario

# Opcion 1 con clases | Objeto de modelo(importante crearlo)
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

# OBJETO
user_list = [User(id= 1, name="Nahuel",surname="Galeano",age=23),
            User(id=2, name="Mateo",surname="Risso",age=20)
            ]

######################################

# # Opcion 1
# @app.get("/user/{id}") # url
# async def User(id: int):
#     return search_user(id)

# # # Ejemplo 2
# @app.get("/user_query/{id}") # url
# async def User(id: int):
#     return search_user(id)

######################################

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
#     return [{"id":"1","name":"Nahuel","surname": "Galeano","age":"23"},
#             {"id":"2","name":"Mateo","surname": "Risso","age":"20"},
#             ]

######################################

# Agregar un usario con POST

@app.post("/newUser/")
async def createUser(user: User):
        if type(search_user(user.id)) == User:
            return {"Ya existe el usuario."}
        else:
            user_list.append(user)
   
# Consulta para el post

@app.get("/users/")
async def find():
    return user_list   
 

######################################

# Actualizar el usuario

@app.put("/updateUser/")
async def user(user: User):
    for i, update_user in enumerate(user_list):
        if update_user.id == user.id:
            user_list[i] = user
    
# Eliminar el usuario

@app.delete("/user/{id}")
async def delete(id:int):
    for i, delete in enumerate(user_list):
        if delete.id == id:
            del user_list[i]
        
            





######################################
######################################
######################################
######################################
######################################
######################################





# Seguiremos actualizando proximamente.