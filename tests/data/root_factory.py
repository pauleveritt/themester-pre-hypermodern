"""
Sample implementation of a root factory.
"""
from dataclasses import dataclass

from venusian import Scanner
from wired import ServiceContainer, ServiceRegistry
from wired.dataclasses import factory

from themester.protocols import Root


@factory(for_=Root)
@dataclass
class SampleRoot:
    title: str = 'Sample Root'


def root_factory(container: ServiceContainer):
    return SampleRoot()


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    # Register manually instead
    scanner.scan(__file__)
