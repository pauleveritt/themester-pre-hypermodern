from dataclasses import dataclass
from typing import Tuple, Callable

from viewdom import html, VDOM
from viewdom_wired import component, adherent
from wired.dataclasses import injected

from themester.themabaster.protocols import JSFiles
from themester.url import URL


def JSFile(src: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<script type="text/javascript" src="{src}"></script>')


@component(for_=JSFiles)
@adherent(JSFiles)
@dataclass(frozen=True)
class DefaultJSFiles(JSFiles):
    static_url: Callable = injected(URL, attr='static_url')
    site_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        srcs = [
            self.static_url(js_file)
            for js_file in all_files
        ]
        return html('''\n
    {[JSFile(src) for src in srcs]}
            ''')
