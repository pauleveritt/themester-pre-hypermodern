import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.searchbox import SearchBox


@pytest.fixture
def this_props(this_pagecontext, themabaster_config):
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


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom[0].tag
    assert '../mock/search' == this_vdom[0].children[1].children[0].props['action']


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{SearchBox} />')
    rendered = render(this_vdom, container=this_container)
    assert '../mock/search' in rendered
