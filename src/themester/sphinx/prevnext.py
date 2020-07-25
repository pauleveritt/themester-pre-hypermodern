"""
Get the previous and next link information from the container.

Sphinx maintains the linking information. We aren't planning
yet to mirror that into the resource tree. Thus, part of
the Themabaster "adapters" will be to inject ``PreviousLink`` and
``NextLink`` singletons into the request container, by getting
the info from Sphinx.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class PreviousLink:
    """ The minimum information needed from previous/next resources."""

    title: str
    link: str


@dataclass(frozen=True)
class NextLink:
    """ The minimum information needed from previous/next resources."""

    title: str
    link: str
