import pytest
from unittest.mock import mock_open, patch
from utils.helper import get_valid_users_info, get_invalid_users_from_file, get_first_and_last_names_as_parameters


def test_get_valid_users_info_as_dict():
    mock_csv_data = "first_name,last_name,email,password\nJohn,Doe,john.doe@example.com,1234\nJane,Doe,jane.doe@example.com,5678\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = get_valid_users_info(as_parameters=False)
        assert result == [
            {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "password": "1234"},
            {"first_name": "Jane", "last_name": "Doe", "email": "jane.doe@example.com", "password": "5678"},
        ]


def test_get_valid_users_info_as_parameters():
    mock_csv_data = "first_name,last_name,email,password\nJohn,Doe,john.doe@example.com,1234\nJane,Doe,jane.doe@example.com,5678\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = get_valid_users_info(as_parameters=True)
        assert result == [
            ("John", "Doe", "john.doe@example.com", "1234"),
            ("Jane", "Doe", "jane.doe@example.com", "5678"),
        ]


def test_get_invalid_users_from_file():
    mock_csv_data = "email,password\ninvalid1@example.com,wrongpass1\ninvalid2@example.com,wrongpass2\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = get_invalid_users_from_file()
        assert result == [
            {"email": "invalid1@example.com", "password": "wrongpass1"},
            {"email": "invalid2@example.com", "password": "wrongpass2"},
        ]


def test_get_first_and_last_names_as_parameters():
    mock_csv_data = "John,Doe\nJane,Doe\n"
    with patch("builtins.open", mock_open(read_data=mock_csv_data)):
        result = get_first_and_last_names_as_parameters()
        assert result == [("John", "Doe"), ("Jane", "Doe")]
