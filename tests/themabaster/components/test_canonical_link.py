import dataclasses

import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.sphinx import HTMLConfig
from themester.themabaster.components.canonical_link import CanonicalLink


@pytest.fixture
def this_props(sphinx_config, html_config, this_pagecontext):
    props = dict(
        baseurl='https://somewhere.com/mysite',
        file_suffix=html_config.file_suffix,
        pagename=this_pagecontext.pagename,
    )
    return props


@pytest.fixture
def this_component(this_props):
    ci = CanonicalLink(**this_props)
    return ci


def test_construction(this_component: CanonicalLink):
    assert 'https://somewhere.com/mysite/somedoc.html' == this_component.canonical_href


def test_vdom(this_vdom):
    assert 'canonical' == this_vdom.props['rel']
    assert 'https://somewhere.com/mysite/somedoc.html' == this_vdom.props['href']


def test_no_baseurl(this_props):
    this_props['baseurl'] = None
    ci = CanonicalLink(**this_props)
    expected = 'https://somewhere.com/mysite/somedoc.html'
    assert None is ci.canonical_href
    vdom = ci()
    assert None is vdom


def test_render(this_html):
    link = this_html.select_one('link')
    assert 'canonical' == link.get('rel')[0]
    assert 'https://somewhere.com/mysite/somedoc.html' == link.get('href')


def test_wired_render(this_container, html_config):
    sc = dataclasses.replace(
        html_config,
        baseurl='https://somewhere.com/mysite',
    )
    this_container.register_singleton(sc, HTMLConfig)
    this_vdom = html('<{CanonicalLink} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    link = this_html.select_one('link')
    assert 'canonical' == link.get('rel')[0]
    assert 'https://somewhere.com/mysite/somedoc.html' == link.get('href')
