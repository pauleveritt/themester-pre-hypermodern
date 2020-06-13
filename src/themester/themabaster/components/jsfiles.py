from dataclasses import dataclass
from typing import Optional, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected, Context

from themester import Resource
from themester.themabaster.protocols import JSFiles
from themester.url import relative_static_path


def JSFile(src: str) -> VDOM:
    """ Small anonymous component used with the parent """
    # language=HTML
    return html('<script type="text/javascript" src="{src}"></script>')


@component(for_=JSFiles)
@dataclass(frozen=True)
class DefaultJSFiles:
    resource: Resource = injected(Context)
    site_files: Tuple[str, ...] = tuple()
    page_files: Tuple[str, ...] = tuple()

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        srcs = [
            relative_static_path(self.resource, js_file)
            for js_file in all_files
        ]
        return html('''\n
{[JSFile(src) for src in srcs]}
        ''')
