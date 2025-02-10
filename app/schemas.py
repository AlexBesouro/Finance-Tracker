from datetime import date, datetime
from typing import List, Literal

from pydantic import BaseModel, EmailStr
from typing_extensions import Optional
from enum import Enum as PyEnum


class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class UserCredentials(BaseModel):
    email: EmailStr
    password: str

class CreateUser(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    current_job: str
    gender: Optional[str] = None
    user_birthday: Optional[date] = None

class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    first_name: str
    last_name: str
    current_job: str
    gender: Optional[str] = None
    user_birthday: Optional[date] = None
    user_created_at: datetime

    class Config:
        from_attributes = True

class Income(BaseModel):
    amount: float
    category: str

class IncomeResponse(BaseModel):
    id: int
    user_id: int
    amount: float
    category: str
    added_at: date


class Category(BaseModel):
    category: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None

class ExpenseCategorySummary(BaseModel):
    category: str
    total_amount: float
    start_date: date
    end_date: date