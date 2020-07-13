"""
Default implementation of the Themabaster <HTML> component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from .head import Head  # noqa: F401
from ..services.layoutconfig import ThemabasterConfig


@component()
@dataclass(frozen=True)
class HTML:
    lang: str = injected(ThemabasterConfig, attr='lang')

    def __call__(self) -> VDOM:
        return html('''\n
<html lang="{self.lang}">
  <{Head} />
</head>
''')
