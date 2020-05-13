from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import injected, Context

from themester.views import view


@view()
@dataclass
class DummyView:
    resource_name: str = injected(Context, attr='name')

    def __call__(self):
        return html('<div>Hello {self.resource_name}</div>')
