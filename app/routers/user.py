from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas
from app import models
from app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", status_code=201, response_model=schemas.UserResponse)
def create_user(user:schemas.CreateUser, db: Session = Depends(get_db)):
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user