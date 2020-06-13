import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_resource(themester_site_deep):
    this_resource = themester_site_deep['f1']['d2']
    return this_resource


@pytest.fixture
def this_props(this_resource):
    props = dict(
        page_title='Some Page',
        site_name='Some Site',
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.title import DefaultTitle
    ci = DefaultTitle(**this_props)
    return ci


@pytest.fixture
def these_modules():
    from themester.themabaster.components import title
    return title,


def test_protocol():
    from themester.themabaster.protocols import Title
    assert Title


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert this_vdom.children == ['Some Page - Some Site']


def test_vdom_no_site_name():
    """ Maybe the site_name is None """
    from themester.themabaster.components.title import DefaultTitle
    page_title = 'Some Page'
    site_name = None
    this_component = DefaultTitle(page_title=page_title, site_name=site_name)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_vdom_raw_html():
    """ What if the page title has HTML markup? """
    from themester.themabaster.components.title import DefaultTitle
    page_title = '<h1>Some Page</h1>'
    site_name = None
    this_component = DefaultTitle(page_title=page_title, site_name=site_name)
    this_vdom = this_component()
    assert this_vdom.children == ['Some Page']


def test_render(this_html):
    title = this_html.select_one('title').text
    assert 'Some Page - Some Site' == title


def test_wired_render(themabaster_app, this_container, this_props):
    from themester.themabaster.protocols import Title  # noqa
    this_vdom = html('<{Title} page_title="Some Page" site_name="Some Site" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page - Some Site' == title


def test_wired_render_no_site_name(themabaster_app, this_container, this_props):
    from themester.themabaster.protocols import Title  # noqa
    this_vdom = html('<{Title} page_title="Some Page" site_name={None} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    title = this_html.select_one('title').text
    assert 'Some Page' == title
