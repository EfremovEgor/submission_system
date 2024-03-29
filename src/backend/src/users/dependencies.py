from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import db
from .models import User
from . import service


async def user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> User:
    user = await service.get_user(session=session, user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found!",
    )
