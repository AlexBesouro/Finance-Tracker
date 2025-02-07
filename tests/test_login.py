import pytest


def test_login(test_user, client):
    res = client.post("/login", json={"email": test_user["email"], "password": test_user["password"]})
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [("aleks@gmail.com", "wrong password", 401),
                                                          ("wrong@gmail.com", "pass", 401),
                                                          ("wrong@gmail.com", "wrong password", 401),
                                                          (None, "pass", 422),
                                                          ("aleks@gmail.com", None, 422)])
def test_failed_login(test_user, client, email, password, status_code):
    data = {}
    if email is not None:
        data["email"] = email
    if password is not None:
        data["password"] = password
    res = client.post("/login", json=data)
    assert res.status_code == status_code