from typing import List, Optional,Union
from pydantic import BaseModel



class UserBase(BaseModel):
    # id: int
    username: str
    email: str
    # created_at: str
    # updated_at: str


class CreateUser(UserBase):
    password: str

