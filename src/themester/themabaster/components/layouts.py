"""

The various layout components for this theme.

"""

from dataclasses import dataclass
from typing import Iterable

from viewdom import html
from viewdom.h import H
from viewdom_wired import component
from wired.dataclasses import injected

from ..protocols import Layout, LayoutConfig


@component(for_=Layout)
@dataclass
class SiteLayout:
    children: Iterable[H]
    site_name: str = injected(LayoutConfig, attr='site_name')

    def __call__(self):
        c = self.children
        return html('''\
<section>
    <h1>{self.site_name}</h1>
    <div>{self.children}</div>
</section>
        ''')
