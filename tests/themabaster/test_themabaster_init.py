from pathlib import Path
from typing import Tuple

import pytest
from venusian import Scanner
from wired import ServiceRegistry

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.protocols import Root, View
from themester.themabaster import wired_setup
from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.views import PageView


@pytest.fixture
def themabaster_config():
    tc = ThemesterConfig(
        theme_config=ThemabasterConfig(),
        plugins=('themester.themabaster',)
    )
    return tc


@pytest.fixture
def themabaster_app(themabaster_config):
    na = ThemesterApp(themester_config=themabaster_config)
    na.setup_plugins()
    return na


def test_wired_setup(themabaster_config):
    registry = ServiceRegistry()
    registry.register_singleton(themabaster_config, ThemesterConfig)
    scanner = Scanner(registry=registry)
    wired_setup(registry, scanner)


def test_app_default(themabaster_app):
    assert isinstance(themabaster_app.registry, ServiceRegistry)
    assert isinstance(themabaster_app.scanner, Scanner)

    container = themabaster_app.registry.create_container()
    app: ThemesterApp = container.get(ThemesterApp)
    assert app.registry == themabaster_app.registry
    container_root: Root = container.get(Root)
    assert None is container_root
    scanner: Scanner = container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_app_get_view(themabaster_app):
    container = themabaster_app.registry.create_container()
    view = container.get(View)
    assert PageView == view.__class__
    container_root: Root = container.get(Root)
    assert None is container_root


def test_app_render(themabaster_app, html_config, sphinx_config, this_pagecontext):
    r = themabaster_app.registry
    r.register_singleton(sphinx_config, sphinx_config.__class__)
    r.register_singleton(html_config, html_config.__class__)
    r.register_singleton(this_pagecontext, this_pagecontext.__class__)
    html = themabaster_app.render()
    assert '<title>Some Page - Themester' in html


def test_app_get_static_resources(themabaster_app):
    themabaster_app = themabaster_app.themester_config.theme_config.sphinx
    result: Tuple[Path] = themabaster_app.get_static_resources()
    assert 'themabaster.css' == result[0].name
