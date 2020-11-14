from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars import about
from themester.themabaster.sidebars.about import AboutLogo, AboutDescription, AboutGitHubButton, AboutTravisButton


@pytest.mark.parametrize('component_package', (about,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    this_vdom = story0.vdom
    assert AboutLogo == this_vdom[0].tag
    assert AboutDescription == this_vdom[1].tag
    assert AboutGitHubButton == this_vdom[2].tag
    assert AboutTravisButton == this_vdom[3].tag

    story1 = these_stories[1]
    href = story1.html.select_one('p.logo a').get('href')
    assert '../mock/index' == href
