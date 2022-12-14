from fastapi import APIRouter, Depends
from config import get_db
from schemas.user import CreateUser
from sqlalchemy.orm import Session
from controllers.user import create 


router = APIRouter(
    prefix="/users",
    tags=['users']
)


@router.post('/register')
async def register(req: CreateUser, db: Session = Depends(get_db)):
    return create(req,db)
