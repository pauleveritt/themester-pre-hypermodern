from dataclasses import dataclass, field
from typing import Optional

from viewdom import html, VDOM
from viewdom_wired import component
from wired_injector.operators import Get

from ..config import ThemabasterConfig
from ...sphinx import SphinxConfig

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated


# TODO Break each badge into its own component file, sigh
@component()
@dataclass
class DonateBadge:
    donate_url: Optional[str]

    def __call__(self) -> Optional[VDOM]:
        if self.donate_url:
            return html('''\n
<p>
    <a class="badge" href="{self.donate_url}">
    <img src="https://img.shields.io/badge/donate-%E2%9D%A4%C2%A0-ff69b4.svg?style=flat" alt="Donate" />
    </a>
</p>
            ''')
        return None


@component()
@dataclass
class OpenCollectiveBadge:
    opencollective: Optional[str]
    opencollective_button_color: str

    def __call__(self) -> Optional[VDOM]:
        if self.opencollective:
            return html('''\n
<p>
<a class="badge" href="https://opencollective.com/{self.opencollective}/donate" target="_blank">
  <img src="https://opencollective.com/{self.opencollective}/donate/button.png?color={self.opencollective_button_color}" width=300 />
</a>
</p>
            ''')
        return None


@component()
@dataclass
class TideliftBadge:
    project: str
    tidelift_url: Optional[str]

    def __call__(self) -> Optional[VDOM]:
        if self.tidelift_url:
            return html('''\n
<p>
Professionally-supported {self.project} is available with the
<a href="{self.tidelift_url}">Tidelift Subscription</a>.
</p>
            ''')
        return None


@component()
@dataclass
class Donate:
    donate_url: Annotated[Optional[str], Get(ThemabasterConfig, attr='donate_url')]
    opencollective: Annotated[Optional[str], Get(ThemabasterConfig, attr='opencollective')]
    opencollective_button_color: Annotated[str, Get(ThemabasterConfig, attr='opencollective_button_color')]
    project: Annotated[str, Get(SphinxConfig, attr='project')]
    tidelift_url: Annotated[Optional[str], Get(ThemabasterConfig, attr='tidelift_url')]
    show_donate: bool = field(init=False)

    def __post_init__(self):
        self.show_donate = (self.donate_url is not None) or (self.opencollective is not None) or (
                self.tidelift_url is not None)

    def __call__(self) -> Optional[VDOM]:
        if self.show_donate:
            return html('''\n
<h3 class="donation">Donate/support</h3>
<{DonateBadge} donate_url={self.donate_url} />
<{OpenCollectiveBadge} opencollective={self.opencollective} opencollective_button_color={self.opencollective_button_color} />
<{TideliftBadge} tidelift_url={self.tidelift_url} project={self.project}/>
        ''')
        return None
