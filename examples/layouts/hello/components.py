from dataclasses import dataclass
from typing import Optional, Iterable

from viewdom import html
from viewdom_wired import component

from .protocols import Layout


@component()
@dataclass
class MyLayout(Layout):
    children: Optional[Iterable]
    site_name: str = 'My Site'

    def __call__(self):
        return html('<div>Hello {self.site_name}</div>')
