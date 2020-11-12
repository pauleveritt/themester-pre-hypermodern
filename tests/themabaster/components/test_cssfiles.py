from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import cssfiles


@pytest.mark.parametrize('component_package', (cssfiles,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '_static/themabaster.css' == story0.instance.hrefs[0]
    assert '_static/pygments.css' == story0.instance.hrefs[1]
    assert 'page_first.css' == story0.instance.hrefs[2]
    assert 'page_second.css' == story0.instance.hrefs[3]
    assert '_static/themabaster.css' == story0.vdom[0].props['href']
    links = story0.html.select('link')
    assert 4 == len(links)
    assert '_static/themabaster.css' == links[0].attrs['href']

    story1 = these_stories[1]
    links = story1.html.select('link')
    assert 4 == len(links)
    assert '../mock/_static/themabaster.css' == links[0].attrs['href']
