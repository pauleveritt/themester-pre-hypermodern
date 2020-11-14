from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import head
from themester.themabaster.components.cssfiles import CSSFiles
from themester.themabaster.components.jsfiles import JSFiles
from themester.themabaster.components.title import Title


@pytest.mark.parametrize('component_package', (head,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]

    assert '../mock/_static/custom.css' == story0.instance.resolved_custom_css
    assert '../mock/_static/documentation_options.js' == story0.instance.resolved_docs_src
    assert '../mock/' == story0.instance.resolved_static_root

    this_vdom = story0.vdom
    assert 11 == len(this_vdom.children)
    assert 'head' == this_vdom.tag
    assert 'meta' == this_vdom.children[0].tag
    assert 'meta' == this_vdom.children[1].tag
    title = this_vdom.children[2]
    assert Title == title.tag
    css = this_vdom.children[3]
    assert CSSFiles == css.tag
    js = this_vdom.children[5]
    assert JSFiles == js.tag
    # No children
    assert None is this_vdom.children[10]

    story1 = these_stories[1]
    assert 'first' == story1.instance.extrahead[0].props['rel']
    assert 'second' == story1.instance.extrahead[1].props['rel']

    story2 = these_stories[2]
    assert 'D2 - Python' == story2.html.select_one('title').text
    links = story2.html.select('link')
    assert 17 == len(links)
    assert '../mock/site_first.css' == links[0].attrs['href']
