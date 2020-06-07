import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_resource(themester_site_deep):
    this_resource = themester_site_deep['f1']['d2']
    return this_resource


@pytest.fixture
def this_props(this_resource):
    from themester.themabaster.components.cssfiles import DefaultCSSFiles
    from themester.themabaster.components.jsfiles import DefaultJSFiles
    from themester.themabaster.components.title import DefaultTitle
    css_files = DefaultCSSFiles(
        site_files=('c', 'd'),
        page_files=('p', 'q'),
        resource=this_resource,
    )
    js_files = DefaultJSFiles(
        site_files=('c', 'd'),
        page_files=('p', 'q'),
        resource=this_resource,
    )
    title = DefaultTitle(
        page_title='Some Page',
        site_name='Some Site',
    )
    props = dict(
        css_files=css_files,
        js_files=js_files,
        title=title,
        resource=this_resource,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.head import DefaultHead
    ci = DefaultHead(**this_props)
    return ci


@pytest.fixture
def these_modules():
    from themester.themabaster.components import head
    return head,


def test_protocol():
    from themester.themabaster import Head
    assert Head


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    from themester.themabaster.components.title import DefaultTitle
    assert len(this_vdom.children) == 5
    assert this_vdom.tag == 'head'
    assert this_vdom.children[0].tag == 'meta'
    assert this_vdom.children[1].tag == 'meta'
    assert isinstance(this_vdom.children[2], DefaultTitle)


def test_render(this_html):
    assert this_html.select_one('title').text == 'Some Page - Some Site'


def test_wired_render(this_container, this_props):
    from themester.themabaster import Head  # noqa
    del this_props['resource']
    this_vdom = html('<{Head} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('title').text == 'Some Page - Some Site'
