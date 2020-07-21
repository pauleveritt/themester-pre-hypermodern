import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.content import Content
from themester.themabaster.components.sidebar1 import Sidebar1


@pytest.fixture
def this_component(this_props):
    ci = Content()
    return ci


def test_vdom(this_vdom, this_props):
    assert Sidebar1 == this_vdom.tag


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Content} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert None is this_html.select_one('body')
