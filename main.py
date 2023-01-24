################# BACKEND ##################
############################################

#   Comandos basicos
#   pip install "fastapi[all]" # --user si no funciona al final 
#   pip install "uvicorn[standard]"
#   uvicorn main:app --reload | or | python -m uvicorn main:app --reload

#   url/docs # para ver al documentacion automatica del API

from fastapi import FastAPI

app = FastAPI()

@app.get("/") # url
async def root():
    return "Hola FastAPI"

@app.get("/github") # url/github
async def root():
    return "https://github/severaltool"


