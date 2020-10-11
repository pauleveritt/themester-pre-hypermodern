import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.themabaster.sidebars.about_travis_button import AboutTravisButton


@pytest.fixture
def this_props(theme_config):
    tp = dict(
        travis_button=theme_config.travis_button,
        travis_path=theme_config.travis_path,
        github_repo=theme_config.github_repo,
        github_user=theme_config.github_user,
        badge_branch=theme_config.badge_branch,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = AboutTravisButton(**this_props)
    return ci


def test_construction(this_component: AboutTravisButton):
    assert 'None/None' == this_component.resolved_path


def test_vdom(this_vdom):
    assert None is this_vdom


def test_vdom_with_badge(this_props):
    this_props['travis_button'] = True
    this_props['github_user'] = 'thisuser'
    this_props['github_repo'] = 'thisrepo'
    ci = AboutTravisButton(**this_props)
    this_vdom = ci()
    anchor = this_vdom.children[0]
    assert 'a' is anchor.tag
    assert 'https://travis-ci.org/thisuser/thisrepo' == anchor.props['href']
    img = anchor.children[0]
    assert 'img' == img.tag
    u = 'https://secure.travis-ci.org/thisuser/thisrepo.svg?branch=master'
    assert u == img.props['alt']
    assert u == img.props['src']


def test_wired_render(this_container):
    local_vdom = html('<{AboutTravisButton} />')
    rendered = render(local_vdom, container=this_container)
    assert '' == rendered


def test_wired_render_with_badge(this_container, theme_config):
    tc = dataclasses.replace(
        theme_config,
        travis_button=True,
        github_repo='thisrepo',
        github_user='thisuser',
    )
    this_container.register_singleton(tc, ThemeConfig)
    this_vdom = html('<{AboutTravisButton} />')
    rendered = render(this_vdom, container=this_container)
    local_html = BeautifulSoup(rendered, 'html.parser')
    src = local_html.select_one('img').get('src')
    assert 'thisrepo' in src
    assert 'thisuser' in src
