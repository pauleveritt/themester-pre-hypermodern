"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass, field
from typing import Optional, Callable, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from ..canonical_link import CanonicalLink
from ..cssfiles import CSSFiles
from ..faviconset import FaviconSet
from ..jsfiles import JSFiles
from ..linktags import Linktags
from ..title import Title
from ....sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Head:
    pathto: Annotated[
        Callable[[str, int], str],
        Get(PageContext, attr='pathto'),
    ]
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
