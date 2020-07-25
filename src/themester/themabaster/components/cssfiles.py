from dataclasses import dataclass
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component()
@dataclass(frozen=True)
class CSSFiles:
    site_files: Tuple[str, ...]
    page_files: Tuple[str, ...]
    pathto: Callable[[str], int] = injected(PageContext, attr='pathto')

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        hrefs = [
            self.pathto(css_file, 1)
            for css_file in all_files
        ]
        return html('''\n
{[CSSFile(href) for href in hrefs]}
        ''')
