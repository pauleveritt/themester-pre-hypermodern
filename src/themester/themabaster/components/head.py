"""
Default implementation of the Themabaster <Head> component.
"""

from dataclasses import dataclass
from typing import Iterable

from viewdom import H, html
from viewdom_wired import component, Component

from ..protocols import Head, Title


@component(for_=Head)
@dataclass(frozen=True)
class DefaultHead(Head):
    title: Title = None
    # TODO Have a Meta component and make this an iterable of those
    metatags: Iterable[Component] = tuple()

    def __call__(self) -> H:
        return html('''\n
<head>
  {[meta for meta in self.metatags]}
  {self.title}
</head>
''')
