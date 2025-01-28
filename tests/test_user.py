import pytest
from utils.user import User


def test_user_creation_with_all_fields():
    user = User(
        first_name="John",
        last_name="Doe",
        email="john@example.com",
        password="password123",
        token="abc123"
    )
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john@example.com"
    assert user.password == "password123"
    assert user.token == "abc123"


def test_user_creation_without_token():
    user = User(
        first_name="Jane",
        last_name="Smith",
        email="jane@example.com",
        password="pass456"
    )
    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.email == "jane@example.com"
    assert user.password == "pass456"
    assert user.token == ""


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


def test_user_dataclass_equality():
    user1 = User("John", "Doe", "john@example.com", "pass123", "token123")
    user2 = User("John", "Doe", "john@example.com", "pass123", "token123")
    assert user1 == user2


def test_user_dataclass_inequality():
    user1 = User("John", "Doe", "john@example.com", "pass123", "token123")
    user2 = User("Jane", "Doe", "john@example.com", "pass123", "token123")
    assert user1 != user2
