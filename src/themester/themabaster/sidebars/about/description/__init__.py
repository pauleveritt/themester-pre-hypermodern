"""
AboutDescription is a block in the About component.
"""

from dataclasses import dataclass
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from themester.protocols import ThemeConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


@component()
@dataclass
class AboutDescription:
    """ The description block in the About sidebar """

    description: Annotated[
        Optional[str],
        Get(ThemeConfig, attr='description')
    ]

    def __call__(self) -> Optional[VDOM]:
        if self.description:
            return html('<p class="blurb">{self.description}</p>')
        return None
