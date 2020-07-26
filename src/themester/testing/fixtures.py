"""
Fixtures to construct parts of themester for tests in pluggable ways.

Quickly construct an app using defaults. Override those defaults with
local fixtures of the same name.
"""
from typing import Optional, Dict, Any, Callable

import pytest
from bs4 import BeautifulSoup
from markupsafe import Markup
from venusian import Scanner
from viewdom import render, VDOM
from wired import ServiceContainer

from .config import ThemesterConfig
from .resources import Site, Document, Collection
from .. import themabaster
from ..app import ThemesterApp
from ..protocols import Resource
from ..sphinx import PageContext, SphinxConfig
from ..sphinx.prevnext import PreviousLink, NextLink
from ..themabaster.config import ThemabasterConfig


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
def themester_app(themester_site, sphinx_config) -> ThemesterApp:
    """ An app that depends on a root and a config """

    return ThemesterApp(
        root=themester_site,
        sphinx_config=sphinx_config,
    )


@pytest.fixture
def themester_scanner(themester_app) -> Scanner:
    scanner: Scanner = themester_app.container.get(Scanner)
    return scanner


@pytest.fixture
def sphinx_config() -> SphinxConfig:
    tc = SphinxConfig(copyright='Bazinga')
    return tc


@pytest.fixture
def themester_config() -> ThemesterConfig:
    tc = ThemesterConfig()
    return tc


@pytest.fixture
def themabaster_config() -> ThemabasterConfig:
    tc = ThemabasterConfig(
        css_files=('site_first.css', 'site_second.css',),
        favicon='themabaster.ico',
        logo='site_logo.png',
        project='Themester SiteConfig',
        touch_icon='sometouchicon.ico'
    )
    return tc


@pytest.fixture
def themabaster_app(themester_app, themabaster_config):
    """ Wire in the themabaster components, views, layout, etc. """

    themester_app.setup_plugin(themabaster)
    themester_app.registry.register_singleton(themabaster_config, ThemabasterConfig)
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
def this_pathto() -> Callable[[str, Optional[int]], str]:
    def _this_pathto(docname, mode=0) -> str:
        """ Sphinx page context function to get a path to a target """
        return f'../mock/{docname}'

    return _this_pathto


@pytest.fixture
def this_hasdoc() -> Callable[[str], bool]:
    def _this_hasdoc(docname) -> bool:
        """ Sphinx page context function to confirm a path exists """
        return True if docname != 'author' else False

    return _this_hasdoc


@pytest.fixture
def this_toctree() -> Callable[[], str]:
    def _this_toctree() -> str:
        """ Sphinx page context function to return string of toctree """
        return '<ul><li>First</li></ul>'

    return _this_toctree


@pytest.fixture
def this_pagecontext(this_hasdoc, this_pathto, this_toctree):
    pc = PageContext(
        body=Markup('<h1>Some Body</h1>'),
        css_files=('page_first.css', 'page_second.css'),
        display_toc=True,
        hasdoc=this_hasdoc,
        js_files=('page_first.js', 'page_second.js'),
        pagename='somedoc',
        page_source_suffix='.html',
        pathto=this_pathto,
        sourcename='somedoc.rst',
        title='Some Page',
        toc=Markup('<li>toc</li>'),
        toctree=this_toctree,
    )
    return pc


@pytest.fixture
def this_props(this_resource) -> Dict[str, Any]:
    """ Should be implemented by local fixture. Used to construct component. """
    props: Dict[str, Any] = dict()
    return props


@pytest.fixture
def this_resource(themester_site_deep) -> Optional[Resource]:
    this_resource = themester_site_deep['f1']['d2']
    return this_resource


@pytest.fixture
def this_static_url() -> Callable[[str], str]:
    def foo(target: str) -> str:
        return f'mock/{target}'

    return foo


@pytest.fixture
def this_container(
        themester_app,
        themester_scanner,
        this_pagecontext,  # Should have local override
        this_props,  # Should have local override
        this_resource,  # Should have local override
) -> ServiceContainer:
    """ Scan for modules and return a context-bound container """
    this_container = themester_app.container.bind(context=this_resource)

    # For this per-page container, register the PageContext
    # TODO Consider splitting this garbage barge into isolated services
    #   such as PreviousLink and NextLink below
    this_container.register_singleton(this_pagecontext, PageContext)

    # Register singletons for Previous/Next, to mimic the Sphinx "adapter"
    # doing so in html_context, just for this per-request container.
    if this_props.get('previous'):
        this_container.register_singleton(this_props['previous'], PreviousLink)
    if this_props.get('next'):
        this_container.register_singleton(this_props['next'], NextLink)

    return this_container
