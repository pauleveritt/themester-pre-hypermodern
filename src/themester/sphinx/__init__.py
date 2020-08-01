from sphinx.application import Sphinx

from themester.config import ThemesterConfig
from themester.sphinx.builder_finished import builder_finished_setup
from themester.sphinx.builder_init import setup_app
from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.inject_page import make_render_container, make_page_context
from themester.themabaster.config import ThemabasterConfig


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    themester_app = setup_app(app.config)
    setattr(app, 'themester_app', themester_app)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    render_container = make_render_container(
        app.themester_app,
        pagename=pagename,
    )
    context['render_container'] = render_container
    make_page_context(
        render_container=render_container,
        context=context,
        pagename=pagename,
        toc_num_entries=app.env.toc_num_entries,
        sphinxenv_metadata=app.env.metadata,
    )
    del render_container


def setup(app: Sphinx):
    app.add_config_value('themester_config', ThemesterConfig(), 'env')
    app.add_config_value('sphinx_config', SphinxConfig(), 'env')
    app.add_config_value('html_config', HTMLConfig(), 'env')
    app.add_config_value('theme_config', ThemabasterConfig(), 'env')
    app.connect('builder-inited', builder_init)
    app.config.template_bridge = 'themester.sphinx.template_bridge.ThemesterBridge'  # noqa
    app.connect('html-page-context', inject_page)
    app.connect('build-finished', builder_finished_setup)

    return dict(parallel_read_safe=True)
