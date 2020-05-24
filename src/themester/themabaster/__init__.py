"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from venusian import Scanner

from .components.layouts import SiteLayout
from .views import HelloLayout


def wired_setup(scanner: Scanner):
    scanner.scan(HelloLayout)
    for module in (
            SiteLayout,
            HelloLayout
    ):
        scanner.scan(module)

    return
