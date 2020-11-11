from themester.sphinx import HTMLConfig
from themester.sphinx.models import PageContext
from themester.themabaster.storytime_example import fake_pagecontext

singletons = (
    (HTMLConfig(favicon='someicon.png'), HTMLConfig),
    (fake_pagecontext, PageContext),
)
