import pytest

from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.protocols import LayoutConfig

pytest_plugins = [
    'themester.testing.fixtures',
]

@pytest.fixture
def themabaster_config():
    tc = ThemabasterConfig(site_name='Testing')
    return tc


@pytest.fixture
def themabaster_app(themester_app, themester_config):
    """ Wire in the themabaster components, views, etc. """

    from themester import themabaster
    themester_app.setup_plugin(themabaster)
    themester_app.registry.register_singleton(themester_config, LayoutConfig)
    return themester_app

