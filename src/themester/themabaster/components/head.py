"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass
from typing import Iterable, Optional, Callable, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from .cssfiles import CSSFiles  # noqa: F401
from .jsfiles import JSFiles  # noqa: F401
from .linktags import Linktags  # noqa: F401
from .title import Title  # noqa: F401
from ..config import ThemabasterConfig
from ...sphinx import PageContext, SphinxConfig


@component()
@dataclass(frozen=True)
class Head:
    favicon: Optional[str] = injected(ThemabasterConfig, attr='favicon')
    page_title: str = injected(PageContext, attr='title')
    project: Optional[str] = injected(SphinxConfig, attr='project')
    site_css_files: Iterable[str] = injected(ThemabasterConfig, attr='css_files')
    page_css_files: Iterable[str] = injected(PageContext, attr='css_files')
    site_js_files: Iterable[str] = injected(ThemabasterConfig, attr='js_files')
    touch_icon: Optional[str] = injected(ThemabasterConfig, attr='touch_icon')
    page_js_files: Iterable[str] = injected(PageContext, attr='css_files')
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    extrahead: Optional[Tuple[VDOM, ...]] = None
    charset: str = 'utf-8'

    def __call__(self) -> VDOM:
        custom_css = self.pathto('_static/custom.css', 1)
        if self.touch_icon:
            touch_icon_href = self.pathto(self.touch_icon, 1)
            touch_icon = html(
                '<link rel="stylesheet" href="{touch_icon_href}" type="text/css"/>') if self.touch_icon else ''
        else:
            touch_icon = None
        docs_src = self.pathto('_static/documentation_options.js', 1)
        static_root = self.pathto('', 1)
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <{Title} page_title={self.page_title} project={self.project} />
  <link rel="stylesheet" href={self.pathto('_static/themabaster.css', 1)} type="text/css" />
  <link rel="stylesheet" href={self.pathto('_static/pygments.css', 1)} type="text/css" />
  <{CSSFiles} page_files={self.page_css_files} site_files={self.site_css_files} />
  <script id="documentation_options" data-url_root="{static_root}" src="{docs_src}">//</script>
  <{JSFiles} page_files={self.page_js_files} site_files={self.site_js_files} />
  <link rel="stylesheet" href="{custom_css}" type="text/css"/>
  {touch_icon}
  <{Linktags} />
  {self.extrahead}
</head>
''')
