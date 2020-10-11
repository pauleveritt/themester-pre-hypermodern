import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.sphinx import HTMLConfig, SphinxConfig
from themester.themabaster.components.body import Body


@pytest.fixture
def this_component(this_props):
    ci = Body()
    return ci


def test_vdom(this_vdom, this_props):
    assert {} == this_vdom.props


def test_wired_render(this_container, html_config, sphinx_config):
    this_container.register_singleton(html_config, HTMLConfig)
    this_container.register_singleton(sphinx_config, SphinxConfig)
    this_vdom = html('<{Body} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert this_html.select_one('div.sphinxsidebar')
    assert '../mock/_sources/somedoc.rst' == this_html.select_one('a[rel="nofollow"]').attrs['href']
