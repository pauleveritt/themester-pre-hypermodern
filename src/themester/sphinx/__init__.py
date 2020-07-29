from sphinx.application import Sphinx

from themester.sphinx.builder_init_setup_app import setup_app
from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.inject_page import make_render_container, make_page_context
from themester.config import ThemesterConfig
from themester.themabaster.config import ThemabasterConfig


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    themester_app = setup_app(app.config)
    setattr(app, 'themester_app', themester_app)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    render_container = make_render_container(
        app.themester_app,
        pagename='',
    )
    context['render_container'] = render_container
    make_page_context(
        render_container=render_container,
        context=context,
        pagename=pagename,
        toc_num_entries=app.env.toc_num_entries,
        sphinxenv_metadata=app.env.metadata,
    )


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
