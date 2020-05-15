from dataclasses import dataclass

from viewdom import html
from wired import ServiceRegistry
from wired.dataclasses import injected, Context

from themester.views import register_view


@dataclass
class DummyView:
    resource_name: str = injected(Context, attr='name')

    def __call__(self):
        return html('<div>Hello {self.resource_name}</div>')


def wired_setup(registry: ServiceRegistry):
    register_view(registry, DummyView)
