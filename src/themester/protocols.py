"""

Implementation-independent PEP 544 protocols for everything in the
registry.

"""
from __future__ import annotations

from typing import Protocol, Optional

from viewdom.h import H
from wired import ServiceContainer, ServiceRegistry


class App(Protocol):
    container: ServiceContainer
    registry: ServiceRegistry


class Config(Protocol):
    site_name: Optional[str] = None


class Resource(Protocol):
    name: str
    parent: Optional[Resource]


class Root(Resource, dict):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None


class View(Protocol):
    def __call__(self) -> H:
        ...
