import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.linktags import Linktags, SemanticLink


@pytest.fixture
def this_props(this_pathto, this_hasdoc):
    link1: SemanticLink = dict(
        rel='index',
        docname='genindex',
        title='Index'
    )
    link2: SemanticLink = dict(
        rel='author',
        docname='author',
        title='Author'
    )
    link3: SemanticLink = dict(
        rel='copyright',
        docname='copyright',
        title='Copyright'
    )
    links = (link1, link2, link3)
    props = dict(
        hasdoc=this_hasdoc,
        links=links,
        pathto=this_pathto,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = Linktags(**this_props)
    return ci


def test_construction(this_component: Linktags):
    assert 2 == len(this_component.resolved_links)
    assert '../mock/genindex' == this_component.resolved_links[0]['href']


def test_vdom(this_vdom):
    assert '../mock/genindex' == this_vdom[0].props['href']
    assert 'index' == this_vdom[0].props['rel']
    assert 'Index' == this_vdom[0].props['title']
    assert '../mock/copyright' == this_vdom[1].props['href']
    assert 'copyright' == this_vdom[1].props['rel']
    assert 'Copyright' == this_vdom[1].props['title']


def test_render(this_html):
    links = this_html.select('link')
    assert 2 == len(links)
    assert '../mock/genindex' == links[0].attrs['href']
    assert '../mock/copyright' == links[1].attrs['href']


def test_wired_render(this_container, this_props, themabaster_app):
    del this_props['pathto']
    this_vdom = html('<{Linktags} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 2 == len(links)
    assert '../mock/genindex' == links[0].attrs['href']
