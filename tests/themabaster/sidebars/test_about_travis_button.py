from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars.about import travis_button


@pytest.mark.parametrize('component_package', (travis_button,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert 'None/None' == story0.instance.resolved_path
    assert None is story0.vdom

    story1 = these_stories[1]
    anchor = story1.vdom.children[0]
    assert 'a' is anchor.tag
    assert 'https://travis-ci.org/thisuser/thisrepo' == anchor.props['href']
    img = anchor.children[0]
    assert 'img' == img.tag
    u = 'https://secure.travis-ci.org/thisuser/thisrepo.svg?branch=master'
    assert u == img.props['alt']
    assert u == img.props['src']

    story2 = these_stories[2]
    assert '' == str(story2.html)

    story3 = these_stories[3]
    src = story3.html.select_one('img').get('src')
    assert 'thisrepo' in src
    assert 'thisuser' in src
