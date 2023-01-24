################# BACKEND ##################
############################################

#   Comandos basicos
#   pip install "fastapi[all]" # --user si no funciona al final 
#   pip install "uvicorn[standard]"
#   uvicorn main:app --reload | or | python -m uvicorn main:app --reload
#
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola FastAPI"




