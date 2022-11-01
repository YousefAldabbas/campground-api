from fastapi import APIRouter


router = APIRouter(
    prefix="/camps",
    tags=['camps']
)


@router.get('/')
def here():
    return {"hi": "yousef"}
