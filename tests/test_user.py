import pytest

from app import schemas


def test_create_user_success(client):
    response = client.post("/users", json={"email": "aleks@gmail.com",
                                           "password": "pas",
                                           "first_name": "Alex",
                                           "last_name": "Zhukov",
                                           "current_job": "ing",
                                           "gender": None,
                                           "user_birthday": None})
    # res = response.json()
    # assert res["email"] == "aleks@gmail.com"
    res = schemas.UserResponse(**response.json())
    assert response.status_code == 201
    assert res.email == "aleks@gmail.com"
    assert "password" not in response.json()


@pytest.mark.parametrize("email, password, status_code", [("aleks@gmail.com", "password", 409),
                                                          ("leks@gmail.com", None, 422),
                                                          (None, "password", 422),
                                                          ("leks@gmail.com", "pa", 400)])
def test_create_user_unsuccessful(client, test_user, session, email, password, status_code):
    data = {"first_name": "Alex",
           "last_name": "Zhukov",
           "current_job": "ing",
           "gender": None,
           "user_birthday": None}
    if email is not None:
        data["email"] = email
    if password is not None:
        data["password"] = password
    response = client.post("/users/", json=data)

    assert response.status_code == status_code



def test_change_user_success(authorized_client, test_user):
    res = authorized_client.patch("/users", json={"email": "oleks@gmail.com",
                                           "password": "pass",
                                           "first_name": "Alex",
                                           "last_name": "Zhukov",
                                           "current_job": "tech",
                                           "gender": None,
                                           "user_birthday": None})
    assert res.status_code == 200
    res = schemas.UserResponse(**res.json())
    assert res.current_job == "tech"



@pytest.mark.parametrize("email, password, status_code", [("aleks@gmail.com", "password", 409),
                                                          ("leks@gmail.com", None, 422),
                                                          (None, "password", 422),
                                                          ("leks@gmail.com", "p", 400)])
def test_change_user_unsuccessful(authorized_client, test_user, email, password, status_code, client):
    data = {"first_name": "Alex",
           "last_name": "Zhukov",
           "current_job": "ing",
           "gender": None,
           "user_birthday": None}
    if email is not None:
        data["email"] = email
    if password is not None:
        data["password"] = password
    res = authorized_client.patch("/users", json=data)
    assert res.status_code == status_code








