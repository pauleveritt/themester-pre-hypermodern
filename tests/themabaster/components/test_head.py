import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.cssfiles import CSSFiles
from themester.themabaster.components.head import Head
from themester.themabaster.components.jsfiles import JSFiles
from themester.themabaster.components.title import Title


@pytest.fixture
def this_props(this_resource, this_pathto, this_pagecontext):
    props = dict(
        pagename=this_pagecontext.pagename,
        extrahead=None,
        pathto=this_pathto,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = Head(**this_props)
    return ci


def test_construction(this_component: Head):
    assert '../mock/_static/custom.css' == this_component.resolved_custom_css
    assert '../mock/_static/documentation_options.js' == this_component.resolved_docs_src
    assert '../mock/' == this_component.resolved_static_root


def test_vdom(this_vdom, this_props):
    assert 11 == len(this_vdom.children)
    assert 'head' == this_vdom.tag
    assert 'meta' == this_vdom.children[0].tag
    assert 'meta' == this_vdom.children[1].tag
    title = this_vdom.children[2]
    assert Title == title.tag
    css = this_vdom.children[3]
    assert CSSFiles == css.tag
    js = this_vdom.children[5]
    assert JSFiles == js.tag
    # No children
    assert None is this_vdom.children[10]


def test_vdom_extrahead(this_props):
    this_props['extrahead'] = html('''\n
<link rel="first"/>
<link rel="second"/>
    ''')
    head = Head(**this_props)
    assert 'first' == head.extrahead[0].props['rel']
    assert 'second' == head.extrahead[1].props['rel']


def test_wired_render(this_container):
    this_vdom = html('<{Head} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'Some Page - Themester SiteConfig' == this_html.select_one('title').text
    links = this_html.select('link')
    assert 13 == len(links)
    assert '../mock/site_first.css' == links[0].attrs['href']
    assert '../mock/_static/themabaster.css' == links[2].attrs['href']
    assert '../mock/_static/pygments.css' == links[3].attrs['href']
    assert '../mock/page_first.css' == links[4].attrs['href']
    assert '../mock/_static/custom.css' == links[6].attrs['href']


def test_wired_render_extrahead(this_container):
    extrahead = html('''\n
    <link rel="extra" href="first" />
    <link rel="extra" href="second" />
    ''')
    this_vdom = html('<{Head} extrahead={extrahead}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link[rel="extra"]')
    assert len(links) == 2
    assert 'first' == links[0].attrs['href']
