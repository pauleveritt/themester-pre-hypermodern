from dataclasses import dataclass

from viewdom import html
from viewdom.h import H

from themester.views import view
from .components.layouts import SiteLayout  # noqa


@view()
@dataclass
class RootView:
    name: str = 'Layout'

    def __call__(self) -> H:
        return html('<{SiteLayout}><div>One Child</div><//>')
