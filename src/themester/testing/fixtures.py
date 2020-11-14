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
from venusian import Scanner
from viewdom import render, VDOM, html
from wired import ServiceContainer

from .. import make_registry
from ..resources import Site, Document
from ..config import ThemesterConfig
from ..protocols import Resource
from ..sphinx import SphinxConfig
from ..sphinx.models import PageContext
from ..storytime import Story
from ..themabaster.storytime_example import root, fake_pagecontext, fake_pathto, fake_hasdoc, fake_toctree


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
    return root


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
    return fake_pathto


@pytest.fixture
def this_hasdoc() -> Callable[[str], bool]:
    return fake_hasdoc


@pytest.fixture
def this_toctree() -> Callable[[bool, bool], str]:
    return fake_toctree


@pytest.fixture
def this_pagecontext(this_hasdoc, this_pathto, this_toctree):
    return fake_pagecontext


@pytest.fixture
def this_resource(themester_site_deep) -> Document:
    this_resource = themester_site_deep['f1']['d2']
    return this_resource


@pytest.fixture
def this_root(themester_site_deep) -> Site:
    return themester_site_deep


@pytest.fixture
def this_static_url() -> Callable[[str], str]:
    def foo(target: str) -> str:
        return f'mock/{target}'

    return foo


@pytest.fixture
def this_container() -> ServiceContainer:
    from themester.themabaster.stories import (
        singletons,
    )
    from themester.stories import (
        root,
        resource,
    )
    registry = make_registry(
        root=root,
    )
    container = registry.create_container(context=resource)
    for service, iface in singletons:
        container.register_singleton(service, iface)
    return container


@pytest.fixture
def these_stories(component_package) -> Tuple[Story]:
    # Now get the default story
    stories = import_module(component_package.__name__ + '.stories')
    all_stories = getattr(stories, 'all_stories')()
    return all_stories
