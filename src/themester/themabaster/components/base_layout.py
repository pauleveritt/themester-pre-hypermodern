"""
The base layout, possibly extended by sublayouts.
"""
from dataclasses import dataclass

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from ..components.body import Body  # noqa: F401
from ..components.head import Head  # noqa: F401
from ..components.html import HTML  # noqa: F401
from ...sphinx import SphinxConfig


@component()
@dataclass
class BaseLayout:
    language: str = injected(SphinxConfig, attr='language')
    extrahead: VDOM = None
    doctype: Markup = Markup('<!DOCTYPE html>\n')

    def __call__(self) -> VDOM:
        return html('''\n
{self.doctype}
<html lang="{self.language}">
    <{Head} extrahead={self.extrahead} />
    <{Body} />
</html>
        ''')
