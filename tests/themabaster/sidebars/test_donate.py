import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.sidebars.donate import Donate


@pytest.fixture
def this_props(sphinx_config, theme_config):
    tp = dict(
        donate_url=theme_config.donate_url,
        opencollective=theme_config.opencollective,
        opencollective_button_color=theme_config.opencollective_button_color,
        project=sphinx_config.project,
        tidelift_url=theme_config.tidelift_url,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = Donate(**this_props)
    return ci


def test_construction(this_component: Donate):
    assert not this_component.show_donate


def test_construction_show_donate(this_props):
    this_props['donate_url'] = 'someurl'
    ci = Donate(**this_props)
    assert ci.show_donate


def test_vdom(this_vdom):
    assert True


def test_wired_render(this_container):
    this_vdom = html('<{Donate}/>')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered


def test_wired_render_show_donate(this_container, theme_config):
    tc = dataclasses.replace(
        theme_config,
        donate_url='donate.com',
        opencollective='opencollective.com',
        tidelift_url='tidelift.com'
    )
    this_container.register_singleton(tc, ThemabasterConfig)
    this_vdom = html('<{Donate}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    h3 = this_html.select_one('h3').text
    assert 'Donate/support' == h3
    badges = this_html.select('a')
    assert 'donate.com' == badges[0].get('href')
    assert 'https://opencollective.com/opencollective.com/donate' == badges[1].get('href')
    assert 'tidelift.com' == badges[2].get('href')
