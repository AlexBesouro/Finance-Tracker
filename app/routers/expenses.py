from fastapi import APIRouter, Depends, HTTPException
from app import auth
from sqlalchemy.orm import Session
from app import schemas
from app import models
from app.database import get_db

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", status_code=201, response_model=schemas.IncomeResponse)
def add_expenses(expenses:schemas.Income, db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    user = db.query(models.User).filter(models.User.user_id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_expenses = models.Expenses(**expenses.model_dump())
    new_expenses.user_id = current_user.user_id
    db.add(new_expenses)
    db.commit()
    db.refresh(new_expenses)
    return new_expenses