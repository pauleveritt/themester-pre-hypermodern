from dataclasses import dataclass, field
from typing import Optional

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import SphinxConfig
from themester.sphinx.models import PageContext


@component()
@dataclass
class Title:
    page_title: str = injected(PageContext, attr='title')
    project: Optional[str] = injected(SphinxConfig, attr='project')
    resolved_title: str = field(init=False)

    def __post_init__(self):
        if self.project:
            raw_title = f'{self.page_title} - {self.project}'
        else:
            raw_title = f'{self.page_title}'
        self.resolved_title = Markup(raw_title).striptags()

    def __call__(self) -> VDOM:
        return html('<title>{self.resolved_title}</title>')
