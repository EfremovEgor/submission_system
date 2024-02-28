from sqlalchemy import Column, ForeignKey, Table

from core.models import Base


reviewer_to_conference = Table(
    "reviewer_to_conference",
    Base.metadata,
    Column("conference_id", ForeignKey("conferences.id"), primary_key=True),
    Column("reviewer_id", ForeignKey("users.id"), primary_key=True),
)
