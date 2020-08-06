import pytest
from viewdom import html
from viewdom_wired import render

from themester.sphinx.models import Link
from themester.themabaster.sidebars.navigation_extra_links import NavigationExtraLinks


@pytest.fixture
def this_props(theme_config):
    tp = dict(
        extra_nav_links=theme_config.extra_nav_links,
    )
    return tp


@pytest.fixture
def this_component(this_props):
    ci = NavigationExtraLinks(**this_props)
    return ci


def test_construction(this_component: NavigationExtraLinks):
    assert None is this_component.extra_nav_links
    assert None is this_component.resolved_links


def test_construction_with_links():
    extra_nav_links = (
        Link(title='First Link', link='link1.com'),
        Link(title='Second Link', link='link2.com'),
    )
    ci = NavigationExtraLinks(extra_nav_links=extra_nav_links)
    assert 2 == len(ci.resolved_links)


def test_vdom(this_vdom, this_props):
    assert None is this_vdom


def test_vdom_with_links(this_vdom, this_props):
    extra_nav_links = (
        Link(title='First Link', link='link1.com'),
        Link(title='Second Link', link='link2.com'),
    )
    ci = NavigationExtraLinks(extra_nav_links=extra_nav_links)
    local_vdom = ci()
    assert 'hr' == local_vdom[0].tag
    assert 'ul' == local_vdom[1].tag
    li = local_vdom[1].children[0]
    assert 2 == len(li)
    first_a = li[0].children[0]
    assert 'link1.com' == first_a.props['href']
    assert 'First Link' == first_a.children[0]


def test_wired_render(this_container):
    this_vdom = html('<{NavigationExtraLinks} />')
    rendered = render(this_vdom, container=this_container)
    assert '' is rendered
