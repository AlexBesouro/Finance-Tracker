from app import auth
import pytest
from passlib.crypto.digest import mock_fips_mode
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app import models
from app.auth import get_current_user
from app.database import settings, get_db
from app import main

SQLALCHEMY_DATABASE_URL = (f"postgresql://{settings.database_username}:{settings.database_password}@"
                           f"{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

test_session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)


@pytest.fixture
def session():
    print("session runs")
    models.Base.metadata.drop_all(bind=engine)
    models.Base.metadata.create_all(bind=engine)
    db = test_session_local()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    main.app.dependency_overrides[get_db] = override_get_db
    return TestClient(main.app)


@pytest.fixture
def test_user(client):
    mock_user = {"email": "aleks@gmail.com",
                 "password": "pass",
                 "first_name": "Alex",
                 "last_name": "Zhukov",
                 "current_job": "ing",
                 "gender": None,
                 "user_birthday": None}
    res = client.post('/users', json=mock_user)
    res = res.json()
    res["password"] = mock_user["password"] # Adding password to an answer from DB
    return res

@pytest.fixture
def authorized_client(client, test_user):
    token = auth.create_access_token(data={"user_email": test_user["email"]})
    client.headers.update({"Authorization": f"Bearer {token}"})
    return client