import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_url, this_resource):
    props = dict(
        url=this_url,
        favicon='someicon.png',
        page_title='Some Page',
        site_name='Some Site',
        site_css_files=('site1.css', 'site2.css',),
        page_css_files=('page1.css', 'page2.css'),
        site_js_files=('site1.js', 'site2.js',),
        page_js_files=('page1.js', 'page2.js'),
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.head import DefaultHead
    ci = DefaultHead(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    from themester.themabaster.protocols import CSSFiles, JSFiles, Title
    assert len(this_vdom.children) == 5
    assert this_vdom.tag == 'head'
    assert this_vdom.children[0].tag == 'meta'
    assert this_vdom.children[1].tag == 'meta'
    title = this_vdom.children[2]
    assert title.tag == Title
    assert title.props == dict(page_title='Some Page', site_name='Some Site')
    assert title.children == []
    css = this_vdom.children[3]
    assert css.tag == CSSFiles
    assert css.props == dict(
        url=this_props['url'],
        page_files=('page1.css', 'page2.css'),
        site_files=('site1.css', 'site2.css'),
    )
    assert css.children == []
    js = this_vdom.children[4]
    assert js.tag == JSFiles
    assert js.props == dict(
        url=this_props['url'],
        page_files=('page1.js', 'page2.js'),
        site_files=('site1.js', 'site2.js'),
    )
    assert js.children == []


def test_wired_render(themabaster_app, this_container, this_props):
    from themester.themabaster.protocols import Head  # noqa
    this_vdom = html('<{Head} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('title').text == 'Some Page - Themester SiteConfig'
    links = this_html.select('link')
    assert len(links) == 4
    assert links[0].attrs['href'] == '../../../site_first.css'
    assert links[2].attrs['href'] == '../../../page_first.css'
