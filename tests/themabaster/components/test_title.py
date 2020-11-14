from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import title


@pytest.mark.parametrize('component_package', (title,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'Themabaster' == story0.instance.resource_title
    assert 'Story Site' == story0.instance.site_title
    assert 'title' == story0.vdom.tag
    assert 'Themabaster - Story Site' == story0.html.select_one('title').text

    story1 = these_stories[1]
    assert 'Some Page' == story1.instance.resolved_title

    story2 = these_stories[2]
    assert 'Themabaster - Story Site' == story2.instance.resolved_title

    story3 = these_stories[3]
    assert 'D2 - XYZ' == story3.html.select_one('title').text
