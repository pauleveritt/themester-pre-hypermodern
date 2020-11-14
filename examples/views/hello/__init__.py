import pytest

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.skip
@pytest.fixture
def views_hello(themester_app):
    from . import views
    themester_app.scanner.scan(views)
