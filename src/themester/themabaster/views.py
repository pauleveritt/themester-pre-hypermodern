from dataclasses import dataclass

from viewdom import html
from viewdom.h import H

from themester.views import view
from .protocols import Layout  # noqa


@view()
@dataclass
class RootView:

    def __call__(self) -> H:
        return html('<{Layout}><div>One Child</div><//>')
