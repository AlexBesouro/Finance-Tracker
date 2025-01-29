from fastapi import FastAPI
from app.routers import user
app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"home page": "Finance Tracker"}