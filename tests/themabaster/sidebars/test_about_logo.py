from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.sidebars.about import logo


@pytest.mark.parametrize('component_package', (logo,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '../mock/_static/site_logo.png' == story0.instance.resolved_logo
    assert '../mock/index' == story0.instance.resolved_master
    assert 'p' == story0.vdom.tag
    assert '../mock/index' == story0.vdom.children[0].props['href']
    this_logo = '../mock/_static/site_logo.png'
    assert this_logo == story0.vdom.children[0].children[0].props['src']

    story1 = these_stories[1]
    assert None is story1.vdom

    story2 = these_stories[2]
    assert '../mock/index' == story2.html.select_one('p.logo a').get('href')
    assert '../mock/_static/site_logo.png' == story2.html.select_one('p.logo img').get('src')
