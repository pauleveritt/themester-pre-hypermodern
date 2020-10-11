import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.sphinx import HTMLConfig
from themester.themabaster.components.jsfiles import JSFiles


@pytest.fixture
def this_props(this_pathto, html_config, theme_config, this_pagecontext):
    props = dict(
        site_files=html_config.js_files,
        theme_files=theme_config.js_files,
        page_files=this_pagecontext.js_files,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = JSFiles(**this_props)
    return ci


def test_construction(this_component: JSFiles):
    assert 2 == len(this_component.srcs)
    assert 'page_first.js' == this_component.srcs[0]


def test_vdom(this_vdom):
    assert 2 == len(this_vdom)
    assert 'page_first.js' == this_vdom[0].props['src']


def test_render(this_html):
    srcs = this_html.select('script')
    assert 2 == len(srcs)
    assert 'page_first.js' == srcs[0].attrs['src']


def test_wired_render(this_container, this_props, html_config, theme_config):
    this_container.register_singleton(html_config, HTMLConfig)
    this_container.register_singleton(theme_config, ThemeConfig)
    this_vdom = html('<{JSFiles} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    scripts = this_html.select('script')
    assert 2 == len(scripts)
    assert '../mock/page_first.js' == scripts[0].attrs['src']
