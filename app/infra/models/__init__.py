from app.infra.database.sql import engine, Base
from app.infra.models import user

def init_sql():
    Base.metadata.create_all(engine)