"""
The base layout, possibly extended by sublayouts.
"""
from dataclasses import dataclass, field
from typing import Dict, Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get, Attr

from ...components.body import Body
from ...components.head import Head
from ....sphinx import SphinxConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class BaseLayout:
    language: Annotated[
        str,
        Get(SphinxConfig),
        Attr('language'),
    ]
    extrahead: Optional[VDOM] = None
    doctype: Markup = Markup('<!DOCTYPE html>\n')
    html_props: Dict[str, str] = field(init=False)

    def __post_init__(self):
        self.html_props = dict(lang=self.language) if self.language else dict()

    def __call__(self) -> VDOM:
        assert Body, Head
        return html('''\n
{self.doctype}
<html ...{self.html_props}>
    <{Head} extrahead={self.extrahead} />
    <{Body} />
</html>
        ''')
