import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.title import Title


@pytest.fixture
def this_props(this_resource, this_root):
    props = dict(
        resource_title=this_resource.title,
        site_title=this_root.title,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = Title(**this_props)
    return ci


def test_construction(this_component: Title):
    assert 'D2 - Themester Site' == this_component.resolved_title


def test_vdom(this_vdom):
    assert this_vdom.children == ['D2 - Themester Site']


def test_vdom_no_site_name():
    """ Maybe the site_name is None """
    resource_title = 'Some Page'
    project = None
    this_component = Title(resource_title=resource_title, site_title=project)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_vdom_raw_html():
    """ What if the page title has HTML markup? """
    resource_title = '<h1>Some Page</h1>'
    project = None
    this_component = Title(resource_title=resource_title, site_title=project)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_render(this_html):
    title = this_html.select_one('title').text
    assert 'D2 - Themester Site' == title


def test_wired_render(this_container, this_props):
    this_vdom = html('<{Title} site_title="Custom Site Title" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'D2 - Custom Site Title' == title


def test_wired_render_no_site_name(this_container, this_props):
    this_vdom = html('<{Title} resource_title="Some Page" site_title={None} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page' == title
