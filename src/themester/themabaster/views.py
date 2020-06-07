from dataclasses import dataclass

from viewdom import html, VDOM

from themester.views import view
from .protocols import Layout  # noqa


@view()
@dataclass
class RootView:

    def __call__(self) -> VDOM:
        return html('<{Layout}><div>One Child</div><//>')
