from dataclasses import dataclass

from venusian import Scanner
from viewdom import html
from viewdom_wired import component, register_component
from wired import ServiceRegistry


@component()
@dataclass
class Heading1:
    def __call__(self):
        return html('hello')


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    # Register manually instead
    register_component(registry, Heading1, Heading1)
