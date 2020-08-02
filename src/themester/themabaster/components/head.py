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
from .faviconset import FaviconSet  # noqa: F401
from .jsfiles import JSFiles  # noqa: F401
from .linktags import Linktags  # noqa: F401
from .title import Title  # noqa: F401
from ...sphinx.models import PageContext


@component()
@dataclass
class Head:
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    extrahead: Optional[Tuple[VDOM, ...]] = None
    charset: str = 'utf-8'
    resolved_custom_css: str = field(init=False)
    resolved_docs_src: str = field(init=False)
    resolved_static_root: str = field(init=False)

    def __post_init__(self):
        self.resolved_custom_css = self.pathto('_static/custom.css', 1)
        self.resolved_docs_src = self.pathto('_static/documentation_options.js', 1)
        self.resolved_static_root = self.pathto('', 1)

    def __call__(self) -> VDOM:
        return html('''\n
<head>
  <meta charset="{self.charset}" />
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <{Title} />
  <{CSSFiles} />
  <script id="documentation_options" data-url_root="{self.resolved_static_root}" src="{self.resolved_docs_src}">//</script>
  <{JSFiles} />
  <link rel="stylesheet" href="{self.resolved_custom_css}" type="text/css"/>
  <{CanonicalLink} />
  <{FaviconSet}/>
  <{Linktags} />
  {self.extrahead}
</head>
''')
