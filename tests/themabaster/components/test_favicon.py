from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import favicon


@pytest.mark.parametrize('component_package', (favicon,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'someicon.png' == story0.instance.href
    assert 'shortcut icon' == story0.vdom.props['rel']
    assert 'someicon.png' == story0.vdom.props['href']
    assert [] == story0.vdom.children

    story1 = these_stories[1]
    link = story1.html.select_one('link')
    assert '../mock/someicon.png' == link.attrs['href']


@pytest.fixture
def this_props():
    props = dict(
        href='someicon.png',
    )
    return props
