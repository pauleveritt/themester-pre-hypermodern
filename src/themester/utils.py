"""
Helpers to make a registry, render a view, etc.
"""
from collections import Sequence
from importlib import import_module
from typing import Optional, Iterable, Union, Any

from venusian import Scanner
from wired import ServiceRegistry

from themester.protocols import ThemeConfig, Root

Scannable = Any  # Wanted to use Union[str, ModuleType] but PyCharm
Plugin = Any  # Wanted to use Union[str, ModuleType] but PyCharm


def _scan_target(scanner: Scanner, target: Scannable):
    """ Helper to import a target if it is a string, then scan """

    if isinstance(target, str):
        target = import_module(target)
    scanner.scan(target)


def _setup_target(
        registry: ServiceRegistry,
        scanner: Scanner,
        target: Scannable,
):
    """ Helper to import a target if it is a string, then wired_setup """

    if isinstance(target, str):
        target = import_module(target)
    s = getattr(target, 'wired_setup')
    s(registry, scanner)


def make_registry(
        root: Optional[Root] = None,
        scannables: Union[Iterable[Scannable], Scannable] = tuple(),
        plugins: Union[Iterable[Plugin], Plugin] = tuple(),
        theme_config: Optional[ThemeConfig] = None,
) -> ServiceRegistry:
    """ Construct a Themester registry with some defaults """

    registry = ServiceRegistry()

    # Handle the venusian scanner
    scanner = Scanner(registry=registry)
    registry.register_singleton(scanner, Scanner)

    # Handle the root
    if root is not None:
        registry.register_singleton(root, Root)

    # Handle the theme config
    if theme_config is not None:
        registry.register_singleton(theme_config, ThemeConfig)

    # Handle anything that needs to be scanned
    if isinstance(scannables, Sequence):
        for scannable in scannables:
            _scan_target(scanner, scannable)
    else:
        _scan_target(scanner, scannables)

    # Handle any plugins
    if isinstance(plugins, Sequence):
        for plugin in plugins:
            _scan_target(scanner, plugin)
    else:
        _scan_target(scanner, plugins)

    return registry
