from dataclasses import dataclass

from viewdom import html, VDOM
from wired import ServiceContainer

from themester.sphinx.models import PageContext
from themester.views import view


@view()
@dataclass
class RootView:

    container: ServiceContainer

    def __call__(self) -> VDOM:
        pc: PageContext = self.container.get(PageContext)
        body = pc.body
        pagename = pc.pagename
        # Dang, circular imports
        from .components.base_layout import BaseLayout  # noqa: F401
        return html('<{BaseLayout}><div>One Child</div><//>')
