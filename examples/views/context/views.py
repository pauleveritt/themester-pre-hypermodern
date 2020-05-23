"""
A view specific to a container's context.
"""

from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import injected, Context

from themester.views import view

EXPECTED = '<div>Hello Customer</div>'


class Customer:
    name = 'Customer'


# start-after

@view(context=Customer)
@dataclass
class ContextView:
    name: str = injected(Context, attr='name')

    def __call__(self) -> str:
        return html('<div>Hello Customer</div>')

# result = '<div>Hello Context View</div>'
