from dataclasses import dataclass, field
from typing import Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from themester.operators import StaticPathTo, Paths
from themester.protocols import ThemeConfig
from themester.sphinx.config import HTMLConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


def CSSFile(href: str) -> VDOM:
    """ Small anonymous component used with the parent """
    return html('<link rel="stylesheet" href="{href}" type="text/css" />')


@component()
@dataclass
class CSSFiles:
    site_files: Annotated[
        Paths,
        Get(HTMLConfig, attr='css_files'),
        StaticPathTo(),
    ]
    theme_files: Annotated[
        Paths,
        Get(ThemeConfig, attr='css_files'),
        StaticPathTo(),
    ]
    page_files: Annotated[
        Paths,
        Get(PageContext, attr='css_files'),
        StaticPathTo(),
    ]
    hrefs: Tuple[str, ...] = field(init=False)

    def __post_init__(self):
        self.hrefs = self.site_files + self.theme_files + self.page_files

    def __call__(self) -> VDOM:
        return html('{[CSSFile(href) for href in self.hrefs]}')
