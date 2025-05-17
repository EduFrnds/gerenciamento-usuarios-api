from datetime import datetime
from typing import Annotated, List, Optional

from pydantic import BaseModel, Field, EmailStr


class UserCreateSchema(BaseModel):
    username: Annotated[
        str,
        Field(
            default="username",
            description='`@username` aceita apenas letras, números e underscores (_)',
            min_length=5,
            max_length=64,
            pattern=r'^[a-zA-Z0-9_]+$',
        ),
    ]
    email: Annotated[EmailStr, Field(description='email', max_length=256)]
    password: Annotated[
        str, Field(description='senha', min_length=8, max_length=256)
    ]

class UserSchema(UserCreateSchema):
    id: int

class UserSigninSchema(BaseModel):
    username: str
    password: str

class UserCreate(UserCreateSchema):
    """Esquema para criação de usuário."""
    password: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    """Esquema para resposta de usuário."""
    id: int
    username: str
    email: str
    created_at: datetime

    class Config:
        """Configuração do modelo Pydantic."""
        from_attributes = True

class UserListResponse(BaseModel):
    """Esquema para resposta de lista de usuários com paginação."""
    items: List[UserResponse]
    total: int
    page: int
    size: int
    pages: int
