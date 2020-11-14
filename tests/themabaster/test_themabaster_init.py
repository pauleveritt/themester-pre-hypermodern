from pathlib import Path
from typing import Tuple

from bs4 import BeautifulSoup

from themester.protocols import View, ThemeConfig, Root
from themester.resources import Site
from themester.sphinx.models import PageContext
from themester.stories import resource
from themester.themabaster.components.title import Title
from themester.themabaster.config import ThemabasterConfig
from themester.themabaster.stories import page_context
from themester.themabaster.views import PageView
from themester.utils import render_view


def test_make_registry(themabaster_registry):
    container = themabaster_registry.create_container()

    # Config
    theme_config = container.get(ThemeConfig)
    assert isinstance(theme_config, ThemabasterConfig)

    # Root
    root: Site = container.get(Root)
    assert 'Themester Site' == root.title

    # Components
    component = container.get(Title)
    assert component is Title

    # Views
    view = container.get(View)
    assert isinstance(view, PageView)


def test_render_view(themabaster_registry):
    rendered = render_view(
        themabaster_registry,
        context=resource,
        resource=resource,
        singletons=((page_context, PageContext),)
    )
    this_html = BeautifulSoup(rendered, 'html.parser')
    assert 'D2 - Themester SiteConfig' == this_html.select_one('title').text


def test_get_static_resources(themabaster_registry):
    container = themabaster_registry.create_container()
    themabaster_config: ThemabasterConfig = container.get(ThemeConfig)
    result: Tuple[Path] = themabaster_config.get_static_resources()
    assert 'themabaster.css' == result[0].name
