from fastapi import APIRouter, Depends
from security import oauth2_scheme

router = APIRouter(
    prefix="/auth",
    tags=['auth']
)




@router.post("/login")
async def login(token: str = Depends(oauth2_scheme)):
    return {"token": token}