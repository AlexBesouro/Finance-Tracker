from fastapi import FastAPI
from app.routers import user, login

app = FastAPI()

app.include_router(user.router)
app.include_router(login.router)

@app.get("/")
async def root():
    return {"home page": "Finance Tracker"}