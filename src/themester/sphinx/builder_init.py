"""
During Sphinx builder_init, create the Themester app and return it.

The ThemesterApp is a way to "canonicalize" Themester across different
systems. It expects some bootstrap information from the outside world,
then from there, is on its own.

This module provides some glue to "adapt" Sphinx to ThemesterApp.
"""
from sphinx.application import Sphinx
from sphinx.config import Config
from wired import ServiceRegistry

from themester import sphinx as themester_sphinx, make_registry
from themester.protocols import ThemeConfig
from themester.resources import Site
from themester.sphinx.config import SphinxConfig, HTMLConfig


def setup_registry(sphinx_config: Config) -> ServiceRegistry:
    """ Make a registry that is Themester-aware """

    theme_config: ThemeConfig = getattr(sphinx_config, 'theme_config')
    themester_root: Site = getattr(sphinx_config, 'themester_root')
    registry = make_registry(
        root=themester_root,
        scannables=themester_sphinx,
        theme_config=theme_config,
    )
    sc = getattr(sphinx_config, 'sphinx_config')
    hc = getattr(sphinx_config, 'html_config')
    registry.register_singleton(sc, SphinxConfig)
    registry.register_singleton(hc, HTMLConfig)
    return registry


def setup(app: Sphinx):
    """ Handle the Sphinx ``builder_init`` event """

    registry = setup_registry(app.config)
    setattr(app, 'themester_registry', registry)
