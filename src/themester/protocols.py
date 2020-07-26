"""

Implementation-independent PEP 544 protocols for everything in the
registry.

"""
from __future__ import annotations

from types import ModuleType
from typing import Optional

from viewdom import VDOM
from wired import ServiceContainer, ServiceRegistry


class App:
    container: ServiceContainer
    registry: ServiceRegistry

    def setup_plugins(self, module: ModuleType) -> None:
        ...

    def render(self, container: Optional[ServiceContainer]) -> str:
        ...


class Resource:
    name: str
    parent: Optional[Resource]


class Root:
    """ The root of the resource tree """

    name: str = ''
    parent: None = None


class View:
    def __call__(self) -> VDOM:
        ...
