import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.linktags import SemanticLink


def mock_static_url(target: str):
    return f'mock/{target}'


@pytest.fixture
def this_resource(themester_site_deep):
    this_resource = themester_site_deep['f1']['d2']
    return this_resource


@pytest.fixture
def this_props(this_url):
    link1: SemanticLink = dict(
        rel='index',
        docname='1.html',
        title='1'
    )
    link2: SemanticLink = dict(
        rel='author',
        docname='2.html',
        title='2'
    )
    links = (link1, link2)
    props = dict(
        links=links,
        static_url=mock_static_url,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.linktags import DefaultLinktags
    ci = DefaultLinktags(**this_props)
    return ci


@pytest.fixture
def these_modules():
    from themester.themabaster.components import linktags
    return linktags,


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert 'mock/1.html' == this_vdom[0].props['href']
    assert 'index' == this_vdom[0].props['rel']
    assert '1' == this_vdom[0].props['title']
    assert 'mock/2.html' == this_vdom[1].props['href']
    assert 'author' == this_vdom[1].props['rel']
    assert '2' == this_vdom[1].props['title']


def test_render(this_html):
    links = this_html.select('link')
    assert 2 == len(links)
    assert 'mock/1.html' == links[0].attrs['href']
    assert 'mock/2.html' == links[1].attrs['href']


def test_wired_render(this_container, this_props):
    from themester.themabaster.protocols import Linktags  # noqa
    del this_props['static_url']
    this_vdom = html('<{Linktags} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 2 == len(links)
    assert '../../../1.html' == links[0].attrs['href']
