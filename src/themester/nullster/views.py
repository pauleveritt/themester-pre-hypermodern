from dataclasses import dataclass

from viewdom import html, VDOM

from themester.nullster.components.hello_world import HelloWorld
from themester.views import view


@view()
@dataclass
class AllView:
    """ One view for all pages in the site"""
    name: str = 'Nullster View'

    def __call__(self) -> VDOM:
        assert HelloWorld
        return html('<div><{HelloWorld} name="Nullster" /></div>')
