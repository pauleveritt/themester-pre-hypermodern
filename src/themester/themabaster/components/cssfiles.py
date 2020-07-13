from dataclasses import dataclass
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.url import URL


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component()
@dataclass(frozen=True)
class CSSFiles:
    site_files: Tuple[str, ...]
    page_files: Tuple[str, ...]
    static_url: Callable = injected(URL, attr='static_url')

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        hrefs = [
            self.static_url(css_file)
            for css_file in all_files
        ]
        return html('''\n
{[CSSFile(href) for href in hrefs]}
        ''')
