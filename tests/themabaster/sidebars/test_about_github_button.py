import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.sidebars.about_github_button import AboutGitHubButton


@pytest.fixture
def this_props(theme_config):
    tp = dict(
        github_button=theme_config.github_button,
        github_repo=theme_config.github_repo,
        github_user=theme_config.github_user,
        github_type=theme_config.github_type,
        github_count=theme_config.github_count,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = AboutGitHubButton(**this_props)
    return ci


def test_construction(this_component: AboutGitHubButton):
    assert False is this_component.show_button


def test_construction_true(this_component: AboutGitHubButton):
    ci = AboutGitHubButton(
        github_button=True,
        github_repo='repo',
        github_user='user',
        github_count='true',
        github_type='watch',
    )
    assert True is ci.show_button


def test_vdom(this_vdom):
    assert None is this_vdom


def test_wired_render(this_container):
    this_vdom = html('<{AboutGitHubButton} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered


def test_wired_render_with_badge(this_container, theme_config):
    tc = dataclasses.replace(
        theme_config,
        github_button=True,
        github_repo='thisrepo',
        github_user='thisuser',
    )
    this_container.register_singleton(tc, ThemabasterConfig)
    this_vdom = html('<{AboutGitHubButton} />')
    rendered = render(this_vdom, container=this_container)
    local_html = BeautifulSoup(rendered, 'html.parser')
    src = local_html.select_one('iframe').get('src')
    assert 'thisrepo' in src
    assert 'thisuser' in src
