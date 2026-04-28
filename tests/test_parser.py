import pytest

from shell_parser import parse_command

def test_parse_command():
    assert parse_command("3 + 2") == ("+", ["3", "2"])
    assert parse_command("3+2") == ("+", ["3", "2"])

def test_value_error():
    with pytest.raises(ValueError):
        parse_command("foo")