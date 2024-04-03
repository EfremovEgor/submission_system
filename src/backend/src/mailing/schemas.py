from pydantic import BaseModel
from submissions.schemas import Author


class SubmissionEmailData(BaseModel):
    submission_id: int
    conference_email: str
    conference_short_name: str
    conference_name: str
    corresponding_title: str
    first_name: str
    last_name: str
    title: str
    presentation_format: str
    topic: str
    authors: list[Author]
