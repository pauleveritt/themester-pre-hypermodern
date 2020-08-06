import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.sidebar2 import Sidebar2
from themester.themabaster.sidebars.about_logo import AboutLogo
from themester.themabaster.sidebars.localtoc import LocalToc


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


def test_construction(this_component: Sidebar2):
    assert 5 == len(this_component.resolved_sidebars)
    assert LocalToc == this_component.resolved_sidebars[0].tag


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    assert AboutLogo == this_vdom.children[0].children[0].tag


def test_vdom_nosidebar():
    ci = Sidebar2(sidebars=tuple())
    this_vdom = ci()
    assert [] == this_vdom


def test_wired_render(this_container):
    this_vdom = html('<{Sidebar2} />')
    rendered = render(this_vdom, container=this_container)
    assert 'Table of Contents' in rendered
    assert '<li>First' in rendered
