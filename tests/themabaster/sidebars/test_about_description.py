import dataclasses

import pytest
from viewdom import html
from viewdom_wired import render

from themester.protocols import ThemeConfig
from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.sidebars.about_description import AboutDescription


@pytest.fixture
def this_props(theme_config):
    tp = dict(
        description=theme_config.description
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = AboutDescription(**this_props)
    return ci


def test_construction(this_component: AboutDescription):
    assert None is this_component.description


def test_vdom(this_vdom):
    assert None is this_vdom


def test_vdom_with_description():
    ci = AboutDescription('Some Project')
    local_vdom = ci()
    assert 'p' == local_vdom.tag
    assert 'Some Project' == local_vdom.children[0]


def test_wired_render(this_container):
    this_vdom = html('<{AboutDescription} />')
    rendered = render(this_vdom, container=this_container)
    assert '' == rendered


def test_wired_render_with_description(this_container, theme_config):
    tc = dataclasses.replace(theme_config, description='Some Description')
    this_container.register_singleton(tc, ThemeConfig)
    this_vdom = html('<{AboutDescription} />')
    rendered = render(this_vdom, container=this_container)
    assert '<p class="blurb">Some Description</p>' == rendered
