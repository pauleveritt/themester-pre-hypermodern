from __future__ import annotations

from typing import Protocol, Optional


class Resource(Protocol):
    name: str
    parent: Optional[Resource]


class Root(Resource, dict):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None
