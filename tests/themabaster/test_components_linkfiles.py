import pytest
from bs4 import BeautifulSoup
from viewdom import html
from viewdom_wired import render, adherent

from themester.themabaster.components.linktags import SemanticLink
from themester.themabaster.protocols import Hasdoc


@adherent(Hasdoc)
class TestHasDoc(Hasdoc):
    def __call__(self, target: str) -> bool:
        # Remove one of the dummy documents from the listing
        return False if target == 'author' else True


@pytest.fixture
def this_props(this_url, this_static_url):
    link1: SemanticLink = dict(
        rel='index',
        docname='genindex',
        title='Index'
    )
    link2: SemanticLink = dict(
        rel='author',
        docname='author',
        title='Author'
    )
    link3: SemanticLink = dict(
        rel='copyright',
        docname='copyright',
        title='Copyright'
    )
    links = (link1, link2, link3)
    test_hasdoc = TestHasDoc()
    props = dict(
        hasdoc=test_hasdoc,
        links=links,
        static_url=this_static_url,
    )
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.linktags import DefaultLinktags
    ci = DefaultLinktags(**this_props)
    return ci


@pytest.fixture
def these_modules():
    from themester.themabaster.components import linktags
    return linktags,


def test_construction(this_component, this_props):
    for k, v in this_props.items():
        assert getattr(this_component, k) == v


def test_vdom(this_vdom):
    assert 'mock/genindex' == this_vdom[0].props['href']
    assert 'index' == this_vdom[0].props['rel']
    assert 'Index' == this_vdom[0].props['title']
    assert 'mock/copyright' == this_vdom[1].props['href']
    assert 'copyright' == this_vdom[1].props['rel']
    assert 'Copyright' == this_vdom[1].props['title']


def test_render(this_html):
    links = this_html.select('link')
    assert 2 == len(links)
    assert 'mock/genindex' == links[0].attrs['href']
    assert 'mock/copyright' == links[1].attrs['href']


def test_wired_render(this_container, this_props):
    from themester.themabaster.protocols import Linktags  # noqa
    del this_props['static_url']
    this_vdom = html('<{Linktags} ...{this_props}/>')
    rendered = render(this_vdom, container=this_container)
    this_html = BeautifulSoup(rendered, 'html.parser')
    links = this_html.select('link')
    assert 2 == len(links)
    assert '../../../genindex' == links[0].attrs['href']
