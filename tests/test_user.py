import pytest
from utils.user import User


def test_user_creation_with_required_fields():
    user = User(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123"
    )

    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john@example.com"
    assert user.password == "password123"
    assert user.token == ""


def test_user_creation_with_token():
    user = User(
        first_name="Jane",
        last_name="Smith",
        email="jane@example.com",
        password="pass456",
        token="abc123"
    )

    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.email == "jane@example.com"
    assert user.password == "pass456"
    assert user.token == "abc123"


def test_user_creation_with_empty_strings():
    user = User(
        first_name="",
        last_name="",
        email="",
        password=""
    )

    assert user.first_name == ""
    assert user.last_name == ""
    assert user.email == ""
    assert user.password == ""
    assert user.token == ""


def test_user_attributes_are_mutable():
    user = User(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123"
    )

    user.first_name = "Jane"
    user.last_name = "Smith"
    user.email = "jane@example.com"
    user.password = "newpass"
    user.token = "newtoken"

    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.email == "jane@example.com"
    assert user.password == "newpass"
    assert user.token == "newtoken"
