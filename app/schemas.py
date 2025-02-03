from datetime import date, datetime
from pydantic import BaseModel, EmailStr
from typing_extensions import Optional


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
    month_salary: float
    gender: Optional[str] = None
    user_birthday: Optional[date] = None

class UserResponse(BaseModel):
    user_id: int
    email: EmailStr
    first_name: str
    last_name: str
    current_job: str
    month_salary: float
    gender: Optional[str] = None
    user_birthday: Optional[date] = None
    user_created_at: datetime

    class Config:
        from_attributes = True

class UpdateUser(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    current_job: str
    month_salary: float
    gender: Optional[str] = None
    user_birthday: Optional[date] = None