from dataclasses import dataclass, field
from typing import Tuple, Callable, List

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import HTMLConfig
from themester.sphinx.models import PageContext
from themester.themabaster.config import ThemabasterConfig


def JSFile(src: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<script type="text/javascript" src="{src}"></script>')


@component()
@dataclass
class JSFiles:
    pathto: Callable[[str, int], int] = injected(PageContext, attr='pathto')
    site_files: Tuple[str, ...] = injected(HTMLConfig, attr='css_files')
    theme_files: Tuple[str, ...] = injected(ThemabasterConfig, attr='css_files')
    page_files: Tuple[str, ...] = injected(PageContext, attr='css_files')
    srcs: List = field(init=False)

    def __post_init__(self):
        all_files = self.site_files + self.theme_files + self.page_files
        self.srcs = [
            self.pathto(js_file, 1)
            for js_file in all_files
        ]

    def __call__(self) -> VDOM:
        return html('{[JSFile(src) for src in self.srcs]}')
