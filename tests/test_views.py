from dataclasses import dataclass

import pytest
from viewdom.h import html, VDOM
from wired import ServiceRegistry


class ViewsContext:
    name = 'Views Context'


def test_views_hello():
    from themester.views import View, register_view

    @dataclass
    class DefaultView:
        name: str = 'DefaultView'

        def __call__(self) -> VDOM:
            return html('<div>Hello {self.name}</div>')

    registry = ServiceRegistry()
    register_view(registry, DefaultView, context=ViewsContext)
    container = registry.create_container(context=ViewsContext())
    view = container.get(View)
    actual = view()
    assert actual.tag == 'div'
    expected = VDOM(tag='div', props={}, children=['Hello ', 'DefaultView'])
    assert actual == expected


def test_views_context():
    from themester.views import View, register_view

    @dataclass
    class ContextView:
        name: str = 'ContextView'

        def __call__(self) -> VDOM:
            return html('<div>Hello {self.name}</div>')

    registry = ServiceRegistry()
    register_view(registry, ContextView, context=ViewsContext)
    container = registry.create_container(context=ViewsContext())
    view = container.get(View)
    actual = view()
    expected = VDOM(tag='div', props={}, children=['Hello ', 'ContextView'])
    assert actual == expected


def test_views_no_context():
    from themester.views import View, register_view

    @dataclass
    class ContextView:
        name: str = 'ContextView'

        def __call__(self) -> VDOM:
            return html('<div>Hello {self.name}</div>')

    registry = ServiceRegistry()
    register_view(registry, ContextView)
    container = registry.create_container()
    view = container.get(View)
    actual = view()
    expected = VDOM(tag='div', props={}, children=['Hello ', 'ContextView'])
    assert actual == expected


def test_views_named():
    from themester.views import View, register_view

    @dataclass
    class NamedView:
        name: str = 'NamedView'

        def __call__(self) -> str:
            return html('<div>Hello {self.name}</div>')

    registry = ServiceRegistry()
    register_view(registry, NamedView, context=ViewsContext, name='somename')
    container = registry.create_container(context=ViewsContext())
    with pytest.raises(LookupError):
        container.get(View)
    view = container.get(View, name='somename')
    actual = view()
    expected = VDOM(tag='div', props={}, children=['Hello ', 'NamedView'])
    assert actual == expected
