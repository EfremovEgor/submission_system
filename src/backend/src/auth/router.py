from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from .dependencies import active_user_dependency
from .schemas import Token
from mailing.tasks import send_confirmation_email
from core.database import db
from core.redis import redis_instance
from users import service as user_service
from users.schemas import UserCreate, UserBase, UserUpdate
from utils import generate_base64_url_safe_string
from config import CONFIRMATION_LINK_EXPIRATION_TIME, AUTH_PREFIX, DOMAIN_NAME
from sqlalchemy.ext.asyncio import AsyncSession
from . import oauth2

router = APIRouter(
    prefix=AUTH_PREFIX,
    tags=["Auth"],
)


@router.get("/verify_token", status_code=status.HTTP_200_OK)
async def verify_token(
    session: AsyncSession = Depends(db.scoped_session_dependency),
    requester=Depends(active_user_dependency),
):
    return {
        "verified": True,
    }


@router.post("/register")
async def register_user(
    user_in: UserCreate, session: AsyncSession = Depends(db.scoped_session_dependency)
):

    if (
        user := await user_service.get_user_by_email(session, user_in.email)
    ) and user.is_active:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email {user_in.email} already exists and email is confirmed",
        )

    if user is None:
        user = await user_service.create_user(session, user_in)
    else:
        await user_service.update_user(
            session,
            user,
            UserUpdate(password=user_in.password),
            partial=True,
        )
    token = generate_base64_url_safe_string()

    send_confirmation_email.delay(
        email=user.email,
        url=DOMAIN_NAME + AUTH_PREFIX + f"/confirm/{token}",
    )

    redis_instance.setex(
        name=token,
        time=CONFIRMATION_LINK_EXPIRATION_TIME,
        value=user.id,
    )

    return HTTPException(
        status_code=status.HTTP_200_OK,
        detail=f"Email verification sent to {user.email}",
    )


@router.get("/confirm/{token}")
async def confirm(
    token: str, session: AsyncSession = Depends(db.scoped_session_dependency)
):
    if (user_id := redis_instance.get(token)) is not None:
        user_id = int(user_id)
        await user_service.update_user(
            session,
            await user_service.get_user(session, user_id),
            UserUpdate(is_active=True),
            partial=True,
        )
        redis_instance.delete(token)
        return HTTPException(status_code=status.HTTP_200_OK, detail="Confirmed")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="Confirmation link not found"
    )


@router.post("/token", response_model=Token)
async def get_token(
    request: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    user = await user_service.get_user_by_email(session, request.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials"
        )
    if not user_service.verify_password(request.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong password"
        )
    access_token = oauth2.create_access_token(data={"username": user.email})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user.id,
        "username": user.email,
    }
