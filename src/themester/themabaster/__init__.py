"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
import os
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset
from venusian import Scanner

from . import components, views
from .components import cssfiles


def copy_asset_files(app, exc):
    static_dir = Path(__file__).parent.absolute() / 'static'
    asset_files = ('themabaster.css', 'basic.css')
    if exc is None:  # build succeeded
        for fn in asset_files:
            full_fn = str(static_dir / fn)
            copy_asset(full_fn, os.path.join(app.outdir, '_static'))


def wired_setup(scanner: Scanner):
    scanner.scan(components)
    scanner.scan(cssfiles)
    scanner.scan(views)


def setup(app: Sphinx):
    """ Sphinx theming support """

    app.connect('build-finished', copy_asset_files)
