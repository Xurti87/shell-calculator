import pytest
from parser import parse


def test_parse_command():
    assert parse("3 + 2") == ("+", ["3", "2"])
    assert parse("3+2") == ("+", ["3", "2"])
    assert parse("3 +2") == ("+", ["3", "2"])
    assert parse("3+ 2") == ("+", ["3", "2"])


def test_value_error():
    with pytest.raises(ValueError):
        parse("foo")
