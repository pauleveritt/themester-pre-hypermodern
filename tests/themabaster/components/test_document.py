import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.document import Document


@pytest.fixture
def this_component(this_props):
    ci = Document()
    return ci


def test_vdom(this_vdom, this_props):
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Document} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered