"""
Sidebar to show a searchbox.
"""

from dataclasses import dataclass, field
from typing import Callable

from viewdom import VDOM, html
from viewdom_wired import component
from wired.dataclasses import injected

from themester.sphinx.models import PageContext


@component()
@dataclass
class SearchBox:
    builder: str = injected(PageContext, attr='builder')
    pagename: str = injected(PageContext, attr='pagename')
    pathto: Callable[[str], str] = injected(PageContext, attr='pathto')
    resolved_pathto: str = field(init=False)

    def __post_init__(self):
        self.resolved_pathto = self.pathto('search')

    def __call__(self) -> VDOM:
        if self.pagename != 'search' and self.builder != 'singlehtml':
            return html('''\n
<div id="searchbox" style="display: none" role="search" data-testid="searchbox">
    <h3>{{ _('Quick search') }}</h3>
    <div class="searchformwrapper">
        <form class="search" action="{self.resolved_pathto}" method="get">
          <input type="text" name="q" />
          <input type="submit" value="Go" />
          <input type="hidden" name="check_keywords" value="yes" />
          <input type="hidden" name="area" value="default" />
        </form>
    </div>
</div>
<script type="text/javascript">$('#searchbox').show(0);</script>
            ''')
        return html('')
