from dataclasses import dataclass, field
from typing import Protocol, Optional

from viewdom import html, render
from viewdom_wired import Component, adherent


class Header(Component, Protocol):
    """ A slot in the body """

    ...


@adherent(Header)
@dataclass(frozen=True)
class DefaultHeader(Header):
    def __call__(self):
        return html('<header>2</header>')


@dataclass
class DefaultBody:
    header: Optional[Header] = field(default_factory=DefaultHeader)

    def __call__(self):
        return html('''\n
<body>
    {self.header}
</body>
        ''')


def test_component():
    body = DefaultBody(
        header=html('<header>From the view</header>')
    )
    vdom = body()
    response = render(vdom)
    # assert 9 == response
