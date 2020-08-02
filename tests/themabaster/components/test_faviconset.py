import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.faviconset import FaviconSet


@pytest.fixture(scope='function')
def this_props(theme_config, this_pathto):
    props = dict(
        favicons=theme_config.favicons,
        pathto=this_pathto,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = FaviconSet(**this_props)
    return ci


def test_construction(this_component: FaviconSet):
    assert 'favicon.ico' == this_component.favicons.shortcut


def test_vdom(this_vdom):
    shortcut = this_vdom[0]
    assert 4 == len(this_vdom)
    assert 'link' == shortcut.tag
    assert '../mock/static/favicon.ico' == shortcut.props['href']
    png = this_vdom[1]
    assert 'link' == png.tag
    assert '../mock/static/apple-touch-icon-precomposed.png' == png.props['href']
    precomposed = this_vdom[2]
    assert 'link' == precomposed.tag
    assert 'apple-touch-icon-precomposed' == precomposed.props['rel']
    assert '../mock/static/apple-touch-icon-precomposed.png' == precomposed.props['href']
    sizes = list(this_vdom[3])
    assert 3 == len(sizes)
    assert '../mock/static/apple-touch-icon-144x144-precomposed.png' == sizes[0].props['href']
    assert '../mock/static/apple-touch-icon-114x114-precomposed.png' == sizes[1].props['href']


def test_render(this_html):
    links = this_html.select('link')
    assert 6 == len(links)


def test_wired_render(this_container, this_props):
    this_vdom = html('<{FaviconSet} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 6 == len(links)


def test_vdom_no_shortcut(this_props):
    this_props['favicons'].shortcut = None
    ci = FaviconSet(**this_props)
    vdom = ci()
    assert None is vdom[0]


def test_vdom_no_sizes(this_props):
    this_props['favicons'].sizes = None
    ci = FaviconSet(**this_props)
    vdom = ci()
    assert None is vdom[3]
