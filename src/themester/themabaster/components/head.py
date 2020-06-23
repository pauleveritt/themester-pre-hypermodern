"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass
from typing import Iterable, Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected, Context

from themester import Resource
from themester.themabaster.protocols import CSSFiles, Head, JSFiles, LayoutConfig, PageContext, Title  # noqa


@component(for_=Head)
@dataclass(frozen=True)
class DefaultHead:
    page_title: str = injected(PageContext, attr='page_title')
    site_name: Optional[str] = injected(LayoutConfig, attr='site_name')
    site_css_files: Iterable[str] = injected(LayoutConfig, attr='css_files')
    page_css_files: Iterable[str] = injected(PageContext, attr='css_files')
    site_js_files: Iterable[str] = injected(LayoutConfig, attr='js_files')
    page_js_files: Iterable[str] = injected(PageContext, attr='css_files')
    resource: Resource = injected(Context)
    charset: str = 'utf-8'

    # TODO Have a Meta component and make this an iterable of those
    # metatags: Iterable[Component] = tuple()

    def __call__(self) -> VDOM:
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <{Title} page_title={self.page_title} site_name={self.site_name} />
  <{CSSFiles} resource={self.resource} page_files={self.page_css_files} site_files={self.site_css_files} />
  <{JSFiles} resource={self.resource} page_files={self.page_js_files} site_files={self.site_js_files} />
</head>
''')
