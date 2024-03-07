from pydantic import BaseModel


class TopicForConference(BaseModel):
    name: str


class TopicBase(BaseModel):
    name: str | None = None
    conference_id: int | None = None
    category: str | None = None


class TopicCreate(TopicBase):
    name: str
    conference_id: int


class TopicUpdate(TopicBase):
    name: str | None = None
    conference_id: int | None = None


class TopicInDBBase(TopicBase):
    id: int | None = None


class Topic(TopicInDBBase):
    pass
