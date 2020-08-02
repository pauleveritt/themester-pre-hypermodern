import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.sidebars.about import About


@pytest.fixture
def this_props(sphinx_config, this_pagecontext):
    props = dict(
        page_title=this_pagecontext.title,
        project=sphinx_config.project,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = About(**this_props)
    return ci


def test_construction(this_component: About):
    assert 'Some Page - Themester SiteConfig' == this_component.resolved_title


def test_vdom(this_vdom):
    assert this_vdom.children == ['Some Page - Themester SiteConfig']


def test_render(this_html):
    title = this_html.select_one('title').text
    assert 'Some Page - Themester SiteConfig' == title


def test_wired_render(this_container, this_props):
    this_vdom = html('<{About} page_title="Some Page" project="Themester SiteConfig" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page - Themester SiteConfig' == title
