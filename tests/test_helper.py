import csv
import pytest
from unittest.mock import mock_open, patch

from utils.helper import (
    get_valid_users_info,
    get_invalid_users_from_file,
    get_first_and_last_names_as_parameters
)

@pytest.fixture
def valid_users_csv():
    return """first_name,last_name,email,password
John,Doe,john@example.com,password123
Jane,Smith,jane@example.com,password456"""

@pytest.fixture
def invalid_users_csv():
    return """first_name,last_name,email,password
John,,invalid@email,short"""

@pytest.fixture
def names_csv():
    return """John,Doe
Jane,Smith"""

def test_get_valid_users_info_as_dict(valid_users_csv):
    with patch("builtins.open", mock_open(read_data=valid_users_csv)):
        users = get_valid_users_info(as_parameters=False)
        assert len(users) == 2
        assert users[0]["first_name"] == "John"
        assert users[0]["last_name"] == "Doe"
        assert users[0]["email"] == "john@example.com"
        assert users[0]["password"] == "password123"

def test_get_valid_users_info_as_parameters(valid_users_csv):
    with patch("builtins.open", mock_open(read_data=valid_users_csv)):
        users = get_valid_users_info(as_parameters=True)
        assert len(users) == 2
        assert users[0] == ("John", "Doe", "john@example.com", "password123")

def test_get_invalid_users_from_file(invalid_users_csv):
    with patch("builtins.open", mock_open(read_data=invalid_users_csv)):
        users = get_invalid_users_from_file()
        assert len(users) == 1
        assert users[0]["first_name"] == "John"
        assert users[0]["last_name"] == ""
        assert users[0]["email"] == "invalid@email"
        assert users[0]["password"] == "short"

def test_get_first_and_last_names_as_parameters(names_csv):
    with patch("builtins.open", mock_open(read_data=names_csv)):
        names = get_first_and_last_names_as_parameters()
        assert len(names) == 2
        assert names[0] == ("John", "Doe")
        assert names[1] == ("Jane", "Smith")

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        with patch("builtins.open", mock_open()) as mock_file:
            mock_file.side_effect = FileNotFoundError()
            get_valid_users_info()
