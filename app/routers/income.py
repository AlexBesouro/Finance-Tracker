from fastapi import APIRouter, Depends, HTTPException
from app import auth
from sqlalchemy.orm import Session
from app import schemas
from app import models
from app.database import get_db

router = APIRouter(prefix="/income", tags=["income"])

@router.post("/", status_code=201, response_model=schemas.IncomeResponse)
def add_income(income:schemas.Income, db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    user = db.query(models.User).filter(models.User.user_id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_income = models.Income(**income.model_dump())
    new_income.user_id = current_user.user_id
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income