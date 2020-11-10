"""
Helpers to make a registry, render a view, etc.
"""
from collections import Sequence
from dataclasses import field
from importlib import import_module
from typing import Optional, Iterable, Union, Any, Callable, Dict

from venusian import Scanner
from viewdom import html, VDOM
from viewdom_wired import Component, render, register_component
from wired import ServiceRegistry

from themester.protocols import ThemeConfig, Root, Resource

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
        root_factory: Optional[Callable] = None,
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

    # Handle a root factory
    if root_factory is not None:
        registry.register_factory(root_factory, Root)

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
            _setup_target(registry, scanner, plugin)
    else:
        _setup_target(registry, scanner, plugins)

    return registry


def render_component(
        registry: ServiceRegistry,
        component: Component,
        context: Optional[Any] = None,
        resource: Optional[Resource] = None,
) -> str:
    """ Render a component to string with optional context/resource """

    register_component(registry, component, component)
    container = registry.create_container(context=context)
    if resource is not None:
        container.register_singleton(resource, Resource)
    vdom = html('<{component} />')
    result = render(vdom, container=container)
    return result
