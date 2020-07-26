import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.sidebarlogo import SidebarLogo


@pytest.fixture
def this_props(themabaster_config, this_pagecontext):
    tp = dict(
        logo=themabaster_config.logo,
        master_doc=themabaster_config.master_doc,
        pathto=this_pagecontext.pathto,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = SidebarLogo(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    assert 'p' == this_vdom.tag
    assert '../mock/index' == this_vdom.children[0].props['href']
    logo = '../mock/_static/site_logo.png'
    assert logo == this_vdom.children[0].children[0].props['src']


def test_vdom_nosidebar(this_props):
    this_props['logo'] = None
    ci = SidebarLogo(**this_props)
    this_vdom = ci()
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{SidebarLogo} />')
    rendered = render(this_vdom, container=this_container)
    assert '../mock/index' in rendered
    assert '../mock/_static/site_logo.png' in rendered
