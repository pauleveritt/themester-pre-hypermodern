import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.sidebars.searchbox import SearchBox


@pytest.fixture
def this_props(this_pagecontext, theme_config):
    tp = dict(
        builder=this_pagecontext.builder,
        pagename=this_pagecontext.pagename,
        pathto=this_pagecontext.pathto,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = SearchBox(**this_props)
    return ci


def test_construction(this_component: SearchBox):
    assert '../mock/search' == this_component.resolved_pathto


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom[0].tag
    assert '../mock/search' == this_vdom[0].children[1].children[0].props['action']


def test_wired_render(this_container):
    this_vdom = html('<{SearchBox} />')
    rendered = render(this_vdom, container=this_container)
    assert '../mock/search' in rendered
