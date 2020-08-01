"""
Default implementation of the Themabaster <Head> component.
"""

import os
from dataclasses import dataclass, field
from typing import Optional, Callable, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from .cssfiles import CSSFiles  # noqa: F401
from .jsfiles import JSFiles  # noqa: F401
from .linktags import Linktags  # noqa: F401
from .title import Title  # noqa: F401
from ..config import ThemabasterConfig
from ...sphinx.config import HTMLConfig, SphinxConfig
from ...sphinx.models import PageContext


@component()
@dataclass
class Head:
    baseurl: Optional[str] = injected(HTMLConfig, attr='baseurl')
    favicon: Optional[str] = injected(HTMLConfig, attr='favicon')
    file_suffix: str = injected(HTMLConfig, attr='file_suffix')
    page_title: str = injected(PageContext, attr='title')
    project: Optional[str] = injected(SphinxConfig, attr='project')
    site_css_files: Tuple[str, ...] = injected(HTMLConfig, attr='css_files')
    theme_css_files: Tuple[str, ...] = injected(ThemabasterConfig, attr='css_files')
    page_css_files: Tuple[str, ...] = injected(PageContext, attr='css_files')
    site_js_files: Tuple[str, ...] = injected(HTMLConfig, attr='js_files')
    touch_icon: Optional[str] = injected(ThemabasterConfig, attr='touch_icon')
    page_js_files: Tuple[str, ...] = injected(PageContext, attr='css_files')
    pagename: str = injected(PageContext, attr='pagename')
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    extrahead: Optional[Tuple[VDOM, ...]] = None
    charset: str = 'utf-8'
    resolved_custom_css: str = field(init=False)
    resolved_touch_icon: Optional[VDOM] = field(init=False)
    resolved_docs_src: str = field(init=False)
    resolved_static_root: str = field(init=False)
    canonical_link: VDOM = field(init=False)

    def __post_init__(self):
        self.resolved_custom_css = self.pathto('_static/custom.css', 1)
        if self.touch_icon:
            touch_icon_href = self.pathto('_static/' + self.touch_icon, 1)
            self.resolved_touch_icon = html(
                '<link rel="apple-touch-icon" href="{touch_icon_href}" type="text/css"/>') if self.touch_icon else ''
        else:
            self.resolved_touch_icon = None
        self.resolved_docs_src = self.pathto('_static/documentation_options.js', 1)
        self.resolved_static_root = self.pathto('', 1)
        if self.baseurl:
            page_url = os.path.join(self.baseurl, self.pagename + self.file_suffix)
            self.canonical_link = html('<link rel="canonical" href={page_url}/>')
        else:
            self.canonical_link = html('')

    def __call__(self) -> VDOM:
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <{Title} page_title={self.page_title} project={self.project} />
  <{CSSFiles} site_files={self.site_css_files} theme_files={self.theme_css_files} page_files={self.page_css_files} />
  <script id="documentation_options" data-url_root="{self.resolved_static_root}" src="{self.resolved_docs_src}">//</script>
  <{JSFiles} page_files={self.page_js_files} site_files={self.site_js_files} />
  <link rel="stylesheet" href="{self.resolved_custom_css}" type="text/css"/>
  {self.canonical_link}
  {self.resolved_touch_icon}
  <{Linktags} />
  {self.extrahead}
</head>
''')
