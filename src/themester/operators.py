"""
Pipeline operators for Annotated injection.

Themester has some special operators it is going to want to do.
"""
from dataclasses import dataclass

from wired import ServiceContainer
from wired_injector.operators import Operator

from themester.sphinx.models import PageContext


@dataclass(frozen=True)
class PathTo(Operator):
    """ Calculate a relative path to a resource """

    def __call__(self, previous: str, container: ServiceContainer) -> str:
        # Get the pathto service from the PageContext
        page_context = container.get(PageContext)
        pathto = getattr(page_context, 'pathto')
        result: str = pathto(previous, 0)
        return result


@dataclass(frozen=True)
class StaticPathTo(Operator):
    """ Calculate a relative path to a static asset """

    def __call__(self, previous: str, container: ServiceContainer) -> str:
        # Get the pathto service from the PageContext
        page_context = container.get(PageContext)
        pathto = getattr(page_context, 'pathto')
        result: str = pathto(previous, 1)
        return result
