"""
Minimum possible view.

"""

from dataclasses import dataclass

from viewdom import html

from themester.views import view

EXPECTED = '<div>Hello Hello View</div>'


# start-after

@view()
@dataclass
class HelloView:
    name: str = 'Hello View'

    def __call__(self) -> str:
        return html('<div>Hello {self.name}</div>')

# result = '<div>Hello Hello View/div>'
