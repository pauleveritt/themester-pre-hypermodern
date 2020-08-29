"""
During Sphinx builder_init, create the Themester app and return it.

The ThemesterApp is a way to "canonicalize" Themester across different
systems. It expects some bootstrap information from the outside world,
then from there, is on its own.

This module provides some glue to "adapt" Sphinx to ThemesterApp.
"""
from sphinx.config import Config

from themester.app import ThemesterApp
from themester.sphinx.config import SphinxConfig, HTMLConfig


def setup_app(
        sphinx_config: Config
) -> ThemesterApp:
    # site = Site()  # TODO Move this to ThemesterConfig
    themester_config = getattr(sphinx_config, 'themester_config')

    themester_app = ThemesterApp(
        themester_config=themester_config,
    )
    sc = getattr(sphinx_config, 'sphinx_config')
    hc = getattr(sphinx_config, 'html_config')
    tc = getattr(sphinx_config, 'theme_config')
    themester_app.registry.register_singleton(sc, SphinxConfig)
    themester_app.registry.register_singleton(hc, HTMLConfig)
    themester_app.registry.register_singleton(tc, tc.__class__)
    themester_app.setup_plugins()

    return themester_app
