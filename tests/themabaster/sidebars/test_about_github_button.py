from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars.about import github_button


@pytest.mark.parametrize('component_package', (github_button,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert False is story0.instance.show_button

    story1 = these_stories[1]
    assert True is story1.instance.show_button

    story2 = these_stories[2]
    assert '' == str(story2.html)

    story3 = these_stories[3]
    src = story3.html.select_one('iframe').get('src')
    assert 'thisrepo' in src
    assert 'thisuser' in src
