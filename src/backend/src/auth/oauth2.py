from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from users.models import User
from config import AUTH_PREFIX, settings
from datetime import timedelta, datetime
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import db
from users import service as user_service

oauth2_schema = OAuth2PasswordBearer(tokenUrl=AUTH_PREFIX + "/token")
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.OAUTH_ACCESS_TOKEN_EXPIRE_MINUTES
        )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.OAUTH_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_schema),
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authentificate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, settings.OAUTH_SECRET_KEY, algorithms=[ALGORITHM])
        decode_email: str = payload.get("username")
        if decode_email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await user_service.get_user_by_email(session, decode_email)

    if user is None:
        raise credentials_exception

    return user
