from fastapi import Depends, HTTPException, status
from .oauth2 import get_current_user, oauth2_schema
from users.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import db


async def active_user_dependency(
    token: str = Depends(oauth2_schema),
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> User:
    user = await get_current_user(token, session)
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return user


async def super_user_dependency(
    token: str = Depends(oauth2_schema),
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> User:
    user = await get_current_user(token, session)
    if not user.is_super_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return user
