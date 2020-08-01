import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def views_named(themester_app):
    from . import views
    themester_app.scanner.scan(views)
