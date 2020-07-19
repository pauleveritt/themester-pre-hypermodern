import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.footer import Footer


@pytest.fixture
def this_component(this_props):
    ci = Footer()
    return ci


def test_vdom(this_vdom, this_props):
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Footer} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered
