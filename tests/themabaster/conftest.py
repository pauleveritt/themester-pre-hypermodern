import pytest
from bs4 import BeautifulSoup
from viewdom import render

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
def themabaster_app(themester_app, themabaster_config):
    """ Wire in the themabaster components, views, etc. """

    from themester import themabaster
    themester_app.setup_plugin(themabaster)
    themester_app.registry.register_singleton(themabaster_config, LayoutConfig)
    return themester_app


@pytest.fixture
def this_vdom(this_component):
    vdom = this_component()
    return vdom


@pytest.fixture
def this_html(this_vdom):
    rendered = render(this_vdom)
    html = BeautifulSoup(rendered, 'html.parser')
    return html


@pytest.fixture
def this_container(themester_app, themester_scanner, this_props, these_modules):
    """ Load  """
    [themester_scanner.scan(this_module) for this_module in these_modules]
    this_resource = this_props.get('resource', None)
    this_container = themester_app.container.bind(context=this_resource)
    return this_container
