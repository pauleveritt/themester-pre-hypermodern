import pytest

from themester.config import ThemesterConfig
from themester.themabaster import ThemabasterConfig


@pytest.fixture
def themester_config():
    tc = ThemesterConfig(
        theme_config=ThemabasterConfig(),
        plugins=('themester.themabaster',)
    )
    return tc
