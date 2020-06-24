from dataclasses import dataclass
from typing import Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component, adherent

from themester.themabaster.protocols import Favicon


@component(for_=Favicon)
@adherent(Favicon)
@dataclass(frozen=True)
class DefaultFavicon(Favicon):
    filename: str

    def __call__(self) -> VDOM:
        return html('<div/>')   # '<link rel="shortcut icon" href="{{ pathto('_static/' + favicon, 1) }}"/>')
