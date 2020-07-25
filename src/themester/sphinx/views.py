"""

Default views for a page and special pages like genindex.

"""

from dataclasses import dataclass

from venusian import Scanner
from viewdom import html
from wired.dataclasses import injected

from themester import sphinx
from themester.sphinx.models import PageContext
from themester.themabaster.components.base_layout import BaseLayout  # noqa: F401
from themester.views import view


@view()
@dataclass
class DefaultView:
    body: str = injected(PageContext, attr='body')

    def __call__(self):
        return html('<div id="themester-body">{self.body}</div>')


def wired_setup(scanner: Scanner):
    scanner.scan(sphinx.views)
