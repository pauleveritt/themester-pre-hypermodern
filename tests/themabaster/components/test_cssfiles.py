import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.cssfiles import CSSFiles


@pytest.fixture
def this_props(this_pathto):
    props = dict(
        site_files=('c', 'd'),
        page_files=('p', 'q'),
        pathto=this_pathto,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = CSSFiles(**this_props)
    return ci


def test_construction(this_component: CSSFiles):
    assert '../mock/c' == this_component.hrefs[0]


def test_vdom(this_vdom):
    # TODO Need to re-invent VDOM data type to be tuple-ish at the root.
    assert 4 == len(this_vdom)
    assert '../mock/c' == this_vdom[0].props['href']


def test_render(this_html):
    links = this_html.select('link')
    assert 4 == len(links)
    assert '../mock/c' == links[0].attrs['href']


def test_wired_render(this_container, this_props):
    from themester.themabaster.components.cssfiles import CSSFiles  # noqa: F401
    del this_props['pathto']
    this_vdom = html('<{CSSFiles} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 4 == len(links)
    assert '../mock/c' == links[0].attrs['href']
