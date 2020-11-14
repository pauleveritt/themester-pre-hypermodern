from markupsafe import Markup

from themester.protocols import ThemeConfig
from themester.sphinx import HTMLConfig, SphinxConfig
from themester.sphinx.models import PageContext, Link
from themester.themabaster import ThemabasterConfig
from themester.themabaster.storytime_example import fake_pagecontext

theme_config = ThemabasterConfig()
html_config = HTMLConfig(
    css_files=('site_first.css', 'site_second.css',),
    favicon='themabaster.ico',
    logo='site_logo.png',
)
sphinx_config = SphinxConfig()


def fake_hasdoc(docname) -> bool:
    """ Sphinx page context function to confirm a path exists """
    return True if docname != 'author' else False


def fake_pathto(docname, mode=0) -> str:
    """ Sphinx page context function to get a path to a target """
    return f'../mock/{docname}'


def fake_toctree(sidebar_collapse: bool = True, sidebar_includehidden: bool = True) -> str:
    """ Sphinx page context function to return string of toctree """
    return '<ul><li>First</li></ul>'


page_context = PageContext(
    body=Markup('<h1>Some Body</h1>'),
    css_files=('page_first.css', 'page_second.css'),
    display_toc=True,
    hasdoc=fake_hasdoc,
    js_files=('page_first.js', 'page_second.js'),
    pagename='somedoc',
    page_source_suffix='.html',
    pathto=fake_pathto,
    prev=Link(
        title='Previous',
        link='/previous/',
    ),
    next=Link(
        title='Next',
        link='/next/',
    ),
    sourcename='somedoc.rst',
    title='Some Page',
    toc=Markup('<li>toc</li>'),
    toctree=fake_toctree,
)
singletons = (
    (theme_config, ThemeConfig),
    (html_config, HTMLConfig),
    (sphinx_config, SphinxConfig),
    (fake_pagecontext, PageContext),
)
