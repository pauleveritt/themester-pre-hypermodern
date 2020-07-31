from dataclasses import dataclass

import pytest
from venusian import Scanner
from wired import ServiceContainer, ServiceRegistry

from themester.app import ThemesterApp
from themester.protocols import Root
from themester.views import register_view

pytest_plugins = [
    'themester.testing.fixtures',
]


class Customer:
    name = 'Some Customer'


def test_themester_app_default(themester_site_deep, themester_config):
    ta = ThemesterApp(
        root=themester_site_deep,
        themester_config=themester_config,
        sphinx_config=None,
        html_config=None,
        theme_config=None,
    )
    assert isinstance(ta.registry, ServiceRegistry)
    assert isinstance(ta.container, ServiceContainer)

    app: ThemesterApp = ta.container.get(ThemesterApp)
    assert app.registry == ta.registry
    container_root: Root = ta.container.get(Root)
    assert themester_site_deep is container_root
    # Make sure the root/config attributes not on the dataclass instance,
    # as they are InitVars
    with pytest.raises(AttributeError):
        ta.root  # noqa
    scanner: Scanner = ta.container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_themester_app_setup_plugin(themester_app):
    from themester.testing import views
    from themester.views import View

    themester_app.setup_plugin(views)
    view = themester_app.container.get(View)
    assert view.name == 'Fixture View'


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


def test_themester_app_get_static_resources(themester_app):
    """ Combine each plugin's exported resources """

    from typing import Tuple
    from pathlib import Path
    result: Tuple[Path] = themester_app.get_static_resources()
    assert '.css' == result[0].name[-4:]
