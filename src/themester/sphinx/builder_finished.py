"""
Dispatch to functions during Sphinx's ``builder_finished`` lifecycle.
"""
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset
from wired import ServiceContainer

from themester.app import ThemesterApp
from themester.config import ThemesterConfig


class SerCon(object):
    pass


def copy_static_resources(
        themester_app: ThemesterApp,
        outdir: str,
) -> None:
    """ Let each plugin tell Sphinx some files to copy to output """

    # Grab the theme configuration from the container and get
    # to the sphinx config.
    container: ServiceContainer = themester_app.registry.create_container()
    themester_config: ThemesterConfig = container.get(ThemesterConfig)
    theme_config = themester_config.theme_config
    if theme_config is not None:
        static_outdir = Path(outdir) / '_static'
        for static_resource in theme_config.get_static_resources():
            copy_asset(str(static_resource), static_outdir)


def builder_finished_setup(
        app: Sphinx,
        exc: Exception,
) -> None:
    """ Get Sphinx pieces and dispatch to each function """

    if exc is None:
        copy_static_resources(
            themester_app=getattr(app, 'themester_app'),
            outdir=app.outdir,
        )
