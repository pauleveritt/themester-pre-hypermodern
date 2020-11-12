from typing import Tuple

import pytest

from themester.storytime import Story
from themester.themabaster.components import footer


@pytest.mark.parametrize('component_package', (footer,))
def test_stories(these_stories: Tuple[Story, ...]):
    story0 = these_stories[0]
    assert '&copy; Bazinga.' == story0.vdom.children[0]
    assert '|' == story0.vdom.children[1][0]
    assert 'Powered by' == story0.vdom.children[1][1].strip()
    assert 'a' == story0.vdom.children[1][2].tag

    story1 = these_stories[1]
    assert '../mock/_sources/somedoc.rst' == story1.html.select_one('a[rel="nofollow"]').attrs['href']
