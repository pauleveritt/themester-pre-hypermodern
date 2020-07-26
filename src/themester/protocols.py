"""

Implementation-independent PEP 544 protocols for everything in the
registry.

"""
from __future__ import annotations

from typing import Optional

from viewdom import VDOM


class Resource:
    name: str
    parent: Optional[Resource]


class Root(Resource):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None


class View:
    def __call__(self) -> VDOM:
        ...
