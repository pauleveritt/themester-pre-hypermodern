"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass
from typing import Iterable

from viewdom import H, html
from viewdom_wired import component, Component
from wired.dataclasses import injected, Context

from ..protocols import Head, Title, LayoutConfig, CSSFile
from ... import Resource
from ...url import relative_static_path


@component(for_=Head)
@dataclass(frozen=True)
class DefaultHead(Head):
    resource: Resource = injected(Context)
    css_files: Iterable[CSSFile] = injected(LayoutConfig, attr='css_files')
    charset: str = 'utf-8'
    title: Title = None
    # TODO Have a Meta component and make this an iterable of those
    metatags: Iterable[Component] = tuple()

    def __call__(self) -> H:
        relative_files = [
            relative_static_path(self.resource, css_file)
            for css_file in self.css_files
        ]
        css_files = [
            html('<link rel="stylesheet" href="{css_file}"/>')
            for css_file in relative_files
        ]
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  {[meta for meta in self.metatags]}
  {self.title}
  {css_files}
</head>
''')
