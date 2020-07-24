"""
Document is a block in the Content component.
"""

from dataclasses import dataclass

from markupsafe import Markup
from viewdom import html, VDOM
from viewdom_wired import component
from wired.dataclasses import injected

from ..components.relbar1 import Relbar1  # noqa: F401
from ..components.relbar2 import Relbar2  # noqa: F401
from ..services.layoutconfig import ThemabasterConfig
from ..services.documentbody import DocumentBody


@component()
@dataclass(frozen=True)
class Document:
    """ A block in content, holding most of the info on this resource """

    document_body: Markup = injected(DocumentBody, attr='html')
    no_sidebar: bool = injected(ThemabasterConfig, attr='no_sidebar')

    def __call__(self) -> VDOM:
        # Alabaster wraps the main content in <div class="bodywrapper">
        # if no_sidebar is true. Thus, get the main content first, then
        # insert in the two flavors of response.
        main_content = html('''\n
<{Relbar1}/>
  <div class="body" role="main">
    {self.document_body}
  </div>          
<{Relbar2}/>        
        ''')
        inner = main_content if self.no_sidebar else html('<div class="bodywrapper">{main_content}</div>')

        return html('''\n
<div class="documentwrapper">
  {inner}
</div>        
            ''')
