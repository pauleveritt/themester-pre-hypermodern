from dataclasses import dataclass

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
    scanner.scan(__file__)
