from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey, Boolean, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from core.models import Base
from users.models import User
from .association_tables import (
    reviewer_to_conference,
    reviewer_to_topic,
    chair_to_conference,
)
import datetime


class Conference(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    name: Mapped[str | None] = mapped_column(Text, unique=True)
    name_ru: Mapped[str | None] = mapped_column(Text, unique=True)
    name_ru_dative: Mapped[str | None] = mapped_column(Text)
    submissions: Mapped[List["Submission"]] = relationship(
        back_populates="conference", lazy="selectin"
    )
    allow_ru: Mapped[bool | None] = mapped_column(Boolean, default=False)
    site_url: Mapped[str | None] = mapped_column(Text)
    email: Mapped[str | None] = mapped_column(Text)
    description: Mapped[str | None] = mapped_column(Text)
    topics: Mapped[List["Topic"]] = relationship(
        back_populates="conference", lazy="selectin"
    )
    submission_deadline: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    start_date: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    acronym: Mapped[str | None] = mapped_column(Text, unique=True)
    short_name: Mapped[str | None] = mapped_column(Text, unique=True)
    reviewers: Mapped[List["User"]] = relationship(
        secondary=reviewer_to_conference,
        back_populates="reviewer_in",
        lazy=False,
    )
    chairs: Mapped[List["User"]] = relationship(
        secondary=chair_to_conference,
        back_populates="chair_in",
        lazy=False,
    )


class Topic(Base):
    name: Mapped[str] = mapped_column(Text)
    name_ru: Mapped[str | None] = mapped_column(Text)
    conference_id: Mapped[int] = mapped_column(ForeignKey(Conference.id))
    category: Mapped[str | None] = mapped_column(Text)
    category_ru: Mapped[str | None] = mapped_column(Text)
    reviewers: Mapped[List["User"]] = relationship(
        secondary=reviewer_to_topic,
        back_populates="reviewer_in_topics",
        lazy=False,
    )
    conference: Mapped["Conference"] = relationship(
        back_populates="topics", lazy="joined"
    )
