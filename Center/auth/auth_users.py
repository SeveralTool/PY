from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()
oauth = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    email: str
    username: str

class UserDB(User): # Heredacion
    password: str

users_db = {
    "nahuel":{
        "username": "nahuel",
        "email": "nahuel@gmail.com",
        "password": "1234"    
    },
    "PersonTwo":{
        "username": "PersonTwo",
        "email": "persontwo@gmail.com",
        "password": "1234567"    
    }    
}

# Criterio de dependencia - verificación
async def current_user(token: str = Depends(oauth)):
    user = search_user(token)
    if not user:
        # Modo de respuesta de errores : status_code = status. mostrará los errores disponibles.
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,# Codigo de error
            detail="Token no disponible.", # Mensaje
            headers={"WWW.Authenticate": "Bearer"}) # Estandar
        # return "No se encontro el token."
    return user
    
# Funcion para buscan en la DB
def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


@app.post("/login") # url
async def login(form: OAuth2PasswordRequestForm= Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        return "No es correcto el usuario, revise los parametros."
    user = search_user(form.username)
    if not form.password == user.password:
        return "La password no es correcta."
    
    return {"access_token": user.username,"token_type":"bearer"}
        
@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

@app.get("/test")
async def mee():
    return "fuck me"

###########################################################

