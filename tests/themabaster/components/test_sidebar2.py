import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.sidebar2 import Sidebar2


@pytest.fixture
def this_component(this_props):
    ci = Sidebar2()
    return ci


def test_vdom(this_vdom, this_props):
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Sidebar2} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered
