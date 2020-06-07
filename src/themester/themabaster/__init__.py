"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from venusian import Scanner

from .components import (
    head,
    html,
    site_layout,
    title,
)
from .components.cssfiles.protocols import CSSFiles
from .components.jsfiles.protocols import JSFiles
from .components.title.protocols import Title
from .protocols import LayoutConfig
from . import views


def wired_setup(scanner: Scanner):
    for module in (
            head,
            html,
            site_layout,
            views,
    ):
        scanner.scan(module)

__all__= [
    'CSSFiles',
    'JSFiles',
    'LayoutConfig',
    'Title',
]