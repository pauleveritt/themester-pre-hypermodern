"""
Default implementation of the Themabaster <Body> component.
"""

from dataclasses import dataclass

from viewdom import html, VDOM
from viewdom_wired import component

from .content import Content
from .footer import Footer
from .header import Header


@component()
@dataclass(frozen=True)
class Body:
    def __call__(self) -> VDOM:
        assert (Content, Footer, Header)
        return html('''\n
<body>
<{Header} />
<{Content} />
<{Footer} />
</body>
''')
