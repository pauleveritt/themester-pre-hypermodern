import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_pathto):
    props = dict(
        href='someicon.png',
        pathto=this_pathto,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.favicon import Favicon
    ci = Favicon(**this_props)
    return ci


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert 'link' == this_vdom.tag
    assert 'shortcut icon' == this_vdom.props['rel']
    assert '../mock/someicon.png' == this_vdom.props['href']
    assert [] == this_vdom.children


def test_render(this_html):
    link = this_html.select_one('link')
    assert ['shortcut', 'icon'] == link.attrs['rel']
    assert '../mock/someicon.png' == link.attrs['href']


def test_wired_render(themabaster_app, this_container):
    from themester.themabaster.components.favicon import Favicon  # noqa: F401
    this_vdom = html('<{Favicon} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    link = this_html.select_one('link')
    assert '../mock/themabaster.ico' == link.attrs['href']
