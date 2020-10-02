from dataclasses import dataclass, field
from typing import Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.sphinx import SphinxConfig
from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Title:
    page_title: Annotated[
        str,
        Get(PageContext),
        Attr('title'),
    ]
    project: Annotated[
        Optional[str],
        Get(SphinxConfig),
        Attr('project'),
    ]
    resolved_title: str = field(init=False)

    def __post_init__(self):
        if self.project:
            raw_title = f'{self.page_title} - {self.project}'
        else:
            raw_title = f'{self.page_title}'
        self.resolved_title = Markup(raw_title).striptags()

    def __call__(self) -> VDOM:
        return html('<title>{self.resolved_title}</title>')
