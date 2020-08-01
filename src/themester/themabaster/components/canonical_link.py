"""
Generate ``<link rel="canonical"/>`` if ``HTMLConfig.baseurl`` is set.
"""

from dataclasses import dataclass, field
from os.path import join
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import HTMLConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class CanonicalLink:
    baseurl: Optional[str] = injected(HTMLConfig, attr='baseurl')
    canonical_href: Optional[str] = field(init=False)
    file_suffix: str = injected(HTMLConfig, attr='file_suffix')
    pagename: str = injected(PageContext, attr='pagename')

    def __post_init__(self):
        if self.baseurl:
            self.canonical_href = join(self.baseurl, self.pagename + self.file_suffix)
        else:
            self.canonical_href = None

    def __call__(self) -> Optional[VDOM]:
        if self.canonical_href:
            return html('<link rel="canonical" href={self.canonical_href}/>')
        return None
