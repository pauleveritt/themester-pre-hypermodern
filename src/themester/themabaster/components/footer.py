"""
A block in the body, below the content block.
"""

from dataclasses import dataclass, field
from typing import Optional, Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.protocols import ThemeConfig
from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Footer:
    """ A block in the body below the content block. """

    copyright: Annotated[
        Optional[str],
        Get(SphinxConfig),
        Attr('copyright'),
    ]
    has_source: Annotated[
        bool,
        Get(HTMLConfig),
        Attr('has_source'),
    ]
    pathto: Annotated[
        Callable[[str], str],
        Get(PageContext),
        Attr('pathto')
    ]
    show_powered_by: Annotated[
        bool,
        Get(ThemeConfig),
        Attr('show_powered_by'),
    ]
    show_copyright: Annotated[
        bool,
        Get(HTMLConfig),
        Attr('show_copyright'),
    ]
    show_sourcelink: Annotated[
        bool,
        Get(HTMLConfig),
        Attr('show_sourcelink'),
    ]
    sourcename: Annotated[
        str,
        Get(PageContext),
        Attr('sourcename'),
    ]
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
