"""

Example resource types for use in fixtures and tests

"""
from dataclasses import dataclass

from themester.resources import Resource, Root


@dataclass(frozen=True)
class Site(Root, dict):
    """ The root of the resource tree """

    name: str = ''
    parent: None = None

    def __post_init__(self):
        super(dict).__init__()


@dataclass(frozen=True)
class Collection(Resource, dict):
    """ A folder in the resource tree """

    parent: Resource
    name: str

    def __post_init__(self):
        super(dict).__init__()


@dataclass(frozen=True)
class Document(Resource):
    """ A leaf in the resource tree """

    parent: Resource
    name: str
