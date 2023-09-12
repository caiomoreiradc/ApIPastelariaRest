from fastapi import FastAPI
from settings import HOST, PORT, RELOAD

# import das classes com as rotas/endpoints

from mod_cliente import ClienteDAO
from mod_funcionario import FuncionarioDAO

# mapeamento das rotas/endpoints

app = FastAPI()

app.include_router(ClienteDAO.router)
app.include_router(FuncionarioDAO.router)

import db
db.criaTabelas();

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('apiPastelaria:app', host=HOST, port=int(PORT), reload=RELOAD)

# rota padrão
@app.get("/")
def root():
    return {"detail":"API Pastelaria", "Swagger UI": "http://127.0.0.1:8000/docs", "ReDoc": "http://127.0.0.1:8000/redoc" }