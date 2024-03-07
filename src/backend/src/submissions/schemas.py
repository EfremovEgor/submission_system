from datetime import datetime
from pydantic import BaseModel
from conferences.schemas.topic import TopicInDBBase


class ConferenceSubmission(BaseModel):
    id: int | None = None
    name: str | None = None
    acronym: str|None = None

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
    conference: ConferenceSubmission | None = None
    topic_id: int | None = None
    topic: TopicInDBBase = None
    title: str | None = None
    is_ru: bool | None = None
    title_ru: str | None = None
    abstract: str | None = None
    abstract_ru: str | None = None
    keywords: str | None = None
    keywords_ru: str | None = None
    presentation_format: str | None = None
    manuscript: str | None = None
    presentation: str | None = None
    approved: bool | None = None
    authors: list[Author] = []
    created_at: datetime | None = None


class SubmissionCreateIn(BaseModel):
    conference_id: int
    topic_id: int
    is_ru: bool
    title: str
    title_ru: str | None = None
    abstract: str
    abstract_ru: str | None = None
    keywords: str
    keywords_ru: str | None = None
    presentation_format: str
    authors: list[Author]


class SubmissionCreate(SubmissionCreateIn):
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
