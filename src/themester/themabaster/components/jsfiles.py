from dataclasses import dataclass, field
from typing import Tuple, Callable, List

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.models import PageContext


def JSFile(src: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<script type="text/javascript" src="{src}"></script>')


@component()
@dataclass
class JSFiles:
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    site_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()
    resolved_all_files: List[str] = field(init=False)

    def __post_init__(self):
        all_files = self.site_files + self.page_files
        self.resolved_all_files = [
            self.pathto(js_file, 1)
            for js_file in all_files
        ]

    def __call__(self) -> VDOM:
        return html('''\n
    {[JSFile(src) for src in self.resolved_all_files]}
            ''')
