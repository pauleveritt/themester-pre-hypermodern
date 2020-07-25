from dataclasses import dataclass
from typing import Callable, TypedDict, Iterable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx import PageContext


class SemanticLink(TypedDict):
    rel: str
    title: str
    docname: str


@component()
@dataclass(frozen=True)
class Linktags:
    hasdoc: Callable[[str], bool] = injected(PageContext, attr='hasdoc')
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    links: Iterable[SemanticLink] = tuple()

    def __call__(self) -> VDOM:
        resolved_links = (
            dict(
                rel=link['rel'],
                title=link['title'],
                href=self.pathto(link['docname'], 1)
            )
            for link in self.links
            if self.hasdoc(link['docname'])
        )
        return html('''\n
{[
html('<link rel={link["rel"]} href={link["href"]} title={link["title"]} />')
for link in resolved_links
]}
        ''')
