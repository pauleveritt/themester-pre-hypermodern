from dataclasses import dataclass
from typing import Tuple

from viewdom import html, VDOM
from viewdom_wired import component

from themester import Resource
from themester.themabaster.protocols import CSSFiles
from themester.url import relative_static_path


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component(for_=CSSFiles)
@dataclass(frozen=True)
class DefaultCSSFiles:
    resource: Resource
    site_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        hrefs = [
            relative_static_path(self.resource, css_file)
            for css_file in all_files
        ]
        return html('''\n
{[CSSFile(href) for href in hrefs]}
        ''')
