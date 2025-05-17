from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

from app.configs.settings import APP_NAME, API_PREFIX, DEBUG
from app.logs.logging_config import configure_logging
from app.infra.models import init_sql
from app.interface.routers import configure
import uvicorn


# Cria a aplicação FastAPI
app = FastAPI(
    title=APP_NAME,
    description="API REST para gerenciamento de usuários com FastAPI e Arquitetura Hexagonal",
    version="0.1.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=f"{API_PREFIX}/openapi.json",
    debug=DEBUG,
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota para documentação Swagger
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=f"{API_PREFIX}/openapi.json",
        title=f"{APP_NAME} - Documentação da API",
    )

# Configura o logger
logger = configure_logging()

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

# Rota Padrão
@app.get("/", include_in_schema=False)
async def root():
    return {
        "message": f"Bem-vindo à {APP_NAME}",
        "docs": "/docs",
    }

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
