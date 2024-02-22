from pydantic import BaseModel, EmailStr
from submissions.schemas import SubmissionInDBBase
from .topic import TopicForConference, TopicInDBBase


class UserToConferenceBase(BaseModel):
    email: EmailStr | None = None


class UserToConference(UserToConferenceBase):
    id: int


class ConferenceBase(BaseModel):
    user_id: int | None = None
    name: str | None = None
    topics: list[TopicInDBBase] = []
    submissions: list[SubmissionInDBBase] = []
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
