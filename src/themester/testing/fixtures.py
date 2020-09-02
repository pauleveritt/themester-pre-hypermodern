"""
Fixtures to construct parts of themester for tests in pluggable ways.

Quickly construct an app using defaults. Override those defaults with
local fixtures of the same name.
"""
from dataclasses import dataclass
from importlib import import_module
from typing import Optional, Dict, Any, Callable, Tuple

import pytest
from bs4 import BeautifulSoup
from markupsafe import Markup
from venusian import Scanner
from viewdom import render, VDOM, html
from wired import ServiceContainer

from .resources import Site, Document, Collection
from ..config import ThemesterConfig
from ..protocols import Resource
from ..sphinx.models import PageContext, Link
from ..storytime import Story


@dataclass
class ThisComponent:
    name: str = 'This Component'

    def __call__(self) -> VDOM:
        return html('<div>{self.name}</div>')


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
def themester_config(themester_site_deep) -> ThemesterConfig:
    tc = ThemesterConfig(root=themester_site_deep)
    return tc


@pytest.fixture
def themester_app(themester_site, themester_config):
    """ An app that depends on a root and a config """

    from ..app import ThemesterApp
    ta = ThemesterApp(
        themester_config=themester_config,
    )
    ta.setup_plugins()

    return ta


@pytest.fixture
def themester_scanner(themester_app) -> Scanner:
    container = themester_app.registry.create_container()
    scanner: Scanner = container.get(Scanner)
    return scanner


@pytest.fixture
def this_props(this_resource) -> Dict[str, Any]:
    """ Should be implemented by local fixture. Used to construct component. """
    props: Dict[str, Any] = dict()
    return props


@pytest.fixture
def this_component(this_props):
    """ Intended to be overriden """

    ci = ThisComponent(**this_props)

    return ci


@pytest.fixture
def this_vdom(this_component) -> VDOM:
    """ Use a local ``this_component`` fixture and render to a VDOM """
    vdom = this_component()
    return vdom


@pytest.fixture
def this_html(this_vdom) -> BeautifulSoup:
    rendered = render(this_vdom)
    this_html = BeautifulSoup(rendered, 'html.parser')
    return this_html


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
def this_toctree() -> Callable[[bool, bool], str]:
    def _this_toctree(sidebar_collapse: bool = True, sidebar_includehidden: bool = True) -> str:
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
        prev=Link(
            title='Previous',
            link='/previous/',
        ),
        next=Link(
            title='Next',
            link='/next/',
        ),
        sourcename='somedoc.rst',
        title='Some Page',
        toc=Markup('<li>toc</li>'),
        toctree=this_toctree,
    )
    return pc


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
    this_container = themester_app.registry.create_container(context=this_resource)

    # For this per-page container, register the PageContext
    this_container.register_singleton(this_pagecontext, PageContext)

    return this_container


@pytest.fixture
def these_stories(component_package) -> Tuple[Story]:
    # Now get the default story
    stories = import_module(component_package.__name__ + '.stories')
    all_stories = getattr(stories, 'all_stories')()
    return all_stories
