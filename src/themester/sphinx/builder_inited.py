"""
During Sphinx builder_init, create the Themester app and return it.

The ThemesterApp is a way to "canonicalize" Themester across different
systems. It expects some bootstrap information from the outside world,
then from there, is on its own.

This module provides some glue to "adapt" Sphinx to ThemesterApp.
"""
from sphinx.config import Config

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.protocols import Root
from themester.testing.resources import Site


def setup_app(sphinx_config: Config) -> ThemesterApp:
    themester_config: ThemesterConfig = getattr(sphinx_config, 'themester_config')

    # TODO Find a way to get the root
    root = Site(title='Sphinx Site')
    themester_app = ThemesterApp(
        themester_config=themester_config,
    )
    themester_app.setup_plugins()
    themester_app.registry.register_singleton(root, Root)

    return themester_app
