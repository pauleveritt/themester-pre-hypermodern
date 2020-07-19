"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from venusian import Scanner

from . import components, base_layout, services, views
from .components import cssfiles


def wired_setup(scanner: Scanner):
    scanner.scan(components)
    scanner.scan(cssfiles)
    scanner.scan(base_layout)
    scanner.scan(services)
    scanner.scan(views)
