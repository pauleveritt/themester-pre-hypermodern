from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.operators import StaticPathTo
from themester.sphinx.config import HTMLConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Favicon:
    href: Annotated[
        str,
        Get(HTMLConfig),
        Attr('favicon'),
        StaticPathTo(),
    ]

    def __call__(self) -> VDOM:
        return html('<link rel="shortcut icon" href={self.href} />')
