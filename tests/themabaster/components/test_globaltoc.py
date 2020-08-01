import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.globaltoc import GlobalToc


@pytest.fixture
def this_props(this_pagecontext, sphinx_config):
    tp = dict(
        master_doc=sphinx_config.master_doc,
        pathto=this_pagecontext.pathto,
        toctree=this_pagecontext.toctree,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = GlobalToc(**this_props)
    return ci


def test_construction(this_component: GlobalToc):
    assert '../mock/index' == this_component.resolved_pathto
    assert '<ul><li>First</li></ul>' == str(this_component.resolved_toctree)


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    assert 'h3' == this_vdom.children[0].tag
    assert 'a' == this_vdom.children[0].children[0].tag
    assert '../mock/index' == this_vdom.children[0].children[0].props['href']
    assert ['Table of Contents'] == this_vdom.children[0].children[0].children


def test_wired_render(this_container):
    this_vdom = html('<{GlobalToc} />')
    rendered = render(this_vdom, container=this_container)
    assert '../mock/index' in rendered
    assert '<li>First' in rendered
