from markupsafe import Markup
from sphinx.application import Sphinx
from venusian import Scanner

from themester.protocols import Root
from themester.sphinx.config import SphinxConfig
from themester.sphinx.models import PageContext, Link, Rellink
from themester.testing.resources import Site
from themester.themabaster.config import ThemabasterConfig


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    # Circular import
    from themester import themabaster
    from themester.app import ThemesterApp

    site = Site()

    # Get all 3 of the configs: Sphinx, Themester, Themabaster
    sphinx_config: SphinxConfig = getattr(app.config, 'sphinx_config')
    theme_config: ThemabasterConfig = getattr(app.config, 'theme_config')

    themester_app = ThemesterApp(
        root=site,
        sphinx_config=sphinx_config,
        theme_config=theme_config,
    )
    themester_app.setup_plugin(themabaster)
    scanner = themester_app.container.get(Scanner)
    app.themester_app = themester_app  # noqa

    themester_app.registry.register_singleton(sphinx_config, SphinxConfig)
    themester_app.registry.register_singleton(theme_config, ThemabasterConfig)

    # Go through the configuration and register stuff
    themester_plugins = []  # sphinx_config['themester_plugins']
    for plugin in themester_plugins:
        try:
            themester_app.setup_plugin(plugin)
        except AttributeError:
            # No wired_setup so scan it instead
            scanner.scan(plugin)


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
    app.add_config_value('sphinx_config', SphinxConfig(), 'env')
    app.add_config_value('theme_config', ThemabasterConfig(), 'env')
    app.add_config_value('themester_plugins', [], 'env')
    app.connect('builder-inited', builder_init)
    app.config.template_bridge = 'themester.sphinx.template_bridge.ThemesterBridge'  # noqa
    app.connect('html-page-context', inject_page)

    return dict(parallel_read_safe=True)
