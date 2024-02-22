from typing import TYPE_CHECKING, List
from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Boolean,
    Text,
    Table,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from core.models import Base
from users.models import User
from .association_tables import user_to_conference


class Conference(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    name: Mapped[str | None] = mapped_column(Text, unique=True)
    submissions: Mapped[List["Submission"]] = relationship(
        back_populates="conference", lazy="selectin"
    )
    topics: Mapped[List["Topic"]] = relationship(
        back_populates="conference", lazy="selectin"
    )

    reviewers: Mapped[List["User"]] = relationship(
        secondary=user_to_conference, back_populates="reviewer_in", lazy="selectin"
    )


class Topic(Base):
    name: Mapped[str] = mapped_column(Text)
    conference_id: Mapped[int] = mapped_column(ForeignKey(Conference.id))
    conference: Mapped["Conference"] = relationship(
        back_populates="topics", lazy="selectin"
    )
