from typing import Callable
from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component, adherent
from wired.dataclasses import injected

from themester.themabaster.protocols import Favicon
from themester.themabaster.services.layoutconfig import ThemabasterConfig
from themester.url import URL


@component(for_=Favicon)
@adherent(Favicon)
@dataclass(frozen=True)
class DefaultFavicon(Favicon):
    static_url: Callable = injected(URL, attr='static_url')
    href: str = injected(ThemabasterConfig, attr='favicon')

    def __call__(self) -> VDOM:
        href = self.static_url(self.href)
        return html('<link rel="shortcut icon" href={href} />')
