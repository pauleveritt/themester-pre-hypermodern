"""
A "named" view, meaning, not a default view.
"""

from dataclasses import dataclass

from viewdom import html

from themester.views import view

EXPECTED = '<div>Hello Named View</div>'


# start-after

@view(name='somename')
@dataclass
class NamedView:
    name: str = 'Named View'

    def __call__(self) -> str:
        return html('<div>Hello {self.name}</div>')

# result = '<div>Hello Named View</div>'
