from datetime import datetime
from pydantic import BaseModel
from conferences.schemas.topic import TopicInDBBase


class Author(BaseModel):
    first_name: str
    last_name: str
    surname: str | None = None
    email: str
    country: str
    affilation: str
    web_page: str | None = None
    is_presenter: bool = False


class SubmissionBase(BaseModel):
    user_id: int | None = None
    conference_id: int | None = None
    topic_id: int | None = None
    topic: TopicInDBBase = None
    title: str | None = None
    abstract: str | None = None
    keywords: str | None = None
    presentation_format: str | None = None
    manuscript: str | None = None
    presentation: str | None = None
    approved: bool | None = None
    authors: list[Author] = []
    created_at: datetime | None = None


class SubmissionCreateIn(BaseModel):
    conference_id: int
    topic_id: int
    title: str
    abstract: str
    keywords: str
    presentation_format: str
    authors: list[Author]


class SubmissionCreate(SubmissionBase):
    user_id: int
    conference_id: int
    topic_id: int
    title: str
    abstract: str
    presentation_format: str
    keywords: str


class SubmissionUpdate(SubmissionBase):
    pass


class SubmissionInDBBase(SubmissionBase):
    id: int | None = None


class Submission(SubmissionInDBBase):
    pass
