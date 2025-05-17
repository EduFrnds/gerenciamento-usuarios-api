import datetime

import sqlalchemy

from app.infra.database.sql import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String(100), nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.datetime.now)
