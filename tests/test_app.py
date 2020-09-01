from dataclasses import dataclass

import pytest
from venusian import Scanner
from wired import ServiceRegistry
from wired.dataclasses import Context, injected

from themester.app import ThemesterApp
from themester.protocols import Root
from themester.views import register_view

pytest_plugins = [
    'themester.testing.fixtures',
]


@dataclass
class Customer:
    name: str


def test_themester_app_default(themester_site_deep, themester_config):
    ta = ThemesterApp(
        themester_config=themester_config,
    )
    assert isinstance(ta.registry, ServiceRegistry)
    assert isinstance(ta.scanner, Scanner)

    container = ta.registry.create_container()
    app: ThemesterApp = container.get(ThemesterApp)
    assert app.registry == ta.registry
    container_root: Root = container.get(Root)
    assert themester_site_deep is container_root
    scanner: Scanner = container.get(Scanner)
    assert isinstance(scanner, Scanner)


def test_themester_app_setup_plugin(themester_app):
    from themester.testing import views
    from themester.views import View

    themester_app.setup_plugin(views)
    container = themester_app.registry.create_container()
    view = container.get(View)
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
    actual = themester_app.render(context=Customer(name='Some Customer'))
    assert actual == expected


def test_themester_app_multiple_renders(themester_app):
    """ Provide a per-render container

     The ``TemplateBridge`` wants Sphinx's ``inject_page`` to make a
     container with everything that's needed, perhaps as
     ``container.register_singleton``.
     """

    @dataclass
    class ContainerView:
        customer_name: str = injected(Context, attr='name')

        def __call__(self):
            return self.customer_name

    register_view(themester_app.registry, ContainerView, context=Customer)

    # First render
    customer1 = Customer(name='Some Customer')
    assert 'Some Customer' == themester_app.render(context=customer1)

    customer2 = Customer(name='Another Customer')
    assert 'Another Customer' == themester_app.render(context=customer2)


def test_themester_app_render_named(themester_app):
    """ Register a view with a name, then get the view by name """

    expected = 'namedview'

    @dataclass
    class NamedView:

        def __call__(self):
            return expected

    register_view(themester_app.registry, NamedView, context=Customer, name='somename')
    customer = Customer(name='Some Customer')
    # Fail with no name
    with pytest.raises(LookupError):
        themester_app.render(context=customer)

    # Succeeds when looking up by name
    actual = themester_app.render(context=customer, view_name='somename')
    assert actual == expected
