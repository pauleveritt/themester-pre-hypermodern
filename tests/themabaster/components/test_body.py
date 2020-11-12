from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import body


@pytest.mark.parametrize('component_package', (body,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert {} == story0.vdom.props

    story1 = these_stories[1]
    assert story1.html.select_one('div.sphinxsidebar')
    assert '../mock/_sources/somedoc.rst' == story1.html.select_one('a[rel="nofollow"]').attrs['href']
