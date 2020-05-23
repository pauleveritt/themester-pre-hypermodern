from dataclasses import dataclass

import pytest
from venusian import Scanner
from wired import ServiceContainer, ServiceRegistry

from themester import Config, Root
from themester.protocols import App
from themester.testing.fixtures import ThemesterApp
from themester.views import register_view

pytest_plugins = [
    'themester.testing.fixtures',
]


class Customer:
    name = 'Some Customer'


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


def test_themester_app_render_nocontext(themester_app):
    """ Use the app's ``site container`` """

    expected = 'Hello somecustomer'

    @dataclass
    class NoContextView:

        def __call__(self):
            return expected

    register_view(themester_app.registry, NoContextView)

    # Fail with context
    with pytest.raises(LookupError):
        themester_app.render(context=Customer())

    # Succeed with no context
    actual = themester_app.render()
    assert actual == expected


def test_themester_app_render_context(themester_app):
    """ The more-common case, make a context for this rendering """

    expected = 'Hello somecustomer'

    @dataclass
    class ContextView:

        def __call__(self):
            return expected

    register_view(themester_app.registry, ContextView, context=Customer)
    # Fail with no context
    with pytest.raises(LookupError):
        themester_app.render()

    # Succeed with context
    actual = themester_app.render(context=Customer())
    assert actual == expected


def test_themester_app_render_container(themester_app):
    """ Provide a per-render container

     The ``TemplateBridge`` wants Sphinx's ``inject_page`` to make a
     container with everything that's needed, perhaps as
     ``container.register_singleton``.
     """

    expected = 'Hello containerview'

    @dataclass
    class ContainerView:

        def __call__(self):
            return expected

    register_view(themester_app.registry, ContainerView, context=Customer)

    # Fail with no context
    # with pytest.raises(LookupError):
    #     themester_app.render()

    # Succeed with context
    customer = Customer()
    container = themester_app.container.bind(context=customer)
    actual = themester_app.render(container=container)
    assert actual == expected


def test_themester_app_render_named(themester_app):
    """ Register a view with a name, then get the view by name """

    expected = 'namedview'

    @dataclass
    class NamedView:

        def __call__(self):
            return expected

    register_view(themester_app.registry, NamedView, context=Customer, name='somename')
    # Fail with no name
    with pytest.raises(LookupError):
        themester_app.render(context=Customer())

    # Succeeds when looking up by name
    actual = themester_app.render(context=Customer(), view_name='somename')
    assert actual == expected
