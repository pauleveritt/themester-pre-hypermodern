import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.sidebar2 import Sidebar2


@pytest.fixture
def this_props():
    tp = dict(
        no_sidebar=False,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = Sidebar2(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    assert [] == this_vdom


def test_vdom_no_sidebar():
    ci = Sidebar2(no_sidebar=True)
    this_vdom = ci()
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Sidebar2} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered
