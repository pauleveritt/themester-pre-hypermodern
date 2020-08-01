import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def views_context(themester_app):
    from . import views
    themester_app.scanner.scan(views)
