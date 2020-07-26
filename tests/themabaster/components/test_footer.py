import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.components.footer import Footer


@pytest.fixture
def this_props(sphinx_config, theme_config, this_pagecontext):
    tp = dict(
        copyright=sphinx_config.copyright,
        show_copyright=theme_config.show_copyright,
        show_powered_by=theme_config.show_powered_by,
        show_sourcelink=True,
        has_source=True,
        pathto=this_pagecontext.pathto,
        sourcename='thispage.md',
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = Footer(**this_props)
    return ci


def test_vdom(this_vdom, this_props):
    assert '&copy; Bazinga.' == this_vdom.children[0]
    assert '|' == this_vdom.children[1][0]
    assert 'Powered by' == this_vdom.children[1][1].strip()
    assert 'a' == this_vdom.children[1][2].tag
    assert '|' == this_vdom.children[2][0]
    assert 'a' == this_vdom.children[2][1].tag
    assert '../mock/_sources/thispage.md' == this_vdom.children[2][1].props['href']


def test_wired_render(themabaster_app, this_container):
    this_vdom = html('<{Footer} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert '../mock/_sources/somedoc.rst' == this_html.select_one('a[rel="nofollow"]').attrs['href']
