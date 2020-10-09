from pathlib import Path
from typing import Tuple

import pytest
from venusian import Scanner
from wired import ServiceRegistry

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.nullster import wired_setup
from themester.nullster.config import NullsterConfig
from themester.protocols import Root
from themester.views import View


@pytest.fixture
def themester_config():
    tc = ThemesterConfig(
        theme_config=NullsterConfig(),
        plugins=('themester.nullster',)
    )
    return tc


@pytest.fixture
def nullster_app(themester_site, themester_config):
    na = ThemesterApp(themester_config=themester_config)
    na.setup_plugins()
    na.registry.register_singleton(themester_site, Root)
    return na


def test_wired_setup():
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    wired_setup(registry, scanner)


def test_app_default(nullster_app, themester_site):
    assert isinstance(nullster_app.registry, ServiceRegistry)
    assert isinstance(nullster_app.scanner, Scanner)

    container = nullster_app.registry.create_container()
    app: ThemesterApp = container.get(ThemesterApp)
    assert app.registry == nullster_app.registry
    container_root: Root = container.get(Root)
    assert themester_site is container_root
    scanner: Scanner = container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_app_get_view(nullster_app):
    container = nullster_app.registry.create_container()
    view = container.get(View)
    assert 'Nullster View' == view.name


def test_app_render(nullster_app, themester_site_deep):
    resource = themester_site_deep['d1']
    html = nullster_app.render(resource=resource)
    expected = '<div><h1>Resource: D1</h1><span>Hello Nullster</span></div>'
    assert expected == html


def test_app_get_static_resources(nullster_app):
    nullster_app = nullster_app.themester_config.theme_config.sphinx
    result: Tuple[Path] = nullster_app.get_static_resources()
    assert 'nullster.css' == result[0].name
