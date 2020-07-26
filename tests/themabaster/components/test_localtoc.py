import pytest
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.localtoc import LocalToc


@pytest.fixture
def this_props(this_pagecontext, sphinx_config):
    tp = dict(
        display_toc=this_pagecontext.display_toc,
        master_doc=sphinx_config.master_doc,
        pathto=this_pagecontext.pathto,
        toc=this_pagecontext.toc,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = LocalToc(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    assert 'h3' == this_vdom[0].tag
    assert 'a' == this_vdom[0].children[0].tag
    assert '../mock/index' == this_vdom[0].children[0].props['href']
    assert ['Table of Contents'] == this_vdom[0].children[0].children
    assert '<li>toc</li>' == str(this_vdom[1])


def test_vdom_no_display_toc(this_props):
    this_props['display_toc'] = False
    ci = LocalToc(**this_props)
    this_vdom = ci()
    assert [] == this_vdom


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{LocalToc} />')
    rendered = render(this_vdom, container=this_container)
    expected = '<h3><a href="../mock/index">Table of Contents</a></h3><li>toc</li>'
    assert expected == rendered
