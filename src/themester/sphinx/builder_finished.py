"""
Dispatch to functions during Sphinx's ``builder_finished`` lifecycle.
"""
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset
from wired import ServiceContainer, ServiceRegistry

from .factories.copy_theme_resources import CopyThemeResources


def copy_theme_resources(container: ServiceContainer, app: Sphinx):
    ctr: CopyThemeResources = container.get(CopyThemeResources)
    static_outdir = Path(app.outdir) / '_static'
    ctr(copy_asset, static_outdir)


def setup(
        app: Sphinx,
        exc: Exception,
) -> None:
    """ Get Sphinx pieces and dispatch to each function """

    if exc is None:
        registry: ServiceRegistry = getattr(app, 'themester_registry')
        container = registry.create_container()
        copy_theme_resources(
            container=container,
            app=app,
        )
