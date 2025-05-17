from fastapi import FastAPI
from app.logs.logging_config import configure_logging
from app.infra.models import init_sql
from app.interface.routers import configure
import uvicorn

logger = configure_logging()
app = FastAPI()

# Função inicializadora do sql
init_sql()

# Configuração de rotas
configure(app)

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
