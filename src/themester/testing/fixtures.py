"""
Fixtures to construct parts of themester for tests in pluggable ways.

Quickly construct an app using defaults. Override those defaults with
local fixtures of the same name.
"""
from types import ModuleType
from typing import Tuple, Optional, Dict, Any

import pytest
from bs4 import BeautifulSoup
from venusian import Scanner
from viewdom import render, VDOM
from wired import ServiceContainer

from themester.app import ThemesterApp
from .config import ThemesterConfig
from .resources import Site, Document, Collection
from .. import themabaster, Resource
from ..themabaster.config import ThemabasterConfig
from ..themabaster.pagecontext import PageContext
from ..themabaster.protocols import LayoutConfig


@pytest.fixture
def themester_site() -> Site:
    """ A very simple site root with no child resources """
    return Site()


@pytest.fixture
def themester_site_deep() -> Site:
    """ A nested site root with documents and collections """
    site = Site()
    f1 = Collection(name='f1', parent=site, title='F1')
    site['f1'] = f1
    d1 = Document(name='d1', parent=site, title='D1')
    site['d1'] = d1
    d2 = Document(name='d2', parent=f1, title='D2')
    f1['d2'] = d2
    f3 = Collection(name='f3', parent=f1, title='F3')
    f1['f3'] = f3
    d3 = Document(name='d3', parent=f3, title='D3')
    f3['d3'] = d3
    return site


@pytest.fixture
def themester_app(themester_site, themester_config) -> ThemesterApp:
    """ An app that depends on a root and a config """

    return ThemesterApp(root=themester_site, config=themester_config)


@pytest.fixture
def themester_scanner(themester_app) -> Scanner:
    scanner: Scanner = themester_app.container.get(Scanner)
    return scanner


@pytest.fixture
def themester_config() -> ThemesterConfig:
    """ Dead-simple configuration """
    tc = ThemesterConfig(site_name='Themester SiteConfig')
    return tc


@pytest.fixture
def these_modules() -> Tuple[ModuleType, ...]:
    """ A tuple with imported modules for themester to scan """
    return tuple()


@pytest.fixture
def themabaster_config() -> ThemabasterConfig:
    """ Dead-simple configuration """
    tc = ThemabasterConfig(
        site_name='Themester SiteConfig',
        css_files=('site_first.css', 'site_second.css',)
    )
    return tc


@pytest.fixture
def themabaster_app(themester_app, themabaster_config):
    """ Wire in the themabaster components, views, layout, etc. """

    themester_app.setup_plugin(themabaster)
    themester_app.registry.register_singleton(themabaster_config, LayoutConfig)
    return themester_app


@pytest.fixture
def this_vdom(this_component) -> VDOM:
    """ Use a local ``this_component`` fixture and render to a VDOM """
    vdom = this_component()
    return vdom


@pytest.fixture
def this_html(this_vdom) -> BeautifulSoup:
    rendered = render(this_vdom)
    html = BeautifulSoup(rendered, 'html.parser')
    return html


@pytest.fixture
def this_pagecontext():
    pc = PageContext(
        body='<h1>Some Body</h1>',
        css_files=('page_first.css', 'page_second.css'),
        js_files=('page_first.js', 'page_second.js'),
        title='Some Page',
        display_toc=True,
        page_source_suffix='.html',
        sourcename='somedoc.rst',
        toc='<li>toc</li>',
    )
    return pc


@pytest.fixture
def this_props(this_resource) -> Dict[str, Any]:
    """ Should be implemented by local fixture. Used to construct component. """
    props: Dict[str, Any] = dict()
    return props


@pytest.fixture
def this_resource() -> Optional[Resource]:
    """ Use None unless a local test provides a fixture """
    return None


@pytest.fixture
def this_container(
        themester_app,
        themester_scanner,
        this_pagecontext,  # Should have local override
        this_props,  # Should have local override
        these_modules,  # # Should have local override
        this_resource,  # Should have local override
) -> ServiceContainer:
    """ Scan for modules and return a context-bound container """
    [themester_scanner.scan(this_module) for this_module in these_modules]
    this_container = themester_app.container.bind(context=this_resource)

    # For this per-page container, register the PageContext
    this_container.register_singleton(this_pagecontext, PageContext)
    return this_container
