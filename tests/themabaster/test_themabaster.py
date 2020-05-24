import pytest
from bs4 import BeautifulSoup

from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.protocols import LayoutConfig


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


def test_themabaster_components_layouts(themabaster_app):
    result = themabaster_app.render()
    soup = BeautifulSoup(result, 'html.parser')
    actual = soup.select_one('section h1').text
    assert actual == 9
