from dataclasses import dataclass

from venusian import Scanner
from viewdom import html, VDOM
from wired import ServiceRegistry

from themester.testing import views
from themester.views import view, View


@view()
@dataclass
class FixtureView(View):
    name: str = 'Fixture View'

    def __call__(self) -> VDOM:
        return html('<div>View: {self.name}</div>')


def wired_setup(
        registry: ServiceRegistry,
        scanner: Scanner,
):
    scanner.scan(views)
