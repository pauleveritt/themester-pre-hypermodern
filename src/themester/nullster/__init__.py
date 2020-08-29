"""
Null theme used for testing.

We need to make sure we don't couple themester to sphinx to
themabaster too tightly. Make a tiny, echo-style theme that can
be used in tests etc.
"""
from dataclasses import dataclass, field

from venusian import Scanner
from wired import ServiceRegistry

from . import views


@dataclass(frozen=True)
class NullsterSphinxConfig:
    pass


@dataclass(frozen=True)
class NullsterConfig:
    sphinx: NullsterSphinxConfig = field(default_factory=NullsterSphinxConfig)


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    scanner.scan(views)
