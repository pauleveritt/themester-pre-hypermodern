"""
No containers, just make dataclass instances
"""
import pytest
from bs4 import BeautifulSoup
from viewdom import render, html

from themester.testing.resources import Document
from themester.themabaster.components.head import DefaultHead


@pytest.fixture
def document(themester_site_deep) -> Document:
    d = themester_site_deep['f1']['d2']
    return d


@pytest.fixture
def head_title():
    from themester.themabaster.components.title import DefaultTitle
    ht = DefaultTitle(page_title='Page Title', site_name='Site Name')
    return ht


def test_component_head_default(document):
    """ Test both the vdom and rendered for this component """
    c = DefaultHead(resource=document, css_files=())
    assert c.metatags == ()
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [None, []]
    rendered = render(vdom)
    result = BeautifulSoup(rendered, 'html.parser')
    selection = result.select('head meta')
    assert len(selection) == 2


def test_component_head_title(document, head_title):
    """ Pass in a <title> """
    c = DefaultHead(resource=document, css_files=(), title=head_title)
    assert c.metatags == ()
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [[], head_title]
    rendered = render(vdom)
    result = BeautifulSoup(rendered, 'html.parser')
    selection = result.select_one('title').text
    assert selection == head_title.page_title + ' - ' + head_title.site_name


def test_component_head_metatags(document):
    """ Pass in some <meta> tags """
    charset = 'utf-8'
    metas = (
        html('<meta name="foo" content="bar"/>'),
    )
    c = DefaultHead(resource=document, css_files=(), metatags=metas)
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [None, [metas[0], metas[1]]]
    rendered = render(vdom)
    result = BeautifulSoup(rendered, 'html.parser')
    selection = result.find("meta", attrs={"name": "foo"})
    assert selection.attrs['content'] == 'bar'


def test_component_head_css_files(document):
    """ Use the config to pass in some css_files """
    css_files = ('foo.css', 'bar.css')
    c = DefaultHead(resource=document, css_files=css_files)
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [None, [metas[0], metas[1]]]
    rendered = render(vdom)
    result = BeautifulSoup(rendered, 'html.parser')
    selection = result.select('link')
    assert selection[0].attrs['href'] == '../../../foo.css'
    assert selection[1].attrs['href'] == '../../../bar.css'
