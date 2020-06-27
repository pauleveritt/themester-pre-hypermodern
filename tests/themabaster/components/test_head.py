import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_url, this_resource, this_static_url):
    props = dict(
        favicon='someicon.png',
        page_title='Some Page',
        site_name='Some Site',
        touch_icon='sometouchicon.png',
        site_css_files=('site1.css', 'site2.css',),
        page_css_files=('page1.css', 'page2.css'),
        site_js_files=('site1.js', 'site2.js',),
        page_js_files=('page1.js', 'page2.js'),
        static_url=this_static_url,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.head import DefaultHead
    ci = DefaultHead(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    from themester.themabaster.protocols import CSSFiles, JSFiles, Title
    assert len(this_vdom.children) == 8
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
        page_files=('page1.css', 'page2.css'),
        site_files=('site1.css', 'site2.css'),
    )
    assert css.children == []
    js = this_vdom.children[4]
    assert js.tag == JSFiles
    assert js.props == dict(
        page_files=('page1.js', 'page2.js'),
        site_files=('site1.js', 'site2.js'),
    )
    assert js.children == []
    assert 'mock/sometouchicon.png' == this_vdom.children[6].props['href']
    # No children
    assert None == this_vdom.children[7]


def test_vdom_children(this_props):
    """ Fill the "extrahead" slot using children """
    from themester.themabaster.components.head import DefaultHead

    this_props['children'] = html('''\n
<link rel="first"/>
<link rel="second"/>
    ''')
    head = DefaultHead(**this_props)
    assert 'first' == head.children[0].props['rel']
    assert 'second' == head.children[1].props['rel']


def test_wired_render(themabaster_app, this_container, this_props):
    from themester.themabaster.protocols import Head  # noqa
    this_vdom = html('<{Head} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'Some Page - Themester SiteConfig' == this_html.select_one('title').text
    links = this_html.select('link')
    assert 6 == len(links)
    assert '../../../site_first.css' == links[0].attrs['href']
    assert '../../../page_first.css' == links[2].attrs['href']
    assert '../../../_static/custom.css' == links[4].attrs['href']
    assert '../../../sometouchicon.ico' == links[5].attrs['href']


def test_wired_render_extrahead(themabaster_app, this_container, this_props):
    from themester.themabaster.protocols import Head  # noqa
    this_vdom = html('''\n
<{Head}> 
    <link rel="extra" href="first" />
    <link rel="extra" href="second" />
<//>
    ''')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link[rel="extra"]')
    assert len(links) == 2
    assert 'first' == links[0].attrs['href']
