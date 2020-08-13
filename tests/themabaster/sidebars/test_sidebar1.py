import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.sidebars.sidebar1 import Sidebar1


@pytest.fixture
def this_component(this_props):
    ci = Sidebar1()
    return ci


def test_vdom(this_vdom, this_props):
    assert [] == this_vdom


def test_wired_render(this_container):
    this_vdom = html('<{Sidebar1} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered
