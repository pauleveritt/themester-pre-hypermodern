"""
Document is a block in the Content component.
"""

from dataclasses import dataclass, field

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.config import HTMLConfig
from themester.sphinx.models import PageContext
from ..components.relbar1 import Relbar1  # noqa: F401
from ..components.relbar2 import Relbar2  # noqa: F401


@component()
@dataclass
class Document:
    """ A block in content, holding most of the info on this resource """

    body: Markup = injected(PageContext, attr='body')
    nosidebar: bool = injected(HTMLConfig, attr='nosidebar')
    inner: VDOM = field(init=False)

    def __post_init__(self):
        # Alabaster wraps the main content in <div class="bodywrapper">
        # if nosidebar is true. Thus, get the main content first, then
        # insert in the two flavors of response.
        main_content = html('''\n
        <{Relbar1}/>
          <div class="body" role="main">
            {self.body}
          </div>          
        <{Relbar2}/>        
                ''')
        self.inner = main_content if self.nosidebar else html('<div class="bodywrapper">{main_content}</div>')

    def __call__(self) -> VDOM:
        return html('''\n
<div class="documentwrapper">
  {self.inner}
</div>        
            ''')
