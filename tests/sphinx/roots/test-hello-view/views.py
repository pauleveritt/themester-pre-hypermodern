from dataclasses import dataclass

from viewdom import html
from wired import ServiceRegistry
from wired.dataclasses import injected, Context

from themester.sphinx import PageContext
from themester.views import register_view


@dataclass
class DummyView:
    page_context: PageContext
    resource_name: str = injected(Context, attr='name')

    def __call__(self):
        body = self.page_context.body
        return html('''
        <body>
        <h1>{self.resource_name}</h1>
        <div>{body}</div>
        </body>
        ''')


def wired_setup(registry: ServiceRegistry):
    register_view(registry, DummyView)
