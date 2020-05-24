"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from venusian import Scanner

from .components import layouts
from . import views


def wired_setup(scanner: Scanner):
    for module in (
            layouts,
            views,
    ):
        scanner.scan(module)
