from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from requests import Session
from config.database import get_db
from serializers.user import loginSerializer
from security import create_tokens

from schemas.token import Tokens

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)




@router.post("/login", response_model=Tokens)
async def login(req: OAuth2PasswordRequestForm = Depends(),db: Session =Depends(get_db)):
    user = loginSerializer(req,db)
    return create_tokens(user.id)