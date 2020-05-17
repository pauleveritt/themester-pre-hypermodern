import pytest

from themester.app import ThemesterApp
from themester.resources import Root


@pytest.fixture
def themester_app() -> ThemesterApp:
    return ThemesterApp(root=Root())
