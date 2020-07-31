"""
Dispatch to functions during Sphinx's ``builder_finished`` lifecycle.
"""
from pathlib import Path

from sphinx.application import Sphinx
from sphinx.util.fileutil import copy_asset

from themester.app import ThemesterApp


def copy_static_resources(
        themester_app: ThemesterApp,
        outdir: str,
) -> None:
    """ Let each plugin tell Sphinx some files to copy to output """

    static_outdir = Path(outdir) / '_static'
    for static_resource in themester_app.get_static_resources():
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
