import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.sphinx import HTMLConfig
from themester.themabaster.components.favicon import Favicon


@pytest.fixture
def this_props():
    props = dict(
        href='someicon.png',
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.favicon import Favicon
    ci = Favicon(**this_props)
    return ci


def test_construction(this_component: Favicon, this_props):
    assert 'someicon.png' == this_component.href


def test_vdom(this_vdom):
    assert 'link' == this_vdom.tag
    assert 'shortcut icon' == this_vdom.props['rel']
    assert 'someicon.png' == this_vdom.props['href']
    assert [] == this_vdom.children


def test_render(this_html):
    link = this_html.select_one('link')
    assert ['shortcut', 'icon'] == link.attrs['rel']
    assert 'someicon.png' == link.attrs['href']


def test_wired_render(this_container, html_config):
    this_container.register_singleton(html_config, HTMLConfig)
    this_vdom = html('<{Favicon} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    link = this_html.select_one('link')
    assert '../mock/themabaster.ico' == link.attrs['href']
