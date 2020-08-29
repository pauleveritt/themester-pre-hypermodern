from dataclasses import dataclass

from viewdom import html, VDOM

from themester.views import view


@view()
@dataclass
class AllView:
    """ One view for all pages in the site"""
    name = 'Nullster View'

    def __call__(self) -> VDOM:
        return html('<div>Hello World</div>')
