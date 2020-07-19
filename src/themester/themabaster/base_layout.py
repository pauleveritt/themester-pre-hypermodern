"""
The base layout, possibly extended by sublayouts.
"""
from dataclasses import dataclass

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component

from themester.themabaster.services.layoutconfig import ThemabasterConfig
from .components.head import Head  # noqa: F401
from .components.html import HTML  # noqa: F401


@component()
@dataclass
class BaseLayout:
    config: ThemabasterConfig
    extrahead: VDOM = None

    # Blocks
    doctype: Markup = Markup('<!DOCTYPE html>\n')


    def __call__(self) -> VDOM:
        return html('''\n
{self.doctype}
<html lang="{self.config.lang}">
    <head>
    {self.extrahead}
    </head>
</html>
        ''')
