from fastapi import APIRouter


router = APIRouter(
    prefix="/comments",
    tags=['comments']
)


@router.get('/')
def here():
    return {"hi": "yousef"}
