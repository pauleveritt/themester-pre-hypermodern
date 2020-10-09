"""

Implementation-independent PEP 544 protocols for everything in the
registry.

"""
from __future__ import annotations

from pathlib import Path
from typing import Optional, Tuple

from sphinx.application import Sphinx
from viewdom import VDOM
from wired import ServiceRegistry

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol


class ThemeSphinxConfig(Protocol):
    """ Let the theme tell Sphinx what it has/needs """

    @staticmethod
    def get_static_resources() -> Tuple[Path, ...]:
        ...

    def setup_sphinx(self, registry: ServiceRegistry, sphinx_app: Sphinx):
        ...


class ThemeConfig(Protocol):
    """ The setup for the active theme in Themester """
    sphinx: ThemeSphinxConfig


class Resource(Protocol):
    name: str
    parent: Optional[Resource]


class Root(Resource, Protocol):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None


class View(Protocol):
    def __call__(self) -> VDOM:
        ...
