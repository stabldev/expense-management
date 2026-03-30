from fastapi import APIRouter

from .auth import auth_router
from .expense import expense_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(expense_router)
