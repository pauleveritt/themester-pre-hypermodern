import pytest
from bs4 import BeautifulSoup
from markupsafe import Markup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.body import Body
from themester.themabaster.services.documentbody import DocumentBody


@pytest.fixture
def this_component(this_props):
    ci = Body()
    return ci


def test_vdom(this_vdom, this_props):
    assert {} == this_vdom.props


def test_wired_render(themabaster_app, this_container):
    db = DocumentBody(html=Markup('<p>Some content</p>'))
    this_container.register_singleton(db, DocumentBody)
    this_vdom = html('<{Body} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('div.sphinxsidebar')
    assert '../mock/_sources/somedoc.rst' == this_html.select_one('a[rel="nofollow"]').attrs['href']
