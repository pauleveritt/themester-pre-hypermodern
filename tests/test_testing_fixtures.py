"""

Themester has fixtures for testing, those fixtures need tests.

"""
from themester.testing.fixtures import ThemesterApp


def test_themester_app(themester_app: ThemesterApp):
    assert themester_app
