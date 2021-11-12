"""Test cases for the __main__ module."""
from themester import foo


def test_main_succeeds() -> None:
    """It exits with a status code of zero."""
    assert foo() == 9
