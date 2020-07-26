import dataclasses

import pytest
from bs4 import BeautifulSoup
from markupsafe import Markup
from viewdom import html
from viewdom_wired import render

from themester.sphinx.prevnext import PreviousLink, NextLink
from themester.themabaster.components.document import Document
from themester.themabaster.components.relbar1 import Relbar1
from themester.themabaster.components.relbar2 import Relbar2
from themester.themabaster.config import ThemabasterConfig


@pytest.fixture
def this_props():
    tp = dict(
        body=Markup('<p>Some content</p>'),
        nosidebar=False,
        previous=PreviousLink(
            title='Previous',
            link='/previous/',
        ),
        next=NextLink(
            title='Next',
            link='/next/',
        )
    )
    return tp


@pytest.fixture
def this_component(this_props):
    del this_props['previous']
    del this_props['next']
    ci = Document(**this_props)
    return ci


def test_vdom_default(this_vdom, this_props):
    # With sidebars
    assert 'div' == this_vdom.tag
    assert 'documentwrapper' == this_vdom.props['class']
    assert 'div' == this_vdom.children[0].tag
    assert 'bodywrapper' == this_vdom.children[0].props['class']
    assert 1 == len(this_vdom.children[0].children)
    assert Relbar1 == this_vdom.children[0].children[0][0].tag
    assert 'div' == this_vdom.children[0].children[0][1].tag
    assert Relbar2 == this_vdom.children[0].children[0][2].tag


def test_wired_render_default(themabaster_app, this_container, this_props):
    # With sidebars
    this_vdom = html('<{Document} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    div = this_html.select_one('div.documentwrapper')
    assert ['documentwrapper'] == div.get('class')
    assert div.select_one('div.bodywrapper')
    assert div.select_one('div.body')
    # relbars are off by default
    assert not div.select('div.top')
    assert not div.select('div.bottom')


def test_wired_render_without_sidebars(
        themabaster_app, theme_config, this_container, this_props
):
    # Change the themabaster settings in the container
    tc = dataclasses.replace(theme_config, nosidebar=True)
    this_container.register_singleton(tc, ThemabasterConfig)

    this_vdom = html('<{Document} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert None is this_html.select_one('div.bodywrapper')
