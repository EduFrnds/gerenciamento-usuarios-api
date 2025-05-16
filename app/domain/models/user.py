
from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    user_name: str
    user_email: str


    # talvez implementar um regex para melhorar a senha
