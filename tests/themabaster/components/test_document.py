from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import document
from themester.themabaster.components.relbar1 import Relbar1
from themester.themabaster.components.relbar2 import Relbar2


@pytest.mark.parametrize('component_package', (document,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'div' == story0.vdom.tag
    assert 'documentwrapper' == story0.vdom.props['class']
    assert 'div' == story0.vdom.children[0].tag
    assert 'bodywrapper' == story0.vdom.children[0].props['class']
    assert 1 == len(story0.vdom.children[0].children)
    assert Relbar1 == story0.vdom.children[0].children[0][0].tag
    assert 'div' == story0.vdom.children[0].children[0][1].tag
    assert Relbar2 == story0.vdom.children[0].children[0][2].tag

    story1 = these_stories[1]
    div = story1.html.select_one('div.documentwrapper')
    assert ['documentwrapper'] == div.get('class')
    assert div.select_one('div.bodywrapper')
    assert div.select_one('div.body')
    # relbars are off by default
    assert not div.select('div.top')
    assert not div.select('div.bottom')
