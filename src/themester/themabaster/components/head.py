"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass
from typing import Iterable, Optional, Callable, Tuple

from viewdom import html, VDOM
from viewdom_wired import component, adherent
from wired.dataclasses import injected

from themester.themabaster.protocols import CSSFiles, Head, JSFiles, Title  # noqa
from themester.themabaster.services.layoutconfig import ThemabasterConfig
from themester.themabaster.services.pagecontext import PageContext
from themester.url import URL


@component(for_=Head)
@adherent(Head)
@dataclass(frozen=True)
class DefaultHead(Head):
    favicon: Optional[str] = injected(ThemabasterConfig, attr='favicon')
    page_title: str = injected(PageContext, attr='title')
    site_name: Optional[str] = injected(ThemabasterConfig, attr='site_name')
    site_css_files: Iterable[str] = injected(ThemabasterConfig, attr='css_files')
    page_css_files: Iterable[str] = injected(PageContext, attr='css_files')
    site_js_files: Iterable[str] = injected(ThemabasterConfig, attr='js_files')
    touch_icon: Optional[str] = injected(ThemabasterConfig, attr='touch_icon')
    page_js_files: Iterable[str] = injected(PageContext, attr='css_files')
    static_url: Callable = injected(URL, attr='static_url')
    children: Optional[Tuple[VDOM, ...]] = None
    charset: str = 'utf-8'

    def __call__(self) -> VDOM:
        custom_css = self.static_url('_static/custom.css')
        touch_icon_href = self.static_url(self.touch_icon)
        touch_icon = html(
            '<link rel="stylesheet" href="{touch_icon_href}" type="text/css"/>') if self.touch_icon else ''
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <{Title} page_title={self.page_title} site_name={self.site_name} />
  <{CSSFiles} page_files={self.page_css_files} site_files={self.site_css_files} />
  <{JSFiles} page_files={self.page_js_files} site_files={self.site_js_files} />
  <link rel="stylesheet" href="{custom_css}" type="text/css"/>
  {touch_icon}
  {self.children}
</head>
''')
