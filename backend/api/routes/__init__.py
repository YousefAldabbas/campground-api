from fastapi import APIRouter

from .camp import router as camp_router
from .comment import router as comment_router
from .user import router as user_router
from .auth import router as auth_router

routers = APIRouter()

routers.include_router(camp_router)
routers.include_router(comment_router)
routers.include_router(user_router)
routers.include_router(auth_router)