from dataclasses import dataclass
from typing import Optional, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected, Context

from themester import Resource
from themester.themabaster.components.cssfiles.protocols import CSSFiles
from themester.url import relative_static_path


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component(for_=CSSFiles)
@dataclass
class DefaultCSSFiles:
    site_files: Tuple[str, ...]
    page_files: Optional[Tuple[str, ...]]
    resource: Resource = injected(Context)

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        hrefs = [
            relative_static_path(self.resource, css_file)
            for css_file in all_files
        ]
        return html('''\n
{[CSSFile(href) for href in hrefs]}
        ''')
