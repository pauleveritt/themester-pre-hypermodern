import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_url, this_static_url):
    props = dict(
        site_files=('a', 'b'),
        page_files=('x', 'y'),
        static_url=this_static_url,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.jsfiles import DefaultJSFiles
    ci = DefaultJSFiles(**this_props)
    return ci


@pytest.fixture
def these_modules():
    from themester.themabaster.components import jsfiles
    return jsfiles,


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert 4 == len(this_vdom)
    assert 'mock/a' == this_vdom[0].props['src']


def test_render(this_html):
    srcs = this_html.select('script')
    assert 4 == len(srcs)
    assert 'mock/a' == srcs[0].attrs['src']


def test_wired_render(this_container, this_props):
    from themester.themabaster.protocols import JSFiles  # noqa
    del this_props['static_url']
    this_vdom = html('<{JSFiles} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    scripts = this_html.select('script')
    assert 4 == len(scripts)
    assert '../../../a' == scripts[0].attrs['src']
