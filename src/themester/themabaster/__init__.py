"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from venusian import Scanner

from . import views
from .components import (
    cssfiles,
    jsfiles,
    head,
    html,
    # site_layout,
    title,
)


def wired_setup(scanner: Scanner):
    for module in (
            cssfiles,
            jsfiles,
            head,
            html,
            # site_layout,
            title,
            views,
    ):
        scanner.scan(module)
