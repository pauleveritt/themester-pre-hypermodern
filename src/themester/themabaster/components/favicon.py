from dataclasses import dataclass, field
from typing import Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import HTMLConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class Favicon:
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    href: str = injected(HTMLConfig, attr='favicon')
    resolved_href: str = field(init=False)

    def __post_init__(self):
        self.resolved_href = self.pathto(self.href, 1)

    def __call__(self) -> VDOM:
        return html('<link rel="shortcut icon" href={self.resolved_href} />')
