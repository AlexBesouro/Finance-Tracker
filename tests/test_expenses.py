import pytest
from app import models


@pytest.mark.parametrize("amount, category, status_code", [(1000.50, "housing", 201),
                                                           (None, "housing", 422),
                                                           (2000.00, None, 422)])
def test_add_expenses(authorized_client, test_user, amount, category, status_code):
    data = {}
    if amount is not None:
        data["amount"] = amount
    if category is not None:
        data["category"] = category

    res = authorized_client.post("/expenses", json=data)
    assert res.status_code == status_code


def test_add_income_unauthorized(client):
    res = client.post("/expenses", json={"amount": 500, "category": "other"})
    assert res.status_code == 401

def test_add_income_nonexistent_user(authorized_client, session, test_user):
    session.query(models.User).delete()
    session.commit()
    res = authorized_client.post("/expenses", json={"expenses": 1200, "category": "other"})
    assert res.status_code == 404