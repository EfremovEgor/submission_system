from pydantic import BaseModel, EmailStr
from datetime import datetime
from conferences.schemas.conference import UserToConference
from conferences.schemas.topic import TopicInDBBase
from submissions.schemas import SubmissionInDBBase


class ConferenceUser(BaseModel):
    id: int
    name: str | None = None
    acronym: str | None = None


class UserBase(BaseModel):
    id: int
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
    orcid_id: str | None = None
    city: str | None = None
    state: str | None = None
    country: str | None = None
    submissions: list[SubmissionInDBBase] = []
    reviewer_in: list[ConferenceUser] = []
    chair_in: list[ConferenceUser] = []
    reviewer_in_topics: list[TopicInDBBase] = []


class UserCreate(BaseModel):
    id: int| None = None
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    id: int| None = None
    password: str | None = None
    submissions: list[SubmissionInDBBase] | None  = None
    reviewer_in: list[ConferenceUser] | None  = None
    chair_in: list[ConferenceUser] | None   = None

class UserInDBBase(UserBase):
    id: int | None = None
    password: int | None = None


class User(UserInDBBase):
    pass
