# Clase del usuario principal de la DB
from pydantic import BaseModel

class User(BaseModel):
    id: str | None # Esto significa que puede estar o no ese dato
    username: str
    email: str
