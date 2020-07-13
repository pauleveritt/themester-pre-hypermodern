from viewdom import html
from viewdom_wired import render



def test_wired_render_base_layout(themabaster_app, this_container):
    from themester.themabaster.protocols import BaseLayout  # noqa
    this_vdom = html('<{BaseLayout} />')
    rendered = render(this_vdom, container=this_container)
    # assert 9 == rendered


def test_wired_render_sidebar_layout(themabaster_app, this_container):
    from themester.themabaster.layouts.base_layout import SidebarLayout  # noqa
    this_vdom = html('<{SidebarLayout} />')
    rendered = render(this_vdom, container=this_container)
    assert 9 == rendered
