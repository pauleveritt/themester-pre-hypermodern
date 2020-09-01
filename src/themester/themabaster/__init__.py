"""
An Alabaster-style theme, in themester.

A mapping of each knob, structure, and capability of Alabaster,
including the underlying Sphinx basic theme, into components and
themester.

This theme is resource-driven but only lightly.
"""

from venusian import Scanner
from wired import ServiceRegistry

from . import components, sidebars, views
from .components import cssfiles
from .config import ThemabasterConfig
from ..config import ThemesterConfig
from ..sphinx import HTMLConfig, SphinxConfig


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    scanner.scan(components)
    scanner.scan(cssfiles)
    scanner.scan(sidebars)
    scanner.scan(views)

    # Get ThemabasterConfig from the container then register it directly
    container = registry.create_container()
    themester_config: ThemesterConfig = container.get(ThemesterConfig)
    tc: ThemabasterConfig = getattr(themester_config, 'theme_config')
    registry.register_singleton(tc, ThemabasterConfig)

    # Add some of the sub-config as top-level services
    html_config = tc.html_config
    registry.register_singleton(html_config, HTMLConfig)
    sphinx_config = tc.sphinx_config
    registry.register_singleton(sphinx_config, SphinxConfig)
