"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected, Context

from themester import Resource
from themester.themabaster.components.cssfiles.protocols import CSSFiles
from themester.themabaster.components.head.protocols import Head
from themester.themabaster.components.jsfiles.protocols import JSFiles
from themester.themabaster.components.title import Title


@component(for_=Head)
@dataclass(frozen=True)
class DefaultHead:
    css_files: CSSFiles
    js_files: JSFiles
    title: Title
    resource: Resource = injected(Context)
    charset: str = 'utf-8'
    # TODO Have a Meta component and make this an iterable of those
    # metatags: Iterable[Component] = tuple()

    def __call__(self) -> VDOM:
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  {self.title}
  {self.css_files}
  {self.js_files}
</head>
''')
