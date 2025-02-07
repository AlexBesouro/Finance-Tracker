from fastapi import FastAPI
from app.routers import user, login, income, expenses

app = FastAPI()

app.include_router(user.router)
app.include_router(login.router)
app.include_router(income.router)
app.include_router(expenses.router)

@app.get("/")
async def root():
    return {"home page": "Finance Tracker"}