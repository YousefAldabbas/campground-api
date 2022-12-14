from typing import List, Optional,Union
from pydantic import BaseModel,EmailStr



class UserBase(BaseModel):
    # id: int
    username: str
    email: EmailStr
    # created_at: str
    # updated_at: str


class CreateUser(UserBase):
    password: str

