from dataclasses import dataclass
from typing import Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext, HTMLConfig


@component()
@dataclass(frozen=True)
class Favicon:
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    href: str = injected(HTMLConfig, attr='favicon')

    def __call__(self) -> VDOM:
        href = self.pathto(self.href, 1)
        return html('<link rel="shortcut icon" href={href} />')
