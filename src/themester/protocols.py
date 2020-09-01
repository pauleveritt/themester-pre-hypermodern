"""

Implementation-independent PEP 544 protocols for everything in the
registry.

"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Protocol, Tuple

from sphinx.application import Sphinx
from viewdom import VDOM
from wired import ServiceRegistry


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


class Resource:
    name: str
    parent: Optional[Resource]


class Root(Resource):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None


@dataclass
class Document(Resource):
    name: str
    parent: Optional[Resource]


class View:
    def __call__(self) -> VDOM:
        ...
