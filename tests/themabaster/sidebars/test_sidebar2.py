import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.themabaster.sidebars.localtoc import LocalToc
from themester.themabaster.sidebars.relations import Relations
from themester.themabaster.sidebars.searchbox import SearchBox
from themester.themabaster.sidebars.sidebar2 import Sidebar2
from themester.themabaster.sidebars.sourcelink import SourceLink


@pytest.fixture
def this_props(theme_config):
    tp = dict(
        sidebars=theme_config.sidebars,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = Sidebar2(**this_props)
    return ci


def test_construction(this_component: Sidebar2):
    assert 4 == len(this_component.resolved_sidebars)
    assert LocalToc == this_component.resolved_sidebars[0].tag


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    ssw = this_vdom.children[0]
    sidebars = ssw.children[0]
    assert 4 == len(sidebars)
    assert LocalToc == sidebars[0].tag
    assert Relations == sidebars[1].tag
    assert SourceLink == sidebars[2].tag
    assert SearchBox == sidebars[3].tag


def test_vdom_nosidebar():
    ci = Sidebar2(sidebars=tuple())
    this_vdom = ci()
    assert [] == this_vdom


def test_wired_render(this_container, html_config, sphinx_config, theme_config):
    this_container.register_singleton(html_config, HTMLConfig)
    this_container.register_singleton(sphinx_config, SphinxConfig)
    this_container.register_singleton(theme_config, ThemeConfig)
    this_vdom = html('<{Sidebar2} />')
    rendered = render(this_vdom, container=this_container)
    local_html = BeautifulSoup(rendered, 'html.parser')
    assert 'Table of Contents' == local_html.select('h3 a')[0].text
    assert 'Contents' == local_html.select_one('.relations h3').text
