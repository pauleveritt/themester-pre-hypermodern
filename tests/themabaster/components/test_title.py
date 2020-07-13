import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_resource):
    props = dict(
        page_title='Some Page',
        site_name='Some Site',
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.title import Title
    ci = Title(**this_props)
    return ci


def test_vdom(this_vdom):
    assert this_vdom.children == ['Some Page - Some Site']


def test_vdom_no_site_name():
    """ Maybe the site_name is None """
    from themester.themabaster.components.title import Title
    page_title = 'Some Page'
    site_name = None
    this_component = Title(page_title=page_title, site_name=site_name)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_vdom_raw_html():
    """ What if the page title has HTML markup? """
    from themester.themabaster.components.title import Title
    page_title = '<h1>Some Page</h1>'
    site_name = None
    this_component = Title(page_title=page_title, site_name=site_name)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_render(this_html):
    title = this_html.select_one('title').text
    assert 'Some Page - Some Site' == title


def test_wired_render(themabaster_app, this_container, this_props):
    from themester.themabaster.components.title import Title  # noqa: F401
    this_vdom = html('<{Title} page_title="Some Page" site_name="Some Site" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page - Some Site' == title


def test_wired_render_no_site_name(themabaster_app, this_container, this_props):
    from themester.themabaster.components.title import Title  # noqa: F401
    this_vdom = html('<{Title} page_title="Some Page" site_name={None} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page' == title
