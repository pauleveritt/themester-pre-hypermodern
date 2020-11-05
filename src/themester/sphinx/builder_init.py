"""
During Sphinx builder_init, create the Themester app and return it.

The ThemesterApp is a way to "canonicalize" Themester across different
systems. It expects some bootstrap information from the outside world,
then from there, is on its own.

This module provides some glue to "adapt" Sphinx to ThemesterApp.
"""
from sphinx.application import Sphinx
from sphinx.config import Config

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.sphinx.config import SphinxConfig, HTMLConfig


def setup_app(sphinx_config: Config) -> ThemesterApp:
    themester_config: ThemesterConfig = getattr(sphinx_config, 'themester_config')

    themester_app = ThemesterApp(
        themester_config=themester_config,
    )
    themester_app.setup_plugins()

    # Put the Sphinx-specific config stuff into the registry
    sc: ThemesterConfig = getattr(sphinx_config, 'sphinx_config')
    hc: ThemesterConfig = getattr(sphinx_config, 'html_config')
    themester_app.registry.register_singleton(sc, SphinxConfig)
    themester_app.registry.register_singleton(hc, HTMLConfig)

    return themester_app


def setup(app: Sphinx):
    """ Handle the Sphinx ``builder_init`` event """

    themester_app = setup_app(app.config)
    setattr(app, 'themester_app', themester_app)
