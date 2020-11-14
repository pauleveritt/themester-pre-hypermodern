"""
Generate the <link> etc. for various sizes of favicons.

Believe it or not, this is a complicated area with lots of legacy
decisions on one hand, vs. PWAs on the other hand. Let's make a
replaceable component to encapsulate all these decisions.
"""
from dataclasses import dataclass, field
from os.path import join
from typing import Callable, Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.protocols import ThemeConfig
from themester.sphinx.models import PageContext
from themester.themabaster.config import Favicons

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class FaviconSet:
    favicons: Annotated[
        Favicons,
        Get(ThemeConfig),
        Attr('favicons')
    ]
    pathto: Annotated[
        Callable[[str, int], str],
        Get(PageContext, attr='pathto'),
    ]
    shortcut_href: Optional[str] = field(init=False)
    png_href: Optional[str] = field(init=False)

    def __post_init__(self):
        favicons = self.favicons
        self.shortcut_href = self.pathto(join('static', favicons.shortcut), 1) if favicons.shortcut else None
        self.png_href = self.pathto(join('static', favicons.png), 1) if favicons.png else None

    def __call__(self) -> VDOM:
        shortcut = html(
            '<link rel="shortcut icon" type="image/x-icon" href={self.shortcut_href} />') if self.shortcut_href else None
        png = html('<link rel="shortcut icon" type="image/x-icon" href={self.png_href} />') if self.png_href else None
        precomposed = html(
            '<link rel="apple-touch-icon-precomposed" type="image/x-icon" href={self.png_href} />') if self.png_href else None
        if self.favicons.sizes:
            sizes = []
            for size in self.favicons.sizes:
                size_href = self.pathto(join('static', size.filename), 1)
                size_size = size.size
                sizes.append(html(
                    '<link rel="apple-touch-icon-precomposed" sizes={size_size} href={size_href} />'))
        else:
            sizes = None
        return html('''\n
{shortcut}
{png}
{precomposed}
{sizes}
        ''')
