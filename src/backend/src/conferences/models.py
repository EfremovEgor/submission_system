from typing import TYPE_CHECKING, List
from sqlalchemy import (
    ForeignKey,
    Boolean,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from core.models import Base
from users.models import User
from .association_tables import reviewer_to_conference


class Conference(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    name: Mapped[str | None] = mapped_column(Text, unique=True)
    name_ru: Mapped[str | None] = mapped_column(Text, unique=True)
    submissions: Mapped[List["Submission"]] = relationship(
        back_populates="conference", lazy="selectin"
    )
    allow_ru: Mapped[bool | None] = mapped_column(Boolean, default=False)
    site_url: Mapped[str | None] = mapped_column(Text)
    description: Mapped[str | None] = mapped_column(Text)
    topics: Mapped[List["Topic"]] = relationship(
        back_populates="conference", lazy="selectin"
    )
    acronym: Mapped[str | None] = mapped_column(Text, unique=True)
    reviewers: Mapped[List["User"]] = relationship(
        secondary=reviewer_to_conference, back_populates="reviewer_in", lazy="selectin"
    )


class Topic(Base):
    name: Mapped[str] = mapped_column(Text)
    conference_id: Mapped[int] = mapped_column(ForeignKey(Conference.id))
    category: Mapped[str | None] = mapped_column(Text)
    conference: Mapped["Conference"] = relationship(
        back_populates="topics", lazy="selectin"
    )
