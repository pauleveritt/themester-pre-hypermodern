from dataclasses import dataclass
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.models import PageContext


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component()
@dataclass(frozen=True)
class CSSFiles:
    pathto: Callable[[str, int], int] = injected(PageContext, attr='pathto')
    site_files: Tuple[str, ...] = tuple()
    theme_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.theme_files + self.page_files
        hrefs = [
            self.pathto(css_file, 1)
            for css_file in all_files
        ]
        return html('''\n
{[CSSFile(href) for href in hrefs]}
        ''')
