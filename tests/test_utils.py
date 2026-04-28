from utils import fmt

def test_fmt():
    assert fmt(1.0) == "1"
    assert fmt(1.5) == "1.5"