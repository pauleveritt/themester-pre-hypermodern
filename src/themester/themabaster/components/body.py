"""
Default implementation of the Themabaster <Body> component.
"""

from dataclasses import dataclass
from typing import Iterable, Optional, Callable, Tuple

from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.themabaster.services.layoutconfig import ThemabasterConfig
from themester.themabaster.services.pagecontext import PageContext
from themester.url import URL
from .cssfiles import CSSFiles  # noqa: F401
from .jsfiles import JSFiles  # noqa: F401
from .title import Title  # noqa: F401


@component()
@dataclass(frozen=True)
class Body:
    def __call__(self) -> VDOM:
        return html('''\n
<body>
1
</body>
''')
