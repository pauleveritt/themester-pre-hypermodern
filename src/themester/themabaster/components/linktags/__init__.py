from dataclasses import dataclass, field
from typing import Callable, TypedDict, Iterable, List, Any, Dict

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from themester.sphinx.models import PageContext

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


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
@dataclass
class Linktags:
    hasdoc: Annotated[
        Callable[[str], bool],
        Get(PageContext, attr='hasdoc'),
    ]
    pathto: Annotated[
        Callable[[str, int], str],
        Get(PageContext, attr='pathto'),
    ]
    links: Iterable[SemanticLink] = DEFAULT_LINKS
    resolved_links: List[Dict[str, Any]] = field(init=False)

    def __post_init__(self):
        self.resolved_links = [
            dict(
                rel=link['rel'],
                title=link['title'],
                href=self.pathto(link['docname'], 0)
            )
            for link in self.links
            if self.hasdoc(link['docname'])
        ]

    def __call__(self) -> VDOM:
        return html('''\n
{[
html('<link rel={link["rel"]} href={link["href"]} title={link["title"]} />')
for link in self.resolved_links
]}
        ''')
