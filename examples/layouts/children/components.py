from dataclasses import dataclass
from typing import Iterable

from viewdom import html, VDOM
from viewdom_wired import component

from .protocols import Layout


@component()
@dataclass
class MyLayout(Layout):
    children: Iterable[VDOM]
    site_name: str = 'My Site'

    def __call__(self):
        c = self.children
        return html('''\
<section>
    <h1>{self.site_name}</h1>
    <div>{self.children}</div>
</section>
        ''')
