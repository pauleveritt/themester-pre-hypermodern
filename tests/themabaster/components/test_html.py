import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props(this_resource):
    props = dict(
        lang='EN',
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.html import HTML
    ci = HTML(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    from themester.themabaster.components.html import Head
    assert len(this_vdom.children) == 1
    assert this_vdom.tag == 'html'
    assert this_vdom.props['lang'] == this_props['lang']
    assert this_vdom.children[0].tag == Head


def test_wired_render(themabaster_app, this_container, this_props):
    from themester.themabaster.components.html import HTML  # noqa: F401
    this_vdom = html('<{HTML} lang="EN" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('title').text == 'Some Page - Themester SiteConfig'
    links = this_html.select('link')
    assert 6 == len(links)
    assert '../../../site_first.css' == links[0].attrs['href']
    assert '../../../page_first.css' == links[2].attrs['href']
