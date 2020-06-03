from dataclasses import dataclass
from typing import Optional, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected, Context

from themester import Resource
from themester.themabaster.components.jsfiles.protocols import JSFiles
from themester.url import relative_static_path


def JSFile(src: str) -> VDOM:
    """ Small anonymous component used with the parent """
    return html('<script type="text/javascript" src="{src}"></script>')


@component(for_=JSFiles)
@dataclass
class DefaultJSFiles:
    site_files: Tuple[str, ...]
    page_files: Optional[Tuple[str, ...]]
    resource: Resource = injected(Context)

    def __call__(self) -> VDOM:
        all_files = self.site_files + self.page_files
        srcs = [
            relative_static_path(self.resource, js_file)
            for js_file in all_files
        ]
        # language=HTML
        x = '<div '
        return html('''\n
{[JSFile(src) for src in srcs]}
        ''')
