from dataclasses import dataclass
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext


def JSFile(src: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<script type="text/javascript" src="{src}"></script>')


@component()
@dataclass(frozen=True)
class JSFiles:
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    site_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        srcs = [
            self.pathto(js_file, 1)
            for js_file in all_files
        ]
        return html('''\n
    {[JSFile(src) for src in srcs]}
            ''')
