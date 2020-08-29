"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""
from pathlib import Path
from typing import Tuple

from sphinx.config import Config
from venusian import Scanner
from wired import ServiceRegistry, ServiceContainer

from . import components, sidebars, views
from .components import cssfiles
from .config import ThemabasterConfig


def get_static_resources() -> Tuple[Path, ...]:
    """ Return all the files that should get copied to the static output """

    static_dir = Path(__file__).parent.absolute() / 'static'
    static_resources = static_dir.glob('**/*')
    return tuple(static_resources)


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    from ..sphinx import SphinxConfig, HTMLConfig

    scanner.scan(components)
    scanner.scan(cssfiles)
    scanner.scan(sidebars)
    scanner.scan(views)

    # Get some configs off the Sphinx config and put them in the
    # registry
    container: ServiceContainer = registry.create_container()
    sphinx_config: Config = container.get(Config)
    sc = getattr(sphinx_config, 'sphinx_config', SphinxConfig())
    hc = getattr(sphinx_config, 'html_config', HTMLConfig())
    tc = getattr(sphinx_config, 'theme_config', ThemabasterConfig())
    registry.register_singleton(sphinx_config, Config)
    registry.register_singleton(sc, SphinxConfig)
    registry.register_singleton(hc, HTMLConfig)
    registry.register_singleton(tc, ThemabasterConfig)
