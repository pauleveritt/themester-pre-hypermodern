import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster import CSSFiles
from themester.themabaster.components.cssfiles import DefaultCSSFiles


@pytest.fixture
def this_props(themester_site_deep):
    this_resource = themester_site_deep['f1']['d2']
    props = dict(
        site_files=('c', 'd'),
        page_files=('p', 'q'),
        resource=this_resource,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = DefaultCSSFiles(**this_props)
    return ci


def test_protocol():
    assert CSSFiles


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert 4 == len(this_vdom)
    assert '../../../c' == this_vdom[0].props['href']


def test_render(this_html):
    links = this_html.select('link')
    assert 4 == len(links)
    assert '../../../c' == links[0].attrs['href']


@pytest.fixture
def these_modules():
    from themester.themabaster.components import cssfiles
    return cssfiles,


def test_app_render(this_container, this_props):
    del this_props['resource']
    this_vdom = html('<{CSSFiles} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 4 == len(links)
    assert '../../../c' == links[0].attrs['href']
