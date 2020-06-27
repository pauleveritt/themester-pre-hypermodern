from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component, adherent

from themester.themabaster.protocols import ExtraHead


@component(for_=ExtraHead)
@adherent(ExtraHead)
@dataclass(frozen=True)
class DefaultExtraHead(ExtraHead):
    """ By default this is empty """

    def __call__(self) -> VDOM:
        # TODO Post-1.0 When VDOM is a top-level list of tuples, just
        #   return an empty tuple
        return html('')
