from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.configs.settings import DATABASE_URL

URI = DATABASE_URL

engine = create_engine(
    URI,  # Altere para o seu banco de dados específico
    pool_size=5,  # Número máximo de conexões no pool
    max_overflow=10,  # Conexões extras que podem ser criadas além do pool_size
    pool_timeout=30,  # Tempo de espera por uma conexão em segundos
    pool_recycle=1800,  # Reciclagem de conexões a cada 1800 segundos (30 minutos)
)

Base = declarative_base()
Session = sessionmaker(bind=engine)