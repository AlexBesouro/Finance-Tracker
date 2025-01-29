from datetime import date, datetime
from pydantic import BaseModel, EmailStr
from typing_extensions import Optional


class CreateUser(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    current_job: str
    month_salary: float
    gender: Optional[str] = None
    user_birthday: Optional[date] = None

class UserResponse(CreateUser):
    # User : CreateUser
    user_id: int = 1
    # user_created_at: datetime
