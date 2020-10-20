import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.title import Title


@pytest.fixture
def this_props(sphinx_config, this_pagecontext):
    props = dict(
        page_title=this_pagecontext.title,
        project=sphinx_config.project,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = Title(**this_props)
    return ci


def test_construction(this_component: Title):
    assert 'Some Page - Themester SiteConfig' == this_component.resolved_title


def test_vdom(this_vdom):
    assert this_vdom.children == ['Some Page - Themester SiteConfig']


def test_vdom_no_site_name():
    """ Maybe the site_name is None """
    page_title = 'Some Page'
    project = None
    this_component = Title(page_title=page_title, project=project)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_vdom_raw_html():
    """ What if the page title has HTML markup? """
    page_title = '<h1>Some Page</h1>'
    project = None
    this_component = Title(page_title=page_title, project=project)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_render(this_html):
    title = this_html.select_one('title').text
    assert 'Some Page - Themester SiteConfig' == title


def test_wired_render(this_container, this_props):
    this_vdom = html('<{Title} project="Themester SiteConfig" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'D2 - Themester SiteConfig' == title


def test_wired_render_no_site_name(this_container, this_props):
    this_vdom = html('<{Title} page_title="Some Page" project={None} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page' == title
