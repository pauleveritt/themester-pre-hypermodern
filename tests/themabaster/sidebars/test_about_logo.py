import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.sidebars.about_logo import AboutLogo


@pytest.fixture
def this_props(sphinx_config, html_config, this_pagecontext):
    tp = dict(
        logo=html_config.logo,
        master_doc=sphinx_config.master_doc,
        pathto=this_pagecontext.pathto,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = AboutLogo(**this_props)
    return ci


def test_construction(this_component: AboutLogo):
    assert '../mock/_static/site_logo.png' == this_component.resolved_logo
    assert '../mock/index' == this_component.resolved_master


def test_vdom(this_vdom, this_props):
    assert 'p' == this_vdom.tag
    assert '../mock/index' == this_vdom.children[0].props['href']
    logo = '../mock/_static/site_logo.png'
    assert logo == this_vdom.children[0].children[0].props['src']


def test_vdom_nosidebar(this_props):
    this_props['logo'] = None
    ci = AboutLogo(**this_props)
    this_vdom = ci()
    assert None is this_vdom


def test_wired_render(this_container):
    this_vdom = html('<{AboutLogo} />')
    rendered = render(this_vdom, container=this_container)
    assert '../mock/index' in rendered
    assert '../mock/_static/site_logo.png' in rendered
