from markupsafe import Markup

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.protocols import Resource
from themester.sphinx import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext, Link
from ..resources import Site, Document, Collection
from themester.themabaster import ThemabasterConfig

root = Site(title='Themester Site')
f1 = Collection(name='f1', parent=root, title='F1')
root['f1'] = f1
d1 = Document(name='d1', parent=root, title='D1')
root['d1'] = d1
d2 = Document(name='d2', parent=f1, title='D2')
f1['d2'] = d2
f3 = Collection(name='f3', parent=f1, title='F3')
f1['f3'] = f3
d3 = Document(name='d3', parent=f3, title='D3')
f3['d3'] = d3

resource = root['f1']['d2']
themester_config = ThemesterConfig(
    root=root,
    theme_config=ThemabasterConfig(),
    plugins=('themester.themabaster',)
)

themester_app = ThemesterApp(
    themester_config=themester_config,
)
themester_app.registry.register_singleton(SphinxConfig(), SphinxConfig)
themester_app.registry.register_singleton(HTMLConfig(), HTMLConfig)
themester_app.registry.register_singleton(resource, Resource)


def fake_hasdoc(docname) -> bool:
    """ Sphinx page context function to confirm a path exists """
    return True if docname != 'author' else False


def fake_pathto(docname, mode=0) -> str:
    """ Sphinx page context function to get a path to a target """
    return f'../mock/{docname}'


def fake_toctree(sidebar_collapse: bool = True, sidebar_includehidden: bool = True) -> str:
    """ Sphinx page context function to return string of toctree """
    return '<ul><li>First</li></ul>'


fake_pagecontext = PageContext(
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

themester_app.registry.register_singleton(fake_pagecontext, PageContext)
