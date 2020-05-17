from dataclasses import dataclass

from venusian import Scanner
from viewdom import html

from themester import testing
from themester.views import view


@view()
@dataclass
class FixtureView:
    name: str = 'Fixture View'

    def __call__(self) -> str:
        return html('<div>View: {self.name}</div>')


def wired_setup(scanner: Scanner):
    scanner.scan(testing.views)
