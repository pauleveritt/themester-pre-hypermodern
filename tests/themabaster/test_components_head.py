"""
No containers, just make dataclass instances
"""
import pytest
from viewdom import render, html

from themester.themabaster.components.head import DefaultHead


@pytest.fixture
def head_title():
    from themester.themabaster.components.title import DefaultTitle
    ht = DefaultTitle(page_title='Page Title', site_name='Site Name')
    return ht


def test_component_head_default():
    """ Test both the vdom and rendered for this component """
    c = DefaultHead()
    assert c.metatags == ()
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [None, []]
    result = render(vdom)
    assert result == '<head></head>'


def test_component_head_title(head_title):
    """ Pass in a <title> """
    c = DefaultHead(title=head_title)
    assert c.metatags == ()
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [[], head_title]
    result = render(vdom)
    assert result == '<head><title>Page Title - Site Name</title></head>'


def test_component_head_metatags():
    """ Pass in some <meta> tags """
    charset = 'utf-8'
    metas = (
        html('<meta charset="{charset}"/>'),
        html('<meta name="viewport" content="width=device-width, initial-scale=1"/>'),
    )
    c = DefaultHead(metatags=metas)
    vdom = c()
    tag, props, children = vdom
    assert tag == 'head'
    assert props == {}
    # TODO Re-enable when we omit None and [] from html()
    # assert children == [None, [metas[0], metas[1]]]
    result = render(vdom)
    assert result == '<head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/></head>'
