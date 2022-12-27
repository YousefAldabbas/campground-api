from typing import List, Optional, Union
from pydantic import BaseModel


class TokenBase(BaseModel):
    scope: str
    type: str


class TokenData(TokenBase):
    sub: str


class Tokens(BaseModel):
    access_token: str
    refresh_token: str
    type: str
