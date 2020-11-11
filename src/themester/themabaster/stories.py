from themester.protocols import ThemeConfig
from themester.sphinx import HTMLConfig
from themester.sphinx.models import PageContext
from themester.themabaster import ThemabasterConfig
from themester.themabaster.storytime_example import fake_pagecontext

theme_config = ThemabasterConfig()
html_config = HTMLConfig(favicon='someicon.png')
singletons = (
    (theme_config, ThemeConfig),
    (html_config, HTMLConfig),
    (fake_pagecontext, PageContext),
)
