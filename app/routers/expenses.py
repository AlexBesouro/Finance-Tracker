import matplotlib.pyplot as plt
import io
from fastapi.responses import Response
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func

from app import auth
from sqlalchemy.orm import Session
from app import schemas
from app import models
from app.database import get_db

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", status_code=201, response_model=schemas.IncomeResponse)
def add_expenses(expenses:schemas.Income, db: Session = Depends(get_db),
                current_user: models.User = Depends(auth.get_current_user)):
    print(expenses)
    user = db.query(models.User).filter(models.User.user_id == current_user.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_expenses = models.Expenses(**expenses.model_dump())
    new_expenses.user_id = current_user.user_id
    db.add(new_expenses)
    db.commit()
    db.refresh(new_expenses)
    return new_expenses

@router.get("/", response_model=schemas.ExpenseCategorySummary)
def get_expenses_by_category(category_name: schemas.Category,  db: Session = Depends(get_db),
                             current_user: models.User = Depends(auth.get_current_user)):
    expenses_by_category = (db.query(models.Expenses.category, func.sum(models.Expenses.amount).label("total_amount"))
                            .filter(models.Expenses.user_id == current_user.user_id)
                            .filter(models.Expenses.category == category_name.category))
    if category_name.start_date:
        expenses_by_category = expenses_by_category.filter(models.Expenses.added_at >= category_name.start_date)
    if category_name.end_date:
        expenses_by_category = expenses_by_category.filter(models.Expenses.added_at <= category_name.end_date)
    expenses_by_category = expenses_by_category.group_by(models.Expenses.category).first()

    if not expenses_by_category:
        raise HTTPException(status_code=404, detail="No expenses found")
    print(expenses_by_category)
    return expenses_by_category



# Graph try
@router.get("/graph", response_class=Response)
def get_expenses_graph(category_name: schemas.Category,
                       db: Session = Depends(get_db),
                       current_user: models.User = Depends(auth.get_current_user)):

    expenses_by_category = (db.query(models.Expenses.category,
                                     func.sum(models.Expenses.amount).label("total_amount"))
                            .filter(models.Expenses.user_id == current_user.user_id)
                            .filter(models.Expenses.category == category_name.category))

    if category_name.start_date:
        expenses_by_category = expenses_by_category.filter(models.Expenses.added_at >= category_name.start_date)
    if category_name.end_date:
        expenses_by_category = expenses_by_category.filter(models.Expenses.added_at <= category_name.end_date)

    expenses_by_category = expenses_by_category.group_by(models.Expenses.category).all()

    if not expenses_by_category:
        raise HTTPException(status_code=404, detail="No expenses found")


    categories = [str(expense[0]) for expense in expenses_by_category]
    amounts = [expense[1] for expense in expenses_by_category]


    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color="blue")
    plt.xlabel("Category")
    plt.ylabel("Total Amount")
    plt.title("Expenses by Category")


    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)

    return Response(content=buf.getvalue(), media_type="image/png")
