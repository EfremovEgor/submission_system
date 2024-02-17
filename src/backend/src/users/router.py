from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.oauth2 import get_current_user
from auth.dependencies import super_user_dependency

from .dependencies import user_by_id
from .models import User
from core.database import db
from . import service
from .schemas import UserBase, UserUpdate
from .service import get_users
from pydantic import EmailStr

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/", response_model=list[UserBase])
async def get_users(
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return await service.get_users(session)


@router.get("/{user_id}", response_model=UserBase)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(db.scoped_session_dependency),
    user=Depends(user_by_id),
    current_super_user: UserBase = Depends(super_user_dependency),
):

    return user


@router.put("/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user=Depends(user_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):

    return await service.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.patch("/{user_id}/")
async def update_user_partial(
    user_update: UserUpdate,
    user=Depends(user_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return await service.update_user(
        session=session,
        user=user,
        user_update=user_update,
        partial=True,
    )


@router.delete("/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> None:
    await service.delete_user(session=session, user=user)
