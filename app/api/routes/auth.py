from app.api.deps import SessionDep
from fastapi import APIRouter
from app.schemas import UserCreate

auth_router = APIRouter()


@auth_router.post("/register")
async def register(user: UserCreate, session: SessionDep):
    ...
    # user = await session.
