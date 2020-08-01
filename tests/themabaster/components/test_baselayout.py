import dataclasses

from bs4 import BeautifulSoup, Doctype
from markupsafe import Markup
from viewdom import html
from viewdom_wired import render

from themester.sphinx import SphinxConfig
from themester.themabaster.components.base_layout import BaseLayout  # noqa: F401


def doctype(soup):
    items = [item for item in soup.contents if isinstance(item, Doctype)]
    return items[0] if items else None


def test_construction(sphinx_config):
    ci = BaseLayout(
        language=sphinx_config.language,
        extrahead=None,
    )
    assert dict(lang='EN') == ci.html_props


def test_defaults(this_container):
    vdom = html('<{BaseLayout} />')
    rendered = render(vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')

    assert 'EN' == this_html.select_one('html').get('lang')
    assert 12 == len(this_html.select('html head link'))
    assert 'html' == doctype(this_html)


def test_config(this_container, sphinx_config):
    sc = dataclasses.replace(
        sphinx_config,
        language='FR'
    )
    this_container.register_singleton(sc, SphinxConfig)
    this_vdom = html('<{BaseLayout} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'FR' == this_html.select_one('html').get('lang')


def test_extrahead(this_container):
    extrahead = html('<link rel="stylesheet" />')
    this_vdom = html('<{BaseLayout} extrahead={extrahead} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 13 == len(this_html.select('html head link'))


def test_doctype(this_container):
    this_doctype = Markup('<!DOCTYPE html5>\n')
    this_vdom = html('<{BaseLayout} doctype={this_doctype} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'html5' == doctype(this_html)
