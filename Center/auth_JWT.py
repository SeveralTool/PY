#AUTENTICACION CON ENCRIPTACIÓN

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime,timedelta


ALGORITHM = "HS256"
ACCES_TOKEN_DURATION = 1
crypt = CryptContext(schemes=["bcrypt"])

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

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

@app.post("/login") # url
async def login(form: OAuth2PasswordRequestForm= Depends()):
    
    user_db = users_db.get(form.username)
    if not user_db:
        return "No es correcto el usuario, revise los parametros."
    
    user = search_user(form.username)
    if not crypt.verify(form.password, user.password):
        return "La password no es correcta."
    
    access_token = {
        "sub": user.username,
        "expireDate": datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_DURATION),
    }
    
    return {"access_token": access_token ,"token_type":"bearer"}






    