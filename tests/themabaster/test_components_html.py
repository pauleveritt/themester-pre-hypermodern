# """
# No containers, just make dataclass instances
# """
# from viewdom import render
#
# from themester.themabaster.components.head import DefaultHead
# from themester.themabaster.components.html import DefaultHTML
# from themester.themabaster.components.title import DefaultTitle
#
#
# def test_component_html():
#     """ Test both the vdom and rendered for this component """
#
#     title = DefaultTitle(page_title='Page Title', site_name='Site Name')
#     head = DefaultHead(title=title)
#     c = DefaultHTML(head=head, lang='EN')
#     vdom = c()
#     tag, props, children = vdom
#     assert tag == 'html'
#     assert props == dict(lang='EN')
#     assert children == [head]
#     result = render(vdom)
#     assert result == '<html lang="EN"><head><title>Page Title - Site Name</title></head></html>'

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
        lang='EN',
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.html import DefaultHTML
    ci = DefaultHTML(**this_props)
    return ci


@pytest.fixture
def these_modules():
    from themester.themabaster.components import (
        cssfiles,
        head,
        html,
        jsfiles,
        title,
    )
    return cssfiles, head, html, jsfiles, title


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom, this_props):
    from themester.themabaster.protocols import Head
    assert len(this_vdom.children) == 1
    assert this_vdom.tag == 'html'
    assert this_vdom.props['lang'] == this_props['lang']
    assert this_vdom.children[0].tag == Head


def test_wired_render(themabaster_app, this_container, this_props):
    from themester.themabaster.protocols import HTML  # noqa
    this_vdom = html('<{HTML} lang="EN" />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('title').text == 'Some Page - Themester SiteConfig'
    links = this_html.select('link')
    assert len(links) == 4
    assert links[0].attrs['href'] == '../../../site_first.css'
    assert links[2].attrs['href'] == '../../../page_first.css'
