from dataclasses import dataclass
from typing import Callable, TypedDict, Iterable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.models import PageContext


class SemanticLink(TypedDict):
    rel: str
    title: str
    docname: str


DEFAULT_LINKS = (
    SemanticLink(rel='author', title='About these documents', docname='about'),
    SemanticLink(rel='genindex', title='Index', docname='genindex'),
    SemanticLink(rel='search', title='Search', docname='search'),
    SemanticLink(rel='copyright', title='Copyright', docname='copyright'),
)


@component()
@dataclass(frozen=True)
class Linktags:
    hasdoc: Callable[[str], bool] = injected(PageContext, attr='hasdoc')
    pathto: Callable[[str, int], str] = injected(PageContext, attr='pathto')
    links: Iterable[SemanticLink] = DEFAULT_LINKS

    def __call__(self) -> VDOM:
        resolved_links = (
            dict(
                rel=link['rel'],
                title=link['title'],
                href=self.pathto(link['docname'], 0)
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
