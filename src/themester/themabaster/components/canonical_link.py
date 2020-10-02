"""
Generate ``<link rel="canonical"/>`` if ``HTMLConfig.baseurl`` is set.
"""

from dataclasses import dataclass, field
from os.path import join
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.sphinx import HTMLConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class CanonicalLink:
    baseurl: Annotated[
        Optional[str],
        Get(HTMLConfig),
        Attr('baseurl')
    ]
    canonical_href: Optional[str] = field(init=False)
    file_suffix: Annotated[
        str,
        Get(HTMLConfig),
        Attr('file_suffix'),
    ]
    pagename: Annotated[
        str,
        Get(PageContext),
        Attr('pagename')
    ]

    def __post_init__(self):
        if self.baseurl:
            self.canonical_href = join(self.baseurl, self.pagename + self.file_suffix)
        else:
            self.canonical_href = None

    def __call__(self) -> Optional[VDOM]:
        if self.canonical_href:
            return html('<link rel="canonical" href={self.canonical_href}/>')
        return None
