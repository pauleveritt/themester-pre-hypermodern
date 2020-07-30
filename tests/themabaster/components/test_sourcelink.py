import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.sourcelink import SourceLink


@pytest.fixture
def this_props(this_pagecontext, theme_config):
    tp = dict(
        show_sourcelink=True,
        has_source=True,
        pathto=this_pagecontext.pathto,
        sourcename='thispage.md',
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = SourceLink(**this_props)
    return ci


def test_construction(this_component: SourceLink):
    assert '../mock/_sources/thispage.md' == this_component.resolved_pathto


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    a = this_vdom.children[1].children[0].children[0]
    assert 'a' == a.tag
    assert '../mock/_sources/thispage.md' == a.props['href']


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{SourceLink} />')
    rendered = render(this_vdom, container=this_container)
    assert '<div' in rendered
