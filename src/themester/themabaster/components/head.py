"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass, field
from typing import Optional, Callable, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from .canonical_link import CanonicalLink  # noqa: F401
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
    favicon: Optional[str] = injected(HTMLConfig, attr='favicon')
    page_title: str = injected(PageContext, attr='title')
    project: Optional[str] = injected(SphinxConfig, attr='project')
    touch_icon: Optional[str] = injected(ThemabasterConfig, attr='touch_icon')
    pagename: str = injected(PageContext, attr='pagename')
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    extrahead: Optional[Tuple[VDOM, ...]] = None
    charset: str = 'utf-8'
    resolved_custom_css: str = field(init=False)
    resolved_touch_icon: Optional[VDOM] = field(init=False)
    resolved_docs_src: str = field(init=False)
    resolved_static_root: str = field(init=False)

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

    def __call__(self) -> VDOM:
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <{Title} page_title={self.page_title} project={self.project} />
  <{CSSFiles} />
  <script id="documentation_options" data-url_root="{self.resolved_static_root}" src="{self.resolved_docs_src}">//</script>
  <{JSFiles} />
  <link rel="stylesheet" href="{self.resolved_custom_css}" type="text/css"/>
  <{CanonicalLink} />
  {self.resolved_touch_icon}
  <{Linktags} />
  {self.extrahead}
</head>
''')
