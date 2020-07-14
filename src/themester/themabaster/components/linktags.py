from dataclasses import dataclass
from typing import Callable, TypedDict, Iterable

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.protocols import Hasdoc
from themester.url import URL


class SemanticLink(TypedDict):
    rel: str
    title: str
    docname: str


@component()
@dataclass(frozen=True)
class Linktags:
    hasdoc: Hasdoc  # TODO Sphinx "adapter" has to register this in container
    static_url: Callable = injected(URL, attr='static_url')
    links: Iterable[SemanticLink] = tuple()

    def __call__(self) -> VDOM:
        resolved_links = (
            dict(
                rel=link['rel'],
                title=link['title'],
                href=self.static_url(link['docname'])
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
