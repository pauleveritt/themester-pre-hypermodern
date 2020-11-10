from dataclasses import dataclass
from importlib import import_module

from venusian import Scanner
from viewdom import html
from viewdom_wired import component
from wired import ServiceRegistry


@component()
@dataclass
class Heading2:
    def __call__(self):
        return html('hello')


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    # Scan manually instead
    scanner.scan(import_module(Heading2.__module__))
