from typing import TYPE_CHECKING, List
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from core.models import Base
from conferences.association_tables import reviewer_to_conference


class User(Base):
    email: Mapped[str] = mapped_column(String(255), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow
    )
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.utcnow
    )
    is_super_user: Mapped[bool] = mapped_column(Boolean(), default=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=False)
    title: Mapped[str | None] = mapped_column(String(255))
    first_name: Mapped[str | None] = mapped_column(String(255))
    last_name: Mapped[str | None] = mapped_column(String(255))
    surname: Mapped[str | None] = mapped_column(String(255))
    affilation: Mapped[str | None] = mapped_column(String(255))
    web_page: Mapped[str | None] = mapped_column(String(255))
    address_line_1: Mapped[str | None] = mapped_column(String(255))
    address_line_2: Mapped[str | None] = mapped_column(String(255))
    city: Mapped[str | None] = mapped_column(String(255))
    state: Mapped[str | None] = mapped_column(String(255))
    country: Mapped[str | None] = mapped_column(String(255))
    submissions: Mapped[List["Submission"]] = relationship(
        back_populates="user", lazy="selectin"
    )
    reviewer_in: Mapped[List["Conference"]] = relationship(
        secondary=reviewer_to_conference, back_populates="reviewers", lazy="selectin"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, user_email={self.email!r})"

    def __repr__(self):
        return str(self)
