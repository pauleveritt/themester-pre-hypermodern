import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.cssfiles import CSSFiles


@pytest.fixture
def this_props(html_config, theme_config, this_pagecontext):
    props = dict(
        site_files=html_config.css_files,
        theme_files=theme_config.css_files,
        page_files=this_pagecontext.css_files,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = CSSFiles(**this_props)
    return ci


def test_construction(this_component: CSSFiles):
    assert 'site_first.css' == this_component.hrefs[0]
    assert '_static/themabaster.css' == this_component.hrefs[2]
    assert 'page_first.css' == this_component.hrefs[4]


def test_vdom(this_vdom):
    assert 6 == len(this_vdom)
    assert 'site_first.css' == this_vdom[0].props['href']


def test_render(this_html):
    links = this_html.select('link')
    assert 6 == len(links)
    assert 'site_first.css' == links[0].attrs['href']


def test_wired_render(this_container):
    this_vdom = html('<{CSSFiles} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 6 == len(links)
    assert '../mock/site_first.css' == links[0].attrs['href']
