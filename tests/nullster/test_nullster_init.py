from pathlib import Path
from typing import Tuple

import pytest

from themester import make_registry, nullster
from themester.nullster.config import NullsterConfig
from themester.protocols import Root, ThemeConfig
from themester.resources import Site
from themester.stories import root
from themester.utils import render_view
from themester.views import View


@pytest.fixture
def nullster_registry():
    from themester.stories import root
    theme_config = NullsterConfig()
    plugins = nullster
    registry = make_registry(
        root=root,
        plugins=plugins,
        theme_config=theme_config,
    )
    return registry


def test_make_registry(nullster_registry):
    from themester.nullster.components.hello_world import HelloWorld
    from themester.nullster.views import AllView
    container = nullster_registry.create_container()

    # Config
    theme_config = container.get(ThemeConfig)
    assert isinstance(theme_config, NullsterConfig)

    # Root
    root: Site = container.get(Root)
    assert 'Themester Site' == root.title

    # Components
    component = container.get(HelloWorld)
    assert component is HelloWorld

    # Views
    view = container.get(View)
    assert isinstance(view, AllView)
    assert 'Nullster View' == view.name


def test_render_view(nullster_registry):
    resource = root['d1']
    html = render_view(nullster_registry, resource=resource)
    expected = '<div><h1>Resource: D1</h1><span>Hello Nullster</span></div>'
    assert expected == html


def test_get_static_resources(nullster_registry):
    container = nullster_registry.create_container()
    nullster_config: NullsterConfig = container.get(ThemeConfig)
    result: Tuple[Path] = nullster_config.get_static_resources()
    assert 'nullster.css' == result[0].name
