from dataclasses import dataclass
from typing import Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.services.layoutconfig import ThemabasterConfig
from themester.url import URL


@component()
@dataclass(frozen=True)
class Favicon:
    static_url: Callable = injected(URL, attr='static_url')
    href: str = injected(ThemabasterConfig, attr='favicon')

    def __call__(self) -> VDOM:
        href = self.static_url(self.href)
        return html('<link rel="shortcut icon" href={href} />')
