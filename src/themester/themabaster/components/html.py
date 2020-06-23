"""
Default implementation of the Themabaster <HTML> component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component, adherent
from wired.dataclasses import injected

from ..protocols import HTML, LayoutConfig, Head  # noqa


@component(for_=HTML)
@adherent(HTML)
@dataclass(frozen=True)
class DefaultHTML(HTML):
    lang: str = injected(LayoutConfig, attr='lang')

    def __call__(self) -> VDOM:
        return html('''\n
<html lang="{self.lang}">
  <{Head} />
</head>
''')
