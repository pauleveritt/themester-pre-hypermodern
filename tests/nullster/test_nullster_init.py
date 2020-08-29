import pytest
from venusian import Scanner
from wired import ServiceRegistry

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.nullster import wired_setup
from themester.protocols import Root
from themester.views import View


@pytest.fixture
def nullster_config():
    tc = ThemesterConfig(
        plugins=('themester.nullster',)
    )
    return tc


def test_wired_setup():
    registry = ServiceRegistry()
    scanner = Scanner(registry=registry)
    wired_setup(registry, scanner)


def test_app_default(nullster_config):
    themester_app = ThemesterApp(themester_config=nullster_config)
    assert isinstance(themester_app.registry, ServiceRegistry)
    assert isinstance(themester_app.scanner, Scanner)

    container = themester_app.registry.create_container()
    app: ThemesterApp = container.get(ThemesterApp)
    assert app.registry == themester_app.registry
    container_root: Root = container.get(Root)
    assert None is container_root
    scanner: Scanner = container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_app_get_view(nullster_config):
    themester_app = ThemesterApp(themester_config=nullster_config)
    themester_app.setup_plugins()
    container = themester_app.registry.create_container()
    view = container.get(View)
    assert 'Nullster View' == view.name
    container_root: Root = container.get(Root)
    assert None is container_root


def test_app_render(nullster_config):
    themester_app = ThemesterApp(themester_config=nullster_config)
    themester_app.setup_plugins()
    html = themester_app.render()
    assert '<div>Hello World</div>' == html
