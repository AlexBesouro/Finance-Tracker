from datetime import date, datetime
from enum import Enum as PyEnum
from sqlalchemy import Enum, TIMESTAMP, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from app.database import engine


class Base(DeclarativeBase):
    pass

class Gender(PyEnum):
    male = "male"
    female = "female"

class User(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column( nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    current_job: Mapped[str] = mapped_column(nullable=False)
    month_salary: Mapped[float] = mapped_column(nullable=False)
    user_birthday: Mapped[date] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=True)
    user_created_at: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=text("NOW()"))


# SQLAlchemy way to create tables
# def create_tables():
#     Base.metadata.create_all(bind=engine)
#     print("✅ Tables created successfully!")
#
# # Run this function once to create tables
# create_tables()