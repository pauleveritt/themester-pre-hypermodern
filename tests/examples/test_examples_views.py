import pytest
from viewdom.h import H

from themester.views import View


@pytest.fixture
def scanned_modules():
    from .views import (
        hello,
        context,
        named,
    )
    return hello, context, named,


def test_views_hello(registry):
    container = registry.create_container()
    view = container.get(View)
    actual = view()
    expected = H(tag='div', props={}, children=['Hello ', 'DefaultView'])
    assert actual == expected


def test_views_context(registry):
    from .views.context import Customer
    context = Customer()
    container = registry.create_container(context=context)
    view = container.get(View)
    actual = view()
    expected = H(tag='div', props={}, children=['Hello ', 'Customer'])
    assert actual == expected


def test_views_named(registry):
    container = registry.create_container()
    view = container.get(View, name='somename')
    actual = view()
    expected = H(tag='div', props={}, children=['Hello ', 'Named'])
    assert actual == expected
