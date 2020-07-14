from viewdom import html
from viewdom_wired import render


def test_wired_render_base_layout(themabaster_app, this_container):
    from themester.themabaster.layouts.base_layout import BaseLayout  # noqa: F401
    extrahead = html('<link rel="stylesheet" />')
    this_vdom = html('<{BaseLayout} extrahead={extrahead} />')
    rendered = render(this_vdom, container=this_container)
    assert '<html lang="EN"><head><link rel="stylesheet"/></head></html>' == rendered


def test_wired_render_sidebar_layout(themabaster_app, this_container):
    from themester.themabaster.layouts.base_layout import SidebarLayout  # noqa
    this_vdom = html('<{SidebarLayout} />')
    rendered = render(this_vdom, container=this_container)
    assert '<html lang="EN"><head></head></html>' == rendered
