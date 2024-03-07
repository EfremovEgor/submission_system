from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}

    id: Mapped[int] = mapped_column(primary_key=True)
