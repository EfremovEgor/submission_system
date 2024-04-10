from sqlalchemy import Column, ForeignKey, Table

from core.models import Base


reviewer_to_conference = Table(
    "reviewer_to_conference",
    Base.metadata,
    Column("conference_id", ForeignKey("conferences.id"), primary_key=True),
    Column("reviewer_id", ForeignKey("users.id"), primary_key=True),
)
reviewer_to_topic = Table(
    "reviewer_to_topic",
    Base.metadata,
    Column("topic_id", ForeignKey("topics.id"), primary_key=True),
    Column("reviewer_id", ForeignKey("users.id"), primary_key=True),
)
chair_to_conference = Table(
    "chair_to_conference",
    Base.metadata,
    Column("conference_id", ForeignKey("conferences.id"), primary_key=True),
    Column("chair_id", ForeignKey("users.id"), primary_key=True),
)
