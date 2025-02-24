from fastapi import FastAPI
from api.routes import router
from database.session import init_db

app = FastAPI()

# Inicializa o banco de dados
init_db()

# Inclui as rotas
app.include_router(router)