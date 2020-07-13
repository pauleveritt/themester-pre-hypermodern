"""
The base layout, possibly extended by sublayouts.
"""
from dataclasses import dataclass
from typing import Optional, Tuple

from viewdom import html, VDOM
from viewdom_wired import component, adherent

from themester.themabaster.protocols import HTML, BaseLayout, Head  # noqa
from themester.themabaster.services.layoutconfig import ThemabasterConfig


@component(for_=BaseLayout)
@adherent(BaseLayout)
@dataclass
class DefaultBaseLayout(BaseLayout):
    config: ThemabasterConfig
    extrahead: Tuple[VDOM, ...] = None

    def __call__(self) -> VDOM:
        return html('''\n
<html lang="{self.config.lang}">
    <head>
    </head>
</html>
        ''')

@component()
@dataclass
class SidebarLayout:
    name: str = 'Sidebar Layout'

    def __call__(self) -> VDOM:
        return html('''\n
<{BaseLayout}>
<//>
        ''')