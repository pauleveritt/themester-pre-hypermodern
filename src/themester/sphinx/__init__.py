from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from wired import ServiceRegistry, ServiceContainer

from themester.app import ThemesterApp
from themester.config import ThemesterConfig
from themester.protocols import Root
from themester.sphinx.builder_finished import builder_finished_setup
from themester.sphinx.builder_inited import setup_app
from themester.sphinx.config import SphinxConfig, HTMLConfig
from themester.sphinx.inject_page import make_render_container, make_page_context, make_resource
from themester.testing.resources import Site


def builder_init(app: Sphinx):
    """ Wire up some global stuff after Sphinx startup """

    themester_app = setup_app(app.config)
    setattr(app, 'themester_app', themester_app)


def doctree_resolved(app: Sphinx, doctree, docname: str):
    """ Once content is read, perform some housekeeping """

    # Make a Site instance and register as the Root
    themester_app: ThemesterApp = getattr(app, 'themester_app')
    container: ServiceContainer = themester_app.registry.create_container()
    sphinx_config: SphinxConfig = container.get(SphinxConfig)
    site = Site(title=sphinx_config.project)
    themester_app.registry.register_singleton(site, Root)


def inject_page(app, pagename, templatename, context, doctree):
    """ Store a resource-bound container in Sphinx context """

    env: BuildEnvironment = app.env
    themester_app: ThemesterApp = getattr(app, 'themester_app')
    registry: ServiceRegistry = themester_app.registry
    container = registry.create_container()
    root = container.get(Root)

    resource = make_resource(root, env, pagename)

    render_container = make_render_container(
        document_metadata=env.metadata[pagename],
        registry=registry,
        pagename=pagename,
        resource=resource,
    )
    context['render_container'] = render_container
    make_page_context(
        render_container=render_container,
        context=context,
        pagename=pagename,
        toc_num_entries=env.toc_num_entries,
        document_metadata=env.metadata[pagename],
    )


def setup(app: Sphinx):
    app.add_config_value('themester_config', ThemesterConfig(root=Site()), 'env')
    app.add_config_value('sphinx_config', SphinxConfig(), 'env')
    app.add_config_value('html_config', HTMLConfig(), 'env')
    app.connect('builder-inited', builder_init)
    app.connect('doctree-resolved', doctree_resolved)
    app.config.template_bridge = 'themester.sphinx.template_bridge.ThemesterBridge'  # noqa
    app.connect('html-page-context', inject_page)
    app.connect('build-finished', builder_finished_setup)

    return dict(parallel_read_safe=True)
