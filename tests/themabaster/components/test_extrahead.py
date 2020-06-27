import pytest
from viewdom import html
from viewdom_wired import render


@pytest.fixture
def this_props():
    props = dict()
    return props


@pytest.fixture
def this_component(this_props):
    from themester.themabaster.components.extra_head import DefaultExtraHead
    ci = DefaultExtraHead()
    return ci


def test_vdom(this_vdom):
    # TODO Need to re-invent VDOM data type to be tuple-ish at the root.
    assert 0 == len(this_vdom)


def test_wired_render(this_container, this_props, themabaster_app):
    from themester.themabaster.protocols import ExtraHead  # noqa
    this_vdom = html('<{ExtraHead} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered
