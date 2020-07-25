import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_pathto):
    props = dict(
        site_files=('a', 'b'),
        page_files=('x', 'y'),
        pathto=this_pathto,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.jsfiles import JSFiles
    ci = JSFiles(**this_props)
    return ci


def test_vdom(this_vdom):
    assert 4 == len(this_vdom)
    assert '../mock/a' == this_vdom[0].props['src']


def test_render(this_html):
    srcs = this_html.select('script')
    assert 4 == len(srcs)
    assert '../mock/a' == srcs[0].attrs['src']


def test_wired_render(this_container, this_props, themabaster_app):
    from themester.themabaster.components.jsfiles import JSFiles  # noqa: F401
    del this_props['pathto']
    this_vdom = html('<{JSFiles} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    scripts = this_html.select('script')
    assert 4 == len(scripts)
    assert '../mock/a' == scripts[0].attrs['src']
