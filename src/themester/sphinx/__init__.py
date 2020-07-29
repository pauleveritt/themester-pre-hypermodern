from markupsafe import Markup
from sphinx.application import Sphinx

from themester.protocols import Root
from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.models import PageContext, Link, Rellink
from themester.testing.config import ThemesterConfig
from themester.themabaster.config import ThemabasterConfig
from .builder_init_setup_app import setup_app


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    themester_app = setup_app(app.config)
    setattr(app, 'themester_app', themester_app)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    from themester.app import ThemesterApp

    themester_app: ThemesterApp = app.themester_app
    themester_root = themester_app.container.get(Root)

    sphinx_config: SphinxConfig = app.config.sphinx_config

    # If this is a Sphinx site that wants to do resource-oriented
    # pages, get the current resource.
    if getattr(sphinx_config, 'use_resources', False):
        resource = themester_root[pagename]
    else:
        resource = themester_root

    render_container = themester_app.container.bind(context=resource)
    context['render_container'] = render_container

    # Gather the Sphinx per-page render info into an object that
    # can be retrieved from the container
    display_toc = app.env.toc_num_entries[pagename] > 1 if 'pagename' in app.env.toc_num_entries else False
    parents = tuple([
        Link(title=link.title, link=link.title)
        for link in context.get('parents')
    ])
    rellinks = tuple([
        Rellink(
            pagename=link[0],
            link_text=link[3],
            title=link[1],
            accesskey=link[2],
        )
        for link in context.get('rellinks')
    ])
    page_context = PageContext(
        body=Markup(context.get('body', '')),
        css_files=context.get('css_files'),
        display_toc=display_toc,
        hasdoc=context.get('hasdoc'),
        js_files=context.get('js_files'),
        meta=app.env.metadata,
        metatags=context.get('metatags'),
        next=context.get('next'),
        page_source_suffix=context.get('page_source_suffix'),
        pagename=pagename,
        pathto=context.get('pathto'),
        prev=context.get('prev'),
        sourcename=context.get('sourcename'),
        rellinks=rellinks,
        title=context.get('title'),
        toc=Markup(context.get('toc')),
        toctree=context.get('toctree'),
    )
    render_container.register_singleton(page_context, PageContext)


def setup(app: Sphinx):
    app.add_config_value('themester_config', ThemesterConfig(), 'env')
    app.add_config_value('sphinx_config', SphinxConfig(), 'env')
    app.add_config_value('html_config', HTMLConfig(), 'env')
    app.add_config_value('theme_config', ThemabasterConfig(), 'env')
    app.add_config_value('themester_plugins', [], 'env')
    app.connect('builder-inited', builder_init)
    app.config.template_bridge = 'themester.sphinx.template_bridge.ThemesterBridge'  # noqa
    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
