import pytest
from viewdom import html
from viewdom_wired import render

from themester.sphinx import SphinxConfig
from themester.themabaster.sidebars.relations import Relations


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
    ci = Relations(**this_props)
    return ci


def test_construction(this_component: Relations):
    assert '../mock/index' == this_component.resolved_pathto
    assert '<ul><li>First</li></ul>' == str(this_component.resolved_toctree)


def test_vdom(this_vdom, this_props):
    assert 'div' == this_vdom.tag
    assert 'h3' == this_vdom.children[0].tag
    ul = this_vdom.children[1]
    assert 'ul' == ul.tag
    assert 'li' == ul.children[0].tag
    first_li = ul.children[0]
    assert 'li' == first_li.tag
    assert 'a' == first_li.children[0].tag
    assert '../mock/index' == first_li.children[0].props['href']
    assert ['Documentation overview'] == first_li.children[0].children


def test_wired_render(this_container, sphinx_config):
    this_container.register_singleton(sphinx_config, SphinxConfig)
    this_vdom = html('<{Relations} />')
    rendered = render(this_vdom, container=this_container)
    assert '<div class="relations">' in rendered
