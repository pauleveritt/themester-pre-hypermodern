import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.body import Body


# Perhaps unused...
# @pytest.fixture
# def this_props(this_url, this_resource, this_static_url):
#     props = dict(
#     )
#     return props


@pytest.fixture
def this_component(this_props):
    ci = Body()
    return ci


def test_vdom(this_vdom, this_props):
    assert {} == this_vdom.props


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Body} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert [] == this_html.select_one('body').contents
