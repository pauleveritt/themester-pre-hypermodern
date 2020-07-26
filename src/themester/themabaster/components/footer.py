"""
A block in the body, below the content block.
"""

from dataclasses import dataclass
from typing import Optional, Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext, SphinxConfig
from themester.themabaster.config import ThemabasterConfig


@component()
@dataclass(frozen=True)
class Footer:
    """ A block in the body below the content block. """

    copyright: Optional[str] = injected(SphinxConfig, attr='copyright')
    has_source: bool = injected(ThemabasterConfig, attr='has_source')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    show_powered_by: bool = injected(ThemabasterConfig, attr='show_powered_by')
    show_copyright: bool = injected(ThemabasterConfig, attr='show_copyright')
    show_sourcelink: bool = injected(ThemabasterConfig, attr='show_sourcelink')
    sourcename: str = injected(PageContext, attr='sourcename')

    def __call__(self) -> VDOM:
        copyright = f'&copy; {self.copyright}.' if self.copyright else ''
        powered_by = html('''\n
{'|' if self.copyright else ''}
Powered by <a href="http://sphinx-doc.org/">Sphinx</a>
        ''') if self.show_powered_by else html('')
        if self.show_sourcelink and self.has_source and self.sourcename:
            ps = self.pathto(f'_sources/{self.sourcename}')
            page_source = html('''\n
{'|' if self.show_copyright or self.show_powered_by else ''}
<a href={ps} rel="nofollow">Page source</a>
            ''')
        else:
            page_source = html('')
        return html('''\n
<div class="footer">
    {copyright}
    {powered_by}
    {page_source}
</div>
        ''')
