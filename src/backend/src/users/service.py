from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import UserBase, UserCreate, UserUpdate
from .models import User
from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password) -> bool:
    return password_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return password_context.hash(password)


async def get_users(session: AsyncSession) -> list[User]:
    stmt = select(User).order_by(User.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> User:
    return await session.get(User, user_id)


async def get_user_by_email(session: AsyncSession, email: str) -> User:
    stmt = select(User).where(User.email == email)
    result: Result = await session.execute(stmt)
    user = result.scalar()
    return user


async def create_user(session: AsyncSession, user_in: UserCreate) -> User:
    user_in.password = get_password_hash(user_in.password)
    user = User(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user


async def update_user(
    session: AsyncSession,
    user: UserBase,
    user_update: UserUpdate,
    partial: bool = False,
) -> User:

    for name, value in user_update.model_dump(exclude_unset=partial).items():
        if name == "password":
            value = get_password_hash(value)
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(session: AsyncSession, user: User) -> None:
    await session.delete(user)
    await session.commit()
