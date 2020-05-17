"""

Default views for a page and special pages like genindex.

"""

from dataclasses import dataclass

from viewdom import html
from wired import ServiceRegistry
from wired.dataclasses import injected

from themester.sphinx.models import PageContext
from themester.views import register_view


@dataclass
class DefaultView:
    body: str = injected(PageContext, attr='body')

    def __call__(self):
        return html('<div>{self.body}</div>')


def wired_setup(registry: ServiceRegistry):
    register_view(registry, DefaultView, context=None)
