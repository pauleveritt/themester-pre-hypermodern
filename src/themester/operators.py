"""
Pipeline operators for Annotated injection.

Themester has some special operators it is going to want to do.
"""
from dataclasses import dataclass
from typing import Union, Tuple, Callable

from wired import ServiceContainer
from wired_injector.operators import Operator

from themester.sphinx.models import PageContext

Paths = Union[str, Tuple[str]]


@dataclass(frozen=True)
class PathTo(Operator):
    """ Calculate a relative path to a path or list of paths """

    def __call__(self, previous: Paths, container: ServiceContainer) -> Paths:
        # Get the pathto service from the PageContext
        page_context = container.get(PageContext)
        pathto: Callable[[str, int], str] = getattr(page_context, 'pathto')

        # Handle a single item differently than a list
        if type(previous) in [list, tuple]:
            return tuple([
                pathto(this_previous, 0)
                for this_previous in previous
            ])
        else:
            return pathto(previous, 0)


@dataclass(frozen=True)
class StaticPathTo(Operator):
    """ Calculate a path to a static asset or list of assets """

    def __call__(self, previous: Paths, container: ServiceContainer) -> Paths:
        # Get the pathto service from the PageContext
        page_context = container.get(PageContext)
        pathto: Callable[[str, int], str] = getattr(page_context, 'pathto')

        # Handle a single item differently than a list
        if type(previous) in [list, tuple]:
            return tuple([
                pathto(this_previous, 1)
                for this_previous in previous
            ])
        else:
            return pathto(previous, 1)
