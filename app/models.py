from datetime import date, datetime
from enum import Enum as PyEnum
from sqlalchemy import Enum, TIMESTAMP, text, DATE, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# SQLAlchemy way to create tables
# from app.database import engine
# def create_tables():
#     Base.metadata.create_all(bind=engine)
#     print("✅ Tables created successfully!")
#
# # Run this function once to create tables
# create_tables()

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
    user_birthday: Mapped[date] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(Enum(Gender), nullable=True)
    user_created_at: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=text("NOW()"))


class Income(Base):
    __tablename__ = "income"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[str] = mapped_column(nullable=False)
    added_at: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=text("NOW()"))


class ExpensesCategory(PyEnum):
    groceries = "groceries"
    utilities = "utilities"
    housing = "housing"
    transportation = "transportation"
    entertainment = "entertainment"
    hobby = "hobby"
    medical = "medical"
    vacation = "vacation"
    other = "other"

expenses_category_enum = Enum(ExpensesCategory, name="expenses_category", create_type=False)

class Expenses(Base):
    __tablename__ = "expenses"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    category: Mapped[ExpensesCategory] = mapped_column(expenses_category_enum, nullable=False)
    added_at: Mapped[datetime] = mapped_column(DATE, nullable=False, server_default=text("NOW()"))