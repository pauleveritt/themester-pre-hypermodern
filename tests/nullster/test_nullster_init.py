from pathlib import Path
from typing import Tuple

import pytest
from venusian import Scanner
from wired import ServiceRegistry

from themester import make_registry, nullster
from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.nullster import wired_setup
from themester.nullster.config import NullsterConfig
from themester.protocols import Root, ThemeConfig
from themester.views import View


@pytest.fixture
def themester_config(themester_site):
    tc = ThemesterConfig(
        root=themester_site,
        theme_config=NullsterConfig(),
        plugins=('themester.nullster',)
    )
    return tc


@pytest.fixture
def nullster_app(themester_site, themester_config):
    na = ThemesterApp(themester_config=themester_config)
    na.setup_plugins()
    return na


@pytest.fixture
def nullster_registry():
    theme_config = NullsterConfig()
    plugins = nullster
    registry = make_registry(
        plugins=plugins,
        theme_config=theme_config,
    )
    return registry


def test_make_registry(nullster_registry):
    from themester.nullster.components.hello_world import HelloWorld
    from themester.nullster.views import AllView
    container = nullster_registry.create_container()
    theme_config = container.get(ThemeConfig)
    assert isinstance(theme_config, NullsterConfig)
    component = container.get(HelloWorld)
    assert component is HelloWorld
    view = container.get(View)
    assert isinstance(view, AllView)
    assert 'Nullster View' == view.name



def test_app_render(nullster_app, themester_site_deep):
    resource = themester_site_deep['d1']
    html = nullster_app.render(resource=resource)
    expected = '<div><h1>Resource: D1</h1><span>Hello Nullster</span></div>'
    assert expected == html


def test_app_get_static_resources(nullster_app):
    nullster_app = nullster_app.themester_config.theme_config
    result: Tuple[Path] = nullster_app.get_static_resources()
    assert 'nullster.css' == result[0].name
