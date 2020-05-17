import pytest
from venusian import Scanner
from wired import ServiceContainer, ServiceRegistry

from themester.config import Config
from themester.resources import Root
from themester.testing.fixtures import ThemesterApp


# TODO Replace with fixtures
class AppRoot(Root):
    title = 'Site Title'


class AppConfig(Config):
    theme = 'Site Theme'


@pytest.fixture
def app_root():
    return AppRoot()


def test_themester_app_default(app_root):
    ta = ThemesterApp(root=app_root)
    assert isinstance(ta.registry, ServiceRegistry)
    assert isinstance(ta.container, ServiceContainer)

    root: Root = ta.container.get(Root)
    assert root == app_root
    # Make sure the root attribute isn't on the dataclass instance, as it
    # is an InitVar
    with pytest.raises(AttributeError):
        ta.root  # noqa
    scanner: Scanner = ta.container.get(Scanner)
    assert isinstance(scanner, Scanner)
    assert ta.config is None


def test_themester_app_config(app_root):
    config = AppConfig()
    ta = ThemesterApp(root=app_root, config=config)
    assert ta.config == config
    ta_config = ta.container.get(Config)
    assert ta_config == config


def test_themester_app_setup_plugin(app_root):
    from themester.testing import views
    from themester.views import View

    ta = ThemesterApp(root=app_root)
    ta.setup_plugin(views)
    view = ta.container.get(View)
    assert view.name == 'Fixture View'


def test_themester_app_setup_render_nocontainer(app_root):
    from themester.testing import views
    ta = ThemesterApp(root=app_root)
    ta.setup_plugin(views)
    actual = ta.render()
    assert actual == '<div>View: Fixture View</div>'


def test_themester_app_setup_render_container(app_root):
    from themester.testing import views
    ta = ThemesterApp(root=app_root)
    ta.setup_plugin(views)
    container = ta.registry.create_container(context=app_root)
    actual = ta.render(container)
    assert actual == '<div>View: Fixture View</div>'
