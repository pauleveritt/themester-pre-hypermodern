import dataclasses

from bs4 import BeautifulSoup, Doctype
from markupsafe import Markup
from viewdom import html
from viewdom_wired import render

from themester.themabaster.base_layout import BaseLayout  # noqa: F401
from themester.themabaster.base_layout import ThemabasterConfig


def doctype(soup):
    items = [item for item in soup.contents if isinstance(item, Doctype)]
    return items[0] if items else None


def test_defaults(themabaster_app, this_container):
    vdom = html('<{BaseLayout} />')
    rendered = render(vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')

    assert 'EN' == this_html.select_one('html').get('lang')
    assert 6 == len(this_html.select('html head link'))
    assert 'html' == doctype(this_html)


def test_config(themabaster_app, this_container, themabaster_config):
    tc = dataclasses.replace(
        themabaster_config,
        lang='FR'
    )
    this_container.register_singleton(tc, ThemabasterConfig)
    this_vdom = html('<{BaseLayout} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'FR' == this_html.select_one('html').get('lang')


def test_extrahead(themabaster_app, this_container):
    extrahead = html('<link rel="stylesheet" />')
    this_vdom = html('<{BaseLayout} extrahead={extrahead} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 7 == len(this_html.select('html head link'))


def test_doctype(themabaster_app, this_container):
    this_doctype = Markup('<!DOCTYPE html5>\n')
    this_vdom = html('<{BaseLayout} doctype={this_doctype} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'html5' == doctype(this_html)
