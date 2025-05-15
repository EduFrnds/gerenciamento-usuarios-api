from fastapi import FastAPI
from app.logging_config import configure_logging

# Configurar o logger e obtê-lo
logger = configure_logging()  # Agora 'logger' é o objeto de logging

app = FastAPI()

@app.get("/")
def read_root():
    logger.info("Projeto FASTAPI iniciado.")
    return {
        "message": "API de Gerenciamento de Usuários"
        }