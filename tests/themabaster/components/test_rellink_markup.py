from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import rellink_markup


@pytest.mark.parametrize('component_package', (rellink_markup,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'li' == story0.instance.resolved_previous.tag
    assert 'li' == story0.instance.resolved_previous.tag
    this_vdom = story0.vdom
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

    story1 = these_stories[1]
    this_html = story1.html
    links = this_html.select('nav#rellinks ul li a')
    assert 2 == len(links)
    assert '/previous/' == links[0].get('href')
    assert 'Previous Document' == links[0].get('title')
    assert 'Previous' == links[0].text
    assert '/next/' == links[1].get('href')
    assert 'Next Document' == links[1].get('title')
    assert 'Next' == links[1].text
