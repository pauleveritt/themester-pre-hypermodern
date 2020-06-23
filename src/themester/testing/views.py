from dataclasses import dataclass
from typing import List

from venusian import Scanner
from viewdom import html, VDOM

from themester import testing
from themester.views import view, View


@view()
@dataclass
class FixtureView(View):
    name: str = 'Fixture View'

    def __call__(self) -> VDOM:
        return html('<div>View: {self.name}</div>')


def wired_setup(scanner: Scanner):
    scanner.scan(testing.views)
