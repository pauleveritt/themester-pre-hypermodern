import pytest


@pytest.fixture
def scanned_module():
    from .examples.views import (
        views01,
    )
    return views01,


def test_views01():
    from themester.views import View
    v = View()
    assert 9 == v
