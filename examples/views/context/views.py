"""
A view specific to a container's context.
"""

from dataclasses import dataclass

from viewdom import html
from themester.views import view
from wired_injector.operators import Context, Attr

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


EXPECTED = '<div>Hello Customer</div>'


class Customer:
    name = 'Customer'


# start-after

@view(context=Customer)
@dataclass
class ContextView:
    name: Annotated[str, Context(), Attr('name')]

    def __call__(self) -> str:
        return html('<div>Hello Customer</div>')

# result = '<div>Hello Context View</div>'
