import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render

from themester.sphinx.prevnext import PreviousLink, NextLink
from themester.themabaster.components.rellink_markup import RellinkMarkup


@pytest.fixture
def this_props():
    tp = dict(
        previous=PreviousLink(
            title='Previous',
            link='/previous/',
        ),
        next=NextLink(
            title='Next',
            link='/next/',
        )
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = RellinkMarkup(**this_props)
    return ci


def test_construction(this_component: RellinkMarkup):
    assert 'li' == this_component.resolved_previous.tag
    assert 'li' == this_component.resolved_next.tag


def test_vdom(this_vdom, this_props):
    assert 'nav' == this_vdom.tag
    assert dict(id='rellinks') == this_vdom.props
    assert 'ul' == this_vdom.children[0].tag
    c = this_vdom.children[0].children
    assert 'li' == c[0].tag == c[1].tag
    assert '&larr;' == c[0].children[0]
    prev = c[0].children[1]
    assert 'a' == prev.tag
    assert '/previous/' == prev.props['href']
    assert 'Previous Document' == prev.props['title']
    assert 'Previous' == prev.children[0]
    assert '&rarr;' == c[1].children[1]
    n = c[1].children[0]
    assert 'a' == n.tag
    assert '/next/' == n.props['href']
    assert 'Next Document' == n.props['title']
    assert 'Next' == n.children[0]


def test_wired_render(this_container, this_props):
    this_vdom = html('<{RellinkMarkup} />')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('nav#rellinks ul li a')
    assert 2 == len(links)
    assert '/previous/' == links[0].get('href')
    assert 'Previous Document' == links[0].get('title')
    assert 'Previous' == links[0].text
    assert '/next/' == links[1].get('href')
    assert 'Next Document' == links[1].get('title')
    assert 'Next' == links[1].text
