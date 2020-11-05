from sphinx.application import Sphinx


# def doctree_resolved(app: Sphinx, doctree, docname: str):
#     """ Once content is read, perform some housekeeping """
#
#     # Make a Site instance and register as the Root
#     themester_app: ThemesterApp = getattr(app, 'themester_app')
#     container: ServiceContainer = themester_app.registry.create_container()
#     sphinx_config: SphinxConfig = container.get(SphinxConfig)
#     # site = Site(title=sphinx_config.project)
#     # themester_app.registry.register_singleton(site, Root)

def setup(app: Sphinx, doctree, docname: str):
    pass
