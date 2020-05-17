import pytest
from wired import ServiceRegistry

from themester import View
from themester.sphinx.template_bridge import ThemesterBridge


class RenderView(View):

    def __call__(self) -> str:
        from viewdom import html
        return html('<div>hello</div>')


@pytest.fixture
def render_themester_bridge() -> ThemesterBridge:
    tb = ThemesterBridge()
    return tb


@pytest.fixture
def render_view() -> View:
    return RenderView()


@pytest.fixture
def render_context(render_view):
    registry = ServiceRegistry()
    render_container = registry.create_container()
    render_container.register_singleton(render_view, View)
    rc = dict(View=render_view)
    c = dict(render_container=render_container)
    return c


def test_render_construction(render_themester_bridge):
    assert render_themester_bridge
    assert render_themester_bridge.newest_template_mtime() == 0
    with pytest.raises(NotImplementedError):
        render_themester_bridge.render_string('', {})


def test_render_render(render_themester_bridge, render_context):
    actual = render_themester_bridge.render('', render_context)
    assert actual == '<div>hello</div>'
