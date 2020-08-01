import pytest

from themester.app import ThemesterApp
from themester.sphinx.template_bridge import ThemesterBridge

pytest_plugins = [
    'themester.testing.fixtures',
]


@pytest.fixture
def render_themester_bridge() -> ThemesterBridge:
    tb = ThemesterBridge()
    return tb


@pytest.fixture
def render_context(themester_app: ThemesterApp):
    from themester.testing import views
    themester_app.setup_plugin(views)
    container = themester_app.registry.create_container()
    c = dict(render_container=container)
    return c


def test_themester_bridge_construction(render_themester_bridge):
    assert render_themester_bridge
    # Bring these back when we stop using BuiltinTemplateLoader
    # assert render_themester_bridge.newest_template_mtime() == 0
    # with pytest.raises(NotImplementedError):
    #     render_themester_bridge.render_string('', {})


def test_themester_bridge_render(render_themester_bridge, render_context):
    actual = render_themester_bridge.render('', render_context)
    assert '<div>View: Fixture View</div>' == actual
