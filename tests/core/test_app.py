import pytest
from venusian import Scanner
from wired import ServiceContainer, ServiceRegistry

from themester import Config, Root
from themester.protocols import App
from themester.testing.fixtures import ThemesterApp

pytest_plugins = [
    'themester.testing.fixtures',
]


def test_themester_app_default(themester_site):
    ta = ThemesterApp(root=themester_site, config=None)
    assert isinstance(ta.registry, ServiceRegistry)
    assert isinstance(ta.container, ServiceContainer)

    app: ThemesterApp = ta.container.get(App)
    assert app.registry == ta.registry
    root: Root = ta.container.get(Root)
    assert root == themester_site
    # Make sure the root/config attributes not on the dataclass instance,
    # as they are InitVars
    with pytest.raises(AttributeError):
        ta.root  # noqa
    scanner: Scanner = ta.container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_themester_app_config(themester_site, themester_config):
    ta = ThemesterApp(root=themester_site, config=themester_config)
    ta_config = ta.container.get(Config)
    assert ta_config == themester_config


def test_themester_app_setup_plugin(themester_site):
    from themester.testing import views
    from themester import View

    ta = ThemesterApp(root=themester_site, config=None)
    ta.setup_plugin(views)
    view = ta.container.get(View)
    assert view.name == 'Fixture View'


def test_themester_app_setup_render_nocontext(themester_site):
    """ Use the app's ``site container`` """
    from themester.testing import views
    ta = ThemesterApp(root=themester_site, config=None)
    ta.setup_plugin(views)
    actual = ta.render()
    assert actual == '<div>View: Fixture View</div>'


def test_themester_app_setup_render_context(themester_site):
    """ The more-common case, make a container for this rendering """
    from themester.testing import views
    ta = ThemesterApp(root=themester_site, config=None)
    ta.setup_plugin(views)
    actual = ta.render(context=themester_site)
    assert actual == '<div>View: Fixture View</div>'
