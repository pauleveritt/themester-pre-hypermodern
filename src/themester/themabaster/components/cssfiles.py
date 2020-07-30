from dataclasses import dataclass, field
from typing import Tuple, Callable, List

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.models import PageContext


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component()
@dataclass
class CSSFiles:
    pathto: Callable[[str, int], int] = injected(PageContext, attr='pathto')
    site_files: Tuple[str, ...] = tuple()
    theme_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()
    hrefs: List = field(init=False)

    def __post_init__(self):
        all_files = self.site_files + self.theme_files + self.page_files
        self.hrefs = [
            self.pathto(css_file, 1)
            for css_file in all_files
        ]

    def __call__(self) -> VDOM:
        return html('''\n
{[CSSFile(href) for href in self.hrefs]}
        ''')
