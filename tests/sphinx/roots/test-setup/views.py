from dataclasses import dataclass

from viewdom import html
from wired.dataclasses import injected, Context, factory

from themester import View
from themester.resources import Resource


@factory(for_=View, context=Resource)
@dataclass
class DummyView:
    resource_name: str = injected(Context, attr='name')

    def __call__(self):
        return html('<div>Hello {self.resource_name}</div>')
