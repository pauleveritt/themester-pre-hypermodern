"""
A block in the body, below the content block.
"""

from dataclasses import dataclass, field
from typing import Optional, Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext
from themester.themabaster.config import ThemabasterConfig


@component()
@dataclass
class Footer:
    """ A block in the body below the content block. """

    copyright: Optional[str] = injected(SphinxConfig, attr='copyright')
    has_source: bool = injected(HTMLConfig, attr='has_source')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    show_powered_by: bool = injected(ThemabasterConfig, attr='show_powered_by')
    show_copyright: bool = injected(HTMLConfig, attr='show_copyright')
    show_sourcelink: bool = injected(HTMLConfig, attr='show_sourcelink')
    sourcename: str = injected(PageContext, attr='sourcename')
    resolved_copyright: str = field(init=False)
    resolved_powered_by: VDOM = field(init=False)
    resolved_page_source: VDOM = field(init=False)

    def __post_init__(self):
        self.resolved_copyright = f'&copy; {self.copyright}.' if self.copyright else ''
        self.resolved_powered_by = html('''\n
{'|' if self.copyright else ''}
Powered by <a href="http://sphinx-doc.org/">Sphinx</a>
        ''') if self.show_powered_by else html('')
        if self.show_sourcelink and self.has_source and self.sourcename:
            ps = self.pathto(f'_sources/{self.sourcename}')
            self.resolved_page_source = html('''\n
{'|' if self.show_copyright or self.show_powered_by else ''}
<a href={ps} rel="nofollow">Page source</a>
            ''')
        else:
            self.resolved_page_source = html('')

    def __call__(self) -> VDOM:
        return html('''\n
<div class="footer">
    {self.resolved_copyright}
    {self.resolved_powered_by}
    {self.resolved_page_source}
</div>
        ''')
