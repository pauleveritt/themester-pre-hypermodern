import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.sphinx.prevnext import PreviousLink, NextLink
from themester.themabaster.components.relbar2 import Relbar2
from themester.themabaster.components.rellink_markup import RellinkMarkup
from themester.themabaster.config import ThemabasterConfig


@pytest.fixture
def this_props():
    tp = dict(
        show_relbar_bottom=True,
        show_relbars=True,
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
    ci = Relbar2(**this_props)
    return ci


def test_construction(this_component: Relbar2):
    assert this_component.show_relbar_top


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    assert 'related top' == this_vdom.props['class']
    assert RellinkMarkup == this_vdom.children[0].tag


def test_wired_render(themabaster_app, this_container):
    # By default, no relbars should be shown as config is False
    this_vdom = html('<{Relbar2} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered


def test_wired_render_show_relbars(themabaster_app, this_container,
                                   theme_config):
    # Change the config to show relbars
    tc = dataclasses.replace(
        theme_config,
        show_relbar_top=True,
        show_relbars=True
    )
    this_container.register_singleton(tc, ThemabasterConfig)
    this_vdom = html('<{Relbar2} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert ['related', 'top'] == this_html.select_one('div').get('class')
    links = this_html.select('a')
    assert 2 == len(links)
    assert '/previous/' == links[0].get('href')
    assert 'Previous Document' == links[0].get('title')
    assert 'Previous' == links[0].text
    assert '/next/' == links[1].get('href')
    assert 'Next Document' == links[1].get('title')
    assert 'Next' == links[1].text
