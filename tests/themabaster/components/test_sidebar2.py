import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.sidebar2 import Sidebar2
from themester.themabaster.components.sidebarlogo import SidebarLogo


@pytest.fixture
def this_props(theme_config):
    tp = dict(
        sidebars=theme_config.sidebars,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = Sidebar2(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    assert SidebarLogo == this_vdom.children[0].children[0].tag


def test_vdom_nosidebar():
    ci = Sidebar2(sidebars=tuple())
    this_vdom = ci()
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Sidebar2} />')
    rendered = render(this_vdom, container=this_container)
    assert 'Table of Contents' in rendered
    assert '<li>First' in rendered
