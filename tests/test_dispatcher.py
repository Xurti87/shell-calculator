import pytest
from dispatcher import dispatch


def test_dispatch():
    assert dispatch("+", ["3", "2"]) == ("5")


def test_value_error():
    with pytest.raises(ValueError):
        dispatch("@", ["3", "2"])
