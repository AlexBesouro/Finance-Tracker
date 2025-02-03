import jwt
from datetime import datetime, timedelta, timezone
from typing import Optional

from sqlalchemy.orm import Session

from app import models
from app.config import settings
from fastapi import Depends, status, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer

from app.database import get_db

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
EXPIRE_TIME = settings.expire_time

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    to_encode = data.copy()
    expire_time = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_TIME)
    to_encode.update({"exp": expire_time})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt

def verify_token(token:str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None


def get_current_user(token: str = Security(oauth2_schema), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    user = db.query(models.User).filter(models.User.email == payload["user_email"]).first()
    print(user)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    print(user.__dict__)
    return user