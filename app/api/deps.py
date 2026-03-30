from typing import Annotated
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.db import get_async_session
from app.core.config import JWT_SECRET

oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login")
SessionDep = Annotated[AsyncSession, Depends(get_async_session)]


async def get_current_user(token: str = Depends(oauth_scheme)):
    try:
        paylod = jwt.decode(token, JWT_SECRET, algorithms="HS256")
        return paylod.get("sub")
    except JWTError:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Token not valid")


CurrentUser = Annotated[str, Depends(get_current_user)]
