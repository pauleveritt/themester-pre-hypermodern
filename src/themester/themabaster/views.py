from dataclasses import dataclass

from viewdom import html, VDOM

from themester.protocols import Root, Resource
from themester.views import view


@view(context=Root)
@dataclass
class RootView:

    def __call__(self) -> VDOM:
        # Dang, circular imports
        from .components.base_layout import BaseLayout  # noqa: F401
        return html('<{BaseLayout}><//>')


@view(context=None)
@view(context=Resource)
@dataclass
class PageView:

    def __call__(self) -> VDOM:
        # Dang, circular imports
        from .components.base_layout import BaseLayout  # noqa: F401
        return html('<{BaseLayout}><//>')
