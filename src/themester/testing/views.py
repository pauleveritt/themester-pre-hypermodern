from dataclasses import dataclass
from typing import List

from venusian import Scanner
from viewdom import html
from viewdom.h import H

from themester import testing
from themester.views import view, View


@view()
@dataclass
class FixtureView(View):
    name: str = 'Fixture View'

    def __call__(self) -> H:
        return html('<div>View: {self.name}</div>')


def wired_setup(scanner: Scanner):
    scanner.scan(testing.views)
