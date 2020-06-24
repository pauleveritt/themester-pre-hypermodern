from dataclasses import dataclass
from typing import Tuple

from viewdom import html, VDOM
from viewdom_wired import component, adherent

from themester.themabaster.protocols import CSSFiles
from themester.url import URL


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component(for_=CSSFiles)
@adherent(CSSFiles)
@dataclass(frozen=True)
class DefaultCSSFiles(CSSFiles):
    url: URL
    site_files: Tuple[str, ...]
    page_files: Tuple[str, ...]

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        hrefs = [
            self.url.static_url(css_file)
            for css_file in all_files
        ]
        return html('''\n
{[CSSFile(href) for href in hrefs]}
        ''')
