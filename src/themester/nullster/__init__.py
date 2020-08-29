"""
Null theme used for testing.

We need to make sure we don't couple themester to sphinx to
themabaster too tightly. Make a tiny, echo-style theme that can
be used in tests etc.
"""

from venusian import Scanner
from wired import ServiceRegistry

from . import views


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    scanner.scan(views)
