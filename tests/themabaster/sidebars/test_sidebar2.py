from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import sidebar2
from themester.themabaster.sidebars.localtoc import LocalToc
from themester.themabaster.sidebars.relations import Relations
from themester.themabaster.sidebars.searchbox import SearchBox
from themester.themabaster.sidebars.sourcelink import SourceLink


@pytest.mark.parametrize('component_package', (sidebar2,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 4 == len(story0.instance.resolved_sidebars)
    assert LocalToc == story0.instance.resolved_sidebars[0].tag
    assert 'div' == story0.vdom.tag
    ssw = story0.vdom.children[0]
    sidebars = ssw.children[0]
    assert 4 == len(sidebars)
    assert LocalToc == sidebars[0].tag
    assert Relations == sidebars[1].tag
    assert SourceLink == sidebars[2].tag
    assert SearchBox == sidebars[3].tag

    story1 = these_stories[1]
    assert [] == story1.vdom

    story2 = these_stories[2]
    assert 'Table of Contents' == story2.html.select('h3 a')[0].text
    assert 'Contents' == story2.html.select_one('.relations h3').text
