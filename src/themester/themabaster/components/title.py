"""
Default implementation of the Themabaster <Title> component.
"""

from dataclasses import dataclass
from typing import Optional

from markupsafe import Markup
from viewdom import H, html
from viewdom_wired import component
from wired.dataclasses import injected

from ..protocols import Title, LayoutConfig


@component(for_=Title)
@dataclass(frozen=True)
class DefaultTitle(Title):
    page_title: str
    site_name: Optional[str] = injected(LayoutConfig, attr='site_name')

    def __call__(self) -> H:
        if self.site_name:
            raw_title = f'{self.page_title} - {self.site_name}'
        else:
            raw_title = f'{self.page_title}'
        title = Markup(raw_title).striptags()
        return html('<title>{title}</title>')
