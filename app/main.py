from fastapi import FastAPI
from app.configs.database import create_tables, populate_db
from app.logging_config import configure_logging
from app.adapters.entrypoints.rest.v1.user import router as user_router
import uvicorn


logger = configure_logging()
app = FastAPI()

# Criar tabelas e popular o banco de dados
# create_tables()
# populate_db()
# logger.info("Tabelas do banco de dados criadas e populadas")

# Incluir o router de usuários
app.include_router(user_router)

@app.get("/")
def get_users():
    """Endpoint de teste inicial"""
    logger.info("Requisição recebida no endpoint teste")
    return {
        "mensagem": "API de Gerenciamento de Usuários",
        "status": "Online"
    }


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
