from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings

# NOT SECURE AND STATIC WAY
# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:admin@localhost:5432/finance_tracker"

SQLALCHEMY_DATABASE_URL = (f"postgresql://{settings.database_username}:{settings.database_password}@"
                           f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()