import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.content import Content
from themester.themabaster.components.document import Document
from themester.themabaster.components.sidebar1 import Sidebar1
from themester.themabaster.components.sidebar2 import Sidebar2


@pytest.fixture
def this_component(this_props):
    ci = Content()
    return ci


def test_vdom(this_vdom, this_props):
    assert Sidebar1 == this_vdom[0].tag
    assert Document == this_vdom[1].children[0].tag
    assert Sidebar2 == this_vdom[1].children[1].tag


def test_wired_render(this_container, this_props):
    this_vdom = html('<{Content} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('div.sphinxsidebar')
