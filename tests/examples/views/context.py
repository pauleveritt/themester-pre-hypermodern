from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import Context, injected

from themester.views import view


class Customer:
    name: str = 'Customer'


@view(context=Customer)
@dataclass
class DefaultView:
    name: str = injected(Context, attr='name')

    def __call__(self) -> str:
        return html('<div>Hello {self.name}</div>')
