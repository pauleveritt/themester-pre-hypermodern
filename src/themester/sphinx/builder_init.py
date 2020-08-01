"""
During Sphinx builder_init, create the Themester app and return it.

The ThemesterApp is a way to "canonicalize" Themester across different
systems. It expects some bootstrap information from the outside world,
then from there, is on its own.

This module provides some glue to "adapt" Sphinx to ThemesterApp.
"""
from sphinx.config import Config

from themester.app import ThemesterApp


def setup_app(
        sphinx_config: Config
) -> ThemesterApp:
    # TODO Hmm, is this the right place to put this? Should
    #    it be in ThemesterConfig?

    from themester.testing.resources import Site
    site = Site()

    themester_app = ThemesterApp(
        root=site,
        themester_config=getattr(sphinx_config, 'themester_config'),
        sphinx_config=getattr(sphinx_config, 'sphinx_config'),
        html_config=getattr(sphinx_config, 'html_config'),
        theme_config=getattr(sphinx_config, 'theme_config'),
    )

    return themester_app
