from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Resource:
    """ Minimum to participate in themester resources """

    name: str
    parent: Optional[Resource]

    @property
    def __name__(self) -> str:
        return self.name

    @property
    def __parent__(self) -> Optional[Resource]:
        return self.parent


@dataclass
class Collection(Resource, dict):
    """ A container resource """

    name: str
    parent: Resource

    def __post_init__(self):
        super(dict).__init__()

    @property
    def __parent__(self) -> Resource:
        return self.parent


@dataclass
class Root(Resource, dict):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None

    def __post_init__(self):
        super(dict).__init__()

    @property
    def __parent__(self) -> Resource:
        return self.parent


__all__ = [
    'Resource',
    'Collection',
    'Root',
]
