import pytest
from wired import ServiceRegistry

from themester.sphinx.template_bridge import ThemesterBridge
from themester.testing.views import FixtureView
from themester.views import View


@pytest.fixture
def render_themester_bridge() -> ThemesterBridge:
    tb = ThemesterBridge()
    return tb


@pytest.fixture
def render_context():
    registry = ServiceRegistry()
    render_container = registry.create_container()
    fixture_view = FixtureView()
    render_container.register_singleton(fixture_view, View)
    rc = dict(View=fixture_view)
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
