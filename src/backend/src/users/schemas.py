from pydantic import BaseModel, EmailStr
from datetime import datetime
from conferences.schemas.conference import UserToConference
from conferences.schemas.topic import TopicInDBBase
from submissions.schemas import SubmissionInDBBase


class ConferenceUser(BaseModel):
    id: int
    name: str | None = None


class UserBase(BaseModel):
    email: EmailStr | None = None
    last_login: datetime | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    created_at: datetime | None = None
    title: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    surname: str | None = None
    affilation: str | None = None
    web_page: str | None = None
    address_line_1: str | None = None
    address_line_2: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    submissions: list[SubmissionInDBBase] = []
    reviewer_in: list[ConferenceUser] = []


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: str | None = None


class UserInDBBase(UserBase):
    id: int | None = None
    password: int | None = None


class User(UserInDBBase):
    pass
