import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.sphinx import HTMLConfig, SphinxConfig
from themester.themabaster.sidebars.about import About
from themester.themabaster.sidebars.about_description import AboutDescription
from themester.themabaster.sidebars.about_github_button import AboutGitHubButton
from themester.themabaster.sidebars.about_logo import AboutLogo
from themester.themabaster.sidebars.about_travis_button import AboutTravisButton


@pytest.fixture
def this_component():
    ci = About()
    return ci


def test_construction(this_component: About):
    assert this_component


def test_vdom(this_vdom):
    assert AboutLogo == this_vdom[0].tag
    assert AboutDescription == this_vdom[1].tag
    assert AboutGitHubButton == this_vdom[2].tag
    assert AboutTravisButton == this_vdom[3].tag


def test_wired_render(this_container, html_config, sphinx_config):
    this_container.register_singleton(html_config, HTMLConfig)
    this_container.register_singleton(sphinx_config, SphinxConfig)
    this_vdom = html('<{About}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    href = this_html.select_one('p.logo a').get('href')
    assert '../mock/index' == href
