from fastapi import FastAPI
from app.logging_config import configure_logging

logger = configure_logging()
app = FastAPI()

@app.get("/testeapi")
def read_root():
    logger.info("Projeto FASTAPI iniciado.")
    return {
        "mensagem": "API de Gerenciamento de Usuários"
        }
