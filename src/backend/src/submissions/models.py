from typing import TYPE_CHECKING, List
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from core.models import Base
from conferences.models import Conference, Topic
from users.models import User


class Submission(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    user: Mapped["User"] = relationship(back_populates="submissions", lazy="selectin")
    conference_id: Mapped[int] = mapped_column(ForeignKey(Conference.id))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow
    )
    conference: Mapped["Conference"] = relationship(
        back_populates="submissions", lazy="selectin"
    )
    topic_id: Mapped[int] = mapped_column(ForeignKey(Topic.id))
    topic: Mapped["Topic"] = relationship(lazy="selectin")
    title: Mapped[str] = mapped_column(Text)
    abstract: Mapped[str] = mapped_column(Text)
    keywords: Mapped[str] = mapped_column(Text)
    presentation_format: Mapped[str | None] = mapped_column(Text)
    manuscript: Mapped[str | None] = mapped_column(Text)
    presentation: Mapped[str | None] = mapped_column(Text)
    approved: Mapped[Boolean] = mapped_column(Boolean, default=False)
    authors: Mapped[List["Author"]] = relationship(
        back_populates="submission", lazy="selectin"
    )


class Author(Base):
    first_name: Mapped[str | None] = mapped_column(String(255))
    last_name: Mapped[str | None] = mapped_column(String(255))
    surname: Mapped[str | None] = mapped_column(String(255))
    email: Mapped[str | None] = mapped_column(String(255))
    country: Mapped[str | None] = mapped_column(String(255))
    affilation: Mapped[str | None] = mapped_column(String(255))
    web_page: Mapped[str | None] = mapped_column(String(255))
    is_presenter: Mapped[bool | None] = mapped_column(Boolean, default=False)
    submission_id: Mapped[int] = mapped_column(ForeignKey(Submission.id))
    submission: Mapped["Submission"] = relationship(
        back_populates="authors", lazy="selectin"
    )
