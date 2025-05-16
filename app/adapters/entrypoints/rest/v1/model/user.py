from typing import Optional

from pydantic import BaseModel


class CreateUserV1Request(BaseModel):
    user_name: str
    user_email: str


class CreateUserV1Response(BaseModel):
    user_id: int
    user_name: Optional[str] = ""
    user_email: Optional[str] = ""

class CreateUserV1ResponseError(BaseModel):
    message: str

class CreateUserV1ListResponse(BaseModel):
    users: list[CreateUserV1Response]