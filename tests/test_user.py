import pytest
from utils.user import User

def test_user_initialization():
    user = User(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        password="securepassword123"
    )
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.password == "securepassword123"
    assert user.token == ""

def test_user_initialization_with_token():
    user = User(
        first_name="Jane",
        last_name="Smith",
        email="jane.smith@example.com",
        password="anothersecurepassword",
        token="sometoken123"
    )
    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
    assert user.email == "jane.smith@example.com"
    assert user.password == "anothersecurepassword"
    assert user.token == "sometoken123"
