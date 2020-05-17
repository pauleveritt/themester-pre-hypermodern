import pytest
from venusian import Scanner
from wired import ServiceContainer, ServiceRegistry

from themester import Config, Root
from themester.testing.fixtures import ThemesterApp


def test_themester_app_default(themester_site):
    ta = ThemesterApp(root=themester_site, config=None)
    assert isinstance(ta.registry, ServiceRegistry)
    assert isinstance(ta.container, ServiceContainer)

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


def test_themester_app_setup_render_nocontainer(themester_site):
    from themester.testing import views
    ta = ThemesterApp(root=themester_site, config=None)
    ta.setup_plugin(views)
    actual = ta.render()
    assert actual == '<div>View: Fixture View</div>'


def test_themester_app_setup_render_container(themester_site):
    from themester.testing import views
    ta = ThemesterApp(root=themester_site, config=None)
    ta.setup_plugin(views)
    container = ta.registry.create_container(context=themester_site)
    actual = ta.render(container)
    assert actual == '<div>View: Fixture View</div>'
