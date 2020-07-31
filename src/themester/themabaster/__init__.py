"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from pathlib import Path
from typing import Tuple

from venusian import Scanner

from . import components, views
from .components import cssfiles


def get_static_resources() -> Tuple[Path, ...]:
    """ Return all the files that should get copied to the static output """

    static_dir = Path(__file__).parent.absolute() / 'static'
    static_resources = static_dir.glob('**/*')
    return tuple(static_resources)


def wired_setup(scanner: Scanner):
    scanner.scan(components)
    scanner.scan(cssfiles)
    scanner.scan(views)
