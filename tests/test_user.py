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


def test_user_equality():
    user1 = User("John", "Doe", "john@example.com", "pass123", "token1")
    user2 = User("John", "Doe", "john@example.com", "pass123", "token1")
    user3 = User("Jane", "Doe", "jane@example.com", "pass456", "token2")

    assert user1 == user2
    assert user1 != user3


def test_user_repr():
    user = User("John", "Doe", "john@example.com", "pass123", "token1")
    expected = "User(first_name='John', last_name='Doe', email='john@example.com', password='pass123', token='token1')"
    assert repr(user) == expected


def test_user_empty_strings():
    user = User(
        first_name="",
        last_name="",
        email="",
        password="",
        token=""
    )
    assert user.first_name == ""
    assert user.last_name == ""
    assert user.email == ""
    assert user.password == ""
    assert user.token == ""
