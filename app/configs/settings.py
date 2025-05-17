import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env se existir
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# Configurações da aplicação
APP_NAME = "API de Gerenciamento de Usuários"
API_PREFIX = "/api/v1"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Configurações de segurança - Não implementei
# SECRET_KEY = os.getenv("SECRET_KEY", "insecure_key_for_dev_only_please_change_in_production")
# ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
# ALGORITHM = "HS256"

# Configurações do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/main.db")

# Configurações de paginação
DEFAULT_PAGE_SIZE = int(os.getenv("DEFAULT_PAGE_SIZE", "10"))
MAX_PAGE_SIZE = int(os.getenv("MAX_PAGE_SIZE", "100"))