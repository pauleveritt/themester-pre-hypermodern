from dataclasses import dataclass

from viewdom import html, VDOM

from themester.views import view
from .layouts.base_layout import BaseLayout  # noqa: F401


@view()
@dataclass
class RootView:

    def __call__(self) -> VDOM:
        return html('<{BaseLayout}><div>One Child</div><//>')
