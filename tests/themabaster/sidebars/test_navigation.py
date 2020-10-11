import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.sphinx.models import Link
from themester.themabaster.sidebars.navigation import Navigation


@pytest.fixture
def this_props(this_pagecontext, sphinx_config, theme_config):
    tp = dict(
        master_doc=sphinx_config.master_doc,
        pathto=this_pagecontext.pathto,
        sidebar_collapse=theme_config.sidebar_collapse,
        sidebar_includehidden=theme_config.sidebar_includehidden,
        toctree=this_pagecontext.toctree,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = Navigation(**this_props)
    return ci


def test_construction(this_component: Navigation):
    assert '../mock/index' == this_component.resolved_pathto
    assert '<ul><li>First</li></ul>' == str(this_component.resolved_toctree)


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    assert 'h3' == this_vdom.children[0].tag
    assert 'a' == this_vdom.children[0].children[0].tag
    assert '../mock/index' == this_vdom.children[0].children[0].props['href']
    assert ['Table of Contents'] == this_vdom.children[0].children[0].children


def test_wired_render(this_container, sphinx_config):
    this_container.register_singleton(sphinx_config, SphinxConfig)
    this_vdom = html('<{Navigation} />')
    rendered = render(this_vdom, container=this_container)
    assert '../mock/index' in rendered
    assert '<li>First' in rendered


def test_wired_render_with_navlinks(this_container, html_config, theme_config, sphinx_config):
    extra_nav_links = (
        Link(title='First Link', link='link1.com'),
        Link(title='Second Link', link='link2.com'),
    )
    tc = dataclasses.replace(
        theme_config,
        extra_nav_links=extra_nav_links,
    )
    this_container.register_singleton(sphinx_config, SphinxConfig)
    this_container.register_singleton(tc, ThemeConfig)
    this_vdom = html('<{Navigation} />')
    rendered = render(this_vdom, container=this_container)
    local_html = BeautifulSoup(rendered, 'html.parser')
    links = local_html.select('li.toctree-l1')
    assert 2 == len(links)
    assert 'First Link' == links[0].text
