import pytest
from viewdom import html
from wired import ServiceContainer

from themester import View
from themester.resources import Root


class DummyView:
    name = 'dummyview'

    def __call__(self):
        return html('<div>Hello</div>')


class DummyContext:
    name = 'dummycontext'


@pytest.fixture
def scanned_modules():
    from themester import renderer
    return renderer,
    # return []


@pytest.fixture
def app_container(registry, sample_tree) -> ServiceContainer:
    # Make the app-wide container, each request "clones" this in the renderer
    ac = registry.create_container()
    ac.register_singleton(sample_tree, Root)
    dummy_view = DummyView()
    ac.register_singleton(dummy_view, View)
    return ac


def test_vdom_renderer(app_container):
    from themester.renderer import Renderer
    vdom_renderer = app_container.get(Renderer)
    response = vdom_renderer('/f1/')
    assert '<div>Hello</div>' == response
