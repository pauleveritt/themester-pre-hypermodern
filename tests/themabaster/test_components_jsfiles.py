import pytest

from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster import JSFiles
from themester.themabaster.components.jsfiles import DefaultJSFiles


@pytest.fixture
def this_props(themester_site_deep):
    this_resource = themester_site_deep['f1']['d2']
    props = dict(
        site_files=('a', 'b'),
        page_files=('x', 'y'),
        resource=this_resource,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = DefaultJSFiles(**this_props)
    return ci


def test_protocol():
    assert JSFiles


@pytest.fixture
def these_modules():
    from themester.themabaster.components import jsfiles
    return jsfiles,


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert 4 == len(this_vdom)
    assert '../../../a' == this_vdom[0].props['src']


def test_render(this_html):
    srcs = this_html.select('script')
    assert 4 == len(srcs)
    assert '../../../a' == srcs[0].attrs['src']


def test_app_render(this_container, this_props):
    del this_props['resource']
    this_vdom = html('<{JSFiles} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    scripts = this_html.select('script')
    assert 4 == len(scripts)
    assert '../../../a' == scripts[0].attrs['src']
