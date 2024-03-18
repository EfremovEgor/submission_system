from pydantic import BaseModel, EmailStr
from submissions.schemas import SubmissionInDBBase
from .topic import TopicForConference, TopicInDBBase
import datetime


class UserToConferenceBase(BaseModel):
    email: EmailStr | None = None


class UserToConference(UserToConferenceBase):
    id: int


class ConferenceBase(BaseModel):
    user_id: int | None = None
    name: str | None = None
    name_ru: str | None = None
    allow_ru: bool | None = None
    acronym: str | None = None
    short_name: str | None = None
    description: str | None = None
    site_url: str | None = None
    topics: list[TopicInDBBase] = []
    submission_deadline: datetime.datetime | None = None
    start_date: datetime.datetime | None = None
    # submissions: list[SubmissionInDBBase] = []
    reviewers: list[UserToConference] = []


class ConferenceCreateIn(BaseModel):
    name: str
    topics: list[TopicForConference]
    reviewers: list[UserToConferenceBase]


class ConferenceCreate(ConferenceCreateIn):
    user_id: int


class ConferenceUpdate(ConferenceBase):
    user_id: int | None = None
    name: str | None = None
    reviewers: list[EmailStr] = []


class ConferenceInDBBase(ConferenceBase):
    id: int | None = None


class Conference(ConferenceInDBBase):
    pass
