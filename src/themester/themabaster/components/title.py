from dataclasses import dataclass, field
from typing import Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from themester.protocols import Resource
from themester.sphinx import SphinxConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class Title:
    resource_title: Annotated[
        str,
        Get(Resource),
        Attr('title'),
    ]
    site_title: Annotated[
        Optional[str],
        Get(SphinxConfig),
        Attr('project'),
    ]
    resolved_title: str = field(init=False)

    def __post_init__(self):
        if self.site_title:
            raw_title = f'{self.resource_title} - {self.site_title}'
        else:
            raw_title = f'{self.resource_title}'
        self.resolved_title = Markup(raw_title).striptags()

    def __call__(self) -> VDOM:
        return html('<title>{self.resolved_title}</title>')
