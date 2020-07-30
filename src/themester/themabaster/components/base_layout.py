"""
The base layout, possibly extended by sublayouts.
"""
from dataclasses import dataclass, field
from typing import Dict, Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from ..components.body import Body  # noqa: F401
from ..components.head import Head  # noqa: F401
from ...sphinx import SphinxConfig


@component()
@dataclass
class BaseLayout:
    language: str = injected(SphinxConfig, attr='language')
    extrahead: Optional[VDOM] = None
    doctype: Markup = Markup('<!DOCTYPE html>\n')
    html_props: Dict[str, str] = field(init=False)

    def __post_init__(self):
        self.html_props = dict(lang=self.language) if self.language else dict()

    def __call__(self) -> VDOM:
        return html('''\n
{self.doctype}
<html ...{self.html_props}>
    <{Head} extrahead={self.extrahead} />
    <{Body} />
</html>
        ''')
